---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/auto_concurrency_limiter|auto_concurrency_limiter]]"]
tags: [term]
aliases:
  - "min_latency（brpc 自适应限流）"
  - "最小延迟 EMA"
---


# min_latency

## 定义
min_latency 是 brpc [[concepts/自适应限流|自适应限流]]（auto concurrency limiter）机制中的一个核心指标，指实际测定的 latency 中较小值的指数移动平均（[[concepts/EMA|EMA]]），用作 [[concepts/noload_latency|noload_latency]] 的估算值。当并发度（concurrency）不大于 `best_max_concurrency` 时，min_latency 与 noload_latency 的值较为接近（可能会有轻微上升）。其计算规则为：仅在当前测得的 latency 小于 min_latency 时才进行更新，通过 EMA 平滑以减少抖动影响。

## 关键特征
- **基于较小值采样**：min_latency 只取实际测得 latency 中的较小值进行平滑，过滤掉因排队或拥塞导致的高延迟样本。
- **仅在更优值出现时更新**：当本次测得的 latency 小于当前的 min_latency 时才触发更新，避免在系统出现拥塞时把高延迟样本引入估算。
- **指数移动平均（EMA）平滑**：采用 EMA 算法对较小值进行平滑处理，以减少瞬时抖动对估算结果的影响。
- **noload_latency 的近似估算**：在 concurrency 不大于 `best_max_concurrency` 的区间内，min_latency 接近真实的无负载延迟（noload_latency），因此可作为其在线估算值。
- **依赖周期性降级**：准确估算 min_latency 的关键挑战在于需要定期降低 [[concepts/max_concurrency|max_concurrency]]，为 min_latency 的下降提供探索空间；否则 min_latency 可能被历史较大值"卡住"而无法收敛到真实的 noload_latency。

## 应用
- **noload_latency 在线估算**：在无法直接停机测量 baseline latency 的在线系统中，min_latency 提供了一种持续近似服务无负载延迟的方案。
- **自适应并发度控制**：brpc 的 auto_concurrency_limiter 利用 min_latency 评估服务在低并发下的真实处理能力，从而更准确地推导 `best_max_concurrency`。
- **延迟基线动态跟踪**：用于在长时运行的分布式服务中跟踪延迟基线的漂移，及时反映服务性能随流量、版本或硬件变化的趋势。

## 相关概念
- [[concepts/自适应限流|自适应限流]]
- [[concepts/noload_latency|noload_latency]]
- [[concepts/EMA|EMA]]
- [[concepts/max_concurrency|max_concurrency]]

## 相关实体
- No related entities

## 来源提及
- min_latency: 实际测定的latency中的较小值的ema，当concurrency不大于best_max_concurrency时，min_latency和noload_latency接近(可能轻微上升）。 — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]
- min_latency是最近一段时间测量到的latency较小值的ema，是noload_latency的估算值。 — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]