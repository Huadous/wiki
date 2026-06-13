---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-features]]"]
tags: [term]
aliases:
  - "custom defaults"
  - "自定义默认值"
---


# Custom default values

## 定义
Custom default values（自定义默认值）是 Protobuf 字段可以指定的非默认默认值，通过 `[default = ...]` 语法在字段级别设置。它允许字段在反序列化未提供值时回退到一个用户指定的特定值，而不是字段类型的内在默认值。

## 关键特征
- 通过 `[default = ...]` 字段选项在字段级别声明，区别于字段类型自身的默认默认值
- 在 EXPLICIT presence 字段上仍然受支持
- 在 LEGACY_REQUIRED 字段上仍然受支持
- IMPLICIT presence 字段不能设置自定义默认值
- 当 IMPLICIT 字段为 submessage 类型时，其默认值设置会被忽略
- 此行为与 proto3 中 implicit 字段的语义保持一致

## 应用
- 在 Protobuf Editions 中作为字段级别的默认行为配置机制，用于为 EXPLICIT 或 LEGACY_REQUIRED 字段指定业务所需的回退值
- 在 schema 演进中保持向后兼容的语义：当字段缺失时，接收端可以基于自定义默认值进行反序列化推断
- 用于在存在性语义（field presence）明确的字段上编码"未设置"与"设置为特定值"的区分

## 相关概念
- [[concepts/implicit-presence|IMPLICIT presence]]
- [[concepts/defaulted-fields|defaulted fields]]
- [[concepts/features-field-presence|features.field_presence]]

## 相关实体
（无相关实体）

## 来源提及
- "they cannot have custom defaults and are ignored on submessage fields" — [[sources/editions-edition-zero-features|editions-edition-zero-features]]
- "Reject custom defaults for `IMPLICIT` fields. This is technically not really needed for converged semantics, but trying to remove the Proto3-ness from `IMPLICIT` fields seems useful for consistency." — [[sources/editions-edition-zero-features|editions-edition-zero-features]]