---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/client|client]]"]
tags: [term]
aliases:
  - "CallId"
  - "RPC调用ID"
---


# brpc::CallId

## 定义
`brpc::CallId` 是 brpc 中用于唯一标识一次 RPC 调用的不透明（opaque）类型。它通过 `Controller.call_id()` 在发起 RPC **之前**获取，作为异步等待与取消操作的句柄。

## 关键特征
- **唯一标识**：在同一次 RPC 调用生命周期内唯一标识该调用。
- **不透明类型**：用户无需也不应该解读其内部结构，只能将其作为句柄传递。
- **捕获时机敏感**：必须在调用 `CallMethod` 之前捕获，否则 RPC 发起后 `Controller` 随时可能被回调删除，导致 `call_id` 失效。
- **支持多线程 Join**：多个线程可以同时 `Join` 同一个 `call_id`，它们都会在对应 RPC 完成时被唤醒。
- **幂等性**：若对应 RPC 已经结束，`Join` 调用将立刻返回。
- **支持跨线程取消**：`call_id` 可以在另一个线程中被 `StartCancel` 取消。
- **预先取消**：甚至可以在 RPC 发起前就取消该 `call_id`，已取消 `call_id` 上的 RPC 会直接结束，`done` 回调仍会被调用。
- **与 race condition 相关**：除"发起 RPC 前"外的任何时刻通过 `Controller.call_id()` 访问，都可能存在 race condition。

## 应用
- **异步 RPC 同步等待**：发起 RPC 后在另一个线程通过 `brpc::Join(call_id)` 等待该调用完成。
- **跨线程取消 RPC**：通过 `brpc::StartCancel(call_id)` 从任意线程取消尚未结束或尚未发起的 RPC。
- **异步访问模式**：在 brpc 的异步访问场景中作为 RPC 的引用句柄，避免对 `Controller` 指针的生命周期依赖。
- **与 `correlation_id` 配合**：可与请求/响应上下文中的 `correlation_id` 协同使用，用于追踪与关联 RPC 调用。

## 相关概念
- [[concepts/brpc-join|brpc::Join]]
- [[concepts/brpc-startcancel|brpc::StartCancel]]
- [[concepts/异步访问|异步访问]]
- [[concepts/correlation-id|correlation_id]]

## 相关实体
- [[entities/brpc-controller|brpc::Controller]]
- [[entities/brpc-channel|brpc::Channel]]

## 来源提及
- `const brpc::CallId cid1 = controller1->call_id();` — [[sources/client|client]]
- `brpc::StartCancel(call_id)可取消对应的RPC，call_id必须**在发起RPC前**通过Controller.call_id()获得，其他时刻都可能有race condition。` — [[sources/client|client]]
- `**在发起RPC前**调用Controller.call_id()获得一个id，发起RPC调用后Join那个id。` — [[sources/client|client]]