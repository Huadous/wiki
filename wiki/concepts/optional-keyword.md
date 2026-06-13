---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-features|editions-edition-zero-features]]"]
tags: [term]
aliases:
  - "optional 关键字"
  - "optional field"
  - "optional label"
---


# optional 关键字

## 定义
`optional` 是 proto2/proto3 中用于标记 singular 字段的关键字。在 proto2 中，`optional` 用于显式地声明字段为可选，并为该字段暴露 hasbit 以表达显式存在语义（EXPLICIT presence）；在 proto3 中，对应的关键字是 `proto3_optional`，同样赋予 singular 字段显式存在能力。Editions 决定消除该关键字，以减少从 proto2/proto3 迁移到 editions 时的语法噪声，追求最简洁的语法表达。

## 关键特征
- 在 proto2 中为 singular 字段提供显式存在语义（EXPLICIT presence），并通过 hasbit 暴露字段是否被设置
- 在 proto3 中以 `proto3_optional` 形式存在，为默认隐式存在的 proto3 字段赋予显式存在能力
- 是 proto2/proto3 → editions 迁移中的语法噪声来源之一，Editions 计划将其完全消除
- 迁移时需要执行 Large-Scale Change（LSC），删除 google3 中所有现存实例（共 385,236 个）
- 文档讨论了多种替代方案：要求保留 `optional`、发明新关键字（如 `singular`）、或允许 `optional` 与无标签共存，最终选择消除以追求最简洁语法

## 应用
- proto2/proto3 schema 中声明可选字段，使消费方能区分"未设置"与"设置为零值"
- 在 editions 迁移的 LSC 中被大规模删除，被更简洁的字段存在性机制取代
- 作为 Proto3 显式存在语义（field presence）讨论的核心关键字之一

## 相关概念
- [[concepts/explicit-presence|EXPLICIT presence]]
- [[concepts/required-keyword|required keyword]]
- [[concepts/proto3-syntax|proto3 syntax]]
- [[concepts/proto2-syntax|proto2 syntax]]
- [[concepts/large-scale-change|Large-Scale Change]]
- [[concepts/field-presence|field presence]]
- [[concepts/implementing-proto3-presence|Implementing Proto3 Presence]]
- [[concepts/editions-edition-zero-features|editions-edition-zero-features]]

## 相关实体
（无相关实体）

## 来源提及
- "Migration will require deleting every instance of `optional` in proto files in google3, of which there are 385,236." — [[sources/editions-edition-zero-features|editions-edition-zero-features]]
- "Migrating from proto2/3 involves deleting all `optional`/`required` labels and adding `IMPLICIT` and `LEGACY_REQUIURED` annotations where necessary." — [[sources/editions-edition-zero-features|editions-edition-zero-features]]