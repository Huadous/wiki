---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/auto_concurrency_limiter|auto_concurrency_limiter]]"]
tags: [term]
aliases:
  - "max_qps"
  - "最大 QPS"
---


# max_qps

## 定义
max_qps 是最近一段时间测定的实际 QPS（Queries Per Second，每秒查询数）极大值。它表示在过去一段时间窗口内观察到的 QPS 上限值，反映系统在运行过程中所能达到的实际吞吐量峰值。

## 关键特征
- max_qps 表示实际测定的 QPS 中的较大值，取自最近一段时间窗口的观测数据。
- 由于 QPS 具有物理上限，max_qps 始终小于等于 [[concepts/peak_qps|peak_qps]]，不论系统是否处于拥塞状态。
- 在 [[concepts/自适应限流|自适应限流]] 算法中，max_qps 是计算 [[concepts/max_concurrency|max_concurrency]] 的核心输入之一。
- max_qps 在计算过程中采用 EMA（Exponential Moving Average，指数移动平均）平滑处理，但其 EMA 平滑参数仅为 [[concepts/min_latency|min_latency]] 的十分之一。
- 之所以采用较小的 EMA 平滑参数，是因为 max_qps 下降不一定代表系统极限下降，而 min_latency 下降通常意味着 noload_latency 确实下降，因此需要更敏感地追踪 max_qps 的变化。

## 应用
- 应用于 brpc 的 [[sources/auto_concurrency_limiter|auto_concurrency_limiter]] 自适应限流机制，作为评估系统实际处理能力的关键指标。
- 用于在自适应限流算法中推导 [[concepts/max_concurrency|max_concurrency]]，从而动态调整并发控制阈值。
- 与 [[concepts/peak_qps|peak_qps]] 配合使用，区分理论极限与实际可达吞吐量。

## 相关概念
- [[concepts/自适应限流]]
- [[concepts/peak_qps]]
- [[concepts/EMA]]
- [[concepts/max_concurrency]]
- [[concepts/min_latency]]

## 相关实体
无相关实体。

## 来源提及
- "max_qps: 实际测定的qps中的较大值。由于qps具有上限，max_qps总是会小于peak_qps，不论拥塞与否。" — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]
- "max_qps是最近一段时间测量到的qps的极大值。" — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]