---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
  - "[[brpc/auto_concurrency_limiter.md]]"
tags:
  - "method"
aliases:
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "Max concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "max_concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "Max concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "自适应限流算法"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "Max concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "max_concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "Max concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "自适应限流"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "Max concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "max_concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "Max concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "自适应限流算法"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "Max concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "max_concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "Max concurrency"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
  - "MaxConcurrencyOf"
  - "自动并发限制器"
  - "Auto Concurrency Limiter"
---

## Description
自适应限流是 brpc 在 method 级别提供的一种动态并发控制机制。在实际生产环境中，服务的最大并发度并非一成不变，而在每次上线前逐个压测并设置服务的最大并发非常繁琐。自适应限流算法通过将 `method_max_concurrency` 设置为 `"auto"` 来启用，能够根据当前负载情况自动调整最大并发度，从而在保证服务稳定性的同时减少运维成本。自适应限流解决了固定最大并发在复杂拓扑和变化负载场景下需要大量压测工作的问题，其核心目标是找到服务的 `noload_latency` 和 `peak_qps`，并将最大并发设置为靠近两者乘积的一个值。具体来说，算法基于 [[concepts/littles-law|Little's Law]] 估算这两个关键参数，并通过公式 `max_concurrency = max_qps * ((2+alpha) * min_latency - latency)` 动态计算最大并发度。该算法通常结合 EMA（指数移动平均）等统计方法以及类 netflix gradient 的思路对延迟和 QPS 进行平滑处理，从而在服务接近饱和时主动降低并发上限。

## Related Concepts
- [[concepts/littles-law|Little's Law]]
- 最大并发控制 (`max_concurrency`)
- `noload_latency`
- `peak_qps`
- netflix gradient 算法
- EMA (指数移动平均)

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: [[sources/server|server]]**
> - "实际生产环境中,最大并发未必一成不变，在每次上线前逐个压测和设置服务的最大并发也很繁琐。这个时候可以使用自适应限流算法。"
> - "// Set auto concurrency limiter for all methods
brpc::ServerOptions options;
options.method_max_concurrency = \"auto\";"

> **Source: [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]**
> - "自适应限流能动态调整服务的最大并发，在保证服务不过载的前提下，让服务尽可能多的处理请求。"
> - "自适应限流就是要找到服务的noload_latency和peak_qps， 并将最大并发设置为靠近两者乘积的一个值。"