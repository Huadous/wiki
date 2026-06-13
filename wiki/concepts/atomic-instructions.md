---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[brpc/bvar.md]]"
tags:
  - "term"
aliases:
  - "Atomic Operations"
  - "Atomic Variables"
  - "原子操作"
---

## Related Concepts
- [[concepts/wait-free|Wait-Free]]
- [[concepts/work-stealing|Work Stealing]]
- [[concepts/bthread|Bthread]]
- [[concepts/lock-free|Lock-Free]]
- [[concepts/memory-ordering|Memory Ordering]]
- [[concepts/compare-and-swap|Compare-and-Swap (CAS)]]
- [[concepts/cache-bouncing|Cache Bouncing]]
- [[concepts/cacheline|Cacheline]]
- [[concepts/thread-local-storage|Thread Local 存储]]

## Related Entities
- [[entities/socket|Socket]]
- [[entities/socketid|SocketId]]
- [[entities/socketuniqueptr|SocketUniquePtr]]
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/bthread|Bthread]]
- [[entities/bvar|bvar]]
- [[entities/braft|braft]]
- [[entities/ubmonitor|UbMonitor]]

## Mentions in Source
> **Source: [[sources/en_io|en_io]]**
> - "To understand exactly how that atomic variable works, you can read atomic instructions first, then check Socket::StartInputEvent."

> **Source: [[sources/bvar|bvar]]**
> - "它利用了thread local存储减少了cache bouncing，相比UbMonitor(百度内的老计数器库)几乎不会给程序增加性能开销，也快于竞争频繁的原子操作"
> - "下图是bvar和原子变量，静态UbMonitor，动态UbMonitor在被多个线程同时使用时的开销"