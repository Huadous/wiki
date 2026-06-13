---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_backup_request]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/client.md]]"
  - "[[brpc/bthread_or_not.md]]"
tags:
  - "method"
aliases:
  - "异步 RPC"
  - "Asynchronous RPC"
  - "Asynchronous call"
  - "异步 RPC"
  - "Asynchronous RPC"
  - "异步访问"
  - "异步 RPC"
  - "Asynchronous RPC"
  - "Asynchronous call"
  - "异步 RPC"
  - "Asynchronous RPC"
  - "异步接口"
  - "异步 RPC"
  - "Asynchronous RPC"
  - "Asynchronous call"
  - "异步 RPC"
  - "Asynchronous RPC"
  - "异步访问"
  - "异步 RPC"
  - "Asynchronous RPC"
  - "Asynchronous call"
  - "异步 RPC"
  - "Asynchronous RPC"
---

## Description
异步 RPC 是 brpc 中与同步调用相对的非阻塞调用模式：调用方在 `CallMethod` 时传入一个 `done` 回调（`done->Run`），`CallMethod` 仅在请求发送完成后即返回，而不是等到 RPC 整体完成；真正收到响应或调用失败时，框架会在另一个 bthread 上触发 `done->Run()`，从而避免在同步等待期间持锁导致死锁。由于 `CallMethod` 返回时 RPC 尚未结束，`Response`、`Controller`、`done` 等对象通常必须分配在堆上，并在 `done->Run()` 中删除，否则回调可能访问到已释放的内存。`Channel` 本身在异步 `CallMethod` 返回后即可销毁（除非还有未完成的 RPC 需要访问它），而在 `SelectiveChannel` 场景下，传入的 `Request` 必须等到 RPC 完成之后才能释放。

异步 `done` 回调的常见实现方式有两种：一种是使用 `brpc::NewCallback` 生成的独立 `Closure` 对象（涉及三次内存分配），另一种是继承 `google::protobuf::Closure` 并把 `response`、`controller` 作为成员变量（仅需一次内存分配），后者在内存开销与缓存局部性上更为友好。异步 RPC 还被作为一种「备份请求」的替代实现思路进行讨论：发起两个并行的异步调用，在各自的 done 回调中互相取消，先返回的那个会取消另一个尚未完成的调用，从而实现「谁先成功谁生效」的语义。文档同时指出，这种方式会无条件地向后端发送两次请求，将后端压力翻倍，是一种「在任何维度上都不经济」的实现，因此被明确标记为「不推荐」并建议尽量避免；实际生产中应优先使用 [[concepts/backup-request|Backup Request]] 机制（如 `example/backup_request_c++`）或基于 [[concepts/selective-channel|SelectiveChannel]] 的方案。

根据 `bthread_or_not` 文档的阐述，brpc 的异步与单线程 JavaScript 等环境中的异步在本质上是不同的：brpc 的异步回调「会运行在与调用处不同的线程中」，因此天然具备多核扩展性，调用方不会被限制在单一线程上串行处理回调。这与「有阻塞的地方就有回调」的核心理念一致——使用异步的目的就是用回调取代阻塞等待。文档给出了一条 `qps * latency` 与 CPU 核数对比的决策依据：当 `qps * latency` 远大于机器 CPU 核数时（例如 `qps=100`、`latency=5s` 时计算结果为 500，与核数不在同一数量级），程序大部分时间都花在让线程阻塞等待响应上，切换到异步可以显著节省线程资源（主要是每线程栈占用的内存）。同时，brpc 提供了 [[concepts/parallel-channel|组合访问]]（如 [[concepts/combo-channel|ComboChannel]]、[[concepts/parallel-channel|ParallelChannel]]），以声明式的方式表达复杂的异步访问流程，从而简化异步编程模型。

## Related Concepts
- [[concepts/backup-request|Backup Request]]
- [[concepts/selective-channel|SelectiveChannel]]
- [[concepts/streaming-rpc|Streaming RPC]]
- [[concepts/synchronous-call|Synchronous call]]
- [[concepts/controller|Controller]]
- [[concepts/cancel-rpc|Cancel RPC]]
- [[concepts/bthread|bthread]]
- [[concepts/newcallback|NewCallback]]
- [[concepts/combo-channel|ComboChannel]]
- [[concepts/parallel-channel|ParallelChannel]]
- [[concepts/qps-latency|qps * latency 决策公式]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/examplecancel_c++|cancel_c++ 示例]]
- [[entities/examplebackup_request_c++|backup_request_c++ 示例]]
- [[entities/exampleselective_echo_c++|SelectiveChannel 备份请求示例]]
- [[entities/ubaserver|ubaserver]]

## Mentions in Source

> **Source: [[sources/en_backup_request|en_backup_request]]**
> - "[Not Recommended] Issue two asynchronous RPC calls and join them. They cancel each other in their done callback."
> - "The problem of this method is that the program always sends two requests, doubling the pressure to back-end services. It is uneconomical in any sense and should be avoided as much as possible."

> **Source: [[sources/en_client|en_client]]**
> - "Pass a callback `done` to CallMethod, which resumes after sending request, rather than completion of RPC."
> - "Generally they should be allocated on heap and deleted in done->Run(). If they're deleted too early, done->Run() may access invalid memory."
> - "The callback runs in a different bthread, even the RPC fails just after entering CallMethod."

> **Source: [[sources/client|client]]**
> - "异步访问指的是：给CallMethod传递一个额外的回调对象done，CallMethod在发出request后就结束了，而不是在RPC结束后。"
> - "由于CallMethod结束不意味着RPC结束，response/controller仍可能被框架及done->Run()使用，它们一般得创建在堆上，并在done->Run()中删除。"
> - "发起异步请求后Channel可以立刻析构。"

> **Source: [[sources/bthread_or_not|bthread_or_not]]**
> - "异步即用回调代替阻塞，有阻塞的地方就有回调。"
> - "brpc中的异步和单线程的异步是完全不同的，异步回调会运行在与调用处不同的线程中，你会获得多核扩展性"
> - "qps = 100, latency = 5s, 计算结果 = 100 * 5s = 500。和核数不在同一个数量级，用异步。"