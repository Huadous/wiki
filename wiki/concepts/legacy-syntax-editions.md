---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-readme]]"]
tags: [term]
aliases:
  - "遗留语法 Edition"
  - "Legacy Syntax Editions"
---


# Legacy Syntax Editions

## 定义
Legacy Syntax Editions（遗留语法 Edition）是 Protobuf Editions 设计文档体系中关于将 proto2、proto3 等遗留语法纳入 Editions 框架的设计文档。该机制允许现有的 proto2/proto3 schema 能够被映射或迁移到 Editions 体系中，从而保护既有生态投资并提供平稳的升级路径。它是 Editions 体系保持向后兼容性和促进生态演化的关键设计，与 Edition Lifetimes、Minimum Required Edition 等机制共同保障迁移过程的可行性。

## 关键特征
- 属于 Protobuf Editions 设计文档体系下的子主题之一，位于 [[sources/editions-readme]] 所列出的文档目录中
- 关注 proto2、proto3 等遗留语法与 Editions 框架之间的映射/迁移关系
- 强调向后兼容性，确保已有 schema 在升级至 Editions 时不会立即失效
- 与 Edition Lifetimes、Minimum Required Edition 等机制协同，共同保障生态演化的可行性
- 与 Edition Evolution 和 [[concepts/editions-group-migration-issues|Editions: Group Migration Issues]] 等议题紧密相关

## 应用
- 为已有的 proto2/proto3 文件提供向 Editions 体系迁移的指导与规范
- 帮助工具链（如编译器、运行时）正确识别和转换遗留语法的语义
- 在不破坏现有 API 与数据兼容性的前提下，允许用户逐步采用 Editions 特性
- 作为 Protobuf 语言演化的桥梁机制，使新特性的引入与遗留语法的退出可以平滑过渡

## 相关概念
- [[concepts/edition-lifetimes|Edition Lifetimes]]
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/editions-group-migration-issues|Editions: Group Migration Issues]]
- [[concepts/edition-evolution|Edition Evolution]]

## 相关实体
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- "The following topics are in this repository:" — [[sources/editions-readme]]
- "[Legacy Syntax Editions](legacy-syntax-editions.md)" — [[sources/editions-readme]]