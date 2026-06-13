---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/flatmap|flatmap]]"]
tags: [product]
aliases:
  - "std::map (C++)"
  - "C++ std::map"
  - "std::map"
---


# std::map

## 基本信息
- Type: product
- Source: [[sources/flatmap|flatmap]]

## 描述
std::map 是 C++ 标准模板库 (STL) 中的关联容器，提供有序的键值对存储与查找能力。其内部实现一般为[[concepts/红黑树|红黑树]]，因此查找、插入、删除操作的时间复杂度为 O(log N)，而非 [[concepts/哈希表|哈希表]] 通常所能达到的 O(1)。在 brpc 源码的性能基准测试中，std::map 与 [[entities/flatmap|FlatMap]]、[[entities/flatmap|AlignHashMap]]、[[entities/flatmap|CowHashMap]] 并列对比，结果显示 FlatMap 的查找速度在各类场景下通常是 std::map 的 10 倍以上。它的优点在于有序性以及成熟稳定的实现，但哈希表在纯检索性能上往往远超它。

## 相关实体
- [[entities/flatmap|FlatMap]]
- [[entities/flatmap|AlignHashMap]]
- [[entities/flatmap|CowHashMap]]

## 相关概念
- [[concepts/红黑树|红黑树]]
- [[concepts/哈希表|哈希表]]

## 来源提及
- "std::map：非哈希表，一般是红黑树。" — [[sources/flatmap|flatmap]]
- "Sequentially inserting   100 into FlatMap/AlignHashMap/CowHashMap/std::map takes 15/19/30/102ns" — [[sources/flatmap|flatmap]]
- "Seeking  1000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 3/7/11/78ns" — [[sources/flatmap|flatmap]]
---