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
  - "[[brpc/io.md]]"
  - "[[brpc/en_streaming_log.md]]"
  - "[[brpc/en_client.md]]"
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

## Related Concepts
- [[concepts/work-stealing|工作窃取（work stealing）]]
- [[concepts/bthread-work-stealing|bthread work stealing]]
- [[concepts/noflush|noflush]]
- [[concepts/thread-local-bufferr|thread-local 缓冲]]
- [[concepts/brpc-server|brpc::Server]]
- [[concepts/pthread模式|pthread模式]]
- [[concepts/bthread-local|bthread-local]]
- [[concepts/session-local-data|session-local data]]
- [[concepts/server-thread-local-data|server-thread-local data]]
- [[concepts/resourcepool|ResourcePool<t>]]
- [[concepts/taskmeta|TaskMeta]]
- [[concepts/bthread_t|bthread_t]]
- [[concepts/bthread-栈管理|bthread 栈管理]]
- [[concepts/guard-page|guard page]]
- [[concepts/edge-triggered-模式|Edge triggered 模式]]
- [[concepts/socketuniqueptr|SocketUniquePtr]]
- [[concepts/命名服务|命名服务]]
- [[concepts/健康检查|健康检查]]
- [[concepts/periodicservicervice|PeriodicNamingService]]
- [[concepts/bthread_mutex_t|bthread_mutex_t]]
- [[concepts/bthread_concurrency|bthread_concurrency]]
- [[concepts/channel|Channel]]
- [[concepts/timeout|Timeout]]

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
> - "NamingServiceThread 也以 bthread 形式运行，并可被多个 Channel 通过 intrusive_ptr 共享。"

> **Source: [[sources/io|io]]**
> - "当收到事件时，EDISP 给一个原子变量加1，只有当加1前的值是0时启动一个bthread处理对应fd上的数据。"
> - "在背后，EDISP把所在的pthread让给了新建的bthread，使其有更好的cache locality，可以尽快地读取fd上的数据。而EDISP所在的bthread会被偷到另外一个pthread继续执行，这个过程即是bthread的work stealing调度。"
> - "若一次从某个fd读取出n个消息(n > 1)，InputMessenger会启动n-1个bthread分别处理前n-1个消息，最后一个消息则会在原地被Process。"

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "The noflush feature also support bthread so that we can push lots of logs from the server's bthreads without actually print them (using noflush), and flush the whole log at the end of RPC."
> - "Note that you should not use noflush when implementing an asynchronous method since it will change the underlying bthread, leaving noflush out of function."

> **Source: [[sources/en_client|en_client]]**
> - "There's no independent thread pool for client in brpc. All Channels and Servers share the same backing threads via bthread."
> - "Replace pthread lock with bthread lock (bthread_mutex_t)"
> - "Setting number of worker pthreads in Server works for Client as well if Server is in used."