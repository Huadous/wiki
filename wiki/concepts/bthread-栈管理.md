---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management|memory_management]]"]
tags: [method]
aliases:
  - "bthread栈管理"
  - "bthread Stack Management"
  - "bthread栈"
---


# bthread 栈管理

## 定义
bthread 栈管理是 bthread 协程库为不同使用场景提供差异化栈规格的内存管理机制。由于 ResourcePool 中所有 bthread 的栈必须等长，bthread 按栈大小将栈分为不同的 pool，以适配不同的负载场景，并通过 mmap 配合 mprotect 设置 4K guard page 来检测栈溢出。

## 关键特征
- **按大小分池**：ResourcePool 要求同一个 pool 中所有 bthread 栈等长，因此按栈大小划分为多个独立 pool。
- **NORMAL 栈**：默认大小为 1M，对应属性 `BTHREAD_ATTR_NORMAL`，适合 server 运行用户代码的场景。
- **SMALL 栈**：默认大小为 32K，对应属性 `BTHREAD_ATTR_SMALL`，适合大量小任务的轻量场景。
- **LARGE 栈**：与 pthread 默认栈大小相同，不做 caching，因此创建相对较慢。
- **默认两池策略**：基于实际观察，大部分用户只关心两种大小的栈，因此默认仅提供 NORMAL 与 SMALL 两种 pool。
- **mmap 分配 + guard page**：栈底层使用 `mmap` 分配，并配合 `mprotect` 设置 4K 的 guard page，以检测栈溢出。

## 应用
- **brpc server**：默认使用 `BTHREAD_ATTR_NORMAL`（1M 栈）运行用户 RPC 处理代码，兼顾栈空间充裕与调度效率。
- **高并发小任务**：使用 `BTHREAD_ATTR_SMALL`（32K 栈）创建大量短生命周期 bthread，减少内存占用。
- **特殊重负载**：对于需要与 pthread 同等栈空间的场景，使用 LARGE 栈（不做 caching，创建较慢）。
- **栈溢出检测**：借助 guard page 在测试或调试阶段捕获栈越界写入。

## 相关概念
- [[concepts/bthread|bthread]]
- [[concepts/guard-page|guard page]]
- [[concepts/mmap|mmap]]
- [[concepts/resourcepool|ResourcePool<T>]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- 使用ResourcePool加快创建的副作用是：一个pool中所有bthread的栈必须是一样大的。 — [[sources/memory_management|memory_management]]
- 大部分用户并不关心栈的具体大小，而只需要两种大小的栈 — [[sources/memory_management|memory_management]]
- 两种栈分别对应属性BTHREAD_ATTR_NORMAL（栈默认为1M）和BTHREAD_ATTR_SMALL（栈默认为32K）。 — [[sources/memory_management|memory_management]]
- server默认使用BTHREAD_ATTR_NORMAL运行用户代码。 — [[sources/memory_management|memory_management]]