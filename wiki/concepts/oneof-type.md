---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/overview]]"
  - "[[sources/style]]"
tags:
  - "term"
aliases:
  - "oneof"
  - "联合类型"
  - "Oneof Names"
  - "oneof"
  - "联合类型"
---

## Description

Oneof type 是 Protocol Buffers 中用于表示互斥字段集合的关键语法结构。它通过内存共享和自动清理机制，确保同一组内的多个字段中最多只有一个处于有效状态。一个重要的命名约定是，oneof 的名称应使用 `lower_snake_case`（例如 `song_id`），这与其他标识符（如字段名）的风格保持一致，有助于代码生成工具避免命名冲突，并提高代码的可读性。典型的使用场景包括定义 RPC 方法的返回值（成功结果或错误信息）、状态机中的互斥状态，以及配置消息中的多种可能类型。

## Related Concepts

- [[concepts/field-cardinality|Field cardinality]]
- [[concepts/field-names|Field Names]]
- [[concepts/identifier-naming-styles|Identifier naming styles]]
- [[concepts/message-type|Message type]]
- [[concepts/proto-file|proto-file]]

## Related Entities

- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/protoc|protoc]]

## Mentions in Source

> **Source: [[sources/overview|overview]]**
> - "A field can also be of: ... oneof type, which you can use when a message has many optional fields and at most one field will be set at the same time."

> **Source: [[sources/style|style]]**
> - "Use lower_snake_case for oneof names. oneof song_id { string song_human_readable_id = 1; int64 song_machine_id = 2; }"