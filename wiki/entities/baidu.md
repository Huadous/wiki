---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_overview]]"
tags:
  - "organization"
aliases:
  - "百度"
  - "baidu-rpc"
---

## Related Entities
- [[entities/bns|BNS]] — 百度内部使用的命名服务（Baidu Naming Service）
- [[entities/braft|braft]] — 百度贡献的基于brpc的Raft共识算法实现
- [[entities/brpc|brpc]] — 百度开发并开源的工业级RPC框架

## Related Concepts
- [[concepts/naming-service|Naming Service]] — 命名服务，BNS是百度内部使用的统一服务发现机制
- [[concepts/rpc|RPC]] — 远程过程调用，brpc的核心通信范式

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
- "An industrial-grade RPC framework used throughout Baidu, with 1,000,000+ instances(not counting clients) and thousands kinds of services, called 'baidu-rpc' inside Baidu."
- "Only C++ implementation is opensourced right now."
- "brpc is extensively used in Baidu: map-reduce service & table storages, high-performance computing & model training, all sorts of indexing & ranking servers."
- "Inside Baidu, we use BNS (Baidu Naming Service)."