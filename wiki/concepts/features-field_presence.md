---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/features]]"
  - "[[sources/editions]]"
  - "[[sources/proto3]]"
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
  - "[[protobuf/features.md]]"
  - "[[protobuf/editions.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-java-lite-for-editions.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "term"
aliases:
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field_presence feature"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field presence"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field_presence feature"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "Field Presence"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field_presence feature"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field presence"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field_presence feature"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "Field presence"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field_presence feature"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field presence"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field_presence feature"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "Field Presence"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field_presence feature"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field presence"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field_presence feature"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
---

## Description
`features.field_presence` 是 Edition Zero 中用于统一控制 singular 字段存在性语义的核心特性。在 Edition Zero 的设计中，proto2 的 `optional`/`required` 关键字被完全消除（成为解析错误），singular 字段的存在性行为完全由该特性决定。该特性有三种枚举取值：`EXPLICIT_PRESENCE`（明确存在性）、`IMPLICIT`（隐式存在性）和 `LEGACY_REQUIRED`（遗留必需）。迁移过程中，proto2 的 required 字段需要显式标注为 `LEGACY_REQUIRED`，proto3 的隐式字段需要标注为 `IMPLICIT`。从 `LEGACY_REQUIRED` 迁移到 `ALWAYS_SERIALIZE` 是安全的，因为 `required` 仅约束初始化检查（即值是否被设置）。

## Related Concepts
- [[concepts/features|Feature]]
- [[concepts/global-features|Global features]]
- [[concepts/required-deprecation|Immolation of `required`]]
- [[concepts/field-presence|Field presence]]

## Related Entities
- （暂无直接关联实体）

## Mentions in Source
> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "We can use features to move fields off of `features.field_presence = LEGACY_REQUIRED` (the edition's spelling of `required`) and onto `features.field_presence = EXPLICIT_PRESENCE`."
> - "It is always safe to turn a proto from `LEGACY_REQUIRED` to `ALWAYS_SERIALIZE`, because `required` is a constraint on initialization checking, i.e., that the value was present."

> **Source: [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]**
> - "Fortunately, we already have corresponding bits for most Editions Zero Features in the corresponding `MessageInfo` field entry encoding."
> - "`kHasHasBit (0x1000)` — Keep as-is."

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "This feature is enum-typed and controls the presence discipline of a singular field"
> - "we have chosen to *eliminate both the `optional` and `required` keywords, making them parse errors*."