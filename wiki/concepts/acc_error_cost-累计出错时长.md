---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/circuit_breaker]]"]
tags: [term]
aliases:
  - "累计出错成本"
  - "acc_error_cost"
  - "accumulated error cost"
---


# acc_error_cost (累计出错时长)

## 定义
acc_error_cost（累计出错时长）是 brpc 可选熔断策略（CircuitBreaker）中用于判断节点是否应被熔断的核心指标。它通过记录节点处理请求的累计出错成本，并结合衰减与增益机制，实现对节点健康状态的持续评估。当 acc_error_cost 超过动态计算的最大允许出错成本 `max_error_cost` 时，该节点会被熔断。

## 关键特征
- **累积性**：每次请求失败后，当前请求的 `min(latency, ema_latency * 2)` 被累加到 acc_error_cost 中，使得错误持续积累。
- **衰减性**：每次请求成功后，acc_error_cost 按照 `alpha * acc_error_cost` 进行衰减（`0 < alpha < 1`），允许短暂抖动后恢复正常。
- **阈值触发熔断**：当 `acc_error_cost > max_error_cost` 时触发熔断，其中 `max_error_cost` 基于 EMA 延迟动态计算。
- **平滑性**：设计上使得短暂的随机抖动不会立刻引发熔断，而持续的错误会逐渐累积直至触发保护。

## 应用
- 分布式服务调用的熔断保护：在 brpc 框架中，通过 acc_error_cost 实现对下游节点的熔断决策，避免请求持续打到已不可用的节点。
- 动态故障检测：结合 EMA 延迟估计，自适应判断节点是否处于不稳定状态，适用于高可用性场景。
- 负载均衡优化：在熔断器开启后，跳过已熔断节点，将流量导向健康节点，提升整体系统可用性。

## 相关概念
- [[concepts/max-error-cost|max_error_cost (最大出错时长)]]
- [[concepts/ema|EMA (指数移动平均)]]
- [[concepts/circuit-breaker-strategy|可选熔断策略]]

## 相关实体
- [[entities/circuitbreaker|circuitbreaker (brpc熔断器)]]
- [[entities/bvar|bvar (brpc多维统计库)]]

## 来源提及
- "可选的熔断由CircuitBreaker实现，在开启了熔断之后，CircuitBreaker会记录每一个请求的处理结果，并维护一个累计出错时长，记为acc_error_cost，当acc_error_cost > max_error_cost时，熔断该节点。" — [[sources/circuit_breaker|circuit_breaker]]
- "如果请求处理成功，则令 acc_error_cost = alpha * acc_error_cost" — [[sources/circuit_breaker|circuit_breaker]]
- "如果请求处理失败，则令 acc_error_cost = acc_error_cost + min(latency, ema_latency * 2)" — [[sources/circuit_breaker|circuit_breaker]]