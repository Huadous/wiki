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
  - "[[protobuf/editions-edition-zero-features.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
  - "[[protobuf/editions-cpp-apis-for-edition-zero.md]]"
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
Protocol Buffers（通常缩写为 protobuf）是一种跨语言、跨平台的可扩展结构化数据序列化机制，由 Google 于 2008 年发布（文档源自其官方开发者页面 https://developers.google.com/protocol-buffers/），广泛用于通信协议、数据存储和微服务等场景；它更小、更快、更简单，类似于 JSON 或 XML。它通过 `.proto` 文件定义结构化数据，并借助 `protoc` 编译器为包括 Java、C++、Python、Go 等多种语言生成对应的数据访问类；Protobuf 不仅是一种序列化格式，更是一个完整的生态系统，包含编译器 `protoc` 和多种数据表示格式（如 TextFormat、JSON）。Protobuf 是开源项目 [[entities/protocolbuffersprotobuf|protobuf/protobuf]] 的核心组成部分，长期以来包含 `proto2` 和 `proto3` 两个主要语法版本，而 Editions 是其下一代演进方案。Protobuf 有多个语法/版本——`proto2`、`proto3`，以及较新的 `Edition 2023`、`Edition 2024`——其中 Editions 体系是 Protocol Buffers 较新的演进方向，通过显式的 feature 设置取代旧版语法的隐式行为；二者在字段存在性（field presence）的处理上存在重要差异：`proto2` 历史上主要遵循显式存在性（explicit presence），而 `proto3` 仅暴露无存在性（no presence）语义。Protobuf 是 Google 最古老、最成功的工具链项目之一，其最后的一次重大语法变革（`proto3`）曾使整个生态系统产生分裂，而继 `proto3` 之后的 `editions` 版本系统则引入了按版本配置特性的新机制，配套工具包括 Prototiller 等；Editions 项目的目录下收录了约 20 份围绕其特性设计与演进展开的历史设计文档，并引导读者参阅官方 [Protobuf Editions Overview](https://protobuf.dev/editions/overview/) 获取最新概览。在 3.12 版本中，Protobuf 引入了实验性的 proto3 `optional` 字段支持，该特性用以解决 wrapper 类型在可用性与效率上的不足，并要求包括 Google 官方和第三方在内的所有代码生成器进行相应更新；此功能的加入源自 Google 内部与开源社区的共同反馈。Editions 版本的官方语言指南与 proto3 指南在结构上保持一致，均描述如何使用 protocol buffer 语言组织协议缓冲区数据，包括 `.proto` 文件语法以及如何从中生成数据访问类。在 Java 平台上，Protobuf 还提供了 Java Lite 运行时，专门为 Android 等资源受限场景做了体积和性能优化，可通过 `LITE_RUNTIME` 优化选项生成精简代码，并依赖 R8 进行进一步缩减。Editions 设计文档还涉及与旧版 proto2 group 机制的兼容性问题：Joshua Humphries 在 [[sources/editions-group-migration-issues|editions-group-migration-issues]] 中报告了他在实验性使用 Edition 2023 时发现的一系列 well-timed issues，文档围绕 Edition 2023 引入的 DELIMITED 编码特性以及与旧版 group 字段的迁移冲突展开讨论，并提出多种替代方案的组合，相关讨论还涉及开源仓库中的 issue 16239 及对应的 conformance tests。在 Editions Zero 的设计目标中，一个明确的初衷是：通过恰当应用 features，任意 proto2/proto3 文件都可以无变更语义地转换为 editions；该方案试图以特性标志的方式统一包括 required/optional 字段、枚举开闭性、UTF-8 验证、extensions 支持以及 groups 语法在内的多种历史行为差异，同时保持向后兼容性，但在跨语言一致性方面仍存在现实差距，例如部分语言（如 Go）对 `syntax=proto2` 的 closed enum 语义尚未完整实现。Protobuf 拥有包括 C++、Java、UPB、Ruby、C#、Obj-C、Swift、Go、JSPB、ImmutableJs 和 JsProto 在内的多种语言实现，这些语言实现对枚举开放/封闭性（Enum Field Closedness）的处理方式存在显著差异；[[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]] 文档专门讨论了在 C++ 与 Java 等语言中"由使用该枚举的字段所在文件决定封闭性"的现状，并将其纳入 Edition Zero 试图通过 features 机制统一的语义差异范围。在 C++ 侧，[[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]] 提案直接修改 protobuf C++ 描述符模块的 API，核心涉及 `FileDescriptor`、`FieldDescriptor`、`EnumDescriptor` 三类，并集中改动了 `descriptor.h` 头文件；该提案建议为所有 proto 类型无条件生成 `unknown_fields()` 与 `mutable_unknown_fields()` 方法；根据内部 *FileDescriptor::syntaxAudit Report*（未对外公开）的记录，Google 内部代码库对 `FileDescriptor::syntax()` 存在大量使用，Edition Zero 的演进将破坏这些使用点，因此需要在 API 层面规划平滑的迁移路径。

## Related Entities
- [[entities/brpc|brpc]] — 深度依赖Protobuf的RPC框架，利用protobuf定义所有服务接口
- [[entities/google|Google]] — Protobuf的创始者和主要维护者；其内部代码库存在大量 `FileDescriptor::syntax()` 使用，是 editions-cpp-apis-for-edition-zero 提案中 `syntax()` 弃用迁移的背景
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
- [[entities/protoscope|Protoscope]] — Editions 体系相关工具（在 editions-edition-zero-feature-enum-field-closedness 源中提及）
- [[entities/mcy|mcy]] — editions-edition-zero-feature-enum-field-closedness 相关人员；亦是 editions-cpp-apis-for-edition-zero 提案相关人员

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
- [[concepts/Edition Zero|Edition Zero]] — Editions项目定义的初始版本基线，目标是使现有 proto2/proto3 文件可通过 features 无变更语义地迁移至 editions；其 C++ 实现需要在描述符层面对 API 进行演进
- [[concepts/protobuf service|protobuf service]] — 在.proto文件中定义RPC服务接口的方式
- [[concepts/HTTP/h2服务|HTTP/h2服务]] — brpc中需通过.proto文件声明空请求和响应的HTTP服务类型
- [[concepts/Controller|Controller]] — brpc中的控制对象，用于HTTP请求处理
- [[concepts/Restful URL|Restful URL]] — brpc HTTP服务支持的URL模式
- [[concepts/editions/Protobuf Editions|Protobuf Editions]] — Protobuf的最新语法版本系统
- [[concepts/Message Type|Message Type]] — 由.proto文件定义的协议缓冲区消息结构类型
- [[concepts/Synthetic Oneof|Synthetic Oneof]] — 实现 proto3 optional 字段存在性追踪的关键代码生成技术
- [[concepts/proto2|proto2]] — proto3 之前的语法版本，历史上主要遵循显式存在性纪律
- [[concepts/What are Protobuf Editions?|What are Protobuf Editions?]] — 对 Protobuf Editions 特性的概览介绍主题（来自 editions-readme 源文档）
- [[concepts/Edition Zero Features|Edition Zero Features]] — Editions 项目中关于 Edition Zero 特性集合的主题（来自 editions-readme 源文档）；其设计目标涵盖 required/optional 字段、枚举开闭性（features.enum = {CLOSED, OPEN}）、UTF-8 验证、extensions 支持以及 groups 语法等历史行为差异的统一
- [[concepts/Life of an Edition|Life of an Edition]] — Editions 项目中关于一个 Edition 生命周期的主题（来自 editions-readme 源文档）
- [[concepts/Edition Evolution|Edition Evolution]] — Editions 项目中关于 Edition 演进机制的主题（来自 editions-readme 源文档）
- [[concepts/Delimited encoding|Delimited encoding]] — Edition 2023 中引入的编码特性，与旧版 proto2 group 机制的迁移冲突相关
- [[concepts/Group fields|Group fields]] — proto2 历史遗留的字段分组机制，Edition 2023 的 DELIMITED 编码与之存在兼容性问题
- [[concepts/Codegen|Codegen]] — Editions 迁移问题中涉及的关键代码生成环节
- [[concepts/Text format|Text format]] — protobuf 的人类可读文本表示规范，editions-group-migration-issues 文档的讨论范围之一
- [[concepts/Enum Field Closedness|Enum Field Closedness]] — Editions 体系中关于枚举开放/封闭性的特性主题（来自 editions-edition-zero-feature-enum-field-closedness 源文档）；C++、Java 等语言实现的封闭性由使用该枚举的字段所在文件决定
- [[concepts/Open Enum|Open Enum]] — 枚举字段开放性相关概念（来自 editions-edition-zero-feature-enum-field-closedness 源文档）
- [[concepts/FileDescriptor|FileDescriptor]] — protobuf 描述符（descriptor）模块的核心类之一，是 editions-cpp-apis-for-edition-zero 提案重点改动的对象
- [[concepts/FieldDescriptor|FieldDescriptor]] — protobuf 描述符模块的核心类之一，承载字段元信息（如 `has_zero_default_value`、`enforces_utf8` 等）
- [[concepts/EnumDescriptor|EnumDescriptor]] — protobuf 描述符模块的核心类之一，提供 `is_closed` 等枚举相关 API
- [[concepts/syntax() deprecation migration|syntax() deprecation migration]] — editions-cpp-apis-for-edition-zero 提案中针对 `FileDescriptor::syntax()` 的弃用迁移议题（来自 editions-cpp-apis-for-edition-zero 源文档）
- [[concepts/FieldDescriptor::has_zero_default_value|FieldDescriptor::has_zero_default_value]] — editions-cpp-apis-for-edition-zero 提案涉及的 C++ 描述符字段 API 之一
- [[concepts/FieldDescriptor::enforces_utf8|FieldDescriptor::enforces_utf8]] — editions-cpp-apis-for-edition-zero 提案涉及的 C++ 描述符字段 API 之一
- [[concepts/EnumDescriptor::is_closed|EnumDescriptor::is_closed]] — editions-cpp-apis-for-edition-zero 提案涉及的 C++ 描述符枚举 API 之一
- [[concepts/FileDescriptor::CopyHeadingTo|FileDescriptor::CopyHeadingTo]] — editions-cpp-apis-for-edition-zero 提案涉及的 C++ 描述符文件级 API 之一

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

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "it is an explicit goal that it be possible to take an arbitrary proto2/proto3 file and convert it to editions without semantic changes, via appropriate application of features." (一个明确的目标是：通过对 features 的恰当应用，可以将任意 proto2/proto3 文件无变更语义地转换为 editions。)
> - "For example, in this document we define a feature `features.enum = {CLOSED,OPEN}`. But currently Go does not implement closed enum semantics for `syntax=proto2` as it should." (例如，文档中定义了 `features.enum = {CLOSED,OPEN}` 特性，但 Go 目前并未像应当的那样为 `syntax=proto2` 实现 closed enum 语义。)

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "C++: Determined by the field using the enum's file"
> - "Java: Determined by the field using the enum's file"

> **Source: [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]**
> - "This proposal adds the following code to `descriptor.h:`"
> - "As recorded in *FileDescriptor::syntaxAudit Report* (not available externally), there are significant uses of `FileDescriptor::syntax()` in internal Google repositories that Edition Zero will break"