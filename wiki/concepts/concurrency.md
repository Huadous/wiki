---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/auto_concurrency_limiter|auto_concurrency_limiter]]"]
tags: [term]
aliases:
  - "并发度"
  - "concurrency"
---


# concurrency

## 定义
concurrency（并发度）是指服务同时处理的请求数量，是 brpc 自适应限流算法中最核心的被测量和控制对象。在自适应限流体系中，concurrency 与 latency、qps 共同构成 Little's Law 的三要素：当服务稳定时，concurrency = latency × qps。concurrency 存在一个物理上限即 best_max_concurrency，超过该上限则任务无法被及时处理而暂存在队列中，系统将进入拥塞状态。

## 关键特征
- **物理含义是任务处理槽位**：concurrency 天然存在上限，即 best_max_concurrency，对应服务在不出现排队时所能同时处理的最大请求数。
- **拥塞判断依据**：若实际 concurrency 超过 best_max_concurrency，超出部分任务将被暂存在各种队列中排队等待处理，系统进入拥塞状态。
- **自适应限流的核心控制对象**：自适应限流通过动态调整 max_concurrency，使实际 concurrency 始终贴近 best_max_concurrency，从而在保证服务不过载的前提下最大化吞吐量。
- **低负载时具有探索空间**：当服务处于低负载时，min_latency 约等于 noload_latency，此时计算出来的 max_concurrency 会高于当前 concurrency 但仍低于 best_max_concurrency，为流量上涨预留了探索空间。
- **Little's Law 三要素之一**：与 latency、qps 共同决定系统的稳态行为，三者满足 concurrency = latency × qps。

## 应用
- **brpc 自适应限流（auto concurrency limiter）**：作为核心被测量，concurrency 被实时采样并用于计算 max_concurrency，驱动自适应限流算法的反馈调节。
- **容量评估与调优**：通过观测实际 concurrency 与 best_max_concurrency 的差距，运维人员可以判断服务是否接近容量瓶颈，是否需要扩容或限流。
- **过载保护**：当 concurrency 逼近或超过 best_max_concurrency 时触发限流动作，防止请求堆积导致延迟激增和服务雪崩。

## 相关概念
- [[concepts/max_concurrency|max_concurrency]]
- [[concepts/best_max_concurrency|best_max_concurrency]]
- [[concepts/noload_latency|noload_latency]]
- [[concepts/min_latency|min_latency]]
- [[concepts/peak_qps|peak_qps]]
- [[concepts/max_qps|max_qps]]
- [[concepts/Little's Law|Little's Law]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- **concurrency**: 同时处理的请求数，又被称为"并发度"。 — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]
- 并发的物理含义是任务处理槽位，天然存在上限，这个上限就是 best_max_concurrency。若 max_concurrency 设置的过大，则 concurrency 可能大于 best_max_concurrency，任务将无法被及时处理而暂存在各种队列中排队，系统也会进入拥塞状态。 — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]
- 当服务处于低负载时，min_latency 约等于 noload_latency，此时计算出来的 max_concurrency 会高于 concurrency，但低于 best_max_concurrency，给流量上涨留探索空间。 — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]