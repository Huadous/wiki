---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/auto_concurrency_limiter]]"]
tags: [method]
aliases:
  - "Netflix Gradient"
  - "Netflix gradient 算法"
---


# netflix gradient算法

## 定义
Netflix gradient 算法是 Netflix 提出的自适应限流（adaptive concurrency limiting）算法，其核心公式为：

max_concurrency = min_latency / latency * max_concurrency + queue_size

该算法通过 `min_latency / latency` 这一"梯度"动态调整最大并发数 `max_concurrency`，使客户端在服务端延迟升高时自动降级并发量。

## 关键特征
- **自适应调整**：以 `min_latency / latency` 作为"梯度"因子，根据实时延迟动态调节 `max_concurrency`。
- **公式组成**：调整后的 `max_concurrency = (min_latency / latency) * max_concurrency + queue_size`，由比例项与队列项相加。
- **存在已知缺陷**（brpc 文档指出）：
  1. 使用 latency 的**最小值**而非平均值，导致结果不稳定。
  2. `max_concurrency / latency` 与实际 QPS 脱节，不能真实反映吞吐变化。
  3. `queue_size` 推荐取 `sqrt(max_concurrency)`，方向不合理。

## 应用
- 客户端对后端服务进行自适应限流，避免在服务端过载时继续堆积请求。
- 作为 Netflix 自适应并发控制的早期方案，用于保护下游服务。
- 后续 brpc 自适应限流算法针对其缺陷进行了改进，提供了更稳定的实现。

## 相关概念
- [[concepts/自适应限流]]
- [[concepts/min_latency]]
- [[concepts/max_concurrency]]

## 相关实体
- 无

## 来源提及
- netflix中的gradient算法公式为：max_concurrency = min_latency / latency * max_concurrency + queue_size。 — [[sources/auto_concurrency_limiter]]
- gradient算法的queue_size推荐为sqrt(max_concurrency)，这是不合理的。 — [[sources/auto_concurrency_limiter]]