---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_server]]"]
tags: [theory]
aliases:
  - "Little定理"
  - "利特尔法则"
  - "L = λW"
---


# 利特尔法则

## 定义

利特尔法则是排队论中的一个基本定律，公式为 **L = λW**，其中：
- **L** 是系统中的平均任务数（并发数）
- **λ** 是平均到达率（如 QPS）
- **W** 是平均处理时间（延迟）

该定律在系统容量规划中用于计算服务器最大并发数：`max_concurrency = peak_qps * noload_latency`。

## 关键特征

- **线性关系**：系统中平均任务数与到达率及平均处理时间成正比
- **稳态适用**：假设系统处于统计平衡状态，到达率和处理时间稳定
- **通用性**：适用于任何稳定系统，无需假设具体分布
- **实用性**：只需测量两个可观测指标（峰值QPS和无负载延迟）即可估算并发限制

## 应用

- **限流阈值设定**：计算 `ServerOptions.max_concurrency` 或自动并发限制算法的目标值
- **系统容量规划**：在预上线性能测试中测量峰值QPS和无负载延迟，相乘得到合理的并发限制值
- **性能分析与诊断**：反向推导系统瓶颈，判断是到达率过高还是处理延迟过长
- **负载测试验证**：通过理论值与实测值对比，验证系统是否接近最优状态

## 相关概念

- [[concepts/concurrency-limiting|Concurrency Limiting (限流)]]
- [[concepts/auto-concurrency-limiter|AutoConcurrencyLimiter (自动并发限制器)]]
- [[concepts/queueing-theory|排队论]]
- [[concepts/latency|延迟]]

## 相关实体

- [[entities/brpc|brpc]]

## 来源提及

- "max_concurrency = peak_qps * noload_latency ([little's law](https://en.wikipedia.org/wiki/Little%27s_law))" — [[sources/en_server|en_server]]
- "peak_qps is the maximum of Queries-Per-Second. noload_latency is the average latency measured in a server without pushing to its limit(with an acceptable latency)." — [[sources/en_server|en_server]]
- "peak_qps and nolaod_latency can be measured in pre-online performance tests and multiplied to calculate the max_concurrency." — [[sources/en_server|en_server]]