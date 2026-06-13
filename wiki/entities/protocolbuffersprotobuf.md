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
  - "[[protobuf/editions-edition-lifetimes.md]]"
  - "[[protobuf/editions-cpp-apis-for-edition-zero.md]]"
  - "[[protobuf/cpp_build_systems.md]]"
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
Protobuf（Protocol Buffers）是 Google 开发的开源数据序列化格式与工具集，brpc 广泛使用其作为消息序列化与 RPC Service 接口的基础格式，目前测试可支持到 v29（5.29）版本。Protobuf 提出了 Edition 机制来管理版本演进，并通过 Edition Lifetimes、Feature Lifetimes、Minimum Required Edition 等设计将 Edition 与破坏性变更解耦，简化了版本管理。在数据交换层面，Protobuf 支持二进制与 JSON 两种序列化方式，并经历了从 proto2 到 proto3 在字段存在性、JSON 校验严格度等方面的语义收敛。构建系统方面，Protobuf 项目历史上在 Google 内部使用其专有构建系统（后演变为 Bazel）开发，2008 年开源后改用 Autoconf，随后社区贡献引入了 Bazel；目前 C++ Protobuf 可同时通过 Bazel 和 CMake 构建，以 Bazel 定义为权威源。

## Related Entities
- [[entities/brpc|brpc]] — 使用 Protobuf 作为序列化与 RPC 接口的基础

## Related Concepts
- [[concepts/editions|Editions]] — Protobuf 的版本机制
- [[concepts/edition-lifetimes|Edition Lifetimes]] — Edition 生命周期设计
- [[concepts/feature-lifetimes|Feature Lifetimes]] — 特性生命周期
- [[concepts/edition-zero|Edition Zero]] — 已完成的 Edition 基线版本
- [[concepts/minimum-required-edition|Minimum Required Edition]] — 最低必需版本机制
- [[concepts/field-presence|Field Presence]] — 字段存在性语义
- [[concepts/proto3-presence|Proto3 Presence]] — Proto3 可选字段实现
- [[concepts/bazel|Bazel]] — Protobuf C++ 当前主要使用的构建系统
- [[concepts/cmake|CMake]] — Protobuf C++ 备选构建系统
- [[concepts/blaze|Blaze]] — Bazel 的前身，Google 内部构建系统
- [[concepts/cc-file-list-aspect|cc_file_list_aspect]] — Bazel 中导出 C++ 文件列表的 aspect
- [[concepts/proto-file-list-aspect|proto_file_list_aspect]] — Bazel 中导出 proto 文件列表的 aspect

## Mentions in Source

> **Source: [[sources/getting_started|getting_started]]**
> - "protobuf: Serializations of messages, interfaces of services."
> - "protobuf: 3.0-5.29"
> - "bRPC 中使用了 protobuf 内部 API，上游不保证相关 API 的兼容性，目前测试可以支持到 v29(5.29)，如有问题欢迎反馈。"

> **Source: [[sources/editions-readme|editions-readme]]**
> - "Every Protobuf runtime implementation must specify the newest edition whose constructs it can handle (at a particular rev of that implementation)."

> **Source: [[sources/en_iobuf|en_iobuf]]**
> - "brpc uses butil::IOBuf as data structure for attachment in some protocols and HTTP body."
> - "Serialize to or parse from protobuf messages."

> **Source: [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]**
> - "to the Protobuf language. This would entail a descriptor change to track the values of constants, but they would not be loaded properly by older runtimes."

> **Source: [[sources/baidu_std|baidu_std]]**
> - "它以Protobuf作为基本的数据交换格式，并基于Protobuf内置的RPC Service形式，规定了通信双方之间的数据交换协议，以实现完整的RPC调用。"
> - "调用方法所需参数应放在一个Protobuf消息内。如果方法有返回结果，也同样应放在一个Protobuf消息内。具体定义由通信双方自行约定。特别地，可以使用空的Protobuf消息来表示请求/响应为空的情况。"

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - No directly relevant information

> **Source: [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]**
> - "Today, proto3 fully validates JSON mappings for uniqueness during parsing, while proto2 takes a best-effort approach and allows cases that don't have a 1:1 mapping."（目前，proto3 在解析时会完全校验 JSON 映射的唯一性，而 proto2 采用尽力而为的方式，允许出现不具有 1:1 映射的情况。）
> - "All proto messages can be serialized to JSON"（所有 proto 消息都可以被序列化为 JSON。）
> - "https://github.com/protocolbuffers/protobuf/issues/12525"
> - "Some projects generate proto descriptors at runtime and uses underscores to disambiguate field names."（一些项目在运行时生成 proto 描述符，并使用下划线来消歧字段名。）

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - No directly relevant information

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - No directly relevant information

> **Source: [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]**
> - "Now that Edition Zero is complete, we need to re-evaluate what the lifetimes of features and editions look like going forward."
> - "It separates editions from breaking changes, and means that we only need to worry about one versioning scheme (our OSS release)."
> - No directly relevant information

> **Source: [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]**
> - No directly relevant information

> **Source: [[sources/cpp_build_systems|cpp_build_systems]]**
> - "Protobuf primarily uses Bazel to build the Protobuf C++ runtime and Protobuf compiler."
> - "On a historical note, prior to its release as Open Source Software, the Protobuf project was developed using Google's internal build system, which was the predecessor to Bazel."
> - "Currently, C++ Protobuf can be built with Bazel and CMake."