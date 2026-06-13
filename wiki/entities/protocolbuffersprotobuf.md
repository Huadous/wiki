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
  - "[[protobuf/editions-edition-zero-json-handling.md]]"
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

## Description
Protobuf（Protocol Buffers）是 Google 开发的一种语言无关、平台无关的可扩展序列化结构数据机制，在 brpc 中被用作核心的数据交换格式。brpc 使用 butil::IOBuf 作为部分协议中 attachment 的数据结构以及 HTTP body 的载体，并通过 IOBufAsZeroCopyInputStream 与 IOBufAsZeroCopyOutputStream 与 protobuf 消息进行零拷贝序列化与解析。基于 Protobuf 内置的 RPC Service 形式，brpc 的 baidu_std 协议规定了通信双方之间的数据交换协议，以实现完整的 RPC 调用，其中请求参数与响应结果均封装在 Protobuf message 中。Protobuf 当前主要使用 proto2 与 proto3 两个语法版本，并正在向 Editions 模型演进；为解决新特性与旧运行时之间的兼容性问题，Protobuf 引入了最低必需版本（Minimum Required Edition）机制。当前所有 proto 消息都可以被序列化为 JSON 格式，但在 JSON 映射的字段名冲突方面存在历史遗留问题：proto3 在解析时会完全校验 JSON 映射的唯一性，而 proto2 采用尽力而为的方式，允许出现不具有 1:1 映射的情况。本次 Editions 设计提案（Edition Zero）正是为了解决这一 JSON 字段名冲突问题而提出。在该提案的讨论中，Protobuf 社区引用了 [[protobuf/protocolbuffers/protobuf|protocolbuffers/protobuf]] 仓库中的 Issue #12525 作为 DISALLOW 模式的使用案例，说明存在一些项目在运行时生成 proto 描述符，并使用下划线（underscores）来消歧（disambiguate）字段名。

## Related Entities
- [[entities/edition-zero|Edition Zero]]
- [[entities/mkruskal-google|mkruskal-google]]
- [[entities/protocolbuffers/protobuf|protocolbuffers/protobuf]]（Protobuf 开源项目的官方 GitHub 仓库，其 Issue #12525 被引用为 Edition Zero 提案中 DISALLOW 模式的使用案例示例）

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
- [[concepts/proto2|proto2]]（新增：Protobuf 早期语法版本，对 JSON 映射采用尽力而为的校验策略）
- [[concepts/proto3|proto3]]（新增：Protobuf 当前主要语法版本，对 JSON 映射在解析时进行完全唯一性校验）
- [[concepts/json_name-field-option|json_name field option]]（新增：用于解决 JSON 字段名冲突的字段选项）
- [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]]（新增：Edition Zero 提案要解决的核心问题）
- [[concepts/disallow|DISALLOW]]（新增：Edition Zero 提案中用于表示禁止某特征组合的模式，Issue #12525 作为其使用案例）
- [[concepts/json_format-feature|json_format feature]]（新增：与 Protobuf JSON 序列化能力相关的功能特性）

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

> **Source: [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]**
> - "Today, proto3 fully validates JSON mappings for uniqueness during parsing, while proto2 takes a best-effort approach and allows cases that don't have a 1:1 mapping."（目前，proto3 在解析时会完全校验 JSON 映射的唯一性，而 proto2 采用尽力而为的方式，允许出现不具有 1:1 映射的情况。）
> - "All proto messages can be serialized to JSON"（所有 proto 消息都可以被序列化为 JSON。）
> - "https://github.com/protocolbuffers/protobuf/issues/12525"
> - "Some projects generate proto descriptors at runtime and uses underscores to disambiguate field names."（一些项目在运行时生成 proto 描述符，并使用下划线来消歧字段名。）