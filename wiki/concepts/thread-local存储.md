---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar|bvar]]"]
tags: [method]
aliases:
  - "Thread Local Storage"
  - "TLS"
  - "thread local存储"
---


# thread local存储

## 定义
thread local存储（Thread Local Storage，TLS）是一种为每个执行线程提供独立变量副本的存储技术。它使得同一全局变量在不同的线程中拥有各自独立的实例，线程对自身副本的读写不会影响其他线程的副本。该技术被 [[concepts/cache-bouncing|cache bouncing]] 等问题的解决方案所利用，是 bvar 实现高性能多线程计数的关键基础。

## 关键特征
- **线程隔离性**：每个线程拥有变量的私有副本，线程间互不干扰
- **无竞争写入**：线程仅操作自己的私有变量，无需加锁或使用 [[concepts/原子操作|原子操作]]，彻底避免了多线程写竞争
- **避免 cache bouncing**：由于不存在跨 [[concepts/Cacheline|Cacheline]] 的共享写入，不同线程不会因缓存行失效而产生性能抖动
- **合并读取语义**：写入时各线程独立累加，读取时才将所有线程的私有副本合并为全局值
- **读写性能不对称**：写性能极高（接近无竞争），但读操作因需要遍历所有线程的私有数据而相对较慢

## 应用
thread local存储是 [[entities/bvar|bvar]] 设计哲学的核心实现手段。在多线程计数器场景下：
- **写入路径**：每个线程只累加自己 thread local 变量中的私有计数器，完全不参与全局竞争
- **读取路径**：在需要获取全局计数值时，遍历并汇总所有线程的私有变量
- **性能权衡依据**：计数器读多为低频操作（如监控、统计），写为高频操作，通过牺牲少量读性能换取极高的写性能

相较于 [[entities/UbMonitor|UbMonitor]] 等使用全局原子累加的老计数器库，bvar 利用 thread local存储几乎不会给程序增加性能开销，特别适合高并发写入的计数场景。

## 相关概念
- [[concepts/cache-bouncing|cache bouncing]]
- [[concepts/Cacheline|Cacheline]]
- [[concepts/原子操作|原子操作]]

## 相关实体
- [[entities/bvar|bvar]]
- [[entities/UbMonitor|UbMonitor]]

## 来源提及
- 它利用了thread local存储减少了cache bouncing，相比UbMonitor(百度内的老计数器库)几乎不会给程序增加性能开销 — [[sources/bvar|bvar]]
- 当很多线程都在累加一个计数器时，每个线程只累加私有的变量而不参与全局竞争，在读取时累加所有线程的私有变量 — [[sources/bvar|bvar]]