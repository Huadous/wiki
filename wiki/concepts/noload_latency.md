---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/auto_concurrency_limiter|auto_concurrency_limiter]]"]
tags: [term]
aliases:
  - "无负载延时"
  - "noload latency"
---


# noload_latency

## 定义
noload_latency 是服务的固有属性，表示单纯处理任务所需的延时（不包括排队时间），也可理解为在低负载条件下观察到的延时。它由服务处理任务过程中必经的 CPU 计算时间或对下游调用的等待时间共同决定，是衡量服务自身处理能力的基础指标。

## 关键特征
- 反映服务在不发生排队时的最小处理延时，是服务处理能力的下界。
- 由服务自身执行逻辑（CPU 计算）与对下游依赖的等待时间共同构成。
- 并非静态不变，会随内存碎片、压力变化、业务数据特征变化等因素逐渐漂移。
- 在服务持续高负载场景下，实时观测到的延时难以区分「服务过载导致的排队延时」与「noload_latency 自身的上涨」，给准确估算带来困难。
- 正确估算 noload_latency 是自适应限流算法的核心难题之一。

## 应用
- 应用于 [[sources/auto_concurrency_limiter|auto_concurrency_limiter]] 等自适应限流系统，作为判定服务是否过载、动态调整最大并发度的关键输入参数。
- 与 [[concepts/min_latency|min_latency]]、[[concepts/Little's Law|Little's Law]]、[[concepts/best_max_concurrency|best_max_concurrency]] 等概念配合使用，共同构建并发度自动调优模型。
- 用于在线服务的容量评估与性能基准测试，剥离排队因素后评估服务真实处理效率。

## 相关概念
- [[concepts/自适应限流|自适应限流]]
- [[concepts/min_latency|min_latency]]
- [[concepts/Little's Law|Little's Law]]
- [[concepts/best_max_concurrency|best_max_concurrency]]

## 相关实体
无相关实体。

## 来源提及
- "noload_latency: 单纯处理任务的延时，不包括排队时间。另一种解释是低负载的延时。" — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]
- "服务的noload_latency并非是一成不变的，自适应限流必须能够正确的探测noload_latency的变化。" — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]