---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/techniques]]"
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
tags:
  - "term"
aliases:
  - "textproto"
  - "文本格式"
  - "Protocol Buffers Text Format"
  - "TextProto"
  - "textproto"
  - "文本格式"
  - "Protocol Buffers Text Format"
  - "TextFormat"
  - "textproto"
  - "文本格式"
  - "Protocol Buffers Text Format"
  - "TextProto"
  - "textproto"
  - "文本格式"
  - "Protocol Buffers Text Format"
---

## Description
TextFormat 是 Protocol Buffers 提供的两种主要人类可读表示方式之一（另一种是 JSON），通常由生成的消息类 `DebugString` 方法输出。与 JSON 相比，TextFormat 更接近 wire format 的语义：在某些情况下提供与 wire format 相似的行为，例如在处理 `repeated` 字段时会附加名称-值映射（name-value mappings）来表达多值。由于其"仅包含已存在字段"的特性，TextFormat 在调试和反射（reflection）场景中尤为有用，例如通过文本格式进行消息的往返测试。TextFormat 与 wire format、JSON 并列为三种主要的 protobuf 数据表示方式，其推荐的现代文件扩展名为 `.txtpb`（而非较旧的 `.textproto`）。`DebugString` 输出可以使用 `printf` 风格占位符进行子消息格式化，并且该格式可通过 `--cpp_out` 标志下的 `annotate_headers` 选项让 C++ 代码生成器在输出中包含字段注释。

## Related Concepts
- [[concepts/wire-format|Wire Format]]
- [[concepts/json-format|JSON Format]]
- [[concepts/textproto|TextProto]]
- [[concepts/reserved-field-names|Reserved Field Names]]
- [[concepts/proto3|proto3]]
- [[concepts/reflection|Reflection]]
- [[concepts/synthetic-oneof|Synthetic Oneof]]
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/reflection-based-algorithms|Reflection-based algorithms]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/no-presence-discipline|No Presence Discipline]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]

## Mentions in Source
> **Source: [[sources/techniques|techniques]]**
> - "For Text Format specifically, `.textproto` is also fairly common, but we recommend `.txtpb` for its brevity."
> - "Text Format, Extension: `.txtpb`"

> **Source: [[sources/proto3|proto3]]**
> - "You should also reserve the field name to allow JSON and TextFormat encodings of your message to continue to parse."
> - "The definitions for Message2 and Message3 in the following code sample generate the same code for all languages, and there is no difference in representation in binary, JSON, and TextFormat:"
> - "No directly relevant information"

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "the JSON and TextFormat parsers/serializers in C++ and Java did not require any changes to support proto3 presence"
> - "the best way to test your reflection changes is to try round-tripping a message through text format, JSON, or some other reflection-based parser and serializer"
> - "No directly relevant information"

> **Source: [[sources/field_presence|field_presence]]**
> - "Two notable formats are TextFormat (the output format produced by generated message DebugString methods) and JSON."
> - "TextFormat more closely mimics the semantics of the wire format, and does, in certain cases, provide similar semantics (for example, appending repeated name-value mappings to a repeated field)."