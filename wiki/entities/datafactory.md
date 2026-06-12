---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "other"
aliases:
  - "数据工厂"
  - "session-local/thread-local工厂"
  - "DataFactory"
---

## Related Entities

- [[entities/brpc|brpc]]
- [[entities/echoservice|EchoService]]

## Related Concepts

- 数据局部存储
- [[concepts/serveroptions|ServerOptions]]

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
- "session_local_data_factory is typed DataFactory. You have to implement CreateData and DestroyData inside." — [[sources/en_server|en_server]]
- "NOTE: CreateData and DestroyData may be called by multiple threads simultaneously. Thread-safety is a must." — [[sources/en_server|en_server]]
- "If this field is NULL, Controller::session_local_data() is always NULL." — [[sources/en_server|en_server]]
- "If this field is NULL, brpc::thread_local_data() is always NULL." — [[sources/en_server|en_server]]
- "thread_local_data_factory is typed DataFactory. You need to implement CreateData and DestroyData inside." — [[sources/en_server|en_server]]
- "session_local_data_factory is typed DataFactory. You have to implement CreateData and DestroyData inside." — [[sources/en_server|en_server]]
- "class MySessionLocalDataFactory : public brpc::DataFactory {\npublic:\n    void* CreateData() const { return new MySessionLocalData; }\n    void DestroyData(void* d) const { delete static_cast<MySessionLocalData*>(d); }\n};" — [[sources/en_server|en_server]]