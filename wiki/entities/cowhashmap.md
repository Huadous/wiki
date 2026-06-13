---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/flatmap|flatmap]]"]
tags: [product]
aliases:
  - "CowHashMap (smalltable)"
  - "cow_hash_map"
---


# CowHashMap

## 基本信息
- Type: product
- Source: [[sources/flatmap|flatmap]]

## 描述
CowHashMap 是百度 smalltable 项目（ecom/nova）中的开链哈希表实现，其源代码位于 afs/smalltable/cow_hash_map.hpp。与普通的开链哈希表不同，CowHashMap 内置了 Copy-on-Write（写时复制）逻辑，从而能够在并发读多写少的场景下安全高效地共享底层桶结构。在 [[sources/flatmap|flatmap]] 的性能基准测试中，CowHashMap 的随机查找性能接近 [[entities/flatmap|FlatMap]]，但其删除操作在四种被测实现（FlatMap、AlignHashMap、CowHashMap、std::map）中速度最慢。

## 相关实体
- [[entities/flatmap|FlatMap]]
- AlignHashMap（暂无 Wiki 页面）

## 相关概念
- 开链哈希（暂无 Wiki 页面）
- Copy-on-write（暂无 Wiki 页面）
- 哈希表（暂无 Wiki 页面）

## 来源提及
- "CowHashMap：smalltable中的开链哈希表，和普通开链不同的是带Copy-on-write逻辑。" — [[sources/flatmap|flatmap]]
- "Sequentially inserting   100 into FlatMap/AlignHashMap/CowHashMap/std::map takes 15/19/30/102ns" — [[sources/flatmap|flatmap]]