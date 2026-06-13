---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions]]"]
tags: [term]
aliases:
  - "Singular Field"
  - "singular"
  - "optional field"
---


# Singular Field

## 定义
Singular Field 是 Protocol Buffers 字段基数（cardinality）之一，没有显式的 cardinality 标签。它有两种可能状态：已设置（set）或未设置（unset）。它是 Protobuf 中最基础的字段类型，相对于 [[concepts/Repeated Field|Repeated Field]] 和 [[concepts/Map Field|Map Field]] 而言。

## 关键特征
- **无显式 cardinality 标签**：与 `repeated` 或 `map` 字段不同，singular field 在 .proto 定义中不需要任何基数修饰符。
- **两种可能状态**：
  - **已设置（set）**：包含显式设置或从 wire 解析得到的值，将被序列化到 wire。
  - **未设置（unset）**：返回默认值，不被序列化到 wire。
- **存在性可检测**：开发者可以检查字段值是否被显式设置，这是 [[concepts/Field Presence|Field Presence]] 机制的基础。
- **与 Field Presence 关联**：在 Editions 体系中，singular field 的存在性行为由 [[concepts/Field Presence|Field Presence]] 设置（如 `EXPLICIT`、`IMPLICIT`、`LEGACY_REQUIRED`）控制。

## 应用
- **proto2 中**：所有非 repeated、非 map 的字段默认即为 singular field，通常具备显式存在性（explicit presence），可通过 `has_field()` 检查。
- **proto3 中**：scalar 类型的 singular field 默认使用隐式存在性（implicit presence），无法区分"未设置"与"设置为默认值"。可通过 `optional` 关键字启用显式存在性。
- **Editions 中**：在 Editions 体系里，所有字段默认即为 singular field，其存在性语义通过 [[concepts/Field Presence|Field Presence]] 功能设置显式声明。
- **字段迁移场景**：当需要在 [[entities/proto3|proto3]] 消息中区分"字段未设置"与"字段等于零值"时，singular field（配合显式存在性）提供了关键的语义区分能力。

## 相关概念
- [[concepts/Field Cardinality|Field Cardinality]]
- [[concepts/Field Presence|Field Presence]]
- [[concepts/Repeated Field|Repeated Field]]
- [[concepts/Map Field|Map Field]]

## 相关实体
- [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|Protocol Buffers v3.12.0]]
- [[entities/codegeneratorresponse|CodeGeneratorResponse]]

## 来源提及
- "A singular field has no explicit cardinality label. It has two possible states: the field is set, and contains a value that was explicitly set or parsed from the wire. It will be serialized to the wire." — [[sources/editions]]
- "the field is unset, and will return the default value. It will not be serialized to the wire." — [[sources/editions]]
- "You can check to see if the value was explicitly set." — [[sources/editions]]