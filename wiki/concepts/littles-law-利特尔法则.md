---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/avalanche.md]]"
  - "[[brpc/auto_concurrency_limiter.md]]"
tags:
  - "theory"
aliases:
  - "Little定理"
  - "利特尔法则"
  - "L = λW"
  - "Little's Law"
  - "Little定理"
  - "利特尔法则"
  - "L = λW"
---

## Related Concepts
- [[concepts/concurrency-limiting|Concurrency Limiting (限流)]]
- [[concepts/auto-concurrency-limiter|AutoConcurrencyLimiter (自动并发限制器)]]
- [[concepts/queueing-theory|排队论]]
- [[concepts/latency|延迟]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/en_server]]**
> - "max_concurrency = peak_qps * noload_latency ([little's law](https://en.wikipedia.org/wiki/Little%27s_law))"
> - "peak_qps is the maximum of Queries-Per-Second. noload_latency is the average latency measured in a server without pushing to its limit(with an acceptable latency)."
> - "peak_qps and nolaod_latency can be measured in pre-online performance tests and multiplied to calculate the max_concurrency."

> **Source: [[sources/avalanche]]**
> - "无论程序是同步还是异步，用户都可以通过最大qps * 非拥塞时的延时（秒）来评估最大并发，原理见little's law。"
> - "评估server的最大并发，设置合理的max_concurrency值。"

> **Source: [[sources/auto_concurrency_limiter]]**
> - "在服务处于稳定状态时: concurrency = latency * qps。 这是自适应限流的理论基础。"
> - "根据little's law，qps最多为max_qps * (1 + alpha). alpha是qps的"探索空间"。"