---
type: source
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/proto3]]"
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
  - "Protobuf Editions Language Guide"
  - "Protocol Buffers Editions Reference"
---

## 来源
- 原始文件：[[protobuf/editions.md]]
- 引入时间：2026-06-12
- 补充来源：proto3 文件

## 核心内容
本文档是 Protocol Buffers 语言的官方指南，专注于 editions（2023 和 2024 版本）。它详细说明了如何使用 `.proto` 文件定义消息类型，包括指定字段类型、字段编号、字段基数（singular、repeated、map）。指南强调字段编号不可重用、删除时必须保留的重要性，以避免线协议格式歧义。还介绍了 [[concepts/field_presence-feature|field_presence 特性]]、[[concepts/packed-encoding|打包编码]]以及 [[concepts/scalar-types|标量类型]]。此外，文档涵盖了多种编程语言（C++、Java、Kotlin、Python、Go、Ruby、Objective-C、C#、PHP、Dart）的代码生成过程。本指南是开发人员使用 protobuf editions 的重要参考资料。

Editions 是 Protocol Buffers 的新语法修订机制，旨在统一并取代 proto2 和 proto3 的分离版本。与固定版本的语法不同，editions 允许开发者通过声明式配置（如字段特征）来灵活控制编译行为。该指南指出，对于 editions 语法的详细信息请参考《Protobuf Editions Language Guide》。Editions 代表了 protobuf 未来的演进方向，提供了更大的灵活性和向后兼容性。

## 关键实体
- [[entities/protocol-buffers|Protocol Buffers]] — Google 开发的高效结构化数据序列化协议，支持跨语言数据交换
- [[entities/protoc|protoc]] — Protocol Buffers 命令行编译器，将 `.proto` 文件编译为目标语言源代码

## 关键概念
- [[concepts/edition|Edition]] — protobuf 语言版本标识系统，edition 2023 和 2024 取代了 proto2/proto3
- [[concepts/field-number|字段编号]] — 每个字段的唯一数字标识，范围 1 到 536,870,911，不可重用
- [[concepts/field-cardinality|字段基数]] — 定义字段出现次数：singular、repeated、map
- [[concepts/packed-encoding|打包编码]] — 重复标量数值字段的紧凑序列化方式，editions 中默认启用
- [[concepts/well-formed-messages|Well-formed 消息]] — 序列化/反序列化后字节结构正确的 protobuf 消息
- [[concepts/reserved-field|Reserved 字段]] — 防止删除字段的编号和名称被未来重用
- [[concepts/wire-format|Wire 格式]] — protobuf 二进制序列化格式，使用 varint 和固定宽度编码混合
- [[concepts/enumeration|枚举]] — 命名整数常量的数据类型
- [[concepts/message-type|消息类型]] — protobuf 核心数据结构，用于定义结构化数据格式
- [[concepts/map|Map]] — 键值对集合的特殊字段类型
- [[concepts/extension-declaration|扩展声明]] — 预留扩展字段编号的语法机制
- [[concepts/last-one-wins|Last One Wins]] — 同一字段出现多次时，解析器只保留最后一个值的规则
- [[concepts/dependency-bloat|依赖膨胀]] — 单个 `.proto` 文件中定义过多消息类型导致的编译问题
- [[concepts/proto2|proto2]] — protobuf 早期语法版本，被 editions 取代
- [[concepts/proto3|proto3]] — protobuf 早期语法版本，被 editions 取代
- [[concepts/field|字段]] — 消息类型中的基本数据单元

## 要点
- Editions（2023/2024）是当前 protobuf 语言版本，取代了之前的 proto2/proto3 语法
- Editions 通过声明式配置（如字段特征）统一并取代了 proto2 和 proto3 的分离版本
- 如果未指定 edition 或 syntax，protocol buffer 编译器默认假设使用 proto2
- 字段编号必须在 1 到 536,870,911 之间且唯一，修改字段编号等同于删除并重建字段
- 低字段编号（1-15）编码占用更少空间（1 字节），应优先用于高频字段
- 重用字段编号会导致线协议歧义、数据损坏甚至泄露敏感信息
- 删除字段时必须使用 reserved 关键字保留其编号和名称，防止未来误用
- 字段基数支持 singular（默认）、repeated（打包编码默认开启）和 map 类型
- Field_presence 特性控制 singular 字段的显式/隐式存在跟踪
- protoc 编译器为多种语言（C++、Java、Python、Go 等）生成数据访问类
- 标量类型包括 int32、int64、uint32、uint64、sint32、sint64、fixed32、fixed64、sfixed32、sfixed64、float、double、bool、string、bytes
- 打包编码优化了重复标量数值字段的空间效率