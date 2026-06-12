---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[concepts/单线程反应器]]"
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
  - "[[sources/en_io]]"
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

## Mentions in Source
> **Source: [[sources/en_io|en_io]]**
> - "The pthread worker in which EDISP runs is yielded to the newly created bthread"
> - "the bthread in which EDISP runs will be stolen to another pthread and keep running"
> - "After receiving an event, an atomic variable associated with the fd is added by one atomically. If the variable is zero before addition, a bthread is started to handle the data from the fd."
> - "The bthread in which EDISP runs will be stolen to another pthread and keep running, this mechanism is work stealing used in bthreads."
> - "If n(n > 1) messages are read from the fd, InputMessenger launches n-1 bthreads to handle first n-1 messages respectively, and processes the last message in-place."
> - "In current implementations, if the data cannot be written fully in one call, a KeepWrite bthread is created to write the remaining data."

## Additional Information from Source

bthread是[[entities/brpc|brpc]]中实现的高性能用户态线程（协程），由bthread库管理。[[entities/brpc|brpc]]使用bthread来处理IO事件和运行用户代码。

当[[entities/EventDispatcher|EventDispatcher]]收到事件时，会启动一个bthread来处理数据。具体流程为：当与fd关联的原子变量通过原子操作加1时，如果该变量之前为零，则启动一个bthread来处理该fd的数据。bthread支持工作窃取（work stealing），即bthread中的EDISP执行流会被窃取到另一个pthread上继续运行，从而实现负载均衡和CPU缓存局部性优化。

[[entities/brpc|brpc]]通过bthread将消息处理并发化：如果从fd读取了n（n>1）条消息，[[entities/InputMessenger|InputMessenger]]会启动n-1个bthread分别处理前n-1条消息，并在当前执行流中就地处理最后一条消息，从而降低尾延迟。如果数据在一次调用中无法完全写入，还会创建一个KeepWrite bthread来负责剩余数据的写入。