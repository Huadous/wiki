---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-edition-evolution.md]]"
tags: [Protobuf Editions, Total Ordering of Editions, Protobuf Features, Build Horizon, Backend Features, Edition Evolution, FileDescriptorProto, Edition Naming, Edition Predicates]
aliases: ["editions-edition-evolution", "Edition Evolution 演进提案"]
---

# Edition Evolution - Summary

## 来源
- Original file: [[protobuf/editions-edition-evolution.md]]
- Ingested: 2026-06-13

## 核心内容
本文档由 [[entities/@mcy|@mcy]] 于 2022-07-06 批准，核心议题是 Protobuf Editions 机制的演进策略。文档基于 [[concepts/protobuf-editions|Protobuf Editions]] 这一通过为 .proto 文件添加 edition 字段来隐式或显式启用特性（features）的机制，重点回答两个问题：何时创建 edition？后端如何向 [[entities/protoc|protoc]] 告知其特性默认值？为此文档提出对 edition 字符串定义全序（详见 [[concepts/total-ordering-of-editions|Total Ordering of Editions]]），使得后端可通过 [[concepts/edition-predicates|Edition Predicates]]（如 `EditionIsLaterThan`、`EditionIsBetween`）判断默认值的生效范围。在特性分类上，[[concepts/protobuf-features|Protobuf Features]] 分为 proto: 前缀（由 protoc 前端固有实现）和 [[concepts/backend-features|Backend Features]]（由后端通过描述性 proto 提供默认值）。文档还讨论了"来自未来的 edition"引发的兼容性挑战，提出通过 [[concepts/build-horizon|Build Horizon]] 机制而非禁止新编码特性来解决。需要注意的是，文档中提出的全序方案在后续被 [[concepts/edition-naming|Edition Naming]] 文档部分取代。

## 关键实体
- [[entities/@mcy|@mcy]] — 文档作者，Protobuf Editions 演进提案的主要撰写人
- [[entities/protoc|protoc]] — Protocol Buffers 官方编译器，负责汇总前端与后端的特性信息并向用户展示完整特性集合

## 关键概念
- [[concepts/edition-evolution|Edition Evolution]] — 文档核心议题，描述 Editions 体系随时间发展和引入新特性的策略与规则
- [[concepts/protobuf-editions|Protobuf Editions]] — 通过 edition 字段平滑演进 .proto 文件的机制
- [[concepts/total-ordering-of-editions|Total Ordering of Editions]] — 对 edition 字符串定义全序关系，使后端可通过谓词判断特性生效范围
- [[concepts/protobuf-features|Protobuf Features]] — Editions 体系的基本配置单元，以 namespace:feature_name 命名
- [[concepts/backend-features|Backend Features]] — 由特定代码生成后端实现并定义默认值的特性
- [[concepts/edition-predicates|Edition Predicates]] — 用于查询版本关系的谓词方法集合（`EditionIsLaterThan`、`EditionIsBetween`）
- [[concepts/build-horizon|Build Horizon]] — 为解决"来自未来的 edition"兼容性挑战而提出的机制
- [[concepts/filedescriptorproto|FileDescriptorProto]] — 用于表示 .proto 文件描述符的消息类型，其 edition 字段设计为字符串类型
- [[concepts/edition-naming|Edition Naming]] — 后续替代全序方案的独立提案标准

## 要点
- Protobuf Editions 通过为 .proto 文件添加 edition 字段，以特性标志的形式平滑演进协议文件，避免了 proto2/proto3 式的硬性语法升级
- 文档提出对 edition 字符串定义全序关系（按 '.' 分割后先比长度再比字典序），使后端可通过 EditionIsLaterThan、EditionIsBetween 等谓词判断特性默认值的生效范围
- proto: 前缀特性由 protoc 前端固有实现，backend: 前缀特性则由对应后端通过提供描述性 proto（包含 defaults 列表和谓词）来告知 protoc
- 文档讨论了"来自未来的 edition"引发的兼容性问题：当旧服务解析新版编码消息时可能失败，提出通过 build horizon 机制而非禁止引入新编码特性来解决
- 文档明确指出该全序方案在后续被 Edition Naming 文档部分取代，属于演进过程中的过渡性提案