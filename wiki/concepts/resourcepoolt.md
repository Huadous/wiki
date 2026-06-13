---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management.md]]"]
tags: [method]
aliases:
  - "ResourcePool"
  - "brpc ResourcePool"
---


# ResourcePool<T>

## 定义

ResourcePool<T> 是 brpc 中的核心内存分配模板类，专为等长（fixed-size）对象的分配与回收而设计。它通过批量分配降低单次开销，通过 thread-local free block 与全局 free block 的层级结构避免全局竞争。ResourcePool<T> 返回的是偏移量（offset）而非指针，该偏移量在 O(1) 时间内可转换为对象指针，且一般小于 2^32，可作为 64 位 id 的一部分使用。归还对象时不会调用析构函数，而是进入 freelist，调用方需自行重置对象状态；该类只负责内存分配，不解决 ABA 问题。

## 关键特征

- **批量分配**：通过批量向系统申请内存，降低单次分配的开销。
- **层级化 free block**：采用 thread-local free block + 全局 free block 的两层结构，减少多线程环境下的全局竞争。
- **偏移量返回**：返回的不是裸指针，而是偏移量，O(1) 时间内可换算为对象指针。
- **id 友好**：偏移量一般小于 2^32，可作为 64 位 id 的一部分使用。
- **不调用析构**：对象归还时不执行析构，直接进入 freelist，由调用方负责重置对象状态。
- **不解决 ABA**：仅提供内存分配与回收语义，不处理 ABA 问题。
- **仅适用于等长对象**：作为模板类，针对固定大小的 T 对象设计。

## 应用

- 在 brpc 中负责等长对象的批量分配与回收，是 ObjectPool<T> 的底层基础。
- 所有的 [[concepts/TaskMeta|TaskMeta]]（bthread 的任务元数据）均由 ResourcePool<TaskMeta> 分配。
- 用于 [[concepts/bthread_t|bthread_t]] 等需要以 64 位 id 形式高效表示对象的场景。
- 适合高并发、对分配延迟敏感、且对象大小固定的内部组件。

## 相关概念

- [[concepts/ObjectPool|ObjectPool<T>]]
- [[concepts/等长对象分配|等长对象分配]]
- [[concepts/bthread_t|bthread_t]]
- [[concepts/内存池|内存池]]

## 相关实体

- [[entities/brpc|brpc]]

## 来源提及

- "brpc中的ResourcePool<T>和ObjectPool<T>即提供这类分配。" — [[sources/memory_management|memory_management]]
- "创建一个类型为T的对象并返回一个偏移量，这个偏移量可以在O(1)时间内转换为对象指针。" — [[sources/memory_management|memory_management]]
- "由于对象等长，ResourcePool通过批量分配和归还内存以避免全局竞争，并降低单次的开销。" — [[sources/memory_management|memory_management]]
- "所有的TaskMeta由ResourcePool<TaskMeta>分配。" — [[sources/memory_management|memory_management]]