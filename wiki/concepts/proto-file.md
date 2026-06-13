---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/style]]"
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/editions.md]]"
tags:
  - "term"
aliases:
  - "proto file"
  - "proto definition"
  - "File Structure"
  - "proto file"
  - "proto definition"
  - ".proto file"
  - "proto file"
  - "proto definition"
  - "File Structure"
  - "proto file"
  - "proto definition"
---

## Related Concepts
- [[concepts/serialization|序列化]]
- [[concepts/backward-compatibility|向后兼容]]
- [[concepts/proto3|Proto3]]
- [[concepts/proto2|Proto2]]
- [[concepts/field-number|字段编号]]
- [[concepts/field-cardinality|字段基数]]
- [[concepts/standard-file-formatting|标准文件格式]]
- [[concepts/package|Package]]
- [[concepts/lower-snake-case|lower_snake_case]]
- [[concepts/message-type|Message Type]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/well-formed-messages|Well-formed Messages]]
- [[concepts/scalar-value-type|Scalar Value Type]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/grpc|gRPC]]
- [[entities/google|Google]]

## Mentions in Source
> **Source: [[sources/overview|overview]]**
> - "You define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of data streams and using a variety of languages."

> **Source: [[sources/style|style]]**
> - "Files should be named lower_snake_case.proto"
> - "All files should be ordered in the following manner: License header (if applicable), File overview, Syntax or edition, Package, Imports (sorted), File options, Everything else."
> - "No directly relevant information"

> **Source: [[sources/proto3|proto3]]**
> - "Multiple message types can be defined in a single .proto file. This is useful if you are defining multiple related messages – so, for example, if you wanted to define the reply message format that corresponds to your SearchResponse message type, you could add it to the same .proto file."
> - "Here's the .proto file you use to define the message type."
> - "No directly relevant information"

> **Source: [[sources/editions|editions]]**
> - "Here's the .proto file you use to define the message type."
> - "While multiple message types (such as message, enum, and service) can be defined in a single .proto file, it can also lead to dependency bloat when large numbers of messages with varying dependencies are defined in a single file."
> - "C-style inline/multi-line comments /* ... */ are also accepted."
> - "No directly relevant information"