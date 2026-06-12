---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/editions]]"
  - "[[sources/encoding]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
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
---

## Description
打包字段（packed fields）是Protobuf中针对重复字段（repeated fields）的一种序列化优化技术。在传统的重复字段编码中，每个元素都包含独立的tag-value对，导致额外的元数据开销。打包编码将所有元素的原始值连续存储在一个LEN类型的wire字节中，显著减少消息大小。在proto2和proto3中，标量数字类型的重复字段需要显式声明`[packed=true]`选项才能启用打包编码。从Edition 2023开始，所有原始类型（除string和bytes外的标量类型）的重复字段默认使用打包编码。这种变化通过[[concepts/feature|Feature]]机制和版本迁移来实现，旨在统一不同Protobuf版本之间的行为差异。

## Related Concepts
- [[concepts/field-cardinality|field cardinality]]
- [[concepts/wire-format|wire format]]
- [[concepts/protocol-buffer-encoding|Protocol Buffer Encoding]]
- [[concepts/scalar-types|scalar types]]
- [[concepts/length-delimited-records|Length-delimited records]]
- [[concepts/varint|varint]]
- [[concepts/tag-length-value|Tag-Length-Value (TLV)]]
- [[concepts/repeated-field|repeated field]]
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

> **Source: [[sources/encoding|encoding]]**
> - "Starting in Edition 2023, repeated fields of a primitive type (any scalar type that is not string or bytes) are packed."
> - "LEN: string, bytes, embedded messages, packed repeated fields"

> **Source: [[sources/proto3|proto3]]**
> - "In proto3, repeated fields of scalar numeric types use packed encoding by default."
> - "You can find out more about packed encoding in Protocol Buffer Encoding."
> - "No directly relevant information"

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "We still have `required` and `group`, `packed` is not everywhere, and string accessors in C++ still return `const std::string&`."
> - "Make all scalar `repeated` fields `packed`, improving throughput."