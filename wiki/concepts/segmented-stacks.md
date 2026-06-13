---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management]]"]
tags: [method]
aliases:
  - "分段栈"
  - "segmented stacks"
---


# segmented stacks

## 定义
segmented stacks（分段栈）是一种动态调整栈大小的技术，goroutine 在 1.3 版本之前采用该方案，通过在栈增长时动态链接新的栈段来实现栈空间的伸缩。

## 关键特征
- **动态栈段链接**：栈空间不足时，通过动态链接新的栈段来扩展栈容量，而非一次性分配大块连续内存。
- **栈段拆分与合并**：栈增长时拆分为新段，栈缩小时合并回收段。
- **hot split 问题**：当某些函数恰好在栈段边界处被反复调用时，会导致栈段频繁拆分与合并，造成严重的性能损耗。
- **已被替代**：由于 hot split 性能问题，goroutine 在 1.3 版本后改用变长连续栈方案（类似于 vector resizing 的方式）。
- **适用范围有限**：变长连续栈方案依赖于内存托管能力，并不适用于所有运行时环境。

## 应用
- **goroutine 历史方案**：Go 语言在 1.3 之前使用 segmented stacks 实现 goroutine 的动态栈管理，发现 hot split 问题后切换至变长连续栈。
- **bthread 的取舍**：bthread 运行于 64 位平台，虚存空间庞大，对变长栈需求不明确，加上 segmented stacks 的性能影响，目前暂未规划变长栈方案。
- **栈管理设计参考**：在设计用户态线程或协程的栈管理机制时，segmented stacks 与变长连续栈是两条主要的演进路径，segmented stacks 提供了其中一种可借鉴的实现思路。

## 相关概念
- [[concepts/bthread-栈管理|bthread 栈管理]]
- [[concepts/变长连续栈|变长连续栈]]

## 相关实体
No related entities

## 来源提及
- "goroutine在1.3前通过segmented stacks动态地调整栈大小，发现有hot split问题后换成了变长连续栈（类似于vector resizing，只适合内存托管的语言）。" — [[sources/memory_management]]
- "加上segmented stacks的性能有影响，bthread暂时没有变长栈的计划。" — [[sources/memory_management]]