---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/features]]"]
tags: [product]
aliases:
  - "Prototiller 工具"
  - "prototiller"
---


# Prototiller

## 基本信息
- Type: product
- Source: [[sources/features|features]]

## 描述
Prototiller 是一个命令行工具，专门用于处理 Protocol Buffers 架构文件在不同语法版本与 Editions 之间的迁移工作。该工具能够自动将 proto2、proto3 等传统语法文件转换为 Edition 2023、Edition 2024 等新版格式，并同步处理特性设置的迁移，从而减少手动修改带来的配置错误风险。目前 Prototiller 尚未正式发布，但在 Protocol Buffers 官方文档中被多次引用，作为演示语法迁移过程的示例工具。文档中通过展示运行 Prototiller 后的等效代码，帮助用户理解 Edition 格式下特性设置的表达方式。

## 相关实体
- [[entities/protocol-buffers|protocol-buffers]] — Prototiller 是 Protocol Buffers 生态系统中的工具
- [[entities/protoc|protoc]] — 同为 Protocol Buffers 工具链中的命令行工具
- [[entities/google|google]] — Protocol Buffers 的维护者和 Prototiller 的潜在发布方

## 相关概念
- [[concepts/google-protobuf-any|google-protobuf-any]] — 特性设置中可能使用到的消息类型
- [[concepts/text-format|text-format]] — 与 proto 文件文本格式相关的概念

## 来源提及
- "Prototiller is a command-line tool that updates proto schema configuration files between syntax versions and editions." — [[sources/features|features]]
- "It hasn’t been released yet, but is referenced throughout this topic." — [[sources/features|features]]
- "After running Prototiller, the equivalent code might look like this:" — [[sources/features|features]]