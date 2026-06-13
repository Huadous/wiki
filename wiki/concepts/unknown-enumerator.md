---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence|field_presence]]"]
tags: [term]
aliases:
  - "UNKNOWN enumerator"
  - "枚举零值约定"
  - "zero-valued enumerator"
---


# UNKNOWN enumerator

## 定义
UNKNOWN enumerator 是 proto3 语法中关于枚举类型定义的一条语法约定：所有 `enum` 类型都必须包含一个映射到 0 的枚举值，习惯上命名为 `UNKNOWN` 或类似的语义中性名称。该 0 值枚举项同时充当 proto3 字段在 _no presence_ 语义下的默认值，因此该约定是 proto3 枚举类型能够正常序列化和反序列化的语法前提。

## 关键特征
- 由 proto3 语法强制要求：所有 `enum` 类型必须存在映射到 0 的枚举项。
- 该 0 值枚举项在 _no presence_ 语义下作为 enum 字段的默认值使用。
- 命名上遵循惯例，习惯称为 `UNKNOWN` 或类似的语义中性名称（如 `UNSPECIFIED`），以避免与业务合法值混淆。
- 文档原文表述为：_By convention, this is an `UNKNOWN` or similarly-named enumerator._
- 在概念上是显式存在性（Explicit presence discipline）的替代方案：若合法值域不包含 0，则 0 值仅作为"未知"占位，功能上等效于显式存在性。

## 应用
- 定义任何 proto3 `enum` 类型时，必须显式声明映射到 0 的枚举项，否则 proto 编译器将拒绝生成代码。
- 当业务语义中不存在自然的 0 值时，惯例做法是添加一个名为 `UNKNOWN`、`UNSPECIFIED` 或同义的占位枚举项。
- 作为 enum 字段在 _no presence_ 语义下的默认值，使得序列化时无需写入 enum 字段即可获得一个明确且无歧义的取值。
- 与 [[concepts/Default value|Default value]] 共同构成 proto3 枚举字段零值语义的基础。

## 相关概念
- [[concepts/no-presence-discipline|No presence discipline]]
- [[concepts/default-value|Default value]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/proto3|proto3]]

## 相关实体
_No related entities_

## 来源提及
- The default value for enum-typed fields under _no presence_ is the corresponding 0-valued enumerator. — [[sources/field_presence|field_presence]]
- Under proto3 syntax rules, all enum types are required to have an enumerator value which maps to 0. — [[sources/field_presence|field_presence]]
- By convention, this is an `UNKNOWN` or similarly-named enumerator. — [[sources/field_presence|field_presence]]