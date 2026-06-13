---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes]]"]
tags: [term]
aliases:
  - "FeatureSet Edition Default"
  - "FeatureSetEditionDefault"
---


# FeatureSetEditionDefault

## 定义
FeatureSetEditionDefault 是 Protobuf Edition 系统中的一种 proto 消息类型，用于存储某一给定 Edition 下各项 Feature 的默认值。它是 protoc 生成的"编译期默认值 IR"（compiled defaults IR）的一部分，会被 protoc 共享给各个语言的运行时，从而将默认值校验逻辑集中在 protoc 中，避免在每一个语言运行时中重复实现。

## 关键特征
- 在 Edition 体系中充当"每个 Edition 的 Feature 默认值容器"。
- 包含一个现有的 `features` 字段，用于存放默认值。
- 提案建议新增两个 `FeatureSet` 类型的字段：
  - `overridable_features`：用户**可以**覆盖的默认值。
  - `fixed_features`：用户**不可以**覆盖的默认值。
- 现有的 `features` 字段会被暂时保留，作为迁移工具以避免破坏现有的插件和运行时。
- 属于 protoc 生成的"编译默认值 IR"，在 protoc 与各语言运行时之间传递。
- 设计目标是尽量把校验相关信息集中在该结构中，以减少跨运行时/跨插件的重复实现。

## 应用
- 作为 protoc 在编译期输出的中间表示（IR）的一部分，被下发给各语言的运行时使用。
- 用于集中校验"哪些 Feature 默认值可以被用户覆盖、哪些不可以"，从而替代原先散落在各语言运行时中的校验逻辑。
- 在 Edition 演进过程中，作为迁移桥梁：旧路径仍可使用 `features`，新路径使用 `overridable_features` / `fixed_features`。
- 为插件和运行时提供统一的"Edition → 默认 Feature 集合"映射来源。

## 相关概念
- [[concepts/feature-set|FeatureSet]]
- [[concepts/feature-support|FeatureSupport]]
- [[concepts/behavior-preserving-editions|Behavior-Preserving Editions]]
- [[concepts/edition-support-window|Edition Support Window]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/protobuf|Protobuf]]

## 来源提及
- "Specifically, we will add two new `FeatureSet` fields to `FeatureSetEditionDefault` in addition to the existing `features` field." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
- "we can pack as much information in there as possible to minimize duplication" — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]