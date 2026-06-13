---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [method]
aliases:
  - "半同步调用"
  - "Semi-synchronous call"
---


# Semi-synchronous call

## 定义
Semi-synchronous call 是 brpc 提供的一种 RPC 调用模式，通过 `brpc::Join()` 配合 `brpc::DoNothing()`（一个不执行任何操作的 closure）等待多个异步调用完成。该模式在调用方发起请求时是非阻塞的（表现为异步调用），但在调用方线程上会阻塞等待直到所有 RPC 全部完成，因此兼具异步调用与同步调用的特性。

## 关键特征
- 调用方在发起多个 RPC 后会阻塞，直到全部 RPC 完成才继续执行。
- 由于调用点会阻塞至所有 RPC 完成，`controller` 和 `response` 可以安全地放在栈上而无需堆分配或额外生命周期管理。
- 配合 `brpc::DoNothing()` 使用；`doNothing` 不会删除 `controller`，因此即便在 RPC 完成后访问 `controller.call_id()` 也是安全的。
- `brpc::DoNothing()` 返回的 closure 由 brpc 管理其生命周期，调用方无需手动释放。
- 特别适合在同一线程内并发发起多个 RPC 并等待其全部完成的场景。

## 应用
- 在单个线程中并行发起多个相互独立的 RPC 请求，并统一等待所有结果汇合后再进行后续处理。
- 希望避免异步回调的复杂性，但又不希望对每个 RPC 都进行单独同步阻塞的场景。
- 需要将 `controller` 与 `response` 对象安全地保存在栈上的批量请求场景。
- 适用于 fan-out 式的请求模式：先并发分发请求，再统一汇聚响应结果。

## 相关概念
- [[concepts/asynchronous-call|Asynchronous call]]
- [[concepts/synchronous-call|Synchronous call]]
- [[concepts/brpc-join|brpc::Join]]

## 相关实体
- [[entities/channel|Channel]]
- [[entities/controller|Controller]]
- [[entities/brpcdonothing|brpc::DoNothing]]

## 来源提及
- Join can be used for implementing "Semi-synchronous" call: blocks until multiple asynchronous calls to complete. — [[sources/en_client]]
- Since the callsite blocks until completion of all RPC, controller/response can be put on stack safely. — [[sources/en_client]]
- brpc::DoNothing() gets a closure doing nothing, specifically for semi-synchronous calls. Its lifetime is managed by brpc. — [[sources/en_client]]