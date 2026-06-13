---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_redis_client]]"
  - "[[concepts/单线程反应器]]"
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