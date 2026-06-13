---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar|bvar]]"]
tags: [term]
aliases:
  - "缓存行"
  - "Cache Line"
---


# Cacheline

## 定义
Cacheline（缓存行）是 CPU 缓存与主内存之间数据传输的最小单位。在 brpc 的 bvar 文档中，Cacheline 被视为理解多线程计数器性能的关键前置概念。

## 关键特征
- 是 CPU 缓存（Cache）进行数据读写时的最小粒度单位
- 当多个线程同时修改位于同一缓存行上的数据时，会触发缓存一致性协议（如 MESI），导致该缓存行在多个 CPU 核心之间反复失效与重新加载，即产生 [[concepts/cache-bouncing|cache bouncing]] 现象
- 频繁的 cache bouncing 会使多线程并发计数器的性能急剧下降，远低于理论并发加速比
- 通过让每个线程操作独立的缓存行（thread local 存储）可以避免伪共享（false sharing），从而消除 cache bouncing

## 应用
- **多线程计数器优化**：bvar 等高性能多线程计数库通过 thread local 存储让每个线程拥有独立的缓存行，避免全局竞争，将 cache bouncing 带来的性能损失降至最低
- **数据结构设计**：在设计高并发数据结构时，合理安排字段在缓存行中的位置（cache line padding / alignment），将高频写操作的字段分散到不同缓存行，可显著提升并发性能
- **性能分析**：在排查多线程程序的性能瓶颈时，伪共享是常见但容易被忽略的因素，理解 cacheline 有助于使用 `perf` 等工具定位问题

## 相关概念
- [[concepts/cache-bouncing|cache bouncing]]
- [[concepts/thread-local-storage|thread local 存储]]
- [[concepts/atomic-operation|原子操作]]

## 相关实体
- [[sources/bvar|bvar]]

## 来源提及
- "为了理解bvar的原理，你得先阅读Cacheline这节，其中提到的计数器例子便是bvar" — [[sources/bvar|bvar]]
- "当很多线程都在累加一个计数器时，每个线程只累加私有的变量而不参与全局竞争" — [[sources/bvar|bvar]]