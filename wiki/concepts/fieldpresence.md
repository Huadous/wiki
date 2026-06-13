---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]"]
tags: [term]
aliases:
  - "字段存在性"
  - "FieldPresence"
---


# FieldPresence

## 定义
FieldPresence 是 Protobuf Editions 系统中 Edition Zero Features 定义的一个功能字段（feature field），用于控制 protobuf 消息字段的存在性语义（field presence semantics）。该枚举包含三个取值：EXPLICIT（显式存在性）、IMPLICIT（隐式存在性）和 LEGACY_REQUIRED（遗留必需字段），分别对应 proto2/proto3 中不同的字段存在性行为。

## 关键特征
- **枚举定义**：包含三个值 `EXPLICIT = 0`、`IMPLICIT = 1`、`LEGACY_REQUIRED = 2`
- **默认行为**：在 2023 edition 中，默认值为 `EXPLICIT`
- **Retention 属性**：标记为 `RUNTIME`，影响字段的运行时行为
- **Target 属性**：限定 `target = FIELD`，仅适用于字段实体（field entities）
- **历史行为抽象**：通过可枚举功能将 proto2（EXPLICIT）、proto3（IMPLICIT）、proto2 required（LEGACY_REQUIRED）的行为差异统一抽象
- **Edition 驱动**：是 Editions 核心设计理念的典型示例——将历史行为编码为可枚举的 feature，而非版本号的硬编码差异

## 应用
- **统一字段存在性控制**：允许 schema 作者在同一个 Edition 体系下选择所需的字段存在性语义，无需切换 proto2/proto3
- **向后兼容 proto2**：通过 `LEGACY_REQUIRED` 保留对 proto2 中 required 关键字的兼容能力
- **对齐 proto3 默认行为**：通过 `IMPLICIT` 模拟 proto3 时代无显式 presence 检查的语义
- **运行时存在性检查**：结合 `RUNTIME` retention，使得生成的代码可以在运行时区分"未设置"与"设置为零值"

## 相关概念
- [[concepts/Features|Features]]
- [[concepts/Edition-Defaults|Edition Defaults]]
- [[concepts/Target-Attributes|Target Attributes]]
- [[concepts/Retention|Retention]]

## 相关实体
（无相关实体）

## 来源提及
- `enum FieldPresence { EXPLICIT = 0; IMPLICIT = 1; LEGACY_REQUIRED = 2; }` — [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]
- `optional FieldPresence field_presence = 1 [ retention = RUNTIME, target = FIELD, (edition_defaults) = { edition: "2023", default: "EXPLICIT" } ];` — [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]