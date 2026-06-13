---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/implementing_proto3_presence|implementing_proto3_presence]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
tags:
  - "term"
aliases:
  - "FieldDescriptor class"
  - "google::protobuf::FieldDescriptor"
---

## Related Concepts
- [[concepts/reflection|Reflection]]
- [[concepts/synthetic-oneof|Synthetic Oneof]]
- [[concepts/oneof|Oneof]]
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/enum-field-closedness|Enum Field Closedness]]
- [[concepts/legacy-treat-enum-as-closed|legacy_treat_enum_as_closed]]
- [[concepts/open-enum|Open Enum]]
- [[concepts/enumdescriptor|EnumDescriptor]]

## Related Entities
- [[entities/codegeneratorresponse|Code Generator]]
- [[entities/plugin-proto|protoc]]
- [[entities/mcy|@mcy]]
- [[entities/protocol-buffers|Protocol Buffers]]

## Mentions in Source

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - `bool MessageHasPresence(const google::protobuf::FieldDescriptor* field) { return field->has_presence(); }`
> - `1. Add a `FieldDescriptor::has_presence()` method returning `bool` (adjusted to your language's naming convention).`

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - `an open (lol) question is whether we should move is_closed from EnumDescriptor to FieldDescriptor.`
> - `bool FieldDescriptor::legacy_enum_field_treated_as_closed() const { return type() == TYPE_ENUM && file().syntax() == FileDescriptor::SYNTAX_PROTO2; }`