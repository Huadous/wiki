---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/circuit_breaker]]"]
tags: [method]
aliases:
  - "指数移动平均"
  - "Exponential Moving Average"
---


# EMA

## 定义
EMA (Exponential Moving Average，指数移动平均) 是一种用于平滑时间序列数据的加权移动平均方法，通过对近期数据赋予更高权重来更灵敏地反映趋势变化。在 brpc 的熔断器机制中，EMA 被用于计算平滑后的延迟值 (ema\_latency)，公式为：ema\_latency = ema\_latency * alpha + (1 - alpha) * latency，其中 alpha 是略小于 1 的平滑常数。

## 关键特征
- **指数加权**：历史数据点的权重呈指数衰减，越近的数据权重越高，相比简单移动平均能更快响应变化。
- **递归计算**：无需保留完整历史窗口，仅需存储前一时刻的 EMA 值即可递归更新，内存效率高。
- **平滑参数 alpha**：平滑常数 alpha 控制对新数据的敏感度——alpha 越接近 1，平滑效果越强，响应越慢；alpha 越小，对新数据越敏感。在 brpc 中，alpha 由窗口大小和 `circuit_breaker_epsilon_value` 共同决定。
- **延迟敏感度调优**：通过 EMA 平滑延迟，熔断器能够区分短暂的延迟抖动和持续的延迟恶化，从而减少误触发。

## 应用
- **brpc 熔断器指标计算**：在可选熔断策略中，EMA 平滑原始延迟值计算 `ema_latency`，用于更新 `max_error_cost` 并限制错误请求的延迟贡献，使熔断决策更鲁棒。
- **时间序列预测**：广泛应用于金融、物联网、运维监控等领域，用于预测短期趋势、噪声过滤和异常检测。
- **控制与信号处理**：在嵌入式系统和自动控制中用于滤波，如平滑传感器读数。

## 相关概念
- [[concepts/可选熔断策略|可选熔断策略]]
- [[concepts/alpha|alpha]]
- [[concepts/max-error-cost|max_error_cost]]
- [[concepts/latency|latency]]

## 相关实体
- [[entities/circuitbreaker|circuitbreaker]]

## 来源提及
- "首先需要更新latency的[EMA](https://en.wikipedia.org/wiki/Moving_average)值，记为ema_latency: ema_latency = ema_latency * alpha + (1 - alpha) * latency。" — [[sources/circuit_breaker|circuit_breaker]]
- "上面的window_size和max_error_rate均为gflag所指定的常量, alpha则是一个略小于1的常量，其值由window_size和下面提到的circuit_breaker_epsilon_value决定。" — [[sources/circuit_breaker|circuit_breaker]]