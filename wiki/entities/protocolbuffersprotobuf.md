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
  - "[[protobuf/editions-minimum-required-edition.md]]"
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
- [[entities/protoc|protoc]]（新增：Protobuf 的编译器）
- [[entities/protobuf-editions|Protobuf Editions]]（新增：Protobuf 正在进行的重大演进机制）
- [[entities/prototiller|Prototiller]]（新增：与 Protobuf 工具链相关的项目）
- [[entities/mcy|@mcy]]（新增：相关贡献者）

## Related Concepts
- [[concepts/stricter-schemas-with-editions|Stricter Schemas with Editions]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/identifier-naming-conventions|Identifier naming conventions]]
- [[concepts/reserved-keywords|Reserved keywords]]
- [[concepts/name-resolution-in-protobuf|Name resolution in Protobuf]]
- [[concepts/field-number-reservation|Field number reservation]]
- [[concepts/iobuf|IOBuf]]（通过 IOBufAsZeroCopyInputStream / IOBufAsZeroCopyOutputStream 与 protobuf 互操作）
- [[concepts/iobufaszerocopyinputstream|IOBufAsZeroCopyInputStream]]（将 IOBuf 包装为零拷贝输入流以解析 protobuf 消息）
- [[concepts/iobufaszerocopyoutputstream|IOBufAsZeroCopyOutputStream]]（将 IOBuf 包装为零拷贝输出流以序列化 protobuf 消息）
- [[concepts/zero-copy-buffer|Zero-copy buffer]]（protobuf 与 IOBuf 集成时的关键性能特性）
- [[concepts/minimum-required-edition|Minimum Required Edition]]（新增：解决 Protobuf 新特性与旧运行时兼容性的机制）
- [[concepts/descriptor.proto|descriptor.proto]]（新增：Protobuf 核心描述格式的定义文件）
- [[concepts/filedescriptorproto|FileDescriptorProto]]（新增：描述符相关概念）
- [[concepts/edition|Edition]]（新增：Protobuf 版本演进的基本单位）

## Mentions in Source

> **Source: [[sources/getting_started|getting_started]]**
> - "protobuf: Serializations of messages, interfaces of services."
> - "protobuf: 3.0-5.29"
> - "bRPC 中使用了 protobuf 内部 API，上游不保证相关 API 的兼容性，目前测试可以支持到 v29(5.29)，如有问题欢迎反馈。"

> **Source: [[sources/editions-readme|editions-readme]]**
> - No directly relevant information

> **Source: [[sources/en_iobuf|en_iobuf]]**
> - "brpc uses butil::IOBuf as data structure for attachment in some protocols and HTTP body."
> - "Serialize to or parse from protobuf messages."
> - No directly relevant information

> **Source: [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]**
> - "to the Protobuf language. This would entail a descriptor change to track the values of constants, but they would not be loaded properly by older runtimes."
> - "Every Protobuf runtime implementation must specify the newest edition whose constructs it can handle (at a particular rev of that implementation)."
> - No directly relevant information