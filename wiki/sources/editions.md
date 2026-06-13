---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/editions-protobuf-editions-design-features.md]]"
  - "[[protobuf/editions-java-lite-for-editions.md]]"
tags:
  - "edition"
  - "field number"
  - "field cardinality"
  - "packed encoding"
  - "field_presence feature"
  - "well-formed messages"
  - "reserved field"
  - "scalar types"
  - "wire format"
  - "Enumeration"
  - "Message type"
  - "Map"
  - "Extension Declaration"
  - "Last One Wins"
  - "Dependency Bloat"
aliases:
  - "Protocol Buffers Editions 语言指南"
  - "protobuf editions 文档"
---

## 补充来源
- Original file: editions-protobuf-editions-design-features
- Ingested: 2026-06-13
- 补充说明：未提供与本页直接相关的新信息

- Original file: editions-java-lite-for-editions
- Ingested: 2026-06-13
- 补充说明：未提供与本页直接相关的新信息

## 核心内容
本文档是 [[entities/protocol-buffers|Protocol Buffers]] 官方语言指南的 editions 版本，专门介绍 [[entities/edition-2023|edition 2023]] 与 [[entities/edition-2024|edition 2024]] 的使用方法。文档详细描述了 [[concepts/proto-file|.proto 文件]]的语法结构、消息类型（[[concepts/message-type|Message Type]]）的定义方式、字段编号（[[concepts/field-number|Field Number]]）的分配规则（1 至 536,870,911，19000–19999 为实现保留）以及字段基数（[[concepts/field-cardinality|Field Cardinality]]）的三种形式：[[concepts/singular-field|Singular]]、[[concepts/repeated-field|Repeated]] 和 [[concepts/map-field|Map]]。文档还说明了从 [[entities/proto2|proto2]] / [[entities/proto3|proto3]] 迁移到 editions 时的 [[concepts/field-presence|Field Presence]] 行为差异（LEGACY_REQUIRED 与 IMPLICIT），以及 [[entities/protoc|protoc 编译器]]为 C++、Java、Kotlin、Python、Go 等多种语言生成数据访问类的方式。指南中以 [[entities/searchrequest|SearchRequest]] 和 [[entities/searchresponse|SearchResponse]] 作为典型示例贯穿始终。

## 关键实体
- [[entities/protocol-buffers|Protocol Buffers]]：跨语言、跨平台的数据序列化框架
- [[entities/protoc|protoc]]：Protocol Buffers 官方编译器
- [[entities/edition-2023|edition 2023]]：Protocol Buffers 语言规范的版本之一
- [[entities/edition-2024|edition 2024]]：Protocol Buffers 语言规范的最新版本之一
- [[entities/proto2|proto2]]：Protocol Buffers 早期语言版本
- [[entities/proto3|proto3]]：Protocol Buffers 另一主要语言版本
- [[entities/searchrequest|SearchRequest]]：文档中演示 .proto 语法的示例消息类型
- [[entities/searchresponse|SearchResponse]]：与 SearchRequest 配对的示例响应消息类型

## 关键概念
- [[concepts/message-type|Message Type]]：由命名字段组成的数据结构基本单位
- [[concepts/field-number|Field Number]]：字段在 wire format 中的唯一标识符
- [[concepts/field-cardinality|Field Cardinality]]：字段出现次数与方式（singular/repeated/map）
- [[concepts/scalar-value-type|Scalar Value Type]]：double、float、int32、string 等基础类型
- [[concepts/wire-format|Wire Format]]：二进制编码格式，字段号使用 29 位表示
- [[concepts/packed-encoding|Packed Encoding]]：editions 中 repeated 标量字段的默认编码方式
- [[concepts/reserved-field|Reserved Field]]：通过 reserved 关键字防止字段号和字段名被误用
- [[concepts/field-presence|Field Presence]]：控制字段是否跟踪显式设置的 feature
- [[concepts/well-formed-message|Well-formed Message]]：符合 protobuf 规范的序列化/反序列化字节
- [[concepts/singular-field|Singular Field]]：无显式 cardinality 标签的字段
- [[concepts/repeated-field|Repeated Field]]：可出现零次或多次的字段
- [[concepts/map-field|Map Field]]：配对的 key/value 字段类型
- [[concepts/proto-file|.proto file]]：Protocol Buffers 的源文件格式
- [[concepts/enum|Enum]]：限制字段值为预定义命名常量的类型
- [[concepts/extension-declarations|Extension Declarations]]：为扩展字段保留编号的机制
- [[concepts/builder|Builder]]：protoc 为 Java 生成的辅助构建器类
- [[concepts/last-one-wins|Last One Wins]]：singular 字段在 wire-format 中多次出现时的解析行为
- [[concepts/textformat|TextFormat]]：基于文本的编码格式，字段名会被序列化
- [[concepts/comment|Comment]]：.proto 文件中的注释语法

## 要点
- [[entities/protocol-buffers|Protocol Buffers]] 的 editions 语言指南涵盖 [[entities/edition-2023|edition 2023]] 和 [[entities/edition-2024|edition 2024]] 两个版本
- [[concepts/proto-file|.proto 文件]]必须以 edition 声明作为第一个非空、非注释行，未声明时 [[entities/protoc|protoc]] 默认使用 [[entities/proto2|proto2]]
- 字段必须分配 1 到 536,870,911 之间的唯一编号，19000–19999 为实现保留，较低数字在 [[concepts/wire-format|Wire Format]] 中占用更少空间
- 字段基数支持 [[concepts/singular-field|singular]]、[[concepts/repeated-field|repeated]] 和 [[concepts/map-field|map]] 三种形式
- editions 中 [[concepts/repeated-field|repeated 字段]]的标量数值类型默认使用 [[concepts/packed-encoding|packed encoding]] 以节省空间
- 删除字段时必须同时保留 [[concepts/field-number|字段号]]和字段名，以避免字段号重用引发的数据损坏和 [[concepts/textformat|TextFormat]]/JSON 解析失败
- 从 [[entities/proto2|proto2]]/[[entities/proto3|proto3]] 迁移到 editions 时，[[concepts/field-presence|field_presence feature]] 分别被设置为 LEGACY_REQUIRED 和 IMPLICIT
- [[entities/protoc|protoc 编译器]]为 C++、Java、Kotlin、Python、Go、Ruby、Objective-C、C#、PHP、Dart 等语言生成对应的数据访问类，其中 Java 还包含 [[concepts/builder|Builder]] 类
- 字段号在 [[concepts/wire-format|Wire Format]] 中使用 29 位表示，另外 3 位用于指定字段的 wire 格式
- 单个 [[concepts/singular-field|singular 字段]]在 wire-format 字节中多次出现时，遵循 [[concepts/last-one-wins|Last One Wins]] 语义，只有最后一次出现的值会被访问到