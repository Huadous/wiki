---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/overview]]"
  - "[[sources/en_overview]]"
tags:
  - "method"
aliases:
  - "数据序列化"
  - "serializing structured data"
  - "data serialization"
  - "序列化 (Serialization)"
  - "数据序列化"
  - "serializing structured data"
  - "data serialization"
  - "序列化"
  - "数据序列化"
  - "serializing structured data"
  - "data serialization"
  - "序列化 (Serialization)"
  - "数据序列化"
  - "serializing structured data"
  - "data serialization"
---

## Related Concepts
- [[concepts/RPC|RPC]]
- [[concepts/proto-file|.proto 文件]]
- [[concepts/backward-compatibility|向后兼容性]]
- [[concepts/forward-compatibility|向前兼容性]]
- [[concepts/HTTP|HTTP]]
- [[concepts/protobuf|protobuf]]
- [[concepts/TCP-IP|TCP/IP]]
- [[concepts/json|JSON]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/grpc|gRPC]]
- [[entities/protoc|protoc]]
- [[entities/brpc|brpc]]
- [[entities/thrift|thrift]]
- [[entities/protobuf|protobuf]]

## Mentions in Source
- "Protocol buffers provide a serialization format for packets of typed, structured data that are up to a few megabytes in size." — [[sources/overview|overview]]
- "Protocol buffers are a combination of the definition language ... the serialization format for data that is written to a file (or sent across a network connection), and the serialized data." — [[sources/overview|overview]]
- "RPC needs serialization which is done by protobuf pretty well." — [[sources/en_overview|en_overview]]
- "For http services, json is used for serialization extensively." — [[sources/en_overview|en_overview]]
- "Many protocols support carrying binary data along with protobuf requests and bypass the serialization." — [[sources/en_overview|en_overview]]
- "Users fill requests in format of protobuf::Message, do RPC, and fetch results from responses in protobuf::Message." — [[sources/en_overview|en_overview]]
- "protobuf has good forward and backward compatibility for users to change fields and build services incrementally." — [[sources/en_overview|en_overview]]