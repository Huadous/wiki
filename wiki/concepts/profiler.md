---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[sources/builtin_service]]"
  - "[[brpc/getting_started.md]]"
tags:
  - "method"
aliases:
  - "性能剖析器"
  - "分析工具"
  - "brpc Profiler"
  - "CPU Profiler"
  - "性能剖析器"
  - "分析工具"
  - "brpc Profiler"
  - "CPU profiler"
  - "性能剖析器"
  - "分析工具"
  - "brpc Profiler"
  - "CPU Profiler"
  - "性能剖析器"
  - "分析工具"
  - "brpc Profiler"
  - "cpu profiler"
  - "性能剖析器"
  - "分析工具"
  - "brpc Profiler"
  - "CPU Profiler"
  - "性能剖析器"
  - "分析工具"
  - "brpc Profiler"
  - "CPU profiler"
  - "性能剖析器"
  - "分析工具"
  - "brpc Profiler"
  - "CPU Profiler"
  - "性能剖析器"
  - "分析工具"
  - "brpc Profiler"
---

## Related Concepts
- [[concepts/bvar|bvar]] — brpc 的多维统计库，常与 Profiler 结合使用进行性能分析
- [[concepts/Builtin service|Builtin service]] — brpc 内置的 HTTP 调试服务，Profiler 通过该服务暴露分析接口
- [[concepts/Heap Profiler|Heap Profiler]] — brpc 的堆内存分析器，与 CPU Profiler 共享 tcmalloc 底层依赖，配合定位内存问题
- [[concepts/Contention Profiler|Contention Profiler]] — brpc 的锁竞争分析器，与 CPU Profiler 协同优化并发性能
- [[concepts/相关概念/rpcz|/rpcz]] — brpc 内置服务中的 RPC 查看工具，可辅助分析调用链路

## Related Entities
- [[entities/brpc|brpc]] — 提供 CPU Profiler 工具的 RPC 框架
- [[entities/baidu|baidu]] — brpc 的原始开发组织
- [[entities/bvar|bvar]] — 多维统计库，常与 Profiler 搭配使用分析服务性能

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
- "Debug services [via http](builtin_service.md), and run [cpu](../cn/cpu_profiler.md), [heap](../cn/heap_profiler.md) and [contention](../cn/contention_profiler.md) profilers."
- "analyze [cpu hotspots](../cn/cpu_profiler.md), [heap allocations](../cn/heap_profiler.md) and [lock contentions](../cn/contention_profiler.md) of online services"

> **Source: [[sources/builtin_service|builtin_service]]**
- "cpu profiler: 分析cpu热点。"

> **Source: [[sources/getting_started|getting_started]]**
- "如果你要在样例中启用cpu/heap的profiler："
- "如果你要使用[cpu profiler](cpu_profiler.md)或[heap profiler](heap_profiler.md)，要链接`libtcmalloc_and_profiler.a`。"