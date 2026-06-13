---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-feature-enum-field-closedness]]"]
tags: [term]
aliases:
  - "proto3 enum"
  - "proto3 枚举类型"
---


# proto3 enum

## 定义
proto3 enum 是在 `syntax = "proto3"` 文件中定义的枚举类型。proto3 枚举在传统上被视为**开放枚举（Open Enum）**，不支持非零默认值（受隐式存在性约束 implicit presence 限制）。

## 关键特征
- **开放枚举语义**：proto3 枚举在传统语义上是开放类型，解析器在反序列化时遇到未知枚举值不会报错，而是将其保留或丢弃处理。
- **不支持非零默认值**：由于 proto3 字段采用隐式存在性（implicit presence），枚举的第一个值必须为零值（`0`），且不允许显式设置非零默认值。
- **跨语法引用的边界情况**：当 proto2 消息中的字段引用 proto3 枚举时，某些语言实现可能将该枚举错误地视为封闭类型（closed enum），导致未知枚举值被丢弃到 `UnknownFieldSet`。
- **编译器拒绝反向引用**：proto 编译器拒绝在 proto3 消息中引用 proto2 枚举，因为 proto2 枚举可以拥有非零默认值，这违反了 proto3 的隐式存在性约束。

## 应用
- **Protocol Buffers 模式定义**：用于在 `.proto` 文件中声明有限取值集合，例如错误码、消息类型标识、状态枚举等。
- **跨版本互操作**：在需要同时支持 proto2 和 proto3 消息的系统中，需要特别关注枚举字段在双向引用时的封闭性行为差异。
- **Protobuf Editions 演进**：Editions 体系引入了 `enum_type`（CLOSED/OPEN/UNSPECIFIED）特性来显式控制枚举封闭性，作为对 proto3 隐式行为的精细化替代。

## 相关概念
- [[concepts/enum-field-closedness|Enum Field Closedness]]
- [[concepts/open-enum|Open Enum]]
- [[concepts/unknown-field-set|UnknownFieldSet]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoscope|Protoscope]]

## 来源提及
- `syntax = "proto3";` — [[sources/editions-edition-zero-feature-enum-field-closedness]]
- the proto compiler rejects proto2-enum-valued fields in proto3 messages, because such enums can have nonzero defaults, which proto3 does not support due to implicit presence. — [[sources/editions-edition-zero-feature-enum-field-closedness]]