---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-readme|Protobuf Editions 设计文档索引]]"]
tags: [standard]
aliases:
  - "Edition 命名规范"
  - "Edition Naming Rules"
---


# Edition Naming

## 定义
Edition Naming 是一份关于 Protobuf Editions 版本命名规则与约定的设计文档。它定义了 Edition 标识符的格式、版本号递增策略以及面向用户展示的命名方式，旨在确保 Editions 体系的可发现性与一致性。

## 关键特征
- **标识符格式规范**：定义 Edition 标识符的命名格式与构成规则
- **版本号递增策略**：规定 Edition 版本号如何递增与演进
- **面向用户展示的命名约定**：统一 Edition 在文档、工具链与用户界面中的呈现方式
- **与 Editions 体系协同**：作为 Protobuf Editions 历史设计文档的一部分，与其他 Editions 设计文档共同维护整体一致性

## 应用
- 为 Edition 标识符（如 `2023`、`2024` 等）的发布提供命名层面的规范依据
- 指导工具链、编译器与文档生成系统对 Edition 名称的识别与展示
- 与 [[concepts/minimum-required-edition|Minimum Required Edition]] 配合，明确消息可声明的最低 Edition 范围
- 与 [[concepts/edition-evolution|Edition Evolution]] 协同，规划 Edition 的长期演进路径
- 与 [[concepts/life-of-an-edition|Life of an Edition]] 一起，构成 Edition 生命周期管理的完整规范

## 相关概念
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/edition-evolution|Edition Evolution]]
- [[concepts/life-of-an-edition|Life of an Edition]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protobuf-editions|Protobuf Editions]]

## 来源提及
- "The following topics are in this repository:" — [[sources/editions-readme|Protobuf Editions 设计文档索引]]
- "[Edition Naming](edition-naming.md)" — [[sources/editions-readme|Protobuf Editions 设计文档索引]]
- "This directory contains historical design documents that describe plans for implementing Protobuf Editions." — [[sources/editions-readme|Protobuf Editions 设计文档索引]]