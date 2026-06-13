---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/style]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
tags:
  - "term"
aliases:
  - "Group"
  - "分组语法"
  - "group syntax"
  - "Group Fields"
  - "Group"
  - "分组语法"
  - "group syntax"
---

## Description
组字段是 Protocol Buffers 演化历史上的一种遗留语法特性，它提供了一种紧凑的方式来在消息中嵌套子消息。在 proto2 中，组字段使用 `group` 关键字定义，具有独立的 wire format 编码方式。随着 Protobuf 语言的演进，组字段被认为是一种不理想的语法设计：它在 proto3 中被完全移除，在 Protobuf Editions 中被统一转换为具有特殊编码（delimited representation）的子消息字段。官方样式指南和迁移文档都明确建议使用嵌套消息类型替代组语法，以实现更好的兼容性和可维护性。Edition Zero 计划通过统一所有语法变体，最终彻底消除组字段等遗留构造。

## Related Concepts

- [[concepts/nested-messages|Nested Messages]]
- [[concepts/required-fields|Required Fields]]
- [[concepts/message-names|Message Names]]
- [[concepts/wire-format|Wire Format]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/feature|Feature]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]

## Related Entities

- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]

## Mentions in Source

> **Source: [[sources/style|style]]**
- "Groups is an alternate syntax and wire format for nested messages. Groups are considered deprecated in proto2, were removed from proto3, and are converted to a delimited representation in edition 2023."
- "Use a nested message definition and field of that type instead of using the group syntax, using the message_encoding feature for wire-compatibility."
- "Avoid Groups"

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
- "We still have `required` and `group`, `packed` is not everywhere..."
- "groups will turn into sub message fields with a special encoding."