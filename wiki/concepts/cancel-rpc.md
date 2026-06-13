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
  - "StartCancel"
  - "RPC 取消"
  - "Cancel RPC Mechanism"
  - "brpc::StartCancel"
  - "StartCancel"
  - "RPC 取消"
  - "Cancel RPC Mechanism"
---

## Description
Cancel RPC 是 brpc 客户端用来主动终止一次尚未完成 RPC 的机制。其核心调用形式为 `brpc::StartCancel(call_id)`，其中 `call_id` 必须在 RPC 发起前通过 `Controller.call_id()` 提前获取，其他任何时机获取都可能存在 race condition。需要注意区分的是 `controller->StartCancel()` 被明确禁用且没有实际效果——该接口是 protobuf 默认提供的，但与 `controller` 对象的生命周期存在严重的竞争问题，因此 brpc 强制要求使用全局的 `brpc::StartCancel(call_id)` 形式。`StartCancel` 调用本身是异步的，调用完成后 RPC 并不会立即结束，调用方不应在此刻触碰 `Controller` 的任何字段或删除关联资源，真正的资源回收仍需在 `done->Run()` 中完成；如需原地等待 RPC 彻底结束，可调用 `Join(call_id)`。`call_id` 可以在另一个线程中被取消，同一 `call_id` 被多次取消或重复取消时只有一次生效。Cancel 属于纯客户端能力，server 端是否会随之取消对应的处理动作由 server cancelation 机制另行保证，与本功能相互独立。

## Related Concepts
- [[concepts/asynchronous-call|Asynchronous Call]]
- [[concepts/controller|Controller]]
- [[concepts/correlation-id|correlation_id]]
- [[concepts/异步访问|异步访问]]

## Related Entities
- [[entities/brpc-controller|brpc::Controller]]

## Mentions in Source
> **Source: [[sources/en_client|brpc Client 文档]]**
> - "brpc::StartCancel(call_id) cancels corresponding RPC, call_id must be got from Controller.call_id() before launching RPC"
> - "NOTE: it is brpc::StartCancel(call_id), not controller->StartCancel(), which is forbidden and useless."
> - "Cancel here is a client-only feature, the server-side may not cancel the operation necessarily"

> **Source: [[sources/client|brpc Client 文档]]**
> - "brpc::StartCancel(call_id)可取消对应的RPC，call_id必须在发起RPC前通过Controller.call_id()获得，其他时刻都可能有race condition。"
> - "注意：是brpc::StartCancel(call_id)，不是controller->StartCancel()，后者被禁用，没有效果。后者是protobuf默认提供的接口，但是在controller对象的生命周期上有严重的竞争问题。"