---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-protobuf-editions-design-features.md]]"
tags: [Features, Editions, Custom Options, Feature Inheritance, Target Attributes, Retention, Edition Defaults, InheritFrom, Language-Specific Features, FieldPresence, RepeatedFieldEncoding, MessageEncoding]
aliases: ["Protobuf Editions Features Design"]
---

# Protobuf Editions Design: Features - Summary

## 来源
- Original file: [[protobuf/editions-protobuf-editions-design-features.md]]
- Ingested: 2026-06-13

## 核心内容
本提案由 [[entities/haberman|haberman]] 与 [[entities/fowles|fowles]] 共同撰写，于 2022 年 10 月 13 日获得批准，是 [[entities/protobuf-editions|Protobuf Editions]] 项目的核心设计文档。文档提出使用 Protobuf 已有的 [[concepts/custom-options|自定义选项]]机制来定义和表示 [[concepts/features|特性]]（Features），从而避免引入新的语法形式。版本（Editions）形式上是一组特性的集合，每个特性都有默认值，只能通过引入新版本来更改。文档详细阐述了五大核心机制：通过 [[concepts/language-specific-features|extensions]] 管理语言特定特性；通过单一 Features 消息与 MergeFrom 行为实现 [[concepts/feature-inheritance|特性继承]]；通过 [[concepts/target-attributes|目标属性]]限制特性可附加的实体集合；通过 [[concepts/retention|保留规则]]减少描述符大小；以及通过二分搜索和合并算法构建 [[concepts/edition-defaults|版本特性默认值]]。文档最后给出了 Edition Zero 的潜在特性消息示例。

## 关键实体
- [[entities/haberman|haberman]] — 提案主要作者
- [[entities/fowles|fowles]] — 提案共同作者
- [[entities/protobuf-editions|Protobuf Editions]] — 所属项目

## 关键概念
- [[concepts/features|特性（Features）]] — 版本的基础组成单元
- [[concepts/editions|版本（Editions）]] — 特性集合的演进机制
- [[concepts/custom-options|自定义选项（Custom Options）]] — 特性定义的载体
- [[concepts/feature-inheritance|特性继承（Feature Inheritance）]] — MergeFrom 行为驱动的继承机制
- [[concepts/target-attributes|目标属性（Target Attributes）]] — 限制特性附加实体的元数据
- [[concepts/retention|保留（Retention）]] — 控制描述符运行时保留级别
- [[concepts/edition-defaults|版本默认值（Edition Defaults）]] — 二分搜索构建算法
- [[concepts/inheritfrom|InheritFrom]] — 实现特性继承的算法函数
- [[concepts/language-specific-features|语言特定特性（Language-Specific Features）]] — 通过 extensions 支持的各语言特性
- [[concepts/fieldpresence|FieldPresence]] — 字段存在性特性（EXPLICIT/IMPLICIT/LEGACY_REQUIRED）
- [[concepts/repeatedfieldencoding|RepeatedFieldEncoding]] — 重复字段编码特性（PACKED/EXPANDED）
- [[concepts/messageencoding|MessageEncoding]] — 消息编码特性（LENGTH_PREFIXED/DELIMITED）

## 要点
- Protobuf Editions 项目使用"版本"机制允许 Protobuf 安全演进，每个版本是带默认值的特性集合，特性集合或默认值只能在引入新版本时更改
- 本提案使用 [[concepts/custom-options|自定义选项]]而非字符串来定义和表示特性，避免引入新的语法形式
- 通过 [[concepts/feature-inheritance|特性继承]]的单一 Features 消息扩展所有选项类型，底层使用 MergeFrom 行为，使得自定义后端能轻松实现继承
- [[concepts/target-attributes|目标属性]]避免继承机制被过度使用，[[concepts/retention|保留规则]]减少 protobuf 运行时描述符大小
- [[concepts/edition-defaults|版本默认值]]通过二分搜索和合并算法构建，支持语言作用域特性通过 imports 自动发现
- Edition Zero 样例包含 [[concepts/fieldpresence|field_presence]]、[[concepts/repeatedfieldencoding|repeated_field_encoding]]、[[concepts/messageencoding|message_encoding]] 等特性，所有特性默认 retention = RUNTIME