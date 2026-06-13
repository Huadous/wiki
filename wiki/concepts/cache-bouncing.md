---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar|bvar]]"]
tags: [phenomenon]
aliases:
  - "cache bouncing"
  - "缓存乒乓"
---


# cache bouncing

## 定义
cache bouncing（缓存乒乓）是指在多核 CPU 系统中，多个线程同时更新位于同一缓存行（Cacheline）内的共享数据时，由于 CPU 缓存一致性协议（如 MESI 协议）的介入，导致该缓存行在多个核心之间反复失效、重新加载和同步的现象。这种现象会使写入操作的延迟大幅增加，并随线程数的增长而显著恶化，严重制约多线程程序的并发性能。

## 关键特征
- **触发条件**：多个线程并发写入位于同一缓存行内的不同变量，即使这些变量在逻辑上彼此独立，也会因缓存行级别的伪共享（false sharing）而相互影响。
- **核心机制**：一个核心的写入会使其他核心中对应的缓存行失效（invalidate），迫使它们在下一次访问时重新从内存或另一个核心加载数据。
- **性能影响**：频繁的缓存行同步会消耗大量的总线带宽和 CPU 周期，使单次写入的开销从纳秒级上升到数十甚至上百纳秒。
- **扩展性差**：写入延迟与参与竞争的线程数近似呈线性增长，导致系统在多核扩展时难以获得理想的加速比。
- **与原子操作的关系**：原子计数器或共享累加器通常是 cache bouncing 的典型受害者。

## 应用
- **高性能计数器实现**：在 bvar 等监控/指标库中，通过采用 thread local 存储让每个线程只累加自己的私有副本，最终汇总时再合并，从而完全规避 cache bouncing，使单次写入开销维持在约 20 纳秒的低水平，且基本与线程数无关。
- **数据结构布局优化**：在高性能 C/C++ 程序设计中，常通过内存对齐、填充（padding）或将热数据与冷数据分离等方式，将并发写入的变量分布在不同的缓存行上，以消除伪共享。
- **多线程并发编程**：在锁竞争激烈或共享状态密集的系统中，识别并消除 cache bouncing 是提升多核扩展性的关键优化手段。
- **对比老式计数器库**：相比 UbMonitor 这类依赖全局原子计数器的实现，bvar 通过 thread local 方案几乎不带来额外的性能开销，体现了 cache bouncing 优化的实际价值。

## 相关概念
- [[concepts/cacheline|Cacheline]]
- [[concepts/thread-local-storage|thread local存储]]
- [[concepts/atomic-operation|原子操作]]
- [[concepts/false-sharing|伪共享]]
- [[concepts/cache-coherence-protocol|缓存一致性协议]]

## 相关实体
- [[sources/bvar|bvar]]
- [[sources/bvar_c++|bvar_c++]]

## 来源提及
- "它利用了thread local存储减少了cache bouncing，相比UbMonitor(百度内的老计数器库)几乎不会给程序增加性能开销" — [[sources/bvar|bvar]]
- "bvar的耗时基本和线程数无关，一直保持在极低的水平（~20纳秒）" — [[sources/bvar|bvar]]