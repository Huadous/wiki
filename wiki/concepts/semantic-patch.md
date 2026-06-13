---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-protobuf-editions-for-schema-producers]]"]
tags: [method]
aliases:
  - "Semantic Patch"
  - "语义补丁"
  - "semantic patch"
---


# Semantic Patch

## 定义
Semantic Patch（语义补丁）是 Protobuf Editions 为支持 schema 演进而提出的一种受控变更机制。它以声明式方式描述对 `.proto` 文件的修改，而非直接编辑源文件，从而在不破坏现有 schema 的前提下应用增量变更。

## 关键特征
- **受控变更**：在不破坏现有 `.proto` 文件的前提下描述并应用 schema 修改。
- **双重支持路径**：Protobuf 团队提供两类工具——一是将语义补丁自动应用到 `.proto` 文件并提交至源代码控制；二是 `protoc` 可直接将 `.proto` 文件与语义补丁作为联合输入进行编译，无需物化中间文件。
- **声明式消费**：Bazel 规则可通过 `modifications` 参数引用语义补丁，使消费者能为特定环境添加 features 而不污染上游 schema。
- **可审计性**：补丁与原始文件分离，便于审查、回滚和跨环境复用。

## 应用
- **源代码控制集成**：CI/CD 流程自动将语义补丁应用到 `.proto` 文件并提交结果。
- **直接编译模式**：`protoc` 在编译时同时接受 `.proto` 文件与语义补丁作为输入，跳过文件物化步骤。
- **Bazel 构建系统**：通过 `modifications` 参数在 build 阶段声明式地注入环境相关的 features。
- **多环境 schema 定制**：不同下游消费者（服务端、客户端、测试环境等）可在共享同一上游 schema 的同时附加各自的 features。

## 相关概念
- [[concepts/Schema Consumer]]
- [[concepts/Protobuf Editions]]
- [[concepts/Feature]]

## 相关实体
- [[entities/protoc]]
- [[entities/Bazel]]
- [[entities/Protobuf team]]

## 来源提及
- "we will provide tools for automating updates to `.proto` files in a safe way. These tools will apply semantic patches to `.proto` files that they can then commit into source control." — [[sources/editions-protobuf-editions-for-schema-producers]]