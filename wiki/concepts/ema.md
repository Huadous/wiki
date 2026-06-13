---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/circuit_breaker]]"
  - "[[brpc/auto_concurrency_limiter.md]]"
tags:
  - "method"
aliases:
  - "指数移动平均"
  - "Exponential Moving Average"
---

## Related Concepts
- [[concepts/可选熔断策略|可选熔断策略]]
- [[concepts/alpha|alpha]]
- [[concepts/max-error-cost|max_error_cost]]
- [[concepts/latency|latency]]
- [[concepts/自适应限流|自适应限流]]
- [[concepts/min-latency|min_latency]]
- [[concepts/max-qps|max_qps]]

## Related Entities
- [[entities/circuitbreaker|circuitbreaker]]

## Mentions in Source

> **Source: [[sources/circuit_breaker|circuit_breaker]]**
> - "首先需要更新latency的[EMA](https://en.wikipedia.org/wiki/Moving_average)值，记为ema_latency: ema_latency = ema_latency * alpha + (1 - alpha) * latency。"
> - "上面的window_size和max_error_rate均为gflag所指定的常量, alpha则是一个略小于1的常量，其值由window_size和下面提到的circuit_breaker_epsilon_value决定。"

> **Source: [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]**
> - "为了减少个别窗口的抖动对限流算法的影响，同时尽量降低计算开销，计算min_latency时会通过使用EMA来进行平滑处理"
> - "将max_qps的ema参数置为min_latency的ema参数的十分之一的原因是: max_qps 下降了通常并不意味着极限qps也下降了。而min_latency下降了，通常意味着noload_latency确实下降了。"