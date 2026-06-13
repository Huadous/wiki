---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/flatmap|flatmap]]"]
tags: [product]
aliases:
  - "butil::FlatMap"
  - "FlatMap - Maybe the fastest hashmap"
  - "with tradeoff of space"
---


# FlatMap

## 基本信息
- Type: product
- Source: [[sources/flatmap|flatmap]]

## 描述
FlatMap 是 [[entities/brpc|brpc]] 项目中 [[entities/butil|butil]] 库所实现的一种高性能[[concepts/哈希表|哈希表]]容器，声明于 `butil/containers/flat_map.h` 头文件中。其核心设计借鉴了[[concepts/开链哈希|开链哈希]]策略，将每个开链桶的第一个节点直接内联存储在桶数组内，从而减少一次指针跳转带来的开销。当 value 较大时这种内联策略会消耗更多内存，因此 FlatMap 最适合作为检索过程中需要极快查找的小字典使用场景。

FlatMap 提供了 `init(bucket_count, load_factor)`、`insert`、`seek`、`erase`、`clear` 等基本接口，并通过 PositionHint 机制支持安全地在迭代过程中删除元素，[[concepts/负载因子|负载因子]]参数允许调用方在空间占用与碰撞概率之间做权衡。基准测试数据显示，向 FlatMap / [[entities/alignhashmap|AlignHashMap]] / [[entities/cowhashmap|CowHashMap]] / `std::map` 中顺序插入 100 个元素分别耗时 15 / 19 / 30 / 102 纳秒，FlatMap 在多数场景下性能优于其它三者，且其[[concepts/哈希表|哈希表]]查找性能接近原生数组。[[entities/cowhashmap|CowHashMap]] 借助 [[concepts/copy-on-write|Copy-on-write]] 机制提供读多写少场景下的替代选择。

## 相关实体
- [[entities/butil|butil]]
- [[entities/brpc|brpc]]
- [[entities/alignhashmap|AlignHashMap]]
- [[entities/cowhashmap|CowHashMap]]

## 相关概念
- [[concepts/开链哈希|开链哈希]]
- [[concepts/闭链哈希|闭链哈希]]
- [[concepts/哈希表|哈希表]]
- [[concepts/负载因子|负载因子]]
- [[concepts/copy-on-write|Copy-on-write]]

## 来源提及
- "FlatMap - Maybe the fastest hashmap, with tradeoff of space." — [[sources/flatmap|flatmap]]
- "FlatMap可能是最快的哈希表，但当value较大时它需要更多的内存，它最适合作为检索过程中需要极快查找的小字典。" — [[sources/flatmap|flatmap]]
- "在很多时候，FlatMap的查找性能和原生数组接近。" — [[sources/flatmap|flatmap]]
- "Sequentially inserting   100 into FlatMap/AlignHashMap/CowHashMap/std::map takes 15/19/30/102ns" — [[sources/flatmap|flatmap]]