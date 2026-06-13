---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/flatmap|flatmap]]"]
tags: [method]
aliases:
  - "COW"
  - "写时复制"
  - "Copy-on-write"
---


# Copy-on-write

## 定义
Copy-on-write（写时复制）是一种延迟复制策略，在 [[entities/cowhashmap|CowHashMap]] 中被用于实现并发友好的开链哈希表。当多个读取者共享同一份数据时，写操作才会触发实际复制。该机制使得 [[entities/smalltable|smalltable]] 中的 CowHashMap 在读多写少场景下能获得良好的并发性能，同时与普通开链哈希在内存管理上有所不同。

## 关键特征
- 延迟复制：读取者共享同一份底层数据，无需立即为每个读者分配独立副本
- 写时触发：仅在写操作实际发生时，才执行数据的复制操作
- 并发友好：多读者可同时访问共享数据而无需加锁，写者复制后才独占新副本
- 内存优化：避免了不必要的冗余数据拷贝，减少内存占用与拷贝开销
- 适用场景：读多写少的并发访问模式

## 应用
- [[entities/smalltable|smalltable]] 中的 [[entities/cowhashmap|CowHashMap]] 开链哈希表实现
- 读多写少场景下的并发哈希表查询与更新
- 作为 [[concepts/开链哈希]] 的一种内存管理优化策略

## 相关概念
- [[concepts/开链哈希]]
- [[concepts/哈希表]]

## 相关实体
- [[entities/cowhashmap|CowHashMap]]
- [[entities/smalltable|smalltable]]
- [[entities/alignhashmap|AlignHashMap]]

## 来源提及
- CowHashMap：smalltable中的开链哈希表，和普通开链不同的是带Copy-on-write逻辑。 — [[sources/flatmap|flatmap]]