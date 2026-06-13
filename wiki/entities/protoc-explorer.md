---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-group-migration-issues|editions-group-migration-issues]]"]
tags: [product]
aliases:
  - "protoc explorer"
  - "protoc-explorer 工具"
---


# protoc-explorer

## 基本信息
- Type: product
- Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]

## 描述
protoc-explorer 是一个用于探索和测试不同语言下 protobuf 代码生成结果的工具，在 [[sources/editions-group-migration-issues|editions-group-migration-issues]] 一文中被作者用于系统地比较各种语言运行时对 proto2 groups 的代码生成方式。文档明确指出该工具"not available externally"（外部不可用），是 Google 内部使用的工具，因此外部开发者无法直接访问或复用。通过 protoc-explorer 的输出，作者以表格形式展示了 C++、Java、Python、Go、Dart、upb、Objective-C、Swift、C# 等运行时在生成 group 字段 API 时的差异，并指出这些差异呈现出"a fairly random-seeming mix in different generators"（在不同生成器之间呈现出看似随机的混合状态）的现象。该工具主要用于 protobuf 语言团队评估 [[concepts/group-fields|Group fields]] 与 [[concepts/group-like-fields|Group-like fields]] 在迁移到 Editions 过程中的兼容性问题。

## 相关实体
无相关实体。

## 相关概念
- [[concepts/codegen|Codegen]]
- [[concepts/group-fields|Group fields]]
- [[concepts/group-like-fields|Group-like fields]]

## 来源提及
- "Using protoc-explorer (not available externally), we find the following:" — [[sources/editions-group-migration-issues|editions-group-migration-issues]]
- "The result is that we see a fairly random-seeming mix in different generators." — [[sources/editions-group-migration-issues|editions-group-migration-issues]]