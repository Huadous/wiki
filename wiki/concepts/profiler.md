---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_overview]]"
  - "[[sources/builtin_service]]"
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

## 相关概念
- [[concepts/bvar|bvar]] — brpc的多维统计库，常与Profiler结合使用进行性能分析
- [[concepts/Builtin service|Builtin service]] — brpc内置的HTTP调试服务，Profiler通过该服务暴露分析接口
- [[concepts/Heap Profiler|Heap Profiler]] — brpc的堆内存分析器，与CPU Profiler配合定位内存问题
- [[concepts/Contention Profiler|Contention Profiler]] — brpc的锁竞争分析器，与CPU Profiler协同优化并发性能
- [[concepts/相关概念/rpcz|/rpcz]] — brpc内置服务中的RPC查看工具，可辅助分析调用链路

## 相关实体
- [[entities/brpc|brpc]] — 提供Profiler工具的RPC框架
- [[entities/baidu|baidu]] — brpc的原始开发组织
- [[entities/bvar|bvar]] — 多维统计库，常与Profiler搭配使用分析服务性能

## 来源提及
> **Source: [[sources/en_overview|en_overview]]**
- "Debug services [via http](builtin_service.md), and run [cpu](../cn/cpu_profiler.md), [heap](../cn/heap_profiler.md) and [contention](../cn/contention_profiler.md) profilers."
- "analyze [cpu hotspots](../cn/cpu_profiler.md), [heap allocations](../cn/heap_profiler.md) and [lock contentions](../cn/contention_profiler.md) of online services"

> **Source: [[sources/builtin_service|builtin_service]]**
- "cpu profiler: 分析cpu热点。"