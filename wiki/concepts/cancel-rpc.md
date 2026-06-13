---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [method]
aliases:
  - "StartCancel"
  - "RPC 取消"
  - "Cancel RPC Mechanism"
---


# Cancel RPC

## 定义
Cancel RPC 是 brpc 提供的一种客户端主动取消正在进行的 RPC 调用的机制。其核心接口为 `brpc::StartCancel(call_id)`，通过该接口可以根据 RPC 的唯一标识 `call_id` 主动取消一次尚未完成的 RPC。该机制仅作用于客户端，并不能保证服务端也取消正在执行的操作。

## 关键特征
- **调用接口**：`brpc::StartCancel(call_id)` 取消对应的 RPC；`call_id` 必须在 RPC 发起前通过 `Controller.call_id()` 获取，否则存在竞态问题。
- **使用注意**：是 `brpc::StartCancel(call_id)`，而非 `controller->StartCancel()`，后者被禁用且无实际效果。
- **异步性**：调用 `StartCancel` 后并不代表 RPC 立即结束，仍需在 `done->Run()` 中进行资源回收；如需原地等待完成可调用 `Join(call_id)`。
- **线程安全**：同一 `call_id` 可被多个线程同时取消，但最终只有一个调用生效。
- **作用范围**：仅作用于客户端，并不能保证服务端也取消正在执行的操作。

## 应用
- **客户端超时控制**：当客户端检测到某次 RPC 耗时过长或已无业务意义时，可主动调用 `StartCancel` 释放关联资源。
- **资源回收**：在异步调用场景下，通过在 `done->Run()` 中完成资源回收，配合 `StartCancel` 实现协作式取消。
- **并发取消**：在多线程协作场景中，多个线程可同时对同一 `call_id` 发起取消请求，由 brpc 内部保证仅一个生效。
- **原地等待**：取消后若需要同步等待 RPC 完全结束，可调用 `Join(call_id)` 阻塞至 `done->Run()` 执行完毕。

## 相关概念
- [[concepts/asynchronous-call|Asynchronous Call]]
- [[concepts/controller|Controller]]

## 相关实体
（暂无相关实体）

## 来源提及
- "brpc::StartCancel(call_id) cancels corresponding RPC, call_id must be got from Controller.call_id() before launching RPC" — [[sources/en_client]]
- "NOTE: it is brpc::StartCancel(call_id), not controller->StartCancel(), which is forbidden and useless." — [[sources/en_client]]
- "Cancel here is a client-only feature, the server-side may not cancel the operation necessarily" — [[sources/en_client]]