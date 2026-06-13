---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/overview]]"]
tags: [method]
aliases:
  - "扩展"
  - "message extension"
  - "字段扩展"
---


# Extensions

## 定义
Extensions 是 Protocol Buffers 中一种允许在原始 `.proto` 文件外部为 message 类型添加额外字段的机制。它通过在 message 内部使用 `extensions` 关键字预留字段号范围，其他 `.proto` 文件可以通过 `extend` 关键字在指定的范围内定义新字段。

## 关键特征
- **外部扩展能力**：允许在不修改原始 message 定义的前提下，为其添加新字段。
- **字段号范围预留**：原始 message 使用 `extensions <start> to <end>;` 语法预留一段字段号，供外部扩展使用。
- **独立定义**：扩展字段在其他 `.proto` 文件中通过 `extend <MessageType> { ... }` 语法定义。
- **Proto2 特性**：Extensions 是 Proto2 的核心功能之一，在 Proto3 中被替代，推荐使用 `Any` 类型实现类似功能。
- **框架级扩展点**：常用于库作者或框架设计者提供可插拔的扩展能力，例如 protobuf 库内部为自定义选项预留扩展。

## 应用
- **框架级扩展点**：protobuf 库内部 message schema 使用 extensions 允许用户添加自定义、使用相关的选项。
- **跨团队协作**：当多个团队需要向共享的 message 类型中添加字段，但又无法协调修改原始 `.proto` 文件时，可各自通过 extensions 独立扩展。
- **渐进式演进**：在不破坏现有系统的情况下，逐步为 message 增加新字段（仅限 Proto2 项目）。

## 相关概念
- [[concepts/proto2|Proto2]]
- [[concepts/field-number|Field number]]
- [[concepts/proto-file|.proto file]]
- [[concepts/message-type|message-type]]
- [[concepts/proto3|Proto3]]

## 相关实体
- [[entities/protocol-buffers|protocol-buffers]]

## 来源提及
- "Messages can allow extensions to define fields outside of the message, itself. For example, the protobuf library's internal message schema allows extensions for custom, usage-specific options." — [[protobuf/overview|overview]]