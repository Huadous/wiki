---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/lalb]]"
tags:
  - "project"
aliases:
  - "百度DP系统"
  - "DP分布式系统平台"
  - "DP 2.0"
  - "百度DP系统"
  - "DP分布式系统平台"
  - "DP"
  - "百度DP系统"
  - "DP分布式系统平台"
  - "DP 2.0"
  - "百度DP系统"
  - "DP分布式系统平台"
---

## Description
DP是百度内部开发的分布式系统平台，主要用于解决大规模服务中的负载均衡与流量调度问题。在DP 2.0版本中，团队引入了一种名为Locality-aware load balancing（LALB）的创新算法，该算法能够根据下游节点的实际负载情况动态分配流量，并快速规避失效节点，显著提升了系统的稳定性和响应速度。经过DP系统中的实际业务场景验证，LALB算法后被集成至[[entities/brpc|brpc]]框架中，成为其核心组件之一。DP系统的实践为分布式系统领域提供了有价值的参考案例。

## Related Entities
- [[entities/brpc|brpc]] — LALB算法从DP系统迁移至brpc框架
- [[entities/dp系统|dp系统]] — DP系统本身（别名包含DP 2.0）

## Related Concepts
- [[concepts/lalb|lalb]] — DP 2.0中使用的Locality-aware load balancing算法
- [[concepts/延迟|延迟]] — 通过LALB算法降低响应时间
- [[concepts/qps|qps]] — 负载均衡直接影响每秒查询处理能力

## Mentions in Source
> **Source: [[sources/lalb]]**
- "该算法产生自DP系统，现已加入brpc！"
- "在DP 2.0中我们使用了一种新的算法: Locality-aware load balancing，能根据下游节点的负载分配流量，还能快速规避失效的节点"