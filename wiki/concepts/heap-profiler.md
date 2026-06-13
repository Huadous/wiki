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
  - "堆剖析器"
  - "brpc Heap Profiler"
  - "堆内存分析器"
---

## Related Concepts
- [[concepts/cpu-profiler|CPU Profiler]]
- [[concepts/contention-profiler|Contention Profiler]]
- [[concepts/memory-leak|Memory Leak]]
- [[concepts/profiling|Profiling]]
- [[concepts/tcmalloc|tcmalloc]]
- [[concepts/内置服务|内置服务]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/bvar|bvar]]
- [[entities/baidu|baidu]]
- [[entities/tcmalloc|tcmalloc]]

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
> - "Debug services via http, and run cpu, heap and contention profilers."
> - "analyze [cpu hotspots](../cn/cpu_profiler.md), [heap allocations](../cn/heap_profiler.md) and [lock contentions](../cn/contention_profiler.md) of online services"

> **Source: [[sources/builtin_service|builtin_service]]**
> - "heap profiler: 分析内存占用。"

> **Source: [[sources/getting_started|getting_started]]**
> - "如果你要在样例中启用cpu/heap的profiler："
> - "这两个 profiler都是基于tcmalloc的。"