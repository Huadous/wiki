---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/editions-java-lite-for-editions|editions-java-lite-for-editions]]"
  - "[[protobuf/editions-java-lite-for-editions.md]]"
tags:
  - "term"
aliases:
  - "legacy_closed_enum"
  - "java legacy closed enum"
  - "kLegacyEnumIsClosedBit"
---

## Description
`java.legacy_closed_enum` 是 Editions Zero 中专门面向 Java 实现的特性（feature），不属于通用 wire format 层。在 Java Lite 现有的 `MessageInfo` 编码中，该特性由 `kMapWithProto2EnumValue (0x800)` 位表达，但该位原本只针对 enum map value 设置。在向 Editions 迁移过程中，该位被新引入的 `kLegacyEnumIsClosedBit` 替代，用于表示 `java.legacy_closed_enum` 特性，并扩展为对所有枚举字段设置，而不仅仅是 enum map 值。该位的引入是 Java Lite 编码格式在保持向后兼容前提下的关键扩展之一。过渡期间，仍需在 gencode 中检查 syntax 以兼容旧代码路径，避免破坏既有 Java 客户端的解码行为。`java.legacy_closed_enum` 是否设置，会反过来影响 [[concepts/features.enum_type|features.enum_type]] 在 Java Lite 运行时的隐式判定。

## Related Concepts
- [[concepts/features.enum_type]]
- [[concepts/kMapWithProto2EnumValue]]
- [[concepts/kLegacyEnumIsClosedBit]]
- [[concepts/EnumLiteGenerator]]
- [[concepts/Editions Zero Features]]
- [[concepts/kHasHasBit]]

## Related Entities
- [[entities/Java Lite]]

## Mentions in Source

> **Source: [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]**
> - "Replace with `kLegacyEnumIsClosedBit`"
> - "This will now be set for all enum fields, instead of just enum map values."
> - "We will still need to check syntax in the interim in case of gencode."