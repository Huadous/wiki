---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bthread|bthread]]"]
tags: [term]
aliases:
  - "cache locality"
  - "缓存局部性"
  - "缓存亲和性"
---


# cache locality

## 定义
cache locality（缓存局部性）是衡量程序对CPU高速缓存（特别是 L1 / L2 / L3 缓存）利用效率的性能特征。它描述了程序在时间或空间上对相同内存区域的重复访问能否命中缓存，从而避免访问主存带来的高延迟。cache locality 是现代处理器架构与高性能线程库设计中的核心性能目标之一。

## 关键特征
- 关注 CPU 多级缓存（L1/L2/L3）的命中率与驻留效率，目标是让热点数据尽量驻留在靠近执行核心的缓存层中。
- 包括时间局部性（temporal locality）与空间局部性（spatial locality）两个维度。
- 线程资源（栈、寄存器状态等）越集中于越少的 CPU 核心集合上，cache locality 越好。
- 在 NUMA 架构下还涉及跨节点访问的亲和性，bthread 将"支持 NUMA"作为加分项明确提出。
- 是并发原语（如 channel、同步原语）设计中需要持续权衡的开销因素，再怎么优化也无法完全消除其带来的额外成本。

## 应用
- 在 brpc 的 [[sources/bthread|bthread]] 设计中，被列为关键设计目标："better cache locality, supporting NUMA is a plus"。
- 作为 M:N 线程模型的性能论据：M 个 bthread 映射到 N 个 [[concepts/pthread|pthread]]（N 远小于 M），使得每个 pthread 的栈与寄存器等热数据集中在更小的核心集合附近，从而获得比纯 pthread 模型更好的 cache locality。
- 在 [[concepts/上下文切换|上下文切换]] 与 [[concepts/M:N threading|M:N threading]] 设计中用于评估调度开销。
- 用于评估并发原语（如 channel、锁、消息队列）在切换与同步过程中对缓存的污染程度。

## 相关概念
- [[concepts/NUMA|NUMA]]
- [[concepts/pthread|pthread]]
- [[concepts/M:N threading|M:N threading]]
- [[concepts/上下文切换|上下文切换]]

## 相关实体
- [[entities/bthread|bthread]]
- [[entities/brpc|brpc]]

## 来源提及
- "better cache locality, supporting NUMA is a plus." — [[sources/bthread|bthread]]
- "bthread相比pthread的性能提升很大一部分来自更集中的线程资源。" — [[sources/bthread|bthread]]
- "这个再怎么优化，再怎么尊重cache locality，也是有明显开销的。" — [[sources/bthread|bthread]]