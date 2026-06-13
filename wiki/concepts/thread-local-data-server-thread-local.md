---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
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

## Related Concepts
- [[concepts/session-local-data|session-local data]]
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

> **Source: [[sources/en_server|brpc 服务器端文档]]**
> - "A server-thread-local is bound to a call to service's CallMethod, from entering service's CallMethod, to leaving the method."
> - "brpc::thread_local_data() gets a thread-local."
> - "If the service is asynchronous and the data needs to be accessed from done->Run(), session-local is the only option."
> - "After setting ServerOptions.thread_local_data_factory, call brpc::thread_local_data() to get a thread-local."
> - "MyThreadLocalData* tls = static_cast<MyThreadLocalData*>(brpc::thread_local_data());"
> - "session-local and server-thread-local are similar in a synchronous service, except that the former one has to be created from a Controller."
> - "A server-thread-local is bound to **a call to service's CallMethod**, from entering service's CallMethod, to leaving the method."
> - "After setting ServerOptions.thread_local_data_factory, call brpc::thread_local_data() to get a thread-local."

> **Source: [[sources/server|brpc Server端使用文档]]**
> - "server-thread-local与一次service回调绑定，从进service回调开始，到出service回调结束"
> - "当service是同步时，session-local和server-thread-local基本没有差别"