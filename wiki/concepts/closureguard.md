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

## Related Concepts
- [[concepts/raii|RAII]]
- [[concepts/async-service|异步Service]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/closureguard|ClosureGuard]]

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
> - Interface of ClosureGuard:
> - brpc::ClosureGuard done_guard(done);
> - "Not matter the callback is exited from middle or end, done_guard will be destructed, in which done->Run() is called."

> **Source: [[sources/server|server]]**
> - 强烈建议使用**ClosureGuard**确保done->Run()被调用
> - RAII: Call Run() of the closure on destruction.
> - 这个机制称为[RAII](https://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization)。
> - 不管成功失败，done->Run()必须在请求处理完成后被用户调用一次。