---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_redis_client]]"
  - "[[concepts/单线程反应器]]"
  - "[[brpc/avalanche.md]]"
tags:
  - "term"
aliases:
  - "Queries Per Second"
  - "每秒查询数"
---

## Related Concepts
- [[concepts/延迟|延迟]]
- [[concepts/连接池|连接池]]
- [[concepts/批量命令|批量命令]]
- [[concepts/bthread|bthread]]
- [[concepts/单线程反应器|单线程反应器]]
- [[concepts/雪崩|雪崩]]
- [[concepts/拥塞|拥塞]]
- [[concepts/little's-law|Little's Law]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/redis|redis]]

## Mentions in Source

> **Source: [[sources/en_redis_client|en_redis_client]]**
> - "Accessing redis server at qps=18668 latency=50"
> - "Accessing redis server at qps=301212 latency=164"
> - "Accessing redis server at qps=411669 latency=483"

> **Source: [[sources/单线程反应器|单线程反应器]]**
> - "We can see a tremendous drop of QPS compared to the one using single connection above, and the redis-server has reached the CPU cap."

> **Source: [[sources/avalanche|avalanche]]**
> - "当流量超出服务的最大qps时，服务将无法正常服务；当流量恢复正常时（小于服务的处理能力），积压的请求会被处理。"
> - "A处的最大qps就从线程数 / 平均延时，降到了线程数 / 超时。"
> - "无论程序是同步还是异步，用户都可以通过最大qps * 非拥塞时的延时（秒）来评估最大并发。"