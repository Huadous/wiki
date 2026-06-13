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