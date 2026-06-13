---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "term"
aliases:
  - "字段存在性"
  - "FieldPresence"
  - "presence discipline"
  - "字段存在性"
  - "FieldPresence"
---

## Description
FieldPresence 通过枚举值将历史上分散在不同 proto 语法中的字段存在性语义统一抽象到 Editions 体系下。其底层理论是 **presence discipline**——一种对字段存在性（即 hasbit）的处理规则。从概念层面看，presence discipline 至少包含两类核心策略：**No presence** 指 API 不暴露 hasbit，默认值类似哨兵值，既不序列化也不参与合并语义；**explicit presence** 指 API 通过 `has` 和 `Clear` 方法暴露 hasbit，且只要 hasbit 被设置，即使字段值为默认值也会被序列化。

在工程实现层面，FieldPresence 枚举包含三个取值：`EXPLICIT = 0`（显式存在性，对应 explicit presence 策略）、`IMPLICIT = 1`（隐式存在性，对齐 proto3 时代无显式 presence 检查的语义）、`LEGACY_REQUIRED = 2`（遗留必需字段，保留对 proto2 中 `required` 关键字的向后兼容能力）。该特性被声明为 `optional FieldPresence field_presence = 1`，并标注 `retention = RUNTIME`、`target = FIELD`，其 edition_defaults 指定在 2023 edition 中默认值为 `EXPLICIT`，意味着生成的代码可以在运行时区分"未设置"与"设置为零值"。理解 presence discipline 是理解 proto2 与 proto3 行为差异以及 Edition Zero 特性设计的核心理论基础。

## Related Concepts
- [[concepts/Features|Features]]
- [[concepts/Edition-Defaults|Edition Defaults]]
- [[concepts/Target-Attributes|Target Attributes]]
- [[concepts/Retention|Retention]]
- [[concepts/Presence-Discipline|Presence Discipline]]
- [[concepts/Hasbit|Hasbit]]

## Related Entities
- [[entities/edition-zero|Edition Zero]]

## Mentions in Source

> **Source: [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]**
> - `enum FieldPresence { EXPLICIT = 0; IMPLICIT = 1; LEGACY_REQUIRED = 2; }`
> - `optional FieldPresence field_presence = 1 [ retention = RUNTIME, target = FIELD, (edition_defaults) = { edition: "2023", default: "EXPLICIT" } ];`

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "A **presence discipline** is a handling for the presence (or hasbit) of a field."
> - "**No presence** means that the API does not expose the hasbit."