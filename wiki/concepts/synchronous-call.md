---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client|en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "method"
aliases:
  - "同步调用"
  - "Sync RPC"
  - "Synchronous RPC"
  - "同步访问"
  - "同步调用"
  - "Sync RPC"
  - "Synchronous RPC"
---

## Description
Synchronous call 是 brpc 客户端最直接的调用方式：调用线程发起 `CallMethod` 后会一直阻塞，直到收到服务端的响应或发生错误（包括超时）才返回。在同步访问中，`Response` 与 `Controller`（[[concepts/controller|Controller]]）对象在 `CallMethod` 返回后不会被 brpc 框架再次使用，因此可以安全地分配在栈上，无需额外的生命周期管理。文档对此明确警告：**禁止在持有 pthread 锁的情况下调用 brpc 的同步 `CallMethod`**，否则极易导致死锁；推荐的做法是将 pthread 锁替换为 [[concepts/bthread|bthread]] 锁，或在调用 `CallMethod` 之前先释放锁。同步访问通常通过 [[entities/brpc::Channel|brpc::Channel]] 发起，配合 [[entities/brpc::Controller|brpc::Controller]] 对象使用。与 [[concepts/asynchronous-call|Asynchronous call]]（异步访问）和半同步访问相比，同步访问语义最简单，适合调用方需要同步获取 RPC 结果后才继续后续逻辑的线性场景。

## Related Concepts
- [[concepts/asynchronous-call|Asynchronous call]]
- [[concepts/half-synchronous-call|Half-synchronous call]]
- [[concepts/controller|Controller]]
- [[concepts/timeout|Timeout]]
- [[concepts/bthread|bthread]]
- [[concepts/channel|Channel]]

## Related Entities
- [[entities/brpc-channel|brpc::Channel]]
- [[entities/brpc-controller|brpc::Controller]]

## Mentions in Source
- "CallMethod blocks until response from server is received or error occurred (including timedout)." — [[sources/en_client|en_client]]
- "response/controller in synchronous call will not be used by brpc again after CallMethod, they can be put on stack safely." — [[sources/en_client|en_client]]
- "WARNING: Do NOT use synchronous call when you are holding a pthread lock! Otherwise it is easy to cause deadlock." — [[sources/en_client|en_client]]

> **Source: [[sources/client|client]]**
> - "指的是：CallMethod会阻塞到收到server端返回response或发生错误（包括超时）。"
> - "同步访问中的response/controller不会在CallMethod后被框架使用，它们都可以分配在栈上。"
> - "警告: 请勿在持有pthread锁的情况下，调用brpc的同步CallMethod！否则很容易导致死锁。"