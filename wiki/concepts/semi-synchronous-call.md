---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "method"
aliases:
  - "半同步调用"
  - "Semi-synchronous call"
  - "半同步"
  - "半同步调用"
  - "Semi-synchronous call"
---

## Description
Semi-synchronous call 是 brpc 中通过 `brpc::Join(cntl.call_id())` 实现"等待多个异步访问完成"的访问模式，常配合 `brpc::DoNothing()`（一个什么都不做的 done）使用。在该模式下，调用方先以异步方式并发发起多个 RPC 请求，再在调用点阻塞等待，直到全部 RPC 完成并执行各自的 `done->Run()` 后才继续执行。由于调用处的代码会等到所有 RPC 都结束后再醒来，`controller` 和 `response` 都可以安全地放在栈上，而无需堆分配或额外的生命周期管理。

`brpc::DoNothing()` 返回的 closure 由 brpc 负责管理其生命周期，调用方无需手动释放；同时该 `doNothing` 不会删除 `controller`，因此即便在 RPC 完成后访问 `controller.call_id()` 也是安全的。`Join()` 还具有若干额外行为：如果对应的 RPC 已经结束，则 `Join()` 会立即返回；多个线程可以同时 `Join()` 同一个 id；同步 RPC 也可以在另一个线程中被 `Join()`。这一组合特别适合在同一线程内并发发起多个 RPC 并等待其全部完成的场景，例如 fan-out 式请求分发后统一汇聚响应结果的批量处理流程。

## Related Concepts
- [[concepts/asynchronous-call|Asynchronous call]]
- [[concepts/synchronous-call|Synchronous call]]
- [[concepts/brpc-join|brpc::Join]]
- [[concepts/异步访问|异步访问]]
- [[concepts/同步访问|同步访问]]

## Related Entities
- [[entities/channel|Channel]]
- [[entities/controller|Controller]]
- [[entities/brpcdonothing|brpc::DoNothing]]
- [[entities/brpcchannel|brpc::Channel]]
- [[entities/brpccontroller|brpc::Controller]]

## Mentions in Source

> **Source: [[sources/en_client|en_client]]**
> - "Join can be used for implementing "Semi-synchronous" call: blocks until multiple asynchronous calls to complete."
> - "Since the callsite blocks until completion of all RPC, controller/response can be put on stack safely."
> - "brpc::DoNothing() gets a closure doing nothing, specifically for semi-synchronous calls. Its lifetime is managed by brpc."

> **Source: [[sources/client|client]]**
> - "Join可用来实现"半同步"访问：即等待多个异步访问完成。"
> - "brpc::DoNothing()可获得一个什么都不干的done，专门用于半同步访问。"
> - "brpc::Join(cntl1.call_id())"