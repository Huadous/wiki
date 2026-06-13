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
  - "[[protobuf/editions-life-of-an-edition.md]]"
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
  - "features.packed"
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
  - "`packed` migration"
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
  - "features.packed"
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

## Description
Packed encoding consolidates the on-the-wire representation of repeated scalar numeric fields into one length-delimited entry, reducing both tag overhead and total byte count. In proto3 and Editions (starting with Edition 2023), repeated fields of scalar numeric types use packed encoding by default, meaning schema authors get the wire-format savings without opt-in syntax. In Editions, `features.packed` serves as a global feature that can change the serialization encoding of repeated fields to packed format; it is cited as the existence proof that wire-format-breaking changes are achievable via features, even if very expensive. The migration strategy established for `features.packed` — modifying parsers to accept both the old and new encodings so that old and new readers are both tolerant, then waiting through a long horizon so old writers and readers naturally fall out of circulation, and finally flipping the default so new code uses the new encoding — is the template now being reused for `features.group_encoding`. Because of this proven pattern, long-horizon wire-format break migrations are characterized as "not insurmountable, merely very expensive." Duplicate `repeated` fields append to the field's API representation, though serializing a packed repeated field produces only one length-delimited value in the tag stream. C++ string accessors still return `const std::string&`, and the broader goal of making all scalar `repeated` fields `packed` was adopted to improve throughput.

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
- [[concepts/group_encoding|group_encoding]]
- [[concepts/group-encoded-messages-migration|Group-Encoded Messages migration]]

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

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "Changing the serialization encoding of a field (so long as it does not break readers). E.g., `features.packed`, eventually `features.group_encoding`."
> - "We can do what we did for `packed`."
> - "`packed` is an existence proof that this is not insurmountable, merely very expensive."
> - "E.g., `features.packed`, eventually `features.group_encoding`."
> - "We can do what we did for `packed`."