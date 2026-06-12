---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/lalb]]"
tags:
  - "method"
aliases:
  - "DBD"
  - "双重缓冲数据"
  - "双缓冲数据"
---

## Related Concepts
- [[concepts/locality-aware-load-balancing|Locality-aware load balancing]]
- [[concepts/weight-tree|Weight tree]]
- [[concepts/thread-local-storage|Thread-local storage]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: [[sources/lalb|lalb]]**
> - "完成这些功能的数据结构是DoublyBufferedData<>，我们常简称为DBD。brpc中的所有load balancer都使用了这个数据结构，使不同线程在分流时几乎不会互斥。"
> - "数据分前台和后台。检索线程只读前台，不用加锁。只有一个写线程：修改后台数据，切换前后台，睡眠一段时间……"
> - "我们需要写以某种形式和读同步，但读之间相互没竞争。一种解法是，读拿一把thread-local锁，写需要拿到所有的thread-local锁。"