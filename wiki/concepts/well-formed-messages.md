---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/proto3]]"
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/editions.md]]"
tags:
  - "term"
aliases:
  - "well-formed消息"
  - "格式正确消息"
  - "well-formed message"
  - "well-formed消息"
  - "格式正确消息"
  - "Well-formed message"
  - "well-formed消息"
  - "格式正确消息"
  - "well-formed message"
  - "well-formed消息"
  - "格式正确消息"
  - "Well-formed Message"
  - "well-formed消息"
  - "格式正确消息"
  - "well-formed message"
  - "well-formed消息"
  - "格式正确消息"
  - "Well-formed message"
  - "well-formed消息"
  - "格式正确消息"
  - "well-formed message"
  - "well-formed消息"
  - "格式正确消息"
---

## Related Concepts

- [[concepts/wire-format|wire format]]
- [[concepts/field-number|field number]]
- [[concepts/field-cardinality|field cardinality]]
- [[concepts/edition|edition]]
- [[concepts/singular-field|Singular Field]]
- [[concepts/message-type|Message Type]]

## Related Entities

- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]

## Mentions in Source

> **Source: [[sources/editions|editions]]**
> - "The term "well-formed," when applied to protobuf messages, refers to the bytes serialized/deserialized. The protoc parser validates that a given proto definition file is parseable." — [[protobuf/editions|editions]]
> - "Singular fields can appear more than once in wire-format bytes. The parser will accept the input, but only the last instance of that field will be accessible through the generated bindings." — [[protobuf/editions|editions]]

> **Source: [[sources/proto3|proto3]]**
> - "The term "well-formed," when applied to protobuf messages, refers to the bytes serialized/deserialized." — [[protobuf/proto3|proto3]]
> - "The protoc parser validates that a given proto definition file is parseable." — [[protobuf/proto3|proto3]]
> - "Singular fields can appear more than once in wire-format bytes. The parser will accept the input, but only the last instance of that field will be accessible through the generated bindings. See Last One Wins for more on this topic." — [[protobuf/proto3|proto3]]