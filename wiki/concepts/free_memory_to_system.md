---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "term"
aliases:
  - "-free_memory_to_system_interval"
  - "空闲内存归还系统配置"
  - "ReleaseFreeMemory"
  - "-free_memory_to_system_interval"
  - "空闲内存归还系统配置"
---

## Description
`free_memory_to_system` 是 brpc 提供的一种内存管理机制，通过 gflag `-free_memory_to_system_interval` 控制程序定期尝试将空闲内存返还给操作系统。该值以秒为单位，若设为 0 或负数则禁用此功能，默认值为 0。建议当启用时设置值 ≥ 10 秒，以避免过于频繁释放内存导致性能损失。该特性基于 tcmalloc 的 `MallocExtension::instance()->ReleaseFreeMemory()` 实现，通过设置此 gflag 可以替代在程序中手动周期性调用`ReleaseFreeMemory()`方法。在长期运行的服务中，定期释放空闲内存有助于减少内存碎片和驻留集（RSS），降低内存使用峰值，尤其适用于处理大量短连接或临时大块内存分配的资源密集型场景。在云原生容器化部署环境中，控制内存占用可以避免因内存超限导致的重启或 OOM（内存不足）问题，提高内存利用率和服务稳定性。

## Related Concepts
- [[concepts/tcmalloc|tcmalloc]]
- [[concepts/并发限制|并发限制]]
- [[concepts/bvar|bvar]]
- [[concepts/serveroptions|ServerOptions]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
> - "Set gflag -free_memory_to_system_interval to make the program try to return free memory to system every so many seconds, values <= 0 disable the feature. Default value is 0. To turn it on, values >= 10 are recommended." — [[brpc/en_server|en_server]]
> - "This feature supports tcmalloc, thus `MallocExtension::instance()->ReleaseFreeMemory()` periodically called in your program can be replaced by setting this flag." — [[brpc/en_server|en_server]]