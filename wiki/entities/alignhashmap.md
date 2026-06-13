---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/flatmap|flatmap]]"]
tags: [product]
aliases:
  - "AlignHashMap 闭链哈希表"
  - "百度 AlignHashMap"
---


# AlignHashMap

## 基本信息
- Type: product
- Source: [[sources/flatmap|flatmap]]

## 描述
AlignHashMap 是百度 ecom/nova 项目中实现的一种闭链哈希表（closed-addressing hashmap），被描述为"闭链中较快的实现"。它是 [[entities/flatmap|flatmap]] 基准测试中的主要对比对象之一，与 [[entities/flatmap|flatmap]]、CowHashMap、std::map 一同参与性能对比。基准测试数据显示，无论顺序插入还是随机插入，AlignHashMap 的耗时均高于 [[entities/flatmap|flatmap]]，且当 value 体积增大（如 128 字节）时差距更为显著。这表明 AlignHashMap 虽然在闭链哈希表中表现优秀，但在综合性能上仍不及 [[entities/flatmap|flatmap]]。

## 相关实体
- [[entities/flatmap|flatmap]]
- [[entities/cowhashmap|cowhashmap]]

## 相关概念
- [[concepts/闭链哈希|闭链哈希]]
- [[concepts/哈希表|哈希表]]

## 来源提及
- AlignHashMap：闭链中较快的实现。 — [[sources/flatmap|flatmap]]
- Sequentially inserting   100 into FlatMap/AlignHashMap/CowHashMap/std::map takes 15/19/30/102ns — [[sources/flatmap|flatmap]]
- Randomly inserting   100 into FlatMap/AlignHashMap/CowHashMap/std::map takes 14/56/29/157ns — [[sources/flatmap|flatmap]]