---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/editions]]"
  - "[[sources/proto3]]"
  - "[[sources/encoding]]"
  - "[[protobuf/editions.md]]"
tags:
  - "standard"
aliases:
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "scalar types"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "int32/int64 signed integers (two's complement)"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "scalar types"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "Scalar types"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "scalar types"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "int32/int64 signed integers (two's complement)"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "scalar types"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "Scalar Value Type"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "scalar types"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "int32/int64 signed integers (two's complement)"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "scalar types"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "Scalar types"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "scalar types"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "int32/int64 signed integers (two's complement)"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
  - "scalar types"
  - "标量类型"
  - "primitive data types"
  - "Scalar Value Types"
---

## Description
Scalar Value Type 是 Protocol Buffers 消息字段中最基础的数据类型类别，用于表示单一的原始数值或简单数据。在 .proto 文件中声明字段时，需要为每个字段指定一个标量类型，如 `double`、`int32`、`string`、`bool` 等。Protocol Buffers 为这些标量类型定义了统一的[[concepts/wire-format|wire format]] 编码规则，并在不同目标语言中提供对应的本地类型映射，使开发者能够以类型安全的方式处理序列化和反序列化操作。

值得注意的是，某些整数类型（如 `int32` 和 `int64`）在编码负数时效率较低，因为它们使用[[concepts/varint|varint]]编码，对负数始终以 10 字节表示。对于可能包含负数值的字段，建议使用 `sint32` 或 `sint64`，这两种类型采用[[concepts/zigzag-encoding|ZigZag 编码]]，可以更高效地编码负数。标量类型与[[concepts/composite-type|复合类型]]（如 message）相对，是构建更复杂数据结构的基础组件，与[[concepts/enumeration|枚举类型]]共同构成了 Protocol Buffers 类型系统的核心。

## Related Concepts
- [[concepts/serialization|Serialization]]
- [[concepts/field-cardinality|Field Cardinality]]
- [[concepts/field-number|Field Number]]
- [[concepts/proto-file|Proto File]]
- [[concepts/proto3|Proto3]]
- [[concepts/backward-compatibility|Backward Compatibility]]
- [[concepts/forward-compatibility|Forward Compatibility]]
- [[concepts/packed-encoding|Packed Encoding]]
- [[concepts/enumeration|Enumeration]]
- [[concepts/composite-type|Composite Type]]
- [[concepts/wire-format|Wire Format]]
- [[concepts/varint|Varint]]
- [[concepts/zigzag-encoding|ZigZag Encoding]]
- [[concepts/signed-integers|Signed Integers]]
- [[concepts/default-values|Default Values]]
- [[concepts/message-type|Message Type]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|Protoc]]
- [[entities/grpc|gRPC]]
- [[entities/protoscope|Protoscope]]

## Mentions in Source
> **Source: [[sources/editions|editions]]**
> - "A scalar message field can have one of the following types – the table shows the type specified in the .proto file, and the corresponding type in the automatically generated class"
> - "In the earlier example, all the fields are scalar types: two integers (page_number, results_per_page) and a string (query)."