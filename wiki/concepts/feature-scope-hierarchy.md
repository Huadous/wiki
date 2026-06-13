---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]"]
tags: [term]
aliases:
  - "特征作用域层级"
  - "descriptor levels"
  - "feature declaration levels"
---


# Feature scope hierarchy

## 定义
Feature scope hierarchy（特征作用域层级）描述了 `features` 选项可以在 Protobuf 描述符中被声明的多层级结构。根据设计文档，`features` 选项将被添加到 `descriptor.proto` 中，覆盖 File、Message、Field、Enum、Enum Value、Oneof、Service、Method 以及 Stream（仅限内部仓库）等多个描述符层级。

## 关键特征
- **多层级声明支持**：`features` 选项可在 File、Message、Field、Enum、Enum Value、Oneof、Service、Method、Stream 多个层级声明。
- **作用域继承由特征定义决定**：特征可以在任意层级声明，但是否影响后代类型由 Protobuf 团队针对单个特征的定义自行决定，例如文件级别的特征 opt-out 可能影响该文件中所有字段。
- **与 edition 关键字绑定**：特征只有在配合 `edition` 关键字使用时才会被尊重。
- **不校验特征正确性**：为保证前向与后向兼容性，系统不会校验特征声明的正确性。

## 应用
- 为 Protobuf Editions 提供灵活的特征作用域模型，使同一特征可在不同描述符层级被声明或覆盖。
- 允许通过在文件层级声明特征（如 opt-out）来批量影响该文件内所有嵌套类型，避免逐个字段重复标注。
- 支持语言特定特征与语义特征在合适的作用域层级声明，以满足不同实现层的需求。

## 相关概念
- [[concepts/features-option|features option]]
- [[concepts/edition-keyword|edition keyword]]
- [[concepts/language-specific-features|Language-specific features]]
- [[concepts/semantic-features|Semantic features]]

## 相关实体
- [[entities/descriptor.proto|descriptor.proto]]

## 来源提及
- "The `features` option will be added to `descriptor.proto` for the following descriptor options: File, Message, Field, Enum, Enum Value, Oneof, Service, Method, Stream (internal repositories only)." — [[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]