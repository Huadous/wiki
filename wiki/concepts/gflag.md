---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/circuit_breaker]]"
  - "[[sources/builtin_service]]"
  - "[[sources/en_getting_started]]"
tags:
  - "standard"
aliases:
  - "gflags"
  - "全局标志"
  - "/flags"
  - "gflags"
  - "全局标志"
---

## Related Concepts
- [[concepts/optional-circuit-breaker|可选熔断策略]]
- [[concepts/long-window|长窗口]]
- [[concepts/short-window|短窗口]]
- [[concepts/isolation-time|隔离时间]]
- [[concepts/builtin-service|内置服务]]

## Related Entities
- [[entities/circuitbreaker|circuitbreaker]]
- [[entities/bvar|bvar]]
- [[entities/brpc|brpc]]
- [[entities/protobuf-runtime|protobuf-runtime]]
- [[entities/leveldb|leveldb]]

## Mentions in Source
> **Source: [[sources/circuit_breaker|circuit_breaker]]**
> - "上面的window_size和max_error_rate均为gflag所指定的常量"
> - "这个倍率同样可以通过gflag配置。"
> - "初始的隔离时间为100ms，最大的隔离时间和判断两次熔断是否为连续熔断的时间间隔都使用circuit_breaker_max_isolation_duration_ms控制，默认为30秒。"

> **Source: [[sources/builtin_service|builtin_service]]**
> - "/flags: 所有gflags的状态，可动态修改。"

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "gflags: Extensively used to define global options."
> - "Install common deps, gflags, protobuf, leveldb."
> - "gflags: 2.0-2.2.2"