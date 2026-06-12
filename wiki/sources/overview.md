---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[protobuf/overview.md]]"
tags: [Serialization, Backward compatibility, Forward compatibility, .proto file, Field number, Field cardinality, Proto3, Cross-language compatibility, Proto2, Edition 2023, Scalar Value Types, Message type, Enum type, Oneof type, Map type, Extensions, Reserved field number]
aliases: ["Protobuf 官方概述", "Protocol Buffers Documentation Overview"]
---

# Overview | Protocol Buffers Documentation - Summary

## 来源
- Original file: [[protobuf/overview.md]]
- Ingested: 2026-06-12

## 核心内容
本文件是 Protocol Buffers 官方文档的概览，由 [[entities/google|Google]] 开发并维护。Protocol Buffers 是一种语言中立、平台中立的序列化结构化数据机制，比 JSON 更小更快，并生成原生语言绑定。文档详细介绍了其定义、优势、适用场景、工作原理、数据类型支持（包括 [[concepts/scalar-value-types|Scalar Value Types]]、[[concepts/message-type|Message type]]、[[concepts/enum-type|Enum type]]、[[concepts/oneof-type|Oneof type]] 和 [[concepts/map-type|Map type]]）、[[concepts/backward-compatibility|Backward compatibility]] 与 [[concepts/forward-compatibility|Forward compatibility]] 的重要性，以及多种语法版本（[[concepts/proto2|Proto2]]、[[concepts/proto3|Proto3]] 和 [[concepts/edition-2023|Edition 2023]]）。文档还讨论了 [[entities/protoc|protoc]] 编译器直接支持的语言和通过插件支持的语言，以及 Protocol Buffers 在 [[entities/grpc|gRPC]]、[[entities/google-cloud|Google Cloud]] 和 [[entities/envoy-proxy|Envoy Proxy]] 等项目中的应用。

## 关键实体
- [[entities/protocol-buffers|Protocol Buffers]] — 核心序列化机制
- [[entities/google|Google]] — 开发和维护者
- [[entities/protoc|protoc]] — .proto 文件编译器
- [[entities/grpc|gRPC]] — 与 Protocol Buffers 紧密集成的 RPC 框架
- [[entities/envoy-proxy|Envoy Proxy]] — 使用 Protocol Buffers 的代理项目
- [[entities/google-cloud|Google Cloud]] — 使用 Protocol Buffers 的云平台
- [[entities/github|GitHub]] — 托管源代码和部分运行时库

## 关键概念
- [[concepts/serialization|Serialization]] — 将结构化数据转换为字节流的过程
- [[concepts/proto-file|.proto file]] — 定义数据结构的核心文件格式
- [[concepts/backward-compatibility|Backward compatibility]] — 新定义可被旧代码读取
- [[concepts/forward-compatibility|Forward compatibility]] — 旧消息可被新代码读取
- [[concepts/field-number|Field number]] — 消息字段的唯一数字标识符
- [[concepts/field-cardinality|Field cardinality]] — 字段的出现次数（singular/repeated/optional）
- [[concepts/proto3|Proto3]] 和 [[concepts/proto2|Proto2]] — 主要语法版本
- [[concepts/edition-2023|Edition 2023]] — 最新语法版本
- [[concepts/cross-language-compatibility|Cross-language compatibility]] — 多语言互操作能力
- [[concepts/extensions|Extensions]] — 在消息外部定义字段的机制
- [[concepts/field-number|field-number]] — 字段号保留的最佳实践

## 要点
- Protocol Buffers 比 JSON 更小更快，并生成原生语言绑定，支持向后和向前兼容。
- 通过 .proto 文件定义数据结构，使用 protoc 编译器生成多种语言代码。
- 提供丰富的数据类型：标量类型、消息类型、枚举、oneof 和 map 类型。
- 广泛用于 Google 内部服务通信和数据归档，并与 gRPC 等框架集成。
- 字段编号不能被重用，删除字段时应保留编号以防止兼容性问题。
- 不支持大型数据（超过几兆字节）、非面向对象语言或需要自我描述数据的场景。
- Protocol Buffers 不是正式标准，不适合有法律要求基于标准的环境。
- 支持多种语法版本，其中 Edition 2023 是未来的发展方向。