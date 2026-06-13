---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/style]]"
  - "[[protobuf/editions-protobuf-editions-design-features.md]]"
tags:
  - "term"
aliases:
  - "消息编码特性"
  - "delimited representation"
  - "message_encoding 特性"
  - "MessageEncoding"
  - "消息编码特性"
  - "delimited representation"
  - "message_encoding 特性"
---

## Description
message_encoding 特性是 Protocol Buffers editions 系统中用于控制消息字段编码格式的可枚举功能。从底层设计上看，该特性对应一个 `MessageEncoding` 枚举类型，包含 `LENGTH_PREFIXED`（长度前缀，等于 0）和 `DELIMITED`（分隔符，等于 1）两个值，作为 Edition Zero Features 中的第 5 个功能字段出现（字段编号为 5），其 retention 为 `RUNTIME`，target 为 `FIELD`，并在 2023 edition 中将 `LENGTH_PREFIXED` 设为默认值。该功能体现了 Editions 系统通过可枚举功能来表达序列化行为差异的设计思路。

在实际使用层面，message_encoding 特性被广泛用于替代已废弃的 groups 语法。通过将该特性设置为 `delimited`，可以在保持有线格式兼容的前提下，使用嵌套消息定义和字段类型来替代 groups，实现从旧语法（proto2/proto3）到 edition 2023 的平滑迁移。开发者只需在字段上声明 `message_encoding = DELIMITED`，而无需修改消息的内部结构，从而逐步替换遗留的 groups 定义而无需一次性修改所有依赖的代码和数据。在需要时，该特性也可以与其他特性（如 `LEGACY_REQUIRED`）结合使用，以处理更复杂的迁移场景。

## Related Concepts
- [[concepts/groups|groups]]
- [[concepts/Field presence feature (LEGACY_REQUIRED)|Field presence feature (LEGACY_REQUIRED)]]
- [[concepts/required fields|required fields]]

## Related Entities
- [[entities/Protocol Buffers|Protocol Buffers]]

## Mentions in Source
> **Source: [[sources/style|style]]**
> - "Groups is an alternate syntax and wire format for nested messages. Groups are considered deprecated in proto2, were removed from proto3, and are converted to a delimited representation in edition 2023."
> - "You can use a nested message definition and field of that type instead of using the group syntax, using the message_encoding feature for wire-compatibility."

> **Source: [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]**
> - "enum MessageEncoding {
    LENGTH_PREFIXED = 0;
    DELIMITED = 1;
  }"
> - "optional MessageEncoding message_encoding = 5 [
      retention = RUNTIME,
      target = FIELD,
      (edition_defaults) = {
        edition: \"2023\", default: \"LENGTH_PREFIXED\"
      }
  ];"