---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-features|editions-edition-zero-features]]"]
tags: [phenomenon]
aliases:
  - "parallel repeated fields"
  - "Parallel Arrays"
---


# Parallel arrays

## 定义
Parallel arrays（并行数组）是一种数据结构模式，其中两个 `repeated` 字段按相同索引位置一一对应，索引 `i` 在两个字段中指向同一个逻辑概念。换言之，两个等长的 repeated 字段通过位置上的"锁步（lockstep）"关系来编码成对出现的数据。

## 关键特征
- 由两个 `repeated` 字段组成，期望两者的第 `i` 个元素描述同一条逻辑记录
- 依赖字段间的**锁步索引（lockstep indexing）**：相同下标 `i` 在两字段中必须语义对齐
- 与 [[concepts/closed-enum|closed enum]] 语义交互不良：出现在并行数组槽位中的未知枚举值会被移入 [[concepts/unknown-field-set|Unknown field set]]，导致数组不再"平行"
- 解析与序列化过程可能因把未知枚举值追加到末尾而**重排** repeated closed enum，从而进一步破坏平行结构
- 此现象是促使 open enum 与 closed enum 语义区分的设计动机之一，与 [[concepts/open-enum|Open Enum]] 形成对比

## 应用
- 在 Protocol Buffers（[[entities/protocol-buffers|Protocol Buffers]]）中以成对 repeated 字段编码关联数据
- 作为讨论 closed enum 在未知值处理上局限性的反例
- 用于说明 Edition Zero 中 `features.enum_type`（[[concepts/features-enum-type|features.enum_type]]）所引入的 open enum 语义为何必要

## 相关概念
- [[concepts/closed-enum|Closed Enum]]
- [[concepts/open-enum|Open Enum]]
- [[concepts/unknown-field-set|Unknown field set]]
- [[concepts/features-enum-type|features.enum_type]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- "Closed enums can cause confusion for parallel arrays (two repeated fields that expect to have index i refer to the same logical concept in both fields) because an unknown enum value from a parallel array will be placed in the unknown field set and the arrays will cease being parallel." — [[sources/editions-edition-zero-features|editions-edition-zero-features]]