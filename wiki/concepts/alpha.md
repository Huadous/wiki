---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/auto_concurrency_limiter|auto_concurrency_limiter]]"]
tags: [term]
aliases:
  - "alpha 参数"
  - "可接受的延时上升幅度"
---


# alpha

## 定义
**alpha** 是 brpc 自适应限流（Adaptive Concurrency Limiter）核心公式中的可接受延时上升幅度参数，默认值为 **0.3**。它出现在公式 `max_concurrency = max_qps * ((2+alpha) * min_latency - latency)` 中，代表 qps 的"探索空间"（exploration space）：当 alpha 为 0 时，qps 被锁定为 max_qps，算法可能无法探索到 peak_qps。

## 关键特征
- **可接受的延时上升幅度**：alpha 表示系统允许延时在 min_latency 基础上的上升幅度，默认 0.3（即 30%）。
- **qps 探索空间**：在 latency 极为稳定并等于 min_latency 的理想情况下，公式可简化为 `max_concurrency = max_qps * latency * (1 + alpha)`，根据 Little's Law，qps 上限可达 `max_qps * (1 + alpha)`。
- **零值风险**：当 alpha 为 0 时，qps 被锁定为 max_qps，算法可能永远无法探索到实际的 peak_qps。
- **拥塞下的副作用**：alpha 的存在使得在 qps 未达到 peak_qps 时为流量上涨预留空间，但也会导致在已拥塞时延时上升，从而引发 min_latency 不收敛的问题。
- **缓解手段**：需要通过定期降低 max_concurrency 来缓解 alpha 带来的 min_latency 不收敛问题。

## 应用
- **brpc 自适应限流**：作为核心公式 `max_concurrency = max_qps * ((2+alpha) * min_latency - latency)` 中的关键参数，控制算法对并发上限的估算行为。
- **qps 探索与峰值探测**：通过为 qps 预留 (1 + alpha) 倍的探索空间，使算法有机会发现实际服务能承受的 peak_qps。
- **延时收敛控制**：在已发生拥塞的场景下，通过定期降级 max_concurrency 来对抗 alpha 导致的 min_latency 漂移。

## 相关概念
- [[concepts/max_concurrency]]
- [[concepts/min_latency]]
- [[concepts/max_qps]]
- [[concepts/noload_latency]]
- [[concepts/peak_qps]]
- [[concepts/Little's Law]]

## 相关实体
- [[entities/brpc]]

## 来源提及
- "alpha为可接受的延时上升幅度，默认0.3。" — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]
- "缩小max_concurrency和公式中的alpha存在关联。让我们做个假想实验，若latency极为稳定并都等于min_latency，那么公式简化为max_concurrency = max_qps * latency * (1 + alpha)。根据little's law，qps最多为max_qps * (1 + alpha). alpha是qps的"探索空间"，若alpha为0，则qps被锁定为max_qps，算法可能无法探索到peak_qps。" — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]