---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "method"
aliases:
  - "服务器线程本地数据"
  - "server thread local data"
  - "brpc thread local data"
  - "Server-thread-local data"
  - "服务器线程本地数据"
  - "server thread local data"
  - "brpc thread local data"
  - "server-thread-local data"
  - "服务器线程本地数据"
  - "server thread local data"
  - "brpc thread local data"
  - "Server-thread-local data"
  - "服务器线程本地数据"
  - "server thread local data"
  - "brpc thread local data"
  - "server-thread-local (服务器线程局部存储)"
  - "服务器线程本地数据"
  - "server thread local data"
  - "brpc thread local data"
  - "Server-thread-local data"
  - "服务器线程本地数据"
  - "server thread local data"
  - "brpc thread local data"
  - "server-thread-local data"
  - "服务器线程本地数据"
  - "server thread local data"
  - "brpc thread local data"
  - "Server-thread-local data"
  - "服务器线程本地数据"
  - "server thread local data"
  - "brpc thread local data"
---

## Description
**server-thread-local** 是 brpc 中一种线程局部存储机制，其生命周期绑定到服务端 `CallMethod` 的一次调用：从进入该方法到离开该方法。与 [[concepts/session-local-data|session-local data]] 相比，server-thread-local 可以通过全局函数 `brpc::thread_local_data()` 在任何函数中直接访问（只要该函数在服务端线程内间接或直接执行），无需通过 Controller 对象获取。这使得它在同步服务中成为更简单的选择。然而，在异步服务中，server-thread-local 会在 `CallMethod` 返回后立即失效，因此当数据需要在 `done->Run()` 回调中持久存在时，必须使用 session-local。通过配置 `ServerOptions.thread_local_data_factory` 和 `reserved_thread_local_data`，可以自定义数据的创建与池化行为。

## Related Concepts
- [[concepts/session-local-data|session-local-data]]
- [[concepts/bthread-local|bthread-local]]
- [[concepts/brpccontroller|brpc Controller]]
- [[concepts/asynchronous-service|asynchronous service]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/datafactory|DataFactory]]
- [[entities/serviceoptions|ServiceOptions]]
- [[entities/brpc-server|brpc::Server]]
- [[entities/brpc-controller|brpc::Controller]]

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
> - "A server-thread-local is bound to a call to service's CallMethod, from entering service's CallMethod, to leaving the method."
> - "brpc::thread_local_data() gets a thread-local."
> - "If the service is asynchronous and the data needs to be accessed from done->Run(), session-local is the only option."
> - "After setting ServerOptions.thread_local_data_factory, call brpc::thread_local_data() to get a thread-local."
> - "MyThreadLocalData* tls = static_cast<MyThreadLocalData*>(brpc::thread_local_data());"
> - "session-local and server-thread-local are similar in a synchronous service, except that the former one has to be created from a Controller."

> **Source: [[sources/en_server|en_server]]**
> - "A server-thread-local is bound to **a call to service's CallMethod**, from entering service's CallMethod, to leaving the method."
> - "After setting ServerOptions.thread_local_data_factory, call brpc::thread_local_data() to get a thread-local."