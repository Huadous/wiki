---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/style]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
tags:
  - "term"
aliases:
  - "oneof"
  - "联合类型"
  - "Oneof Names"
  - "oneof"
  - "联合类型"
  - "Oneof"
  - "oneof"
  - "联合类型"
  - "Oneof Names"
  - "oneof"
  - "联合类型"
---

## Description

oneof 是 Protocol Buffers 中的一种字段组合机制，允许消息声明若干互斥的备选字段，运行时同一时刻最多只有一个成员持有值。这种"同时最多一个"的约束属于 API 层的不变式（API-level invariant）。在线缆格式层面，一个 oneof 的多个成员可能在编码后出现多个 (tag, value) 对，但反序列化后的 API 会以"最后一个胜出（last one wins）"的规则进行规范化处理，从而保证应用程序看到的状态与不变式一致。

从存在性语义上看，oneof 与 singular 字段类似——都会显式跟踪"哪一个成员当前持有值"。这使得 oneof 字段在反序列化、序列化和反射等场景下天然携带存在性信息，而无需额外的封装。与之对照的是 proto3 的 `optional` 字段：proto3 的 `optional` 在编译器内部会被放入一个单字段的"synthetic oneof"中，从而获得存在性追踪能力，因此两者在存在性行为上是对齐的，但在源代码层面 `optional` 与显式 `oneof` 仍然是两种不同的声明方式。

## Related Concepts

- [[concepts/field-cardinality|Field cardinality]]
- [[concepts/field-names|Field Names]]
- [[concepts/identifier-naming-styles|Identifier naming styles]]
- [[concepts/message-type|Message type]]
- [[concepts/proto-file|proto-file]]
- [[concepts/field-presence|Field presence]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/wire-format|Wire format]]

## Related Entities

- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/protoc|protoc]]
- [[entities/oneofdescriptor|oneofdescriptor]]
- [[entities/descriptor|descriptor]]
- [[entities/codegeneratorresponse|codegeneratorresponse]]

## Mentions in Source

> **Source: [[sources/overview|overview]]**
> - "A field can also be of: ... oneof type, which you can use when a message has many optional fields and at most one field will be set at the same time."

> **Source: [[sources/style|style]]**
> - "Use lower_snake_case for oneof names. oneof song_id { string song_human_readable_id = 1; int64 song_machine_id = 2; }"

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "Every proto3 optional field is placed into a one-field `oneof`. We call this a 'synthetic' oneof, as it was not present in the source `.proto` file."
> - "Since oneof fields in proto3 already track presence, existing proto3 reflection-based algorithms should correctly preserve presence for proto3 optional fields with no code changes."

> **Source: [[sources/field_presence|field_presence]]**
> - "oneof fields expose the API-level invariant that only one field is set at a time."
> - "However, the wire format may include multiple (tag, value) pairs which notionally belong to the oneof."
> - "Similar to singular fields, oneof fields explicitly track which one of the members, if any, contains a value."