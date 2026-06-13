---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/editions-cpp-apis-for-edition-zero.md]]"
tags:
  - "method"
aliases:
  - "FieldDescriptor::has_presence"
  - "has_presence method"
  - "FieldDescriptor::has_presence()"
  - "FieldDescriptor::has_presence"
  - "has_presence method"
---

## Related Concepts
- [[concepts/Field Presence]]
- [[concepts/Synthetic Oneof]]
- [[concepts/Oneof]]
- [[concepts/FieldDescriptor]]
- [[concepts/Editions]]

## Related Entities
- [[entities/mcy]]

## Mentions in Source

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "Add a `FieldDescriptor::has_presence()` method returning `bool` (adjusted to your language's naming convention). This should return true for all fields that have explicit presence, as documented in [docs/field_presence](field_presence.md). In particular, this includes fields in a oneof, proto2 scalar fields, and proto3 `optional` fields."

> **Source: [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]**
> - "In addition to the above functions, we'll use `FieldDescriptor::has_presence()` and `FieldDescriptor::is_packed()` to migrate callers performing comparisons to `syntax()`."
> - "Whether fields have hasbits (use `has_presence()`)."