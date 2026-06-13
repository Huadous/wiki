---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[sources/builtin_service]]"
  - "[[brpc/getting_started.md]]"
tags:
  - "term"
aliases:
  - "锁竞争分析器"
  - "Contention Profiler"
---

## Related Concepts
- [[concepts/cpu-profiler|CPU Profiler]]
- [[concepts/heap-profiler|Heap Profiler]]
- [[concepts/hotspot-analysis|熱點分析]]
- [[concepts/bthread|bthread]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/bvar|bvar]]
- [[entities/tcmalloc|tcmalloc]]

## Mentions in Source
> **來源: [[sources/en_overview|en_overview]]**
- "Debug services via http, and run cpu, heap and contention profilers."
- "analyze cpu hotspots, heap allocations and lock contentions of online services"
- "Users see very few contentions (via contention profiler) caused by RPC framework even if the service runs at 500,000+ QPS."

> **來源: [[sources/builtin_service|builtin_service]]**
- "contention profiler: 分析锁竞争。"

> **來源: [[sources/getting_started|getting_started]]**
- "而[contention profiler](contention_profiler.md)不需要tcmalloc。"