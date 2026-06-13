---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/style]]"
tags:
  - "standard"
aliases:
  - "枚举值前缀命名约定"
  - "Enum prefixing convention"
  - "Enum value scoping best practice"
---

## 相关概念
- [[concepts/enums|Enums]]
- [[concepts/identifier-naming-styles|Identifier naming styles]]
- [[concepts/protobuf-style-guide|Protocol Buffers Style Guide]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]

## 来源提及
> **来源: [[sources/style|style]]**
> - "Enum values are semantically considered to not be scoped by their containing enum name, so the same name in two sibling enums is not allowed."
> - "To avoid these risks, it is strongly recommended to do one of: Prefix every value with the enum name (converted to UPPER_SNAKE_CASE); Nest the enum inside a containing message."
> - "When prefixing enum values, the remainder of the name with the prefix stripped should still be a legal and style-conformant enum name."

> **来源: [[sources/techniques|techniques]]**
> - "If you choose to prefix the enum values, the name after stripping the prefix must still be a valid and style-compliant enum value name."

> **来源: [[sources/style|style]]**
> - "No directly relevant information"