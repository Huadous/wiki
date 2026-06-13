---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client|en_client]]"]
tags: [method]
aliases:
  - "同步调用"
  - "Sync RPC"
  - "Synchronous RPC"
---


# Synchronous call

## 定义
Synchronous call（同步调用）是 brpc 中的阻塞式 RPC 调用方式。客户端发起 `CallMethod` 后，调用线程会一直阻塞，直到收到服务端的响应或发生错误（包括超时）才返回。在同步调用模式下，`Response` 与 `Controller` 对象在 `CallMethod` 返回后不再被 brpc 使用，因此可以安全地分配在栈上。

## 关键特征
- **阻塞语义**：`CallMethod` 一直阻塞直到收到响应或出错（含超时）。
- **栈上安全**：`Response` 与 `Controller` 在 `CallMethod` 返回后即被 brpc 释放，可直接放在栈上，无需额外生命周期管理。
- **死锁风险**：文档明确警告，不应在持有 pthread 锁的情况下进行同步调用，否则极易造成死锁。
- **锁的替代方案**：推荐使用 bthread 锁，或在调用 `CallMethod` 前先释放 pthread 锁。

## 应用
- 简单的请求-响应场景，调用方需要同步获取 RPC 结果后才继续后续逻辑。
- 客户端逻辑较为线性的服务，无需并发等待多个 RPC 结果。
- 测试代码或调试场景，期望以最直接的方式观察一次调用的完整过程。
- 与异步调用（[[concepts/asynchronous-call|Asynchronous call]]）配合使用，根据业务是否需要等待结果灵活选择调用方式。

## 相关概念
- [[concepts/asynchronous-call|Asynchronous call]]
- [[concepts/controller|Controller]]
- [[concepts/timeout|Timeout]]
- [[concepts/bthread|bthread]]

## 相关实体
（无相关实体）

## 来源提及
- "CallMethod blocks until response from server is received or error occurred (including timedout)." — [[sources/en_client|en_client]]
- "response/controller in synchronous call will not be used by brpc again after CallMethod, they can be put on stack safely." — [[sources/en_client|en_client]]
- "WARNING: Do NOT use synchronous call when you are holding a pthread lock! Otherwise it is easy to cause deadlock." — [[sources/en_client|en_client]]