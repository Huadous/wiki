---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/lalb]]"
tags:
  - "term"
aliases:
  - "基础权值"
  - "base_weight 公式"
  - "LALB 基础权值"
  - "循环队列"
  - "基础权值"
  - "base_weight 公式"
  - "LALB 基础权值"
---

## Related Concepts
- [[concepts/locality-aware-load-balancing|Locality-Aware Load Balancing]]
- [[concepts/inflight-delay|inflight delay]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: [[sources/lalb|lalb]]**
- “权值的计算方法是 `base_weight = QPS * WEIGHT_SCALE / latency ^ p`。”
- “权值计算在各个环节都有最小值限制，为了防止某个节点的权值过低而使其完全没有访问机会。”
- “除了待删除节点，所有节点的权值绝对不会为0。”
- “权值的计算方法是 base_weight = QPS * WEIGHT_SCALE / latency ^ p。”
- “权值计算在各个环节都有最小值限制，为了防止某个节点的权值过低而使其完全没有访问机会。”