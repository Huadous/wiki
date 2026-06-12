---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
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

## Mentions in Source

> **Source: [[concepts/source-en_server|source-en_server]]**
> - "A session-local data is bound to a server-side RPC: from entering CallMethod of the service, to calling the server-side done->Run(), no matter the service is synchronous or asynchronous."
> - "Controller.session_local_data() gets a session-local data."
> - "If ServerOptions.session_local_data_factory is unset, Controller.session_local_data() always returns NULL."
> - "After setting ServerOptions.session_local_data_factory, call Controller.session_local_data() to get a session-local data."
> - "MySessionLocalData* sd = static_cast<MySessionLocalData*>(cntl->session_local_data());"

## Additional Notes

The new source file ("en_server") provides no directly relevant information to session-local data.