---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-edition-lifetimes.md]]"
tags:
  - "method"
aliases:
  - "特性生命周期"
  - "特性演化流程"
  - "Feature Lifetimes"
  - "特性生命周期"
  - "特性演化流程"
---

## Description
特性生命周期（Feature Lifetimes）描述 Protocol Buffers Editions 中每个 Feature 从引入（introduction）、弃用（deprecation）到删除（removal）的完整演进过程，与 Edition 自身的生命周期共享同一组关键事件。该提案建议通过新增四个字段选项——`edition_introduced`、`edition_deprecated`、`deprecation_warning`、`edition_removed`——将特性生命周期显式编码到特性定义中，使每个特性的存在窗口及其在任意给定版本下的默认行为变得完全可预测。文档还引入 `EDITION_LEGACY` 作为占位版本，专门用于表示某个特性被引入之前的旧版行为，从而在 Edition 演进图中保留一个明确的"零号"参照点。与 *Life of an Edition* 相对应，存在一份不对外公开的替代视角文档 *Editions: Life of a Feature*，它尝试对 Feature 与 Edition 之间的相互作用施加更严格的约束。Feature 默认值在不同 Edition 之间可逐步切换（例如 2025 Edition 创建某特性并默认关闭，2027 Edition 将其默认值切换为 true），而只要 `.proto` 文件未使用已被弃用的特性，从一个 Edition 升级到下一个 Edition 就是无副作用的（no-op）操作。

## Related Concepts
- [[concepts/Features]]
- [[concepts/Editions]]
- [[concepts/Feature Inheritance]]
- [[concepts/Language-scoped features]]
- [[concepts/LSC|LSC]]
- [[concepts/edition-lifetimes|Edition Lifetimes]]
- [[concepts/feature-support|FeatureSupport]]
- [[concepts/edition-legacy|EDITION_LEGACY]]

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protoc|Protoc]]
- [[entities/protobuf-team|protobuf-team]]

## Mentions in Source

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
- "Edition "2025" creates features.(pb.cpp).opaque_repeated_fields with a default value of false."
- "Edition "2027" switches the default of features.(pb.cpp).opaque_repeated_fields to true."
- "The key point to note here is that any `.proto` file that does not use deprecated features has a no-op upgrade from one edition to the next and we will provide tools to effect that upgrade."
- "Internal users will be migrated centrally before a feature is deprecated. External users will have the full window of the Google migration as well as the deprecation window to upgrade their own code."

> **Source: [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]**
- "There are three relevant events in the lifetime of both editions and features, introduction, deprecation, and removal."
- "*Editions: Life of a Feature* (not available externally) is an alternate vision to *Life of an Edition*, which tries to put tighter constraints on how features and editions interact."