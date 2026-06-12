---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "method"
aliases:
  - "ClosureGuard RAII 包装"
  - "闭包保护器"
  - "同步服务"
  - "ClosureGuard RAII 包装"
  - "闭包保护器"
  - "RAII"
  - "ClosureGuard RAII 包装"
  - "闭包保护器"
  - "同步服务"
  - "ClosureGuard RAII 包装"
  - "闭包保护器"
---

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: en_server**
> - Interface of ClosureGuard:
> - brpc::ClosureGuard done_guard(done);
> - "Not matter the callback is exited from middle or end, done_guard will be destructed, in which done->Run() is called."

ClosureGuard is a RAII-style utility provided by brpc that ensures the completion callback (`done`) is always invoked when exiting a scope, regardless of whether the exit occurs normally or due to an early return. By wrapping the closure object in a ClosureGuard instance, the `Run()` method of the closure is automatically called upon destruction, preventing callback leakage in asynchronous or mixed synchronous/asynchronous service implementations.