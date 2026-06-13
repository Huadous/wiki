---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]"
  - "[[protobuf/editions-java-lite-for-editions.md]]"
tags:
  - "term"
aliases:
  - "重复字段编码"
  - "RepeatedFieldEncoding"
  - "features.repeated_field_encoding"
  - "重复字段编码"
  - "RepeatedFieldEncoding"
---

## Description
RepeatedFieldEncoding 是 Protobuf Editions 体系下管理 `repeated` 字段 wire 编码行为的核心特性之一。该特性在 2023 edition 中的默认值为 `PACKED`，即默认采用连续字节流的紧凑编码方式；同时支持通过文件级与字段级覆盖机制灵活切换到 `EXPANDED`，以兼容传统的逐元素编码场景。该特性的 `retention` 属性为 `RUNTIME`，意味着其在运行时仍然保留，可被运行时动态解析；`target` 属性为 `FIELD`，表明其作用域为字段级别，与 [[concepts/Feature-Inheritance|Feature Inheritance]] 机制配合实现细粒度配置。

在 Java Lite 运行时的迁移视角下，`features.repeated_field_encoding` 被映射到 `MessageInfo` 字段条目中的 `GetExperimentalJavaFieldTypeForPacked` 表达方式。提案明确指出该特性在编码层的对应关系保持不变（Keep as-is），迁移工作仅需把所有原本通过读取 `is_proto3` 位来推断 packed 行为的代码路径，统一切换到读取该特性位即可。这一改动体现了 Editions 特性替代隐式 `is_proto3` 推断的设计思路，使编码行为决策更加显式与可控。

## Related Concepts
- [[concepts/Features|Features]]
- [[concepts/Edition-Defaults|Edition Defaults]]
- [[concepts/Target-Attributes|Target Attributes]]
- [[concepts/Feature-Inheritance|Feature Inheritance]]
- [[concepts/Java-Lite-Editions-Migration|Java Lite Editions 迁移]]

## Related Entities
- 无相关实体

## Mentions in Source

**Source: [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]**
- `enum RepeatedFieldEncoding { PACKED = 0; EXPANDED = 1; }`
- `optional RepeatedFieldEncoding repeated_field_encoding = 3 [ retention = RUNTIME, target = FIELD, (edition_defaults) = { edition: "2023", default: "PACKED" } ];`

**Source: [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]**
- `features.repeated_field_encoding` — `GetExperimentalJavaFieldTypeForPacked`. Keep as-is.