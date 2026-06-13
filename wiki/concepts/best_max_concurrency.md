---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/auto_concurrency_limiter|auto_concurrency_limiter]]"]
tags: [term]
aliases:
  - "最佳最大并发度"
  - "best_max_concurrency"
---


# best_max_concurrency

## 定义
best_max_concurrency 是并发的物理上限，即任务处理槽位（task processing slot）的天然上限。当一个服务的 noload_latency 和 peak_qps 都比较稳定时，best_max_concurrency 等于两者的乘积，即 best_max_concurrency = noload_latency × peak_qps。

## 关键特征
- 代表系统中并发处理能力的物理极限，由处理槽位数量决定
- 可通过 noload_latency × peak_qps 计算得出
- 是衡量 max_concurrency 设置是否合理的参考基准
- 当 max_concurrency 超过 best_max_concurrency 时，任务会在队列中排队等待，系统进入拥塞状态
- 当 max_concurrency 远小于 best_max_concurrency 时，系统无法达到最佳吞吐
- 自适应限流的目标就是使 max_concurrency 接近 best_max_concurrency
- 其理论依据是 Little's Law（L = λ × W），系统中的平均并发数等于到达率与平均处理时延的乘积

## 应用
- brpc 自适应限流（auto concurrency limiter）算法中的核心参考指标
- 作为评估系统是否处于拥塞状态或欠载状态的基准
- 指导 max_concurrency 动态调整，使系统始终工作在最优并发区间
- 服务容量规划与性能调优

## 相关概念
- [[concepts/自适应限流|自适应限流]]
- [[concepts/noload_latency|noload_latency]]
- [[concepts/peak_qps|peak_qps]]
- [[concepts/max_concurrency|max_concurrency]]
- [[concepts/Little's Law|Little's Law]]

## 相关实体
无相关实体。

## 来源提及
- "best_max_concurrency: 并发的物理含义是任务处理槽位，天然存在上限，这个上限就是best_max_concurrency。" — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]
- "假如一个服务的peak_qps和noload_latency都比较稳定，那么它的best_max_concurrency = noload_latency * peak_qps。" — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]