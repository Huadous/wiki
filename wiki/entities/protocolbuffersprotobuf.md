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
  - "[[brpc/baidu_std.md]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
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
- [[concepts/rpc|RPC]]（新增：Protobuf 内置的 RPC Service 形式是 baidu_std 等协议定义通信的基础）
- [[concepts/rpcmeta|RpcMeta]]（新增：baidu_std 协议中的核心元数据结构，使用 Protobuf message 定义）
- [[concepts/rpcrequestmeta|RpcRequestMeta]]（新增：baidu_std 协议中的请求元数据，使用 Protobuf message 定义）
- [[concepts/rpcresponsemeta|RpcResponseMeta]]（新增：baidu_std 协议中的响应元数据，使用 Protobuf message 定义）

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

> **Source: [[sources/baidu_std|baidu_std]]**
> - "它以Protobuf作为基本的数据交换格式，并基于Protobuf内置的RPC Service形式，规定了通信双方之间的数据交换协议，以实现完整的RPC调用。"
> - "调用方法所需参数应放在一个Protobuf消息内。如果方法有返回结果，也同样应放在一个Protobuf消息内。具体定义由通信双方自行约定。特别地，可以使用空的Protobuf消息来表示请求/响应为空的情况。"
> - No directly relevant information

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - No directly relevant information