---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]"]
tags: [term]
aliases:
  - "Semantic Features"
  - "语义特性"
---


# Semantic features

## 定义
Semantic features（语义特性）是一类横跨语言、跨越 protobuf 数据模型层面的行为变更特性。与语言特定特性（language-specific features）不同，语义特性定义的是独立于具体编程语言、作用于 protobuf 数据模型本身的行为变化。虽然它们可能同时对 API 表面产生影响，但其语义含义远不止于 API 表层。语义特性必须在所有语言实现中保持一致，因此具有显著更广的适用范围。

## 关键特征
- **跨语言一致性**：必须在所有 protobuf 支持的语言中得到正确实现，适用范围显著大于语言特定特性。
- **影响数据模型语义**：其行为变化作用于 protobuf 数据模型层面，而非仅停留在语言 API 层面。
- **可具有 API 影响**：虽然语义深入到底层，但同样可能带来 API 表层的变化。
- **典型示例**：
  - `open enums`：枚举值直接放入字段中，而不再放入 `UnknownFieldSet`。
  - `packed`：`repeated` 字段在线缆上是否使用 packed 编码。
- **默认特性集的传播**：每种语言必须知晓每个 edition 的规范默认特性集；或者由 `protoc` 统一解析默认特性，并显式传播到描述符（descriptor）中。

## 应用
- 作为 Protobuf Editions 特性分类体系中的核心类别之一，与 [[concepts/Language-specific-features|Language-specific features]] 共同构成特性的二维分类。
- 用于指导各语言运行时实现一致的默认行为，例如 `open enums` 和 `packed` 等跨语言语义行为的统一。
- 配合 `features` option 与 [[concepts/Converged-Semantics|Converged Semantics]] 设计共同落地，定义每个 edition 的默认特性集。
- 借助 [[entities/descriptor.proto|descriptor.proto]] 与 [[entities/protoc|protoc]] 的协作机制，将语义特性的默认值显式编码并传播到描述符中。

## 相关概念
- [[concepts/Language-specific-features|Language-specific features]]
- [[concepts/features-option|features option]]
- [[concepts/Converged-Semantics|Converged Semantics]]

## 相关实体
- [[entities/descriptor.proto|descriptor.proto]]
- [[entities/protoc|protoc]]

## 来源提及
- "Semantic features define behavior changes that apply to the protobuf data model, independent of language." — [[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]
- "These can also have API implications, but their meaning goes deeper than just a surface-level API." — [[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]