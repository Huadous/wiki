---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/editions]]"
  - "[[sources/encoding]]"
  - "[[sources/proto3]]"
  - "[[protobuf/proto3.md]]"
tags:
  - "term"
aliases:
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "Reserved field number"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "reserved field"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "Reserved field number"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "reserved"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "Reserved field number"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "reserved field"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "Reserved field number"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "Reserved Field Numbers"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "Reserved field number"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "reserved field"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "Reserved field number"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "reserved"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "Reserved field number"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "reserved field"
  - "字段标签"
  - "field tag"
  - "field identifier"
  - "Reserved field number"
  - "字段标签"
  - "field tag"
  - "field identifier"
---

## Related Concepts
- [[concepts/backward-compatibility|backward-compatibility]]
- [[concepts/serialization|serialization]]
- [[concepts/forward-compatibility|forward-compatibility]]
- [[concepts/reserved-field|reserved field]]
- [[concepts/wire-format|wire format]]
- [[concepts/edition|edition]]
- [[concepts/wire-type|wire type]]
- [[concepts/varint|varint]]
- [[concepts/field-cardinality|field cardinality]]
- [[concepts/packed-encoding|packed encoding]]
- [[concepts/message-type|message type]]
- [[concepts/reserved-field-names|reserved field names]]

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/grpc|grpc]]
- [[entities/protoc|protoc]]
- [[entities/protoscope|protoscope]]

## Mentions in Source
> **Source: [[sources/proto3|proto3]]**
> - "You must give each field in your message definition a number between 1 and 536,870,911 with the following restrictions."
> - "Field numbers 19,000 to 19,999 are reserved for the Protocol Buffers implementation."
> - "Reusing a field number makes decoding wire-format messages ambiguous."
> - "If you update a message type by entirely deleting a field, or commenting it out, future developers can reuse the field number... To make sure this doesn't happen, add your deleted field number to the reserved list."
> - "Reserved field number ranges are inclusive (9 to 11 is the same as 9, 10, 11)."
> - "You must give each field in your message definition a number between 1 and 536,870,911 — proto3"
> - "This number cannot be changed once your message type is in use because it identifies the field in the message wire format."
> - "Field numbers 19,000 to 19,999 are reserved for the Protocol Buffers implementation."
> - "When you no longer need a field and all references have been deleted from client code, you may delete the field definition from the message. However, you must reserve the deleted field number."
> - "To make sure this doesn't happen, add your deleted field number to the reserved list."
> - "The protoc compiler will generate error messages if any future developers try to use these reserved field numbers."