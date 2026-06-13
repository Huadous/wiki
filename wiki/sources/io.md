---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/io.md]]"
tags: [Blocking IO, Non-blocking IO, Asynchronous IO, Edge triggered 模式, Wait-free MPSC 链表, bthread work stealing, KeepWrite, SocketId, bthread, SocketUniquePtr, Streaming RPC, SelectiveChannel, Controller, epoll]
aliases: ["brpc IO 模型", "brpc IO Model and Implementation"]
---

# brpc 的 IO 模型与实现机制 - Summary

## 来源
- Original file: [[brpc/io.md]]
- Ingested: 2026-06-13

## 核心内容
本文档系统介绍了 [[entities/brpc|brpc]] 框架的 IO 实现机制。首先对比了三种 IO 模型：[[concepts/blocking-io|同步阻塞 IO]]、[[concepts/non-blocking-io|non-blocking IO]]（如 [[concepts/epoll|epoll]]/kqueue）和 [[concepts/asynchronous-io|asynchronous IO]]（如 Windows IOCP）。在高并发场景下，brpc 选择 non-blocking IO 以减少内核线程切换并充分利用 thread-local 优化。收消息时使用一个或多个 [[entities/eventdispatcher|EventDispatcher]]（EDISP）监听 fd 事件，由 [[entities/inputmessenger|InputMessenger]] 切割和处理消息，并利用 [[concepts/bthread-work-stealing|bthread work stealing]] 实现 fd 间和 fd 内消息的并发处理；发消息时采用 [[concepts/wait-free-mpsc-链表|wait-free MPSC 链表]] 实现多生产者单消费者的写排队，配合 [[concepts/keepwrite|KeepWrite]] 线程处理大批量写出。最后介绍了 [[entities/socket|Socket]] 数据结构，它使用 64 位 [[concepts/socketid|SocketId]] 替代 weak_ptr 以解决 server 退出延迟问题，并被复用于 [[concepts/selectivechannel|SelectiveChannel]] 的 Sub Channel 管理和 [[concepts/streaming-rpc|Streaming RPC]]，整个设计保证了 fd 操作在多线程下的 wait-free 或 lock-free 特性。

## 关键实体
- [[entities/brpc|brpc]] - Apache 基金会下的开源 RPC 框架，专注于高性能 IO 实现
- [[entities/socket|Socket]] - brpc 中与 fd 相关的核心数据结构，使用 64 位 SocketId 指代
- [[entities/eventdispatcher|EventDispatcher]] - 负责监听 fd 事件的组件（EDISP），仅监听不读取
- [[entities/inputmessenger|InputMessenger]] - 负责从 fd 上切割和处理消息的组件

## 关键概念
- [[concepts/blocking-io|Blocking IO]] - 同步阻塞 IO，POSIX read/write 是典型代表
- [[concepts/non-blocking-io|Non-blocking IO]] - "批量的同步"IO，brpc 在高并发下的核心选择
- [[concepts/asynchronous-io|Asynchronous IO]] - 真正的异步 IO，如 Windows 的 IOCP
- [[concepts/edge-triggered-模式|Edge triggered 模式]] - EDISP 采用的 epoll 触发模式
- [[concepts/wait-free-mpsc-链表|Wait-free MPSC 链表]] - brpc 用于多生产者单消费者写排名的数据结构
- [[concepts/bthread-work-stealing|bthread work stealing]] - bthread 调度机制，优化 cache locality
- [[concepts/keepwrite|KeepWrite]] - 后台写线程，处理大批量写出的流水线
- [[concepts/socketid|SocketId]] - 64 位整数指代 Socket 对象，类似 weak_ptr 但更适用 epoll
- [[concepts/bthread|bthread]] - brpc 使用的用户态线程机制
- [[concepts/socketuniqueptr|SocketUniquePtr]] - 对 Socket 指针的 unique_ptr 封装
- [[concepts/streaming-rpc|Streaming RPC]] - 单连接上持续传输有边界消息流的 RPC 模式
- [[concepts/selectivechannel|SelectiveChannel]] - brpc 中按策略选择 Sub Channel 的通道实现
- [[concepts/controller|Controller]] - 贯穿 RPC 流程的客户端控制对象
- [[concepts/epoll|epoll]] - Linux 下的 non-blocking IO 多路复用机制

## 要点
- brpc 在 IO 模型上选择 [[concepts/non-blocking-io|non-blocking IO]] 而非 [[concepts/blocking-io|blocking IO]]，因高并发下 non-blocking IO 通过少量 event dispatching 线程和可复用 worker 线程显著降低内核线程切换开销，并充分利用 thread-local 优化
- [[entities/eventdispatcher|EventDispatcher]]（EDISP）仅负责监听 fd 事件而非读取，避免了单 IO 线程被繁忙 fd 拖慢的问题；其采用 [[concepts/edge-triggered-模式|epoll Edge triggered 模式]]以规避 epoll bug 和 epoll_ctl 开销
- 收消息时，[[entities/inputmessenger|InputMessenger]] 切割消息后启动多个 [[concepts/bthread|bthread]] 并行处理，并通过 [[concepts/bthread-work-stealing|work stealing]] 调度机制保证 cache locality，使 fd 间和 fd 内消息都能并发处理，特别适合大消息读取
- 发消息时采用 [[concepts/wait-free-mpsc-链表|wait-free MPSC 链表]] 实现多线程写排队，配合 [[concepts/keepwrite|KeepWrite]] 后台线程形成批量写出流水线，在大吞吐时显著提高 IO 效率
- [[entities/socket|Socket]] 设计用 64 位 [[concepts/socketid|SocketId]] 替代 weak_ptr，结合 [[concepts/socketuniqueptr|SocketUniquePtr]] 提供 wait-free/lock-free 的访问，并通过 SetFailed 机制解决 server 退出时引用计数无法清0 的问题，已稳定运行多年