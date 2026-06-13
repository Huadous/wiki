---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/options|options]]"
  - "[[brpc/server.md]]"
  - "[[protobuf/java-lite.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
  - "[[protobuf/features.md]]"
  - "[[brpc/json2pb.md]]"
  - "[[protobuf/editions.md]]"
  - "[[protobuf/editions-stricter-schemas-with-editions.md]]"
  - "[[brpc/getting_started.md]]"
  - "[[protobuf/editions-README.md]]"
  - "[[brpc/en_iobuf.md]]"
tags:
  - "project"
aliases:
  - "protobuf"
  - "Protocol Buffers"
  - "Google Protocol Buffers"
  - "Protobuf"
  - "protobuf"
  - "Protocol Buffers"
  - "Google Protocol Buffers"
---

## Related Entities
（暂无关联实体）

## Related Concepts
- [[concepts/stricter-schemas-with-editions|Stricter Schemas with Editions]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/identifier-naming-conventions|Identifier naming conventions]]
- [[concepts/reserved-keywords|Reserved keywords]]
- [[concepts/name-resolution-in-protobuf|Name resolution in Protobuf]]
- [[concepts/field-number-reservation|Field number reservation]]
- [[concepts/iobuf|IOBuf]]（新增：通过 IOBufAsZeroCopyInputStream / IOBufAsZeroCopyOutputStream 与 protobuf 互操作）
- [[concepts/iobufaszerocopyinputstream|IOBufAsZeroCopyInputStream]]（新增：将 IOBuf 包装为零拷贝输入流以解析 protobuf 消息）
- [[concepts/iobufaszerocopyoutputstream|IOBufAsZeroCopyOutputStream]]（新增：将 IOBuf 包装为零拷贝输出流以序列化 protobuf 消息）
- [[concepts/zero-copy-buffer|Zero-copy buffer]]（新增：protobuf 与 IOBuf 集成时的关键性能特性）

## Mentions in Source

> **Source: getting_started**
> - "protobuf: Serializations of messages, interfaces of services."
> - "protobuf: 3.0-5.29"
> - "bRPC 中使用了 protobuf 内部 API，上游不保证相关 API 的兼容性，目前测试可以支持到 v29(5.29)，如有问题欢迎反馈。"

> **Source: editions-readme**
> - No directly relevant information

> **Source: en_iobuf**
> - "brpc uses butil::IOBuf as data structure for attachment in some protocols and HTTP body."
> - "Serialize to or parse from protobuf messages."
> - No directly relevant information