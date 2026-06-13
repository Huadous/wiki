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
字段存在性（field presence）描述了一个 protobuf 字段是否具有值的概念，并区分了两种不同的存在性表现形式：无存在性（no presence），即生成的消息 API 仅存储字段值；以及显式存在性（explicit presence），即 API 还额外存储字段是否被设置的信息。这两种模式在序列化语义、API 行为以及跨语言兼容性方面存在显著差异。在 editions 体系中，字段存在性通过 `field_presence` 特性进行配置，可选值包括 `LEGACY_REQUIRED`、`EXPLICIT` 和 `IMPLICIT`，分别对应 proto2 的 required 字段语义、显式存在性以及 proto3 隐式存在性的语义。从 proto3 迁移至 editions 的隐式字段将使用 `IMPLICIT` 值，而 proto2 的 required 字段迁移后使用 `LEGACY_REQUIRED`。根据 Proto3 Presence 实现说明，存在性追踪是在综合 Google 内部和开源社区用户反馈后被引入 proto3 的，并且其语法和语义与 proto2 中的存在性完全一致（"Presence in proto3 uses exactly the same syntax and semantics as in proto2"）。无存在性场景下，非消息类型的字段仅有两个状态——设置为非默认值与设置为默认值——而默认值不会被序列化到 wire 上，也无法区分该值是被显式设置还是未被提供。对于显式存在性，optional 字段则拥有明确的已设置（set）与未设置（unset）两种状态。

## Related Concepts
- [[concepts/edition|edition]]
- [[concepts/optional|optional]]
- [[concepts/field-cardinality|field cardinality]]
- [[concepts/implicit-field|implicit field]]
- [[concepts/features-default_symbol_visibility|features-default_symbol_visibility]]
- [[concepts/features-enforce_naming_style|features-enforce_naming_style]]
- [[concepts/packed-encoding|packed-encoding]]
- [[concepts/message-type|message type]]
- [[concepts/wire-format|wire format]]
- [[concepts/proto3|proto3]]
- [[concepts/hasbit|hasbit]]
- [[concepts/wrapper-type|wrapper type]]
- [[concepts/synthetic-oneof|synthetic oneof]]
- [[concepts/no-presence-discipline|no presence discipline]]
- [[concepts/explicit-presence-discipline|explicit presence discipline]]
- [[concepts/hazzer-methods|hazzer methods]]

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/protoc|protoc]]
- [[entities/prototiller|prototiller]]
- [[entities/google|google]]

## Mentions in Source
> **Source: [[sources/features|features]]**
> - "This feature sets the behavior for tracking field presence, or the notion of whether a protobuf field has a value."
> - "Values available: LEGACY_REQUIRED, EXPLICIT, IMPLICIT."
> - "LEGACY_REQUIRED: The field is required for parsing and serialization."
> - "After running Prototiller, the equivalent code might look like this:"

> **Source: [[sources/editions|editions]]**
> - "Proto3 implicit fields that have been migrated to editions will use the field_presence feature set to the IMPLICIT value."
> - "Proto2 required fields that have been migrated to editions will also use the field_presence feature, but set to LEGACY_REQUIRED."

> **Source: [[sources/proto3|proto3]]**
> - "An optional field is in one of two possible states: the field is set, and contains a value that was explicitly set or parsed from the wire... the field is unset, and will return the default value."
> - "In proto3, message-type fields already have field presence. Because of this, adding the optional modifier doesn't change the field presence for the field."
> - "If the field is not a message, it has two states: the field is set to a non-default (non-zero) value... the field is set to the default (zero) value."
> - "The field is set to the default (zero) value. It will not be serialized to the wire. In fact, you cannot determine whether the default (zero) value was set or parsed from the wire or not provided at all."
> - "For more on this subject, see Field Presence"

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "Presence tracking was added to proto3 in response to user feedback, both from inside Google and from open-source users."
> - "Presence in proto3 uses exactly the same syntax and semantics as in proto2."
> - "No directly relevant information"

> **Source: [[sources/field_presence|field_presence]]**
> - "Field presence is the notion of whether a protobuf field has a value."
> - "There are two different manifestations of presence for protobufs: no presence, where the generated message API stores field values (only), and explicit presence, where the API also stores whether or not a field has been set."