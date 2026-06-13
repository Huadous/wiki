---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-readme|editions-readme]]"]
tags: [standard]
aliases:
  - "MRE"
  - "最低必需 Edition"
---


# Minimum Required Edition

## 定义
Minimum Required Edition（最低必需 Edition，简称 MRE）是 Protobuf Editions 中用于在 schema 文件中声明使用该 schema 所需最低 Edition 版本的关键机制。该机制允许 schema 生产者明确告知消费者所需的最低 Editions 版本，从而避免使用过于老旧或不安全的 Edition 特性。Minimum Required Edition 是 Editions 兼容性管理框架的重要组成部分，与 Edition 演进策略及 Edition Lifetimes 紧密相关，为生态系统的平滑升级提供制度保障。

## 关键特征
- **版本声明机制**：在 schema 文件中显式声明消费该 schema 所要求的最低 Edition 版本
- **生产者—消费者契约**：由 schema 生产者设定门槛，消费者需满足该最低 Edition 才能正确使用 schema
- **兼容性保障**：防止消费者使用过于陈旧或不安全的 Edition 特性解析新 schema
- **演进管理**：是 Protobuf Editions 兼容性管理框架的核心组成，与 Edition 演进策略协同
- **生命周期关联**：与 Edition Lifetimes 紧密耦合，为 Edition 的弃用与升级提供制度化支撑

## 应用
- **Schema 版本治理**：在 .proto 文件中通过 `minimum` 或对应选项指定最低 Edition，确保下游工具链、运行时及语言实现满足要求
- **生态系统升级路径规划**：在引入新 Edition 特性时，通过 MRE 提示依赖方升级至受支持的 Edition
- **避免旧 Edition 风险**：阻止旧版运行时因不识别新特性而产生兼容性错误或安全风险
- **跨组织协作**：为分布式团队与外部消费者提供清晰的 Edition 兼容基线

## 相关概念
- [[concepts/edition-lifetimes|Edition Lifetimes]]
- [[concepts/edition-evolution|Edition Evolution]]
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]
- [[concepts/protobuf-editions-for-schema-producers|Protobuf Editions for Schema Producers]]

## 相关实体
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- "The following topics are in this repository: — [[protobuf/editions-README|editions-README]]" — [[sources/editions-readme|editions-readme]]
- "[Minimum Required Edition](minimum-required-edition.md) — [[protobuf/editions-README|editions-README]]" — [[sources/editions-readme|editions-readme]]