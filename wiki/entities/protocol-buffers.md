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
  - "[[protobuf/features.md]]"
  - "[[protobuf/editions.md]]"
  - "[[protobuf/editions-README.md]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
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
Protocol Buffers（通常缩写为 protobuf）是一种跨语言、跨平台的可扩展结构化数据序列化机制，由 Google 于 2008 年发布（文档源自其官方开发者页面 https://developers.google.com/protocol-buffers/），广泛用于通信协议、数据存储和微服务等场景；它更小、更快、更简单，类似于 JSON 或 XML。它通过 `.proto` 文件定义结构化数据，并借助 `protoc` 编译器为包括 Java、C++、Python、Go 等多种语言生成对应的数据访问类；Protobuf 不仅是一种序列化格式，更是一个完整的生态系统，包含编译器 `protoc` 和多种数据表示格式（如 TextFormat、JSON）。Protobuf 是开源项目 [[entities/protocolbuffersprotobuf|protobuf/protobuf]] 的核心组成部分，长期以来包含 `proto2` 和 `proto3` 两个主要语法版本，而 Editions 是其下一代演进方案。Protobuf 有多个语法/版本——`proto2`、`proto3`，以及较新的 `Edition 2023`、`Edition 2024`——其中 Editions 体系是 Protocol Buffers 较新的演进方向，通过显式的 feature 设置取代旧版语法的隐式行为；二者在字段存在性（field presence）的处理上存在重要差异：`proto2` 历史上主要遵循显式存在性（explicit presence），而 `proto3` 仅暴露无存在性（no presence）语义。Protobuf 是 Google 最古老、最成功的工具链项目之一，其最后的一次重大语法变革（`proto3`）曾使整个生态系统产生分裂，而继 `proto3` 之后的 `editions` 版本系统则引入了按版本配置特性的新机制，配套工具包括 Prototiller 等；Editions 项目的目录下收录了约 20 份围绕其特性设计与演进展开的历史设计文档，并引导读者参阅官方 [Protobuf Editions Overview](https://protobuf.dev/editions/overview/) 获取最新概览。在 3.12 版本中，Protobuf 引入了实验性的 proto3 `optional` 字段支持，该特性用以解决 wrapper 类型在可用性与效率上的不足，并要求包括 Google 官方和第三方在内的所有代码生成器进行相应更新；此功能的加入源自 Google 内部与开源社区的共同反馈。Editions 版本的官方语言指南与 proto3 指南在结构上保持一致，均描述如何使用 protocol buffer 语言组织协议缓冲区数据，包括 `.proto` 文件语法以及如何从中生成数据访问类。在 Java 平台上，Protobuf 还提供了 Java Lite 运行时，专门为 Android 等资源受限场景做了体积和性能优化，可通过 `LITE_RUNTIME` 优化选项生成精简代码，并依赖 R8 进行进一步缩减。Editions 设计文档还涉及与旧版 proto2 group 机制的兼容性问题：Joshua Humphries 在 [[sources/editions-group-migration-issues|editions-group-migration-issues]] 中报告了他在实验性使用 Edition 2023 时发现的一系列 well-timed issues，文档围绕 Edition 2023 引入的 DELIMITED 编码特性以及与旧版 group 字段的迁移冲突展开讨论，并提出多种替代方案的组合，相关讨论还涉及开源仓库中的 issue 16239 及对应的 conformance tests。

## Related Entities
- [[entities/brpc|brpc]] — 深度依赖Protobuf的RPC框架，利用protobuf定义所有服务接口
- [[entities/google|Google]] — Protobuf的创始者和主要维护者
- [[entities/open-source-oss-community|open-source-oss-community]] — Protobuf的开源社区维护力量，同时为 proto3 optional 字段支持提供了关键反馈
- [[entities/protoc|protoc]] — Protobuf的编译器，负责从.proto文件生成多语言数据访问类，也是 protobuf 生态系统的核心组件
- [[entities/protocolbuffersprotobuf|protocolbuffersprotobuf]] — Protobuf项目实体页面（开源仓库 protobuf/protobuf 的核心组成部分）
- [[entities/textformat|TextFormat]] — protobuf 生态中的人类可读文本表示格式（来自 field_presence 源文档）
- [[entities/fieldmask|FieldMask]] — protobuf 生态中的字段掩码工具类型（来自 field_presence 源文档）
- [[entities/protocol-buffers-v3-12-0|Protocol Buffers v3.12.0]] — 引入实验性 proto3 `optional` 字段支持的版本
- [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]] — protobuf 的后续发布版本实体
- [[entities/prototiller|Prototiller]] — Editions 体系配套的工具（来自 features 源文档）
- [[entities/edition-2024|Edition 2024]] — Protocol Buffers 的较新语法版本之一（来自 features、editions 源文档）
- [[entities/edition-2023|Edition 2023]] — Protocol Buffers 的较新语法版本之一（来自 features、editions 源文档，也是 editions-group-migration-issues 文档中引入 DELIMITED 编码特性的早期实验版本）
- [[entities/editions-readme|editions-readme]] — Protobuf Editions 历史设计文档索引目录的 README 源文件
- [[entities/joshua-humphries|Joshua Humphries]] — 在 editions-group-migration-issues 中报告 Edition 2023 group 迁移相关问题的人员
- [[entities/mkruskal-google|mkruskal-google]] — editions-group-migration-issues 相关人员

## Related Concepts
- [[concepts/序列化|序列化]] — protobuf的核心能力，将结构化数据转换为线格式
- [[concepts/编码规范|编码规范]] — .proto文件的命名和格式约定
- [[concepts/RPC|RPC]] — protobuf最常见的应用场景
- [[concepts/proto3|proto3]] — 当前主流的protobuf语法版本，brpc 1.8.0后强制要求，其引入曾分裂生态
- [[concepts/editions|editions]] — 继proto3之后的新一代语法版本系统，包含 2023 和 2024 两个发布版本
- [[concepts/字段|字段]] — 消息中的基本数据单元
- [[concepts/字段编号|字段编号]] — 每个字段在二进制编码中的唯一标识号
- [[concepts/线格式|线格式]] — protobuf的二进制编码格式
- [[concepts/变长整数|变长整数]] — 用于紧凑编码整数的关键技术
- [[concepts/标签-长度-值|标签-长度-值]] — protobuf线格式的基本编码单元
- [[concepts/字段基数|字段基数]] — 字段的出现次数规则（optional/repeated/map）
- [[concepts/字段存在性|字段存在性]] — proto3中字段是否存在追踪机制，3.12版本起通过实验性 optional 字段重新引入；proto2 与 proto3 在此概念上存在根本差异（proto2 为显式存在性，proto3 历史上为无存在性）
- [[concepts/显式存在性|显式存在性]] — proto2 历史上遵循的字段存在性纪律（来自 field_presence 源文档）
- [[concepts/无存在性|无存在性]] — proto3 历史上暴露的字段存在性纪律（来自 field_presence 源文档）
- [[concepts/保留字段|保留字段]] —防止已废弃字段编号被重新使用的机制
- [[concepts/打包编码|打包编码]] — repeated字段的压缩编码方式
- [[concepts/features|Features]] — Editions体系下每个版本可独立配置的特性集合，包括 features.default_symbol_visibility、features.enforce_naming_style、features.enum_type、features.field_presence 等具体特性
- [[concepts/Edition Zero|Edition Zero]] — Editions项目定义的初始版本基线
- [[concepts/protobuf service|protobuf service]] — 在.proto文件中定义RPC服务接口的方式
- [[concepts/HTTP/h2服务|HTTP/h2服务]] — brpc中需通过.proto文件声明空请求和响应的HTTP服务类型
- [[concepts/Controller|Controller]] — brpc中的控制对象，用于HTTP请求处理
- [[concepts/Restful URL|Restful URL]] — brpc HTTP服务支持的URL模式
- [[concepts/editions/Protobuf Editions|Protobuf Editions]] — Protobuf的最新语法版本系统
- [[concepts/Message Type|Message Type]] — 由.proto文件定义的协议缓冲区消息结构类型
- [[concepts/Synthetic Oneof|Synthetic Oneof]] — 实现 proto3 optional 字段存在性追踪的关键代码生成技术
- [[concepts/proto2|proto2]] — proto3 之前的语法版本，历史上主要遵循显式存在性纪律
- [[concepts/What are Protobuf Editions?|What are Protobuf Editions?]] — 对 Protobuf Editions 特性的概览介绍主题（来自 editions-readme 源文档）
- [[concepts/Edition Zero Features|Edition Zero Features]] — Editions 项目中关于 Edition Zero 特性集合的主题（来自 editions-readme 源文档）
- [[concepts/Life of an Edition|Life of an Edition]] — Editions 项目中关于一个 Edition 生命周期的主题（来自 editions-readme 源文档）
- [[concepts/Edition Evolution|Edition Evolution]] — Editions 项目中关于 Edition 演进机制的主题（来自 editions-readme 源文档）
- [[concepts/Delimited encoding|Delimited encoding]] — Edition 2023 中引入的编码特性，与旧版 proto2 group 机制的迁移冲突相关
- [[concepts/Group fields|Group fields]] — proto2 历史遗留的字段分组机制，Edition 2023 的 DELIMITED 编码与之存在兼容性问题
- [[concepts/Codegen|Codegen]] — Editions 迁移问题中涉及的关键代码生成环节
- [[concepts/Text format|Text format]] — protobuf 的人类可读文本表示规范，editions-group-migration-issues 文档的讨论范围之一

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

> **Source: [[sources/features|features]]**
> - "Feature Settings for Editions | Protocol Buffers Documentation"
> - "Protobuf Editions features and how they affect protobuf behavior."
> - "View page source"
> - "Edit this page"

> **Source: [[sources/editions|editions]]**
> - "Covers how to use the editions revisions of the Protocol Buffers language in your project."
> - "This guide describes how to use the protocol buffer language to structure your protocol buffer data, including .proto file syntax and how to generate data access classes from your .proto files."

> **Source: [[sources/editions-readme|editions-readme]]**
> - "This directory contains historical design documents that describe plans for implementing Protobuf Editions."
> - "For an up-to-date overview of this feature of Protocol Buffers, see [Protobuf Editions Overview](https://protobuf.dev/editions/overview/)."

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "Joshua Humphries reported some well-timed issues discovered while experimenting with our early release of Edition 2023."
> - "We propose a combination of the alternatives listed below."