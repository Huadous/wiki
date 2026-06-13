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
  - "会话本地数据"
  - "session-local data"
  - "Session Local Storage"
  - "会话本地数据"
  - "session-local data"
  - "数据局部存储"
  - "会话本地数据"
  - "session-local data"
  - "Session Local Storage"
  - "会话本地数据"
  - "session-local data"
---

## Related Concepts

- [[concepts/server-thread-local-data|server-thread-local data]]
- [[concepts/bthread-local|bthread-local]]

## Related Entities

- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
> - "A session-local data is bound to a server-side RPC: from entering CallMethod of the service, to calling the server-side done->Run(), no matter the service is synchronous or asynchronous."
> - "Controller.session_local_data() gets a session-local data."
> - "If ServerOptions.session_local_data_factory is unset, Controller.session_local_data() always returns NULL."
> - "After setting ServerOptions.session_local_data_factory, call Controller.session_local_data() to get a session-local data."
> - "MySessionLocalData* sd = static_cast<MySessionLocalData*>(cntl->session_local_data());"

> **Source: [[sources/server|server]]**
> - "session-local data与一次server端RPC绑定: 从进入service回调开始，到调用server端的done结束"
> - "当service是异步时，且你需要在done->Run()中访问到数据，这时只能用session-local，因为server-thread-local在service回调外已经失效。"