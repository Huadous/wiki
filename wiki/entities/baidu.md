---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[brpc/bthread.md]]"
tags:
  - "organization"
aliases:
  - "百度"
  - "baidu-rpc"
---

## Related Entities
- [[entities/bns|BNS]] — 百度内部使用的命名服务（Baidu Naming Service）
- [[entities/braft|braft]] — 百度贡献的基于 brpc 的 Raft 共识算法实现
- [[entities/brpc|brpc]] — 百度开发并开源的工业级 RPC 框架
- [[entities/bthread|bthread]] — 百度开发并开源的 M:N 线程库
- [[entities/uba-server|uba server]] — 百度内部对异步框架的一次尝试（注意是 ub**a**server 而非 ubserver）

## Related Concepts
- [[concepts/naming-service|Naming Service]] — 命名服务，BNS 是百度内部使用的统一服务发现机制
- [[concepts/rpc|RPC]] — 远程过程调用，brpc 的核心通信范式
- [[concepts/m-n-threading|M:N Threading]] — bthread 采用的线程模型，针对运行时间不确定的协作服务场景设计
- [[concepts/coroutine|Coroutine]] — 协程；百度场景中纯协程会被一个缓慢的函数卡住所有协程
- [[concepts/event-loop|Event Loop]] — ub**a**server 异步框架由多个并行 eventloop 组成，但表现糟糕

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
- "An industrial-grade RPC framework used throughout Baidu, with 1,000,000+ instances(not counting clients) and thousands kinds of services, called 'baidu-rpc' inside Baidu."
- "Only C++ implementation is opensourced right now."
- "brpc is extensively used in Baidu: map-reduce service & table storages, high-performance computing & model training, all sorts of indexing & ranking servers."
- "Inside Baidu, we use BNS (Baidu Naming Service)."

> **Source: [[sources/bthread|bthread]]**
- "百度内大部分在线服务的运行时间并不确定，且很多检索由几十人合作完成，一个缓慢的函数会卡住所有的协程。"
- "ub**a**server（注意那个a，不是ubserver）是百度对异步框架的尝试，由多个并行的eventloop组成，真实表现糟糕：回调里打日志慢一些，访问redis卡顿，计算重一点，等待中的其他请求就会大量超时。"
- "所以这个框架从未流行起来。"