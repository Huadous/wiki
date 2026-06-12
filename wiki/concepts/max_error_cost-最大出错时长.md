---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/circuit_breaker]]"]
tags: [term]
aliases:
  - "最大出错成本"
  - "最大错误成本阈值"
---


# max_error_cost

## 定义

max_error_cost（最大出错时长）是 brpc 可选熔断策略中的一个动态阈值，用于与累计出错时长（acc_error_cost）进行比较，以决定是否熔断某个节点。该阈值在每次请求成功时基于最新的 EMA 延迟（ema_latency）自动更新：`max_error_cost = window_size * max_error_rate * ema_latency`。其中 `window_size` 和 `max_error_rate` 是通过 gflag 指定的常量。

## 关键特征

- **动态调整**：max_error_cost 随延迟变化而动态调整，无需手动配置固定阈值。
- **延迟自适应**：当延迟升高时，阈值相应提高，避免因延迟上升而误触发熔断；当延迟降低时，阈值降低，使系统对错误更加敏感。
- **基于 EMA 延迟**：依赖指数移动平均（EMA）计算的延迟值，对短期波动具有平滑效果。
- **与 acc_error_cost 配合**：熔断决策基于 `acc_error_cost > max_error_cost` 这一条件。

## 应用

- **RPC 服务熔断保护**：在 brpc 框架中，max_error_cost 作为可选熔断策略的核心参数，用于保护下游服务不被大量错误请求淹没。
- **自适应错误容忍**：适用于延迟波动较大的服务场景，如网络不稳定或负载变化明显的分布式系统。
- **动态阈值管理**：可替代静态熔断阈值，避免因延迟变化导致熔断策略失效。

## 相关概念

- [[concepts/acc_error_cost|acc_error_cost]]
- [[concepts/EMA|EMA]]
- [[concepts/可选熔断策略|可选熔断策略]]
- [[concepts/熔断|熔断]]

## 相关实体

- [[entities/brpc|brpc]]
- [[entities/circuitbreaker|circuitbreaker]]

## 来源提及

- "每次请求返回成功之后，更新max_error_cost: 首先需要更新latency的EMA值，记为ema_latency ... 之后根据ema_latency更新max_error_cost: max_error_cost = window_size * max_error_rate * ema_latency。" — [[sources/circuit_breaker|circuit_breaker]]
- "当acc_error_cost > max_error_cost时，熔断该节点。" — [[sources/circuit_breaker|circuit_breaker]]