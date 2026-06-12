---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
tags:
  - "product"
aliases:
  - "brpc bvar"
  - "bvar多维统计库"
---

## Related Entities

- [[entities/brpc|brpc]]
- [[entities/curl|curl]]

## Related Concepts

- [[concepts/性能分析|性能分析]]
- [[concepts/CPU Profiler|CPU Profiler]]
- [[concepts/Heap Profiler|Heap Profiler]]
- [[concepts/Contention Profiler|Contention Profiler]]
- [[concepts/Builtin Service|Builtin Service]]

## Mentions in Source

> **Source: [[sources/en_server]]**
> - "bvar能够记录性能计数器，即使在高QPS（500,000+）下也几乎没有任何内容竞争"
> - "通过/vars路径可以在浏览器中查看bvar数据"
> - "默认显示80、90、99、99.9、99.99百分位的延迟数据"
> - "在fork场景下，采样线程会消失导致bvar数据为零，最新版本brpc会在必要时重新创建该线程"

> **Source: [[sources/en_overview]]**
> - "measure stats by [bvar](bvar.md) which is viewable in [/vars](vars.md)."