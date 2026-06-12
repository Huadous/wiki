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
  - "Message type"
  - "消息类型"
  - "复合数据类型"
  - "message"
  - "Message type"
  - "消息类型"
  - "复合数据类型"
---

## Description

message 是 Protocol Buffers 中数据的基本结构单元，用于定义复合数据类型。一个 message 由一组字段（field）组成，每个字段包含名称、类型、字段编号（field number）和基数（cardinality）。消息类型字段始终具有 field presence，表示该字段是否存在。典型的 message 定义以 SearchRequest 为例：包含查询字符串、页码和每页结果数三个字段。多个消息类型可以定义在同一个 .proto 文件中，并且可以包含注释和保留字段（reserved fields），用于维护向后兼容性。

## Related Concepts

- [[concepts/scalar-value-types|scalar-value-types]]
- [[concepts/proto3|proto3]]
- [[concepts/proto2|proto2]]
- [[concepts/field-number|field-number]]
- [[concepts/serialization|serialization]]
- [[concepts/enum|Enumeration]]
- [[concepts/map|Map]]
- [[concepts/field-cardinality|Field cardinality]]
- [[concepts/wire-format|Wire format]]
- [[concepts/field|Field]]
- [[concepts/field-presence|Field presence]]

## Related Entities

- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/grpc|grpc]]
- [[entities/protoc|protoc]]

## Mentions in Source

> **来源: [[sources/overview|overview]]**
> - "A field can also be of: message type, so that you can nest parts of the definition, such as for repeating sets of data."
> - "You can also create your own composite data types by defining messages that are, themselves, data types that you can assign to a field."

> **来源: [[sources/editions|editions]]**
> - "First let's look at a very simple example. Let's say you want to define a search request message format, where each search request has a query string, the particular page of results you are interested in, and a number of results per page."
> - "The SearchRequest message definition specifies three fields (name/value pairs), one for each piece of data that you want to include in this type of message."

> **来源: [[sources/proto3|proto3]]**
> - "Here’s the .proto file you use to define the message type."
> - "message SearchRequest { string query = 1; int32 page_number = 2; int32 results_per_page = 3; }"
> - "Multiple message types can be defined in a single .proto file."