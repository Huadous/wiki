---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar|bvar]]"]
tags: [product]
aliases:
  - "百度UbMonitor"
  - "UbMonitor计数器库"
---


# UbMonitor

## 基本信息
- Type: product
- Source: [[sources/bvar|bvar]]

## 描述
UbMonitor 是百度内部的旧版计数器库，在 [[sources/bvar|bvar]] 文档中作为性能对比基准对象出现。[[sources/bvar|bvar]] 相比 UbMonitor 几乎不会给程序增加性能开销，其累加耗时基本和线程数无关，一直保持在约 20 纳秒的极低水平。而动态 UbMonitor 在 24 核时每次累加的耗时达到 7 微秒，这意味着使用 300 次 bvar 的开销才抵得上使用一次动态 UbMonitor 变量。UbMonitor 被作为 bvar 设计目标的反面参考，展示了 bvar 在多线程计数器场景下相对于传统计数器库以及 [[concepts/原子操作|原子操作]] 的显著性能优势，同时凸显了 [[concepts/cache bouncing|cache bouncing]] 对高频累加操作的严重影响。

## 相关实体
- [[entities/bvar|bvar]]

## 相关概念
- [[concepts/原子操作|原子操作]]
- [[concepts/cache bouncing|cache bouncing]]

## 来源提及
- 相比UbMonitor(百度内的老计数器库)几乎不会给程序增加性能开销，也快于竞争频繁的原子操作 — [[sources/bvar|bvar]]
- 下图是bvar和原子变量，静态UbMonitor，动态UbMonitor在被多个线程同时使用时的开销 — [[sources/bvar|bvar]]
- 而动态UbMonitor在24核时每次累加的耗时达7微秒，这意味着使用300次bvar的开销才抵得上使用一次动态UbMonitor变量 — [[sources/bvar|bvar]]