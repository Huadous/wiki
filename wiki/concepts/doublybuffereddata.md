---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/lalb]]"
  - "[[brpc/load_balancing.md]]"
tags:
  - "method"
aliases:
  - "DBD"
  - "双重缓冲数据"
  - "双缓冲数据"
---

## Description
DoublyBufferedData 是 brpc 框架中用于解决 LoadBalancer 多线程并发访问互斥问题的关键技术。其核心设计思想是维护两份完全相同的数据副本——前景（foreground）和背景（background）。检索线程只读取前景数据，无需加锁；写入操作由单个写线程负责，在锁保护下修改后台数据，然后原子地切换前后台角色，并睡眠一段时间以确保所有先前持有的前景引用都已失效。这种设计使不同线程在执行负载均衡时几乎不会产生互斥竞争，读操作之间也完全无竞争。

在 brpc 中，所有 LoadBalancer 都基于 DoublyBufferedData 实现，使得负载均衡决策能够高效地在多线程环境下执行。为了处理读写同步，DoublyBufferedData 还引入了 thread-local 锁机制：读操作获取对应的 thread-local 锁，而写操作则需要获取所有 thread-local 锁，从而在保证数据一致性的同时最大化并发性能。这一设计是 brpc 实现高性能 RPC 框架的重要技术支撑之一，也是其 Locality-aware load balancing 等高级特性得以高效运行的基础。

## Related Concepts
- [[concepts/locality-aware-load-balancing|Locality-aware load balancing]]
- [[concepts/weight-tree|Weight tree]]
- [[concepts/thread-local-storage|Thread-local storage]]
- [[concepts/load-balancing|Load balancing]]
- [[concepts/loadbalancer|LoadBalancer]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: [[sources/lalb|lalb]]**
> - "完成这些功能的数据结构是DoublyBufferedData<>，我们常简称为DBD。brpc中的所有load balancer都使用了这个数据结构，使不同线程在分流时几乎不会互斥。"
> - "数据分前台和后台。检索线程只读前台，不用加锁。只有一个写线程：修改后台数据，切换前后台，睡眠一段时间……"
> - "我们需要写以某种形式和读同步，但读之间相互没竞争。一种解法是，读拿一把thread-local锁，写需要拿到所有的thread-local锁。"

> **Source: [[sources/load_balancing|load_balancing]]**
> - "Load balancer最重要的是如何让不同线程中的负载均衡不互斥，解决这个问题的技术是DoublyBufferedData。"