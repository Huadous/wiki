---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-protobuf-editions-for-schema-producers]]"]
tags: [term]
aliases:
  - "Schema 消费者"
  - "Protobuf Schema Consumer"
---


# Schema Consumer

## 定义
Schema Consumer 是与 [[concepts/schema-producer|Schema Producer]] 对应的角色，指消费由 producer 发布的 `.proto` 文件的团队或系统。其使用方式受到构建系统的强烈约束：语言无关的构建系统（如 [[entities/bazel|Bazel]]）可以较容易地将 [[entities/protoc|protoc]] 作为构建步骤运行，而语言特定的构建系统（如 Maven 或 Go）以及传统上无构建系统的语言（如 Python）则使 protoc 的运行更为困难。

## 关键特征
- 与 Schema Producer 形成角色对偶：Producer 负责发布 schema，Consumer 负责消费并使用这些 schema
- 使用方式受构建系统约束：语言无关构建系统集成 protoc 较容易，语言特定或无构建系统的语言集成 protoc 较困难
- 可根据自身需要添加生成器特定的 [[concepts/feature|Feature]]（通过手工或自动化的 `.proto` 重构工具）
- 不应被 Producer 强制施加额外的生成器特定选择，保持 schema 的中立性和可消费性

## 应用
- 在多语言微服务架构中，不同语言的团队以 Consumer 身份消费共享的 `.proto` 文件
- 使用 Bazel 等语言无关构建系统的项目可以直接将 protoc 集成到构建流程中
- 使用 Maven（Java）、Go modules 或 Python 等语言特定工具链的项目需要额外机制来运行 protoc
- Consumer 可通过 [[concepts/semantic-patch|Semantic Patch]] 等自动化重构工具调整 `.proto` 文件以适配本地生成器需求

## 相关概念
- [[concepts/schema-producer|Schema Producer]]
- [[concepts/feature|Feature]]
- [[concepts/semantic-patch|Semantic Patch]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/bazel|Bazel]]

## 来源提及
- "Consumers' usage is heavily constrained by their build system." — [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]]
- "**Consumers** of published schemas may wish to add generator specific features (either by hand or with an automated `.proto` refactoring tool), but **producers** should not force that onto users." — [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]]