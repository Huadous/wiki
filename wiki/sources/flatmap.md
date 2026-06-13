---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/flatmap.md]]"
tags: [哈希表, 开链哈希, 闭链哈希, 哈希函数, 雪崩效应, 负载因子, Copy-on-write, Murmurhash, 线性同余, Hopscotch hashing, Cuckoo hashing, Coalesced hashing, 红黑树, PositionHint, 线性探查, 二次探查, 聚集效应]
aliases: ["FlatMap - Maybe the fastest hashmap, with tradeoff of space", "FlatMap 文档"]
---

# FlatMap - Maybe the fastest hashmap, with tradeoff of space - Summary

## 来源
- Original file: [[brpc/flatmap.md]]
- Ingested: 2026-06-13

## 核心内容
本文档系统介绍了 [[entities/brpc|brpc]] 项目 [[entities/butil|butil]] 库中的 [[entities/flatmap|FlatMap]] 哈希表实现。FlatMap 定位为"可能最快的哈希表"，以空间换时间为设计取舍，其核心原理是将[[concepts/开链哈希|开链桶]]的第一个节点直接存放于桶内，使多数无冲突查找只需一次内存跳转，性能接近原生数组。文档提供了 C++ 使用示例，涵盖 init/insert/seek/erase 等接口，并介绍了专为迭代过程中安全删除元素设计的 [[concepts/positionhint|PositionHint]] 机制。基准测试将 FlatMap 与 [[entities/alignhashmap|AlignHashMap]]（[[concepts/闭链哈希|闭链]]）、[[entities/cowhashmap|CowHashMap]]（[[concepts/copy-on-write|Copy-on-write]] 开链）和 [[entities/stdmap|std::map]]（[[concepts/红黑树|红黑树]]）在不同 value 大小和数据规模下进行对比。文档还概述了[[concepts/哈希表|哈希表]]的基础原理，包括[[concepts/哈希函数|哈希函数]]设计要点（[[concepts/雪崩效应|雪崩效应]]、[[concepts/线性同余|线性同余]]、[[concepts/murmurhash|Murmurhash]]）以及[[concepts/闭链哈希|闭链哈希]]（[[concepts/线性探查|线性探查]]、[[concepts/二次探查|二次探查]]、[[concepts/hopscotch-hashing|Hopscotch hashing]]）、[[concepts/开链哈希|开链哈希]]、[[concepts/cuckoo-hashing|Cuckoo hashing]]（多次哈希）、[[concepts/coalesced-hashing|Coalesced hashing]]（混合）等冲突解决策略的优缺点分析，特别强调了闭链哈希在装载率超过 70% 时产生的[[concepts/聚集效应|聚集效应]]问题。

## 关键实体
- [[entities/flatmap|FlatMap]]：brpc/butil 中的高性能[[concepts/哈希表|哈希表]]，以空间换时间
- [[entities/butil|butil]]：brpc 项目下的 C++ 基础工具库，FlatMap 所属容器模块
- [[entities/brpc|brpc]]：Apache 开源的 RPC 框架项目，FlatMap 的所属项目
- [[entities/alignhashmap|AlignHashMap]]：百度 ecom/nova 项目的[[concepts/闭链哈希|闭链哈希]]实现，基准测试对照
- [[entities/cowhashmap|CowHashMap]]：百度 [[entities/smalltable|smalltable]] 项目中带[[concepts/copy-on-write|Copy-on-write]]逻辑的开链哈希表
- [[entities/stdmap|std::map]]：C++ STL 中的关联容器，[[concepts/红黑树|红黑树]]实现
- [[entities/smalltable|smalltable]]：百度内部的高性能 key/value 容器项目

## 关键概念
- [[concepts/哈希表|哈希表]]：通过哈希函数将 key 分散到不同桶区间的数据结构
- [[concepts/开链哈希|开链哈希]]：桶为链表的哈希实现，FlatMap 的设计基础
- [[concepts/闭链哈希|闭链哈希]]：通过探查法解决冲突的哈希实现，存在[[concepts/聚集效应|聚集效应]]
- [[concepts/哈希函数|哈希函数]]：决定哈希表性能的第一道关键因素
- [[concepts/雪崩效应|雪崩效应]]：衡量哈希函数质量的输入输出扩散性质
- [[concepts/负载因子|负载因子]]：元素数与桶数之比，FlatMap 默认 80
- [[concepts/聚集效应|聚集效应]]：闭链哈希装载率较高时元素大幅偏离应在桶的现象
- [[concepts/copy-on-write|Copy-on-write]]：CowHashMap 采用的延迟复制策略
- [[concepts/murmurhash|Murmurhash]]：文档推荐的通用非加密型哈希算法
- [[concepts/线性同余|线性同余]]：最常见的哈希散列方法
- [[concepts/hopscotch-hashing|Hopscotch hashing]]：解决[[concepts/聚集效应|聚集效应]]的[[concepts/闭链哈希|闭链]]衍生方案
- [[concepts/cuckoo-hashing|Cuckoo hashing]]：多次哈希策略的典型代表
- [[concepts/coalesced-hashing|Coalesced hashing]]：混合开链与闭链的方案
- [[concepts/红黑树|红黑树]]：std::map 的底层实现，O(log N) 复杂度
- [[concepts/positionhint|PositionHint]]：FlatMap 提供的迭代器位置保存与恢复机制
- [[concepts/线性探查|线性探查]]：闭链哈希中最基本的冲突解决方法
- [[concepts/二次探查|二次探查]]：按平方数位移查找空桶的闭链探查方法

## 要点
- FlatMap 的核心原理是将[[concepts/开链哈希|开链]]桶的第一个节点直接放在桶内，使无冲突查找只需一次内存跳转，性能接近原生数组
- FlatMap 以空间换时间，当 value 较大时需要更多内存，最适合作为需要极快查找的小字典
- 基准测试覆盖 value=8/32/128 字节和数据规模 100/1000/10000，对比 FlatMap、AlignHashMap（闭链）、CowHashMap（开链+[[concepts/copy-on-write|COW]]）、std::map（[[concepts/红黑树|红黑树]]）四者性能
- FlatMap 在迭代删除时需要使用 save_iterator/restore_iterator 配合 [[concepts/positionhint|PositionHint]] 机制，因为 erase 后 ++iterator 可能失效
- [[concepts/哈希函数|哈希函数]]设计要点：确定性、[[concepts/雪崩效应|雪崩效应]]、均匀分布、利用现代 CPU 特性（成块计算、减少分支、循环展开），通用算法可选 [[concepts/murmurhash|Murmurhash]]
- [[concepts/开链哈希|开链哈希]]优点：桶独立、resize 不失效、易并发；缺点：至少两次内存跳转、每对 key/value 需额外指针
- [[concepts/闭链哈希|闭链哈希]]缺点：桶个数必须大于元素数、resize 后内存失效、难以并发、装载率超过 70% 时产生严重[[concepts/聚集效应|聚集效应]]导致性能不可预测
- [[concepts/cuckoo-hashing|Cuckoo hashing]]（多次哈希）与 [[concepts/coalesced-hashing|Coalesced hashing]]（混合）是两类衍生冲突解决策略，但文档认为两者均未真正解决内存跳转问题，工程效果有限