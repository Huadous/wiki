---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client|en_client]]"
  - "[[brpc/client.md]]"
  - "[[brpc/bthread_or_not.md]]"
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
  - "同步接口"
  - "同步调用"
  - "Sync RPC"
  - "Synchronous RPC"
  - "同步访问"
  - "同步调用"
  - "Sync RPC"
  - "Synchronous RPC"
---

## Description
Synchronous call 是 brpc 客户端最直接的调用方式：调用线程发起 `CallMethod` 后会一直阻塞，直到收到服务端的响应或发生错误（包括超时）才返回。在同步访问中，`Response` 与 `Controller`（[[concepts/controller|Controller]]）对象在 `CallMethod` 返回后不会被 brpc 框架再次使用，因此可以安全地分配在栈上，无需额外的生命周期管理。文档对此明确警告：**禁止在持有 pthread 锁的情况下调用 brpc 的同步 `CallMethod`**，否则极易导致死锁；推荐的做法是将 pthread 锁替换为 [[concepts/bthread|bthread]] 锁，或在调用 `CallMethod` 之前先释放锁。同步访问通常通过 [[entities/brpc-channel|brpc::Channel]] 发起，配合 [[entities/brpc-controller|brpc::Controller]] 对象使用。

在接口选型上，[[sources/bthread_or_not|bthread_or_not]] 建议：**延时不高、QPS × latency 与 CPU 核数处于同一数量级时，应优先使用简单易懂的同步接口**；这也是 brpc 创建 bthread 的核心动机——让同步代码也能借助 bthread 提升交互性能，不会因为线程阻塞而浪费 CPU。文档给出的经验示例：当 `qps = 2000`、`latency = 10ms` 时，`qps × latency = 2000 × 0.01s = 20`，与常见的 32 核处于同一数量级，此时推荐使用同步接口。然而在**高并发、长延时**的场景下，同步调用会同时占用大量工作线程（每线程都有栈内存开销），造成资源压力，此时应转向 [[concepts/asynchronous-call|Asynchronous call]]（异步访问）或配合回调使用 bthread。与 [[concepts/asynchronous-call|Asynchronous call]] 和 [[concepts/half-synchronous-call|Half-synchronous call]] 相比，同步访问语义最简单，适合调用方需要同步获取 RPC 结果后才继续后续逻辑的线性场景。

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

> **Source: [[sources/bthread_or_not|bthread_or_not]]**
> - "延时不高时你应该先用简单易懂的同步接口"
> - "当然，延时不长，qps不高时，我们更建议使用同步接口，这也是创建bthread的动机：维持同步代码也能提升交互性能。"
> - "qps = 2000，latency = 10ms，计算结果 = 2000 * 0.01s = 20。和常见的32核在同一个数量级，用同步。"