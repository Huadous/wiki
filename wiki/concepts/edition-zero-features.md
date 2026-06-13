---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-readme|editions-readme]]"]
tags: [standard]
aliases:
  - "Edition Zero 特性集"
  - "Edition 0 Features"
  - "Edition 0 特性"
---


# Edition Zero Features

## 定义

Edition Zero Features（Edition Zero 特性集）是 Protobuf Editions 初始版本所包含的核心特性集合的规格说明文档，是整个 Editions 体系的起点和参考实现。Edition Zero 定义了 Protobuf 3 中可用特性在 Editions 框架下的重新组织与表达方式，为后续 Edition 的扩展奠定基础。该特性集覆盖消息字段处理、未知字段处理、JSON 映射等多个方面的设计决策，是理解 Editions 设计哲学与 proto3 差异的关键参考。

## 关键特征

- **Editions 体系的起点**：作为 Editions 框架的首个版本，定义了基础特性集与默认行为。
- **proto3 特性的重新表达**：将 Protobuf 3 中的可用特性在 Editions 框架下重新组织与映射。
- **覆盖消息字段处理**：包含字段存在性（field presence）、默认值等核心语义的设计决策。
- **未知字段处理规范**：明确了对未知字段（unknown fields）的处理策略。
- **JSON 映射规则**：定义了 Protobuf 消息到 JSON 表示的转换规则。
- **参考实现角色**：作为后续 Edition 扩展的基础参考点。

## 应用

- 作为理解 Protobuf Editions 体系演进的基础参考文档。
- 帮助开发者理解从 proto3 迁移到 Editions 时的语义变化。
- 为新增 Edition 提供特性集扩展的起点模板。
- 在工具链与代码生成器实现中，作为初始 Edition 的行为规范。

## 相关概念

- [[concepts/what-are-protobuf-editions|What are Protobuf Editions?]]
- [[concepts/protobuf-editions-design-features|Protobuf Editions Design: Features]]
- [[concepts/edition-zero-converged-semantics|Edition Zero: Converged Semantics]]
- [[concepts/edition-zero-json-handling|Edition Zero: JSON Handling]]

## 相关实体

- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及

- "[Edition Zero Features](edition-zero-features.md)" — [[sources/editions-readme|editions-readme]]
- "The following topics are in this repository:" — [[sources/editions-readme|editions-readme]]