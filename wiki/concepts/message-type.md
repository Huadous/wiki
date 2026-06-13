---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/editions]]"
  - "[[sources/proto3]]"
  - "[[protobuf/proto3.md]]"
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
> - "Here's the .proto file you use to define the message type."
> - "message SearchRequest { string query = 1; int32 page_number = 2; int32 results_per_page = 3; }"
> - "Multiple message types can be defined in a single .proto file."
> - "First let's look at a very simple example. Let's say you want to define a search request message format, where each search request has a query string, the particular page of results you are interested in, and a number of results per page."
> - "The SearchRequest message definition specifies three fields (name/value pairs), one for each piece of data that you want to include in this type of message."
> - "No directly relevant information"