---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/flatmap|flatmap]]"]
tags: [project]
aliases:
  - "百度 smalltable"
  - "smalltable (百度)"
---


# smalltable

## 基本信息
- Type: project
- Source: [[sources/flatmap|flatmap]]

## 描述
smalltable 是百度内部的一个容器/数据结构项目，汇集了多种高性能 key/value 容器实现。其中的 [[entities/cowhashmap|CowHashMap]] 是 smalltable 的开链哈希表实现，特点是带有 Copy-on-write 逻辑，从而在并发场景中实现读写分离。在 brpc [[entities/flatmap|FlatMap]] 的性能基准测试中，CowHashMap 被作为对照实现之一，展示了它在通用开链哈希场景下的性能特征。smalltable 的代码托管于百度 SVN（svn.baidu.com）下的 afs/smalltable 路径。

## 相关实体
- [[entities/cowhashmap|CowHashMap]]
- [[entities/flatmap|FlatMap]]
- [[entities/alignhashmap|AlignHashMap]]
- [[entities/stdmap|std::map]]

## 相关概念
- [[concepts/open-addressing-hash|开链哈希]]
- [[concepts/copy-on-write|Copy-on-write]]
- [[concepts/hash-table|哈希表]]

## 来源提及
- CowHashMap：smalltable中的开链哈希表，和普通开链不同的是带Copy-on-write逻辑。 — [[sources/flatmap|flatmap]]
- [CowHashMap](https://svn.baidu.com/app/ecom/nova/trunk/afs/smalltable/cow_hash_map.hpp)：smalltable中的开链哈希表 — [[sources/flatmap|flatmap]]