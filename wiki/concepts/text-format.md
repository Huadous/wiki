---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/techniques]]"
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
  - "[[protobuf/editions.md]]"
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

## Related Concepts
- [[concepts/wire-format|Wire Format]]
- [[concepts/json-format|JSON Format]]
- [[concepts/textproto|TextProto]]
- [[concepts/reserved-field-names|Reserved Field Names]]
- [[concepts/reserved-field|Reserved Field]]
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
> - "No directly relevant information"

> **Source: [[sources/editions|editions]]**
> - "Reusing an old field name later is generally safe, except when using TextProto or JSON encodings where the field name is serialized."
> - "you should also reserve the field name to allow JSON and TextFormat encodings of your message to continue to parse."
> - "No directly relevant information"