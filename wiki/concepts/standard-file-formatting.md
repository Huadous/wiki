---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/style]]"]
tags: [method]
aliases:
  - "文件格式化规则"
  - "File formatting rules"
---


# 标准文件格式

## 定义
标准文件格式（Standard File Formatting）是指在 Protocol Buffers `.proto` 文件中统一执行的代码格式化规范集合，主要包括行长度控制、缩进风格和字符串引号选用等约定。这些规则作为样式指南的基础部分，旨在保证团队协作中代码的一致性和可读性，并减少代码评审时的格式噪声。

## 关键特征
- **80字符行长度限制**：强制所有代码行不超过80个字符，以保证在不同编辑器、终端和代码审查界面中横向显示完整。
- **2空格缩进**：统一采用2个空格作为缩进单位，不使用Tab，确保不同环境中缩进视觉效果完全一致。
- **双引号优先**：在`.proto`文件中声明字符串时优先使用双引号（`"`）而非单引号（`'`），减少歧义。
- **机械可执行**：规范被设计为可以由自动格式化工具（如 `clang-format` 或自定义 linter）无歧义地应用，支持一致性输出。
- **降低审阅噪声**：格式一致性确保代码变更的 diff 中仅包含逻辑改动，而非缩进或引号风格变化。

## 应用
- **团队代码审查**：在提交 `.proto` 文件变更时，格式统一性避免因个人风格差异引发不必要的讨论。
- **自动化CI/CD流水线**：集成格式化检查作为预提交钩子或CI步骤，自动拒绝不符合规范的提交。
- **跨项目协作**：当多个团队贡献同一个 `.proto` 仓库时，采用相同格式基线降低认知负荷。
- **代码生成与模板系统**：确保自动生成的 `.proto` 文件与人工编写的代码风格一致。

## 相关概念
- [[concepts/文件结构|文件结构]]
- [[concepts/标识符命名风格|标识符命名风格]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- "Keep the line length to 80 characters." — [[sources/style|style]]
- "Use an indent of 2 spaces." — [[sources/style|style]]
- "Prefer the use of double quotes for strings." — [[sources/style|style]]