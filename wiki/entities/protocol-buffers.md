---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/techniques]]"
  - "[[sources/en_server]]"
  - "[[sources/editions]]"
  - "[[sources/style]]"
  - "[[sources/en_overview]]"
  - "[[sources/encoding]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[sources/en_http_service]]"
  - "[[sources/en_getting_started]]"
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/java-lite.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
tags:
  - "product"
aliases:
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Protobuf"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Google Protocol Buffers"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Protobuf"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Google Protobuf"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Protobuf"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Google Protocol Buffers"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Protobuf"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
---

## Description
Protocol Buffers（简称 Protobuf）是 Google 开发的一种语言中立、平台中立的可扩展数据序列化机制，类似于 JSON 或 XML 但更小、更快、更简单，最早由 Google 于 2008 年发布，文档源自其官方开发者页面（https://developers.google.com/protocol-buffers/）。它通过 `.proto` 文件定义结构化数据，并借助 `protoc` 编译器为包括 Java、C++、Python、Go 等多种语言生成对应的数据访问类；Protobuf 不仅是一种序列化格式，更是一个完整的生态系统，包含编译器 `protoc` 和多种数据表示格式（如 TextFormat、JSON）。Protobuf 有两个主要版本——`proto2` 与 `proto3`——二者在字段存在性（field presence）的处理上存在重要差异：`proto2` 历史上主要遵循显式存在性（explicit presence），而 `proto3` 仅暴露无存在性（no presence）语义。Protobuf 是 Google 最古老、最成功的工具链项目之一，其最后的一次重大语法变革（`proto3`）曾使整个生态系统产生分裂，而继 `proto3` 之后的 `editions` 版本系统则引入了按版本配置特性的新机制。在 3.12 版本中，Protobuf 引入了实验性的 proto3 `optional` 字段支持，该特性用以解决 wrapper 类型在可用性与效率上的不足，并要求包括 Google 官方和第三方在内的所有代码生成器进行相应更新；此功能的加入源自 Google 内部与开源社区的共同反馈。在 Java 平台上，Protobuf 还提供了 Java Lite 运行时，专门为 Android 等资源受限场景做了体积和性能优化，可通过 `LITE_RUNTIME` 优化选项生成精简代码，并依赖 R8 进行进一步缩减。

## Related Entities
- [[entities/brpc|brpc]] — 深度依赖Protobuf的RPC框架，利用protobuf定义所有服务接口
- [[entities/google|Google]] — Protobuf的创始者和主要维护者
- [[entities/open-source-oss-community|open-source-oss-community]] — Protobuf的开源社区维护力量，同时为 proto3 optional 字段支持提供了关键反馈
- [[entities/protoc|protoc]] — Protobuf的编译器，负责从.proto文件生成多语言数据访问类，也是 protobuf 生态系统的核心组件
- [[entities/protocolbuffersprotobuf|protocolbuffersprotobuf]] — Protobuf项目实体页面
- [[entities/textformat|TextFormat]] — protobuf 生态中的人类可读文本表示格式（来自 field_presence 源文档）
- [[entities/fieldmask|FieldMask]] — protobuf 生态中的字段掩码工具类型（来自 field_presence 源文档）

## Related Concepts
- [[concepts/序列化|序列化]] — protobuf的核心能力，将结构化数据转换为线格式
- [[concepts/编码规范|编码规范]] — .proto文件的命名和格式约定
- [[concepts/RPC|RPC]] — protobuf最常见的应用场景
- [[concepts/proto3|proto3]] — 当前主流的protobuf语法版本，brpc 1.8.0后强制要求，其引入曾分裂生态
- [[concepts/editions|editions]] — 继proto3之后的新一代语法版本系统
- [[concepts/字段|字段]] — 消息中的基本数据单元
- [[concepts/字段编号|字段编号]] — 每个字段在二进制编码中的唯一标识号
- [[concepts/线格式|线格式]] — protobuf的二进制编码格式
- [[concepts/变长整数|变长整数]] — 用于紧凑编码整数的关键技术
- [[concepts/标签-长度-值|标签-长度-值]] — protobuf线格式的基本编码单元
- [[concepts/字段基数|字段基数]] — 字段的出现次数规则（optional/repeated/map）
- [[concepts/字段存在性|字段存在性]] — proto3中字段是否存在追踪机制，3.12版本起通过实验性 optional 字段重新引入；proto2 与 proto3 在此概念上存在根本差异（proto2 为显式存在性，proto3 历史上为无存在性）
- [[concepts/显式存在性|显式存在性]] — proto2 历史上遵循的字段存在性纪律（来自 field_presence 源文档）
- [[concepts/无存在性|无存在性]] — proto3 历史上暴露的字段存在性纪律（来自 field_presence 源文档）
- [[concepts/保留字段|保留字段]] — 防止已废弃字段编号被重新使用的机制
- [[concepts/打包编码|打包编码]] — repeated字段的压缩编码方式
- [[concepts/features|Features]] — Editions体系下每个版本可独立配置的特性集合
- [[concepts/Edition Zero|Edition Zero]] — Editions项目定义的初始版本基线
- [[concepts/protobuf service|protobuf service]] — 在.proto文件中定义RPC服务接口的方式
- [[concepts/HTTP/h2服务|HTTP/h2服务]] — brpc中需通过.proto文件声明空请求和响应的HTTP服务类型
- [[concepts/Controller|Controller]] — brpc中的控制对象，用于HTTP请求处理
- [[concepts/Restful URL|Restful URL]] — brpc HTTP服务支持的URL模式
- [[concepts/editions/Protobuf Editions|Protobuf Editions]] — Protobuf的最新语法版本系统
- [[concepts/Message Type|Message Type]] — 由.proto文件定义的协议缓冲区消息结构类型
- [[concepts/Synthetic Oneof|Synthetic Oneof]] — 实现 proto3 optional 字段存在性追踪的关键代码生成技术
- [[concepts/proto2|proto2]] — proto3 之前的语法版本，历史上主要遵循显式存在性纪律

## Mentions in Source

> **Source: [[sources/en_http_service|en_http_service]]**
> - "http/h2 services in brpc have to declare interfaces with empty request and response in a .proto file."
> - "Add the service declaration in a proto file."
> - "option cc_generic_services = true;"
> - "Implement the service by inheriting the base class generated in .pb.h, which is same as protobuf services."

> **Source: [[sources/proto3|proto3]]**
> - "Covers how to use the proto3 revision of the Protocol Buffers language in your project."
> - "This guide describes how to use the protocol buffer language to structure your protocol buffer data, including .proto file syntax and how to generate data access classes from your .proto files."
> - "If no syntax is specified, the protocol buffer compiler will assume you are using proto2."

> **Source: [[sources/encoding|encoding]]**
> - (Existing mentions preserved)

> **Source: [[sources/style|style]]**
> - (Existing mentions preserved)

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "Protobuf is one of Google's oldest and most successful toolchain projects."
> - "The last radical change to Protobuf (syntax = "proto3";) split the ecosystem."

> **Source: [[sources/java-lite|java-lite]]**
> - "Protocol Buffers - Google's data interchange format"
> - "Copyright 2008 Google Inc."
> - "https://developers.google.com/protocol-buffers/"
> - "You can generate Java Lite code for your .proto files:"

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "Protobuf release 3.12 adds experimental support for `optional` fields in proto3."
> - "Presence tracking was added to proto3 in response to user feedback, both from inside Google and from open-source users."

> **Source: [[sources/field_presence|field_presence]]**
> - "Field presence is the notion of whether a protobuf field has a value."
> - "Historically, proto2 has mostly followed explicit presence, while proto3 exposes only no presence semantics."
> - "Protobufs can be represented in human-readable, textual forms."