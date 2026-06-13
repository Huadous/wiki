---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]"]
tags: [standard]
aliases:
  - "package anywhere"
  - "package-first requirement"
  - "包声明位置"
---


# Package declaration position

## 定义
Package declaration position（包声明位置）是一项 Protobuf 语言标准提案，要求 `package` 声明必须是 Protobuf 文件中 `syntax` 或 `edition` 之后的第一条语句。该提案借鉴了 Go 语言的包声明风格，旨在消除当前 Protobuf 允许 `package` 出现在文件中 `syntax` 或 `edition` 之后任何位置所引入的实现复杂度与潜在歧义。该变更通过 `features.package_anywhere` 特性标志进行管理，初始值为 `true`（保留现有灵活行为），在未来 edition 中切换为 `false`，以强制要求包声明必须位于文件开头。

## 关键特征
- **位置约束**：要求 `package` 声明紧跟在 `syntax` 或 `edition` 之后，作为文件中的第一条非版本声明语句。
- **借鉴 Go 风格**：与 Go 语言中 `package` 声明必须位于文件开头的惯例保持一致，提供清晰统一的文件头结构。
- **特性标志驱动**：通过 `features.package_anywhere` 特性标志管理，初始为 `true`（兼容旧行为），计划在未来 edition 中切换为 `false`。
- **渐进式迁移**：借助 Editions 的特性门控机制，使旧版文件无需立即修改，仅在切换到新版 edition 并设置标志为 `false` 后才被强制约束。
- **降低实现复杂度**：消除现有"包声明可出现在文件任意位置"的灵活性所带来的解析器与工具链额外复杂度。

## 应用
- 指导 Protobuf 编译器（protoc）及语言运行时在解析 `.proto` 文件时如何处理 `package` 声明的位置。
- 为 Protobuf Editions 的版本演进提供一项可被逐步启用的标准化规则。
- 推动 Protobuf 代码生成器、IDE 插件、Linter 工具对齐统一的包声明位置校验逻辑。
- 与 [[concepts/Nonempty package]]、[[concepts/Feature gating]]、[[concepts/Protobuf Edition]] 等相关概念共同构成 Editions 收紧 Schema 的语义体系。

## 相关概念
- [[concepts/Nonempty package|Nonempty package]]
- [[concepts/Feature gating|Feature gating]]
- [[concepts/Protobuf Edition|Protobuf Edition]]

## 相关实体
- [[entities/stricter-schemas-with-editions|Stricter Schemas with Editions]]
- [[entities/protocol-buffers|Protobuf]]

## 来源提及
- "The `package` declaration can appear anywhere in the file after `syntax` or `edition`. We should take cues from Go and require it to be the first thing in the file, after the edition." — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]
- "We would introduce a feature like `features.package_anywhere`, which would switch from true to false." — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]