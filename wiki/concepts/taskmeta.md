---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management|memory_management]]"]
tags: [term]
aliases:
  - "TaskMeta结构"
  - "TaskMeta"
---


# TaskMeta

## 定义
TaskMeta 是 brpc 中 bthread（用户态线程）的内部数据结构，定义在 `task_meta.h` 头文件中。每个 bthread 对应一个 TaskMeta 实例，所有 TaskMeta 均由 `ResourcePool<TaskMeta>` 统一分配和回收。TaskMeta 保存了 bthread 运行所需的全部上下文信息，是 `bthread_t` 通过偏移量定位后所指向的最终实体。

## 关键特征
- **统一分配管理**：所有 TaskMeta 实例由 `ResourcePool<TaskMeta>` 集中分配和回收，避免了零散的内存申请与释放。
- **等长对象分配策略**：由于 TaskMeta 是定长对象，分配与释放操作非常高效，使得创建一个 bthread 的平均耗时控制在 200ns 以内。
- **O(1) 时间访问**：bthread 的大部分函数需要在 O(1) 时间内通过 `bthread_t` 访问到对应的 TaskMeta。
- **失效检测**：当 `bthread_t` 失效后，访问应返回 NULL 以让函数返回错误。
- **32 位版本号**：TaskMeta 中存储了 bthread 的 32 位版本号，用于在多线程环境下检测对象是否已被复用，从而解决 ABA 问题。查找时先通过偏移量获得 TaskMeta，再检查版本号是否匹配，若不匹配则说明对应的 bthread 已失效。

## 应用
- 作为 bthread 的底层数据载体，承载 bthread 运行所需的全部上下文信息。
- 通过 `bthread_t → TaskMeta` 的偏移量映射机制，实现对 bthread 的高效访问与生命周期管理。
- 通过内置的版本号机制，在高并发多线程环境下安全地检测对象复用，避免 ABA 问题导致的逻辑错误。
- 配合 `ResourcePool<TaskMeta>` 的等长对象分配策略，为 brpc 提供高性能的协程/用户态线程创建能力。

## 相关概念
- [[concepts/bthread_t|bthread_t]]
- [[concepts/ABA问题|ABA问题]]
- [[concepts/等长对象分配|等长对象分配]]
- [[concepts/ResourcePool|ResourcePool<T>]]

## 相关实体
- [[entities/bthread|bthread]]

## 来源提及
- bthread在代码中被称作Task，其结构被称为TaskMeta，定义在task_meta.h中，所有的TaskMeta由ResourcePool<TaskMeta>分配。 — [[sources/memory_management|memory_management]]
- bthread的大部分函数都需要在O(1)时间内通过bthread_t访问到TaskMeta，并且当bthread_t失效后，访问应返回NULL以让函数做出返回错误。 — [[sources/memory_management|memory_management]]
- 查找时先通过偏移量获得TaskMeta，再检查版本，如果版本不匹配，说明bthread失效了。 — [[sources/memory_management|memory_management]]