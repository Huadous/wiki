---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/lalb]]"
tags:
  - "product"
aliases:
  - "UB框架"
  - "百度UB"
  - "UB中间件"
---

## Related Entities

- [[entities/brpc|brpc]] — UB与brpc同属百度内部技术栈，LALB文档中以UB为对比对象分析其不足。

## Related Concepts

- [[concepts/lalb|lalb]] — Locality-Aware Load Balancing，在LALB文档中与UB的WeightedStrategy进行对比，展示自适应负载均衡的优势。
- [[concepts/weightedstrategy|weightedstrategy]] — UB中基于CPU占用率进行分流的负载均衡策略，存在更新频率低和权值转换不准确的问题。
- [[concepts/延迟|延迟]] — WeightedStrategy未能有效解决的问题，LALB则更加注重延时感知。

## Mentions in Source

> **Source: lalb**
- "框架层面也有过一些努力，比如UB中的WeightedStrategy是根据下游的cpu占用率来进行分流，但明显地它解决不了延时相关的问题，甚至cpu的问题也解决不了：因为它被实现为定期reload一个权值列表"
- "框架层面也有过一些努力，比如UB中的WeightedStrategy是根据下游的cpu占用率来进行分流"