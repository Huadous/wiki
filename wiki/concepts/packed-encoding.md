---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions]]"
  - "[[sources/encoding]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/field_presence.md]]"
  - "[[protobuf/editions.md]]"
tags:
  - "method"
aliases:
  - "packed serialization"
  - "打包序列化"
  - "Packed repeated fields"
  - "packed serialization"
  - "打包序列化"
  - "Packed Fields"
  - "packed serialization"
  - "打包序列化"
  - "Packed repeated fields"
  - "packed serialization"
  - "打包序列化"
  - "Packed repeated field"
  - "packed serialization"
  - "打包序列化"
  - "Packed repeated fields"
  - "packed serialization"
  - "打包序列化"
  - "Packed Fields"
  - "packed serialization"
  - "打包序列化"
  - "Packed repeated fields"
  - "packed serialization"
  - "打包序列化"
---

## Related Concepts
- [[concepts/wire-format|wire format]]
- [[concepts/scalar-types|scalar types]]
- [[concepts/length-delimited-records|Length-delimited records]]
- [[concepts/tag-length-value|Tag-Length-Value (TLV)]]
- [[concepts/repeated-field|repeated field]]
- [[concepts/varint|varint]]
- [[concepts/protocol-buffer-encoding|Protocol Buffer Encoding]]
- [[concepts/field-cardinality|field cardinality]]
- [[concepts/feature|Feature]]
- [[concepts/edition|Edition]]
- [[concepts/feature-lifecycle|Feature Lifecycle]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/protoscope|protoscope]]
- [[entities/c++|C++]]

## Mentions in Source
> **Source: [[sources/editions|editions]]**
> - "In proto editions, repeated fields of scalar numeric types use packed encoding by default."
> - "You can find out more about packed encoding in Protocol Buffer Encoding."
> - "No directly relevant information"

> **Source: [[sources/encoding|encoding]]**
> - "Starting in Edition 2023, repeated fields of a primitive type (any scalar type that is not string or bytes) are packed."
> - "LEN: string, bytes, embedded messages, packed repeated fields"

> **Source: [[sources/proto3|proto3]]**
> - "In proto3, repeated fields of scalar numeric types use packed encoding by default."
> - "You can find out more about packed encoding in Protocol Buffer Encoding."
> - "No directly relevant information"
> - "Repeated Fields are Packed by Default: In proto3, repeated fields of scalar numeric types use packed encoding by default."

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "We still have `required` and `group`, `packed` is not everywhere, and string accessors in C++ still return `const std::string&`."
> - "Make all scalar `repeated` fields `packed`, improving throughput."

> **Source: [[sources/field_presence|field_presence]]**
> - "Duplicate `repeated` fields are typically appended to the field's API representation. (Note that serializing a _packed_ repeated field produces only one, length-delimited value in the tag stream.)"