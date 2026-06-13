---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/auto_concurrency_limiter|auto_concurrency_limiter]]"]
tags: [term]
aliases:
  - "queue size"
  - "队列大小"
---


# queue_size

## 定义
queue_size 是 Netflix gradient 限流算法公式中的参数之一，其公式为 `max_concurrency = min_latency / latency * max_concurrency + queue_size`。该参数在公式中作为对 max_concurrency 估计值的偏置项，用于描述系统中不可控的缓存空间（例如 socket 内部缓存）对并发上限的影响。

## 关键特征
- **Netflix 视角**：queue_size 被理解为 socket 等环节中不可控的缓存空间，与 max_concurrency 存在正向关系；推荐将其设为 `sqrt(max_concurrency)`。
- **brpc 自适应限流视角**：queue_size 实际意义是为 concurrency 上升留出的探索空间——并发从低到高增长时，在 max_concurrency 更新前不限制 qps 上升；并发高时则应缩小 queue_size 以防止进一步恶化延时，因此 queue_size 与并发应呈**反向**关系。
- **参数取值差异**：brpc 实现中不单独设置 queue_size，或仅使用常量，认为其作用微乎其微。
- **位置**：作为加性偏置项出现在 gradient 算法的迭代公式中。

## 应用
- 自适应限流算法中用于平滑 max_concurrency 的估计值，避免在延时波动时过度收/放并发。
- 在 Netflix gradient 算法中作为推荐项（`sqrt(max_concurrency)`）调节限流曲线的收敛行为。
- 在 brpc [[sources/auto_concurrency_limiter|auto_concurrency_limiter]] 等自适应限流实现中作为可选的微调项，常以常量替代以简化策略。

## 相关概念
- [[concepts/netflix-gradient算法|netflix gradient算法]]
- [[concepts/max_concurrency|max_concurrency]]
- [[concepts/min_latency|min_latency]]
- [[concepts/latency|latency]]
- [[concepts/自适应限流|自适应限流]]

## 相关实体
- [[entities/Netflix|Netflix]]
- [[entities/brpc|brpc]]

## 来源提及
- netflix中的gradient算法公式为：max_concurrency = min_latency / latency * max_concurrency + queue_size。 — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]
- gradient算法的queue_size推荐为sqrt(max_concurrency)，这是不合理的。netflix对queue_size的理解大概是代表各种不可控环节的缓存，比如socket里的，和max_concurrency存在一定的正向关系情有可原。但在我们的理解中，这部分queue_size作用微乎其微，没有或用常量即可。 — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]