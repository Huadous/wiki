---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/overview]]"
  - "[[sources/editions]]"
  - "[[sources/proto3]]"
tags:
  - "term"
aliases:
  - "Map type"
  - "键值对类型"
  - "map field"
  - "Map"
  - "Map type"
  - "键值对类型"
  - "map field"
  - "map"
  - "Map type"
  - "键值对类型"
  - "map field"
  - "Map"
  - "Map type"
  - "键值对类型"
  - "map field"
  - "Map fields"
  - "Map type"
  - "键值对类型"
  - "map field"
  - "Map"
  - "Map type"
  - "键值对类型"
  - "map field"
  - "map"
  - "Map type"
  - "键值对类型"
  - "map field"
  - "Map"
  - "Map type"
  - "键值对类型"
  - "map field"
---

## Description
Map fields provide a convenient data structure similar to dictionaries or hash maps in many programming languages, allowing developers to add key-value pair definitions directly to their protobuf messages. In the field cardinality system, map is treated as a distinct type alongside `repeated`, `optional`, and singular fields. When serialized, a map field is encoded as a repeated message entry, where each entry contains a key and a value field. This field type is widely used in proto3 syntax and is also supported in the editions language versions. For detailed usage guidance, including key and value type restrictions, developers should refer to the dedicated Maps section in the protobuf documentation.

## Related Concepts
- [[concepts/message-type|Message type]]
- [[concepts/scalar-value-types|标量类型]]
- [[concepts/field-cardinality|字段基数]]
- [[concepts/proto3|proto3 语法]]
- [[concepts/well-formed-messages|well-formed 消息]]
- [[concepts/wire-format|wire format]]
- [[concepts/field-number|字段编号]]
- [[concepts/repeated-fields|重复字段]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]

## Mentions in Source

> **Source: [[sources/overview|overview]]**
> - "A field can also be of: ... map type, to add key-value pairs to your definition." — [[protobuf/overview|overview]] (Protobuf 字段也可以是 map 类型，用于将键值对添加到你的定义中。)

> **Source: [[sources/editions|editions]]**
> - "map: this is a paired key/value field type. See Maps for more on this field type." — [[protobuf/editions|editions]] (map: 这是一种配对的键/值字段类型。有关此字段类型的更多信息，请参阅 Maps。)

> **Source: [[sources/proto3|proto3]]**
> - "This is a paired key/value field type. See Maps for more on this field type." — [[protobuf/proto3|proto3]] (这是一种配对的键/值字段类型。有关此字段类型的更多信息，请参阅 Maps。)
> - "Repeated Fields are Packed by Default" — [[protobuf/proto3|proto3]] (重复字段默认采用打包编码。)
> - "map: this is a paired key/value field type. See Maps for more on this field type." — [[protobuf/proto3|proto3]] (map: 这是一种配对的键/值字段类型。有关此字段类型的更多信息，请参阅 Maps。)