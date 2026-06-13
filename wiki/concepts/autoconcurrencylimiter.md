---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
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
---

## Description
自适应限流是 brpc 在 method 级别提供的一种动态并发控制机制。在实际生产环境中，服务的最大并发度并非一成不变，而在每次上线前逐个压测并设置服务的最大并发非常繁琐。自适应限流算法通过将 `method_max_concurrency` 设置为 `"auto"` 来启用，能够根据当前负载情况自动调整最大并发度，从而在保证服务稳定性的同时减少运维成本。具体算法细节可参见 `auto_concurrency_limiter.md`，该算法通常基于 Little's Law 等排队论原理进行动态调节。

## Related Concepts
- 最大并发控制
- [[concepts/littles-law|Little's Law]]
- 自适应限流

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/grpc|gRPC]]
- [[entities/echoservice|EchoService]]
- [[entities/myechoservice|MyEchoService]]
- [[entities/serviceoptions|serviceoptions]]
- [[entities/serveroptions|ServerOptions]]

## Mentions in Source
> **Source: [[sources/server|server]]**
> - "实际生产环境中,最大并发未必一成不变，在每次上线前逐个压测和设置服务的最大并发也很繁琐。这个时候可以使用自适应限流算法。"
> - "// Set auto concurrency limiter for all methods
brpc::ServerOptions options;
options.method_max_concurrency = \"auto\";"