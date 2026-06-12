---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "method"
aliases:
  - "异步服务"
  - "Asynchronous RPC service"
---

## Related Entities
- [[entities/brpc|brpc]]：提供异步服务实现框架。
- [[entities/echoservice|echoservice]]：brpc 官方示例中的服务，用于演示异步和同步模式。
- [[entities/closurguard|ClosureGuard]]：brpc 中用于自动管理 `done` 生命周期的工具类。
- [[entities/controller|brpc::Controller]]：异步服务中常用的 RPC 控制器。