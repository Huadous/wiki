---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]"]
tags: [term]
aliases:
  - "0x800"
  - "kMapWithProto2EnumValue flag"
---


# kMapWithProto2EnumValue

## 定义
kMapWithProto2EnumValue 是 Java Lite MessageInfo 编码中现有的一个标志位（flag bit），其十六进制值为 0x800。该标志位最初用于表示一个 map 字段的 value 类型是 proto2 枚举值。在 Protobuf Editions 迁移方案中，该位将被新的 [[concepts/kLegacyEnumIsClosedBit|kLegacyEnumIsClosedBit]] 标志位所替代，以实现对 [[concepts/java.legacy_closed_enum|java.legacy_closed_enum]] 特性的通用化编码支持。

## 关键特征
- 属于 Java Lite 运行时 `MessageInfo` 编码格式中的现有标志位
- 十六进制取值为 `0x800`（对应二进制掩码中的特定比特位）
- 原本语义：标识 map 字段的 value 是 proto2 枚举类型
- 是特定语法（proto2 枚举与 map 组合）层面的编码标志，而非通用特性标志
- 在 Editions 迁移中将被 [[concepts/kLegacyEnumIsClosedBit|kLegacyEnumIsClosedBit]] 取代，从"语法机制标志"转向"通用特性机制标志"

## 应用
- 用于 Java Lite 运行时的 `MessageInfo` 编码与解析，标记包含 proto2 枚举 value 的 map 字段
- 在 Protobuf Editions 迁移过程中，作为被废弃的旧编码位出现于 [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]] 提案的编码变更说明中
- 编码替代过程是 [[concepts/java.legacy_closed_enum|java.legacy_closed_enum]] 特性落地的关键步骤之一，使该特性摆脱对特定 map/proto2-enum 组合语法的依赖

## 相关概念
- [[concepts/java.legacy_closed_enum|java.legacy_closed_enum]]
- [[concepts/kLegacyEnumIsClosedBit|kLegacyEnumIsClosedBit]]
- [[concepts/features.enum_type|features.enum_type]]

## 相关实体
- [[sources/java-lite|java-lite]]

## 来源提及
- `kMapWithProto2EnumValue (0x800)` — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]
- Replace with `kLegacyEnumIsClosedBit` — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]