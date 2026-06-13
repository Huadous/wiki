---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/features]]"
  - "[[protobuf/features.md]]"
tags:
  - "term"
aliases:
  - "Scope levels"
  - "Feature scope"
  - "特性设置作用域"
  - "Feature Scope"
  - "Scope levels"
  - "Feature scope"
  - "特性设置作用域"
---

## Related Concepts
- [[concepts/features-field_presence|features.field_presence]]
- [[concepts/features-default_symbol_visibility|features.default_symbol_visibility]]
- [[concepts/features-enforce_naming_style|features.enforce_naming_style]]
- [[concepts/features-enum_type|features.enum_type]]
- [[concepts/protocol-buffers-editions|Protocol Buffers Editions]]

## Related Entities
- [[entities/protocol-buffers|protobuf]]
- [[entities/edition-2024|Edition 2024]]

## Mentions in Source
> **Source: [[sources/features|features]]**
> - "Feature settings apply at different levels: File-level: These settings apply to all elements (messages, fields, enums, and so on) that don't have an overriding setting."
> - "Non-nested: Messages, enums, and services can override settings made at the file level. They apply to everything within them (message fields, enum values) that aren't overridden, but don't apply to other parallel messages and enums."
> - "Nested: Oneofs, messages, and enums can override settings from..."
> - "Lowest-level: Fields, extensions, enum values, extension ranges, and methods are the lowest level at which you can override settings."

> **Source: [[sources/features|features]]**
> - "No directly relevant information"