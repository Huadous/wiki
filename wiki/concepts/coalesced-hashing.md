---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/flatmap|flatmap]]"]
tags: [method]
aliases:
  - "Coalesced hashing"
  - "合并哈希"
---


# Coalesced hashing

## 定义
Coalesced hashing 是一种混合了开链哈希（separate chaining）与闭链哈希（open addressing）的哈希冲突处理方法。它把桶数组的一部分单元拿出来作为容纳冲突元素的溢出空间，从而在哈希表内部直接消解冲突，无需额外的链表节点或链表跳转。Coalesced hashing 是这种"内部溢出区"思路的典型实现方案。

## 关键特征
- 混合开链与闭链：桶数组中预留若干单元作为溢出区，被冲突的元素直接落入这些溢出位置。
- 无外部链表节点：与纯开链相比，不需要额外的指针/链表结构来连接冲突元素。
- 仍存在内存跳转问题：虽然冲突元素安置在表内，但访问冲突元素时仍需跨单元跳转，未能解决开链带来的缓存不友好问题。
- 结构复杂度高于纯闭链：相比简单的线性探测、双散列等闭链方法，其插入与查找逻辑更复杂。
- 工程评价不佳：文档明确指出该方法"没有解决开链的内存跳转问题，结构又比闭链复杂很多，工程效果并不好"。

## 应用
- 哈希表冲突解决策略的学术与教学讨论，用于演示开链与闭链之间的折中思路。
- 在 [[sources/flatmap|flatmap]] 等 brpc 文档中被作为哈希冲突方案的对比对象提及，用以衬托开链实现（如 [[entities/cowhashmap|cow_hash_map]]、[[entities/alignhashmap|AlignHashMap]]）在工程上的优势。

## 相关概念
- [[concepts/open-addressing|开链哈希]]
- [[concepts/closed-addressing|闭链哈希]]
- [[concepts/hash-table|哈希表]]

## 相关实体
- [[entities/flatmap|FlatMap - Maybe the fastest hashmap, with tradeoff of space]]
- [[entities/alignhashmap|AlignHashMap 闭链哈希表]]
- [[entities/cowhashmap|CowHashMap (smalltable)]]

## 来源提及
- "混合开链和闭链：一般是把桶数组中的一部分拿出来作为容纳冲突元素的空间，典型如Coalesced hashing" — [[sources/flatmap|flatmap]]
- "但这种结构没有解决开链的内存跳转问题，结构又比闭链复杂很多，工程效果并不好。" — [[sources/flatmap|flatmap]]