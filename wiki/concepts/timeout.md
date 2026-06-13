---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[sources/circuit_breaker]]"
  - "[[brpc/en_client.md]]"
tags:
  - "term"
aliases:
  - "超时"
  - "超时错误"
  - "RPC超时"
  - "超时"
  - "超时错误"
  - "Deadline"
  - "超时"
  - "超时错误"
  - "RPC超时"
  - "超时"
  - "超时错误"
---

## Related Concepts
- [[concepts/rpc|RPC]]
- [[concepts/retry|Retry]]
- [[concepts/connection-timeout|连接超时]]
- [[concepts/default-circuit-breaker-strategy|默认熔断策略]]
- [[concepts/optional-circuit-breaker-strategy|可选熔断策略]]
- [[concepts/acc-error-cost|acc_error_cost]]
- [[concepts/bthread|bthread]]
- [[concepts/backup-request|Backup Request]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/circuitbreaker|circuitbreaker]]

## Mentions in Source
> **Source: [[sources/en_client|en_client]]**
> - "ChannelOptions.timeout_ms is timeout in milliseconds for all RPCs via the Channel, Controller.set_timeout_ms() overrides value for one RPC. Default value is 1 second"
> - "timeout_ms in brpc is deadline, which means once it's reached, the RPC ends without more retries."
> - "error code of RPC timeout is ERPCTIMEDOUT (1008), ETIMEDOUT is connection timeout and retriable."
> - "As a comparison, other implementations may have session timeouts and deadline timeouts. Do distinguish them before porting to brpc."