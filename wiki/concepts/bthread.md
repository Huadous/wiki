---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[concepts/单线程反应器]]"
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
  - "[[sources/en_io]]"
  - "[[brpc/streaming_log.md]]"
  - "[[brpc/server.md]]"
  - "[[brpc/memory_management.md]]"
  - "[[brpc/load_balancing.md]]"
tags:
  - "other"
aliases:
  - "brpc 协程"
  - "bthread 线程"
  - "num_threads"
  - "brpc 协程"
  - "bthread 线程"
  - "pthread"
  - "brpc 协程"
  - "bthread 线程"
  - "num_threads"
  - "brpc 协程"
  - "bthread 线程"
---

## Description
bthread 是 brpc 框架中用于实现高并发的用户态线程抽象，在代码中被称作 Task，其结构被称为 [[concepts/taskmeta|TaskMeta]]。用户期望通过创建 bthread 获得更高的并发度，因此 bthread 的创建开销必须极低，在当前实现中平均耗时小于 200ns。bthread 默认栈大小为 1MB（远小于 pthread 的 10MB 默认栈），M 个 bthread 会映射至 N 个 worker pthread 中执行（一般 M > N），因此同步 server 的并发度可能超过 worker 数量。

bthread 与 brpc 的 IO 机制深度结合。EventDispatcher（EDISP）所运行的 pthread worker 会被让出（yield）给新创建的 bthread，EDISP 中运行的 bthread 也会通过 [[concepts/work-stealing|工作窃取（work stealing）]]机制被调度到其他 pthread 上继续运行。当一个 fd 上有事件到达时，相关的原子变量加一；若加之前为零，则启动一个 bthread 处理该 fd 的数据。InputMessenger 若一次性从 fd 读取 n(n>1) 条消息，会启动 n-1 个 bthread 分别处理前 n-1 条消息，最后一条消息就地处理。无法一次写完时则会创建 KeepWrite bthread 写入剩余数据。

在日志场景下，bthread 支持 [[concepts/noflush|noflush]] 机制，可以暂不刷出日志直到跨 bthread 边界统一刷出（类似 UB 的 pushnotice 效果）；但若检索过程是异步的，则不应使用 noflush。在 server 端，brpc 会为每个请求建立一个 bthread，因此 server 中的 [[concepts/bthread-local|bthread-local]] 行为特殊。用户代码（客户端的 done，服务器端的 CallMethod）默认运行在栈为 1MB 的 bthread 中。在负载均衡与命名服务场景下，bthread 同样承担重要角色：命名服务线程（NamingServiceThread）以独立 bthread 运行，并可被多个 Channel 通过 intrusive_ptr 共享；健康检查逻辑则为每个需要检查的连接动态创建独立的 bthread（[[entities/socket|Socket]]::StartHealthCheck）来执行，避免了传统单线程健康检查的瓶颈。当 Socket 析构时，对应的健康检查 bthread 会随之退出，实现了生命周期的自动管理。

## Related Concepts
- [[concepts/work-stealing|工作窃取（work stealing）]]
- [[concepts/noflush|noflush]]
- [[concepts/thread-local-bufferr|thread-local 缓冲]]
- [[concepts/brpc-server|brpc::Server]]
- [[concepts/pthread模式|pthread模式]]
- [[concepts/bthread-local|bthread-local]]
- [[concepts/session-local-data|session-local data]]
- [[concepts/server-thread-local-data|server-thread-local data]]
- [[concepts/resourcepool|ResourcePool&lt;t&gt;]]
- [[concepts/taskmeta|TaskMeta]]
- [[concepts/bthread_t|bthread_t]]
- [[concepts/bthread-栈管理|bthread 栈管理]]
- [[concepts/guard-page|guard page]]
- [[concepts/命名服务|命名服务]]
- [[concepts/健康检查|健康检查]]
- [[concepts/periodicservicervice|PeriodicNamingService]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/EventDispatcher|EventDispatcher]]
- [[entities/InputMessenger|InputMessenger]]
- [[entities/Socket|Socket]]
- [[entities/bvar|bvar]]
- [[entities/ClosureGuard|ClosureGuard]]
- [[entities/ServerOptions|ServerOptions]]
- [[entities/baidu|baidu]]
- [[entities/eventdispatcher|eventdispatcher]]
- [[entities/inputmessenger|inputmessenger]]
- [[entities/socket|socket]]
- [[entities/bthread|bthread]]
- [[entities/ub|ub]]
- [[entities/namingservicethread|namingservicethread]]
- [[entities/namingservicewatcher|namingservicewatcher]]

## Mentions in Source

> **Source: [[sources/en_io|en_io]]**
> - "The pthread worker in which EDISP runs is yielded to the newly created bthread"
> - "the bthread in which EDISP runs will be stolen to another pthread and keep running"
> - "After receiving an event, an atomic variable associated with the fd is added by one atomically. If the variable is zero before addition, a bthread is started to handle the data from the fd."
> - "The bthread in which EDISP runs will be stolen to another pthread and keep running, this mechanism is work stealing used in bthreads."
> - "If n(n > 1) messages are read from the fd, InputMessenger launches n-1 bthreads to handle first n-1 messages respectively, and processes the last message in-place."
> - "In current implementations, if the data cannot be written fully in one call, a KeepWrite bthread is created to write the remaining data."

> **Source: [[sources/streaming_log|streaming_log]]**
> - "noflush支持bthread，可以实现类似于UB的pushnotice的效果，即检索线程一路打印都暂不刷出（加上noflush），直到最后检索结束时再一次性刷出。"
> - "注意，如果检索过程是异步的，就不应该使用noflush，因为异步显然会跨越bthread，使noflush仍然失效。"

> **Source: [[sources/server|server]]**
> - "brpc的Server是运行在bthread之上，默认栈大小为1MB，而pthread默认栈大小为10MB"
> - "M个bthread会映射至N个worker中（一般M大于N），所以同步server的并发度可能超过worker数量"
> - "由于brpc会为每个请求建立一个bthread，server中的bthread-local行为特殊"
> - "用户代码（客户端的done，服务器端的CallMethod）默认在栈为1MB的bthread中运行。"

> **Source: [[sources/memory_management|memory_management]]**
> - "用户期望通过创建bthread获得更高的并发度，所以创建bthread必须很快。"
> - "在目前的实现中创建一个bthread的平均耗时小于200ns。"
> - "bthread在代码中被称作Task，其结构被称为TaskMeta"

> **Source: [[sources/load_balancing|load_balancing]]**
> - "这套逻辑会运行在独立的bthread中，即NamingServiceThread。"
> - "brpc简化了这个过程：为需要的连接动态创建一个bthread专门做健康检查（Socket::StartHealthCheck）。"
> - "定期连接直到远端机器被连接上，在这个过程中，如果Socket析构了，那么该线程也就随之退出了。"