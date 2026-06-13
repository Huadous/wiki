---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/field_presence|field_presence]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "method"
aliases:
  - "显式存在性模式"
  - "Explicit Presence"
  - "显式存在性"
  - "EXPLICIT_PRESENCE"
  - "显式存在性模式"
  - "Explicit Presence"
  - "显式存在性"
---

## Description
显式存在性模式（Explicit presence discipline）是一种字段存在性跟踪机制，其中生成的 API 不仅存储字段的值，还显式地存储该字段是否被设置（set）的状态。在这种模式下，代码能够区分"字段未被设置"与"字段被设置为默认值"这两种不同的语义状态。显式设置的值始终会被序列化，即使其值与默认值相同。

在 Protobuf Editions 中，`EXPLICIT_PRESENCE` 是 `features.field_presence` 字段的目标默认值（target default value），代表了字段显式存在的标准语义。当读取器没有在序列化数据中看到该字段的记录时，尝试访问该字段将产生默认值，这正是显式存在性模式的预期行为。在 "ImmoLation of required" 大规模迁移路径中，EXPLICIT_PRESENCE 是迁移 `required` 字段的最终目标状态——在 `LEGACY_REQUIRED` 和 `ALWAYS_SERIALIZE` 被移除后，EXPLICIT_PRESENCE 将成为字段存在性的标准表达方式。该最终状态与 proto3 中无标签字段（unannotated field）的行为保持一致，从而在 Editions 体系下统一了字段存在性的语义。

## Related Concepts
- [[concepts/No presence discipline|No presence discipline]]
- [[concepts/Field presence|Field presence]]
- [[concepts/Hazzer methods|Hazzer methods]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]
- [[concepts/Legacy required|Legacy required]]
- [[concepts/Always serialize|Always serialize]]
- [[concepts/ImmoLation of required|ImmoLation of required]]
- [[concepts/Features|Features]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]

## Mentions in Source

> **Source: [[sources/field_presence|field_presence]]**
> - "explicit presence, where the API also stores whether or not a field has been set."
> - "Explicit presence discipline: Explicitly set values are always serialized, including default values."
> - "The explicit presence discipline relies upon the explicit tracking state instead."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "We can use features to move fields off of `features.field_presence = LEGACY_REQUIRED` (the edition's spelling of `required`) and onto `features.field_presence = EXPLICIT_PRESENCE`."
> - "At this point we can migrate from `ALWAYS_SERIALIZE` to `EXPLICIT_PRESENCE`."