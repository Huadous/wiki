---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/auto_concurrency_limiter|auto_concurrency_limiter]]"]
tags: [organization]
aliases:
  - "奈飞"
  - "Netflix"
  - "Inc."
---


# Netflix

## 基本信息
- Type: organization
- Source: [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]

## 描述
Netflix（奈飞）是一家全球知名的流媒体服务公司，在分布式系统与可观测性工程领域贡献了大量开源工具与设计模式，其中在自适应限流（adaptive concurrency limiting）方向提出的 gradient 算法被业界广泛引用与讨论。该算法的核心公式为 `max_concurrency = min_latency / latency * max_concurrency + queue_size`，旨在利用最小延迟近似无负载延迟（`noLoadLatency`）来动态调整最大并发度。在 [[sources/auto_concurrency_limiter|auto_concurrency_limiter]] 一文对其进行的对比分析中，作者指出 Netflix gradient 算法存在若干设计缺陷：即使采用最小值来代表无负载延迟，只要不对 `max_concurrency` 做定期衰减，无论最小值还是平均值都有可能持续上升，从而导致算法无法收敛。

## 相关实体
（暂无相关实体）

## 相关概念
- [[concepts/netflix-gradient-algorithm|netflix gradient算法]]
- [[concepts/adaptive-concurrency-limiting|自适应限流]]

## 来源提及
- "netflix中的gradient算法公式为：max_concurrency = min_latency / latency * max_concurrency + queue_size。" — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]
- "netflix的原意是最小值能更好地代表noload_latency，但实际上只要不对max_concurrency做定期衰减，不管最小值还是平均值都有可能不断上升使算法不收敛。" — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]