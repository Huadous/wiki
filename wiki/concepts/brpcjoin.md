---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [method]
aliases:
  - "brpc::Join()"
  - "Join()"
  - "JoinResponse()"
---


# brpc::Join

## 定义
`brpc::Join` 是 brpc 提供的一个函数，用于阻塞当前调用线程，直到指定的 RPC 彻底完成——包括用户自定义的 `done->Run()` 回调执行结束。该函数接收一个 `brpc::CallId`，该 CallId 必须在 RPC 发起**之前**通过 `Controller.call_id()` 取得（否则 `Controller` 可能已被 `done` 释放）。`Join` 是 brpc 中"半同步调用"模式的基础组件，调用方通常先发起多个异步 RPC，然后对每个 RPC 的 CallId 分别调用 `Join` 进行等待。

## 关键特征
- 阻塞直到 RPC 完成，并等待用户 `done->Run()` 回调运行结束。
- 如果在调用 `Join` 时 RPC 已经完成，则立即返回，不会阻塞。
- 多个线程可以同时对同一个 `CallId` 调用 `Join`，所有等待的线程都会被唤醒。
- 必须**在 RPC 发起前**通过 `Controller.call_id()` 获取 `CallId`，否则 `Controller` 可能已被释放而导致 `CallId` 失效。
- 历史上曾被命名为 `JoinResponse()`，旧代码编译报错时可将 `JoinResponse()` 直接重命名为 `Join()`。

## 应用
- **半同步调用模式**：在需要并发发起多个异步 RPC、又希望在当前线程同步等待全部结果时，对每个异步调用取 `call_id` 后依次 `Join`。
- **异步转同步的桥接**：在无法直接使用同步 `CallMethod` 的场景（例如需要自定义 `done` 回调的复杂流程）下，借助 `Join` 把异步流程在主线程上转为同步等待。
- **多线程汇合同一 RPC**：当多个工作线程需要等待同一个 RPC 完成（例如共享回调结果）时，可各自调用 `Join` 同一 `CallId`。

## 相关概念
- [[concepts/Controller]]
- [[concepts/Asynchronous call]]
- [[concepts/Synchronous call]]
- [[concepts/Cancel RPC]]

## 相关实体
- 无

## 来源提及
- "Join() blocks until completion of RPC and end of done->Run(), properties of Join: If the RPC is complete, Join() returns immediately. Multiple threads can Join() one id, all of them will be woken up." — [[sources/en_client]]
- "Join() was called JoinResponse() before, if you meet deprecated issues during compilation, rename to Join()." — [[sources/en_client]]