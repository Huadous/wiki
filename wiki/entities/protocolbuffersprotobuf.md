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
  - "[[protobuf/editions-edition-zero-features.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
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
> - No directly relevant information

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - No directly relevant information

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - No directly relevant information