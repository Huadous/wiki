---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-readme|editions-readme]]"]
tags: [term]
aliases:
  - "Editions 特性可见性"
  - "Editions Feature Visibility"
---


# Editions Feature Visibility

## 定义
Editions Feature Visibility（Editions 特性可见性）是 Protobuf Editions 设计文档体系中关于特性可见性机制的设计文档，描述了 Edition 特性如何在生成的代码和运行时 API 中呈现给最终开发者。该机制决定了哪些特性在特定 Edition 下可用、如何向用户暴露这些特性，以及特性在不同代码生成路径中的可见性规则。它是 Editions 特性管理与 API 设计的重要组成部分，与 Editions: Feature Extension Layout（特性扩展底层布局）共同构成了特性的外部暴露与内部表示机制。

## 关键特征
- 定义 Edition 特性在生成代码与运行时 API 层面对最终开发者的可见性规则
- 决定在特定 Edition 下哪些特性可用，以及如何向用户暴露这些特性
- 覆盖特性在不同代码生成路径中的可见性约束
- 与 Editions: Feature Extension Layout 互补：前者关注特性的外部暴露（面向开发者），后者关注特性的内部底层表示（编码与扩展布局）

## 应用
- 作为 Protobuf Editions 体系下 API 设计的参考文档，帮助语言团队与工具链实现者理解特性的暴露方式
- 在代码生成器实现中，依据可见性规则决定是否生成对应 API 入口
- 与 Protobuf Editions Design: Features、Editions: Life of a Featureset 等文档配合，形成完整的特性管理闭环（定义 → 扩展布局 → 可见性 → 生命周期）
- 在多 Edition 兼容场景中，用于判定旧特性是否仍向最终用户开放

## 相关概念
- [[concepts/editions-feature-extension-layout|Editions: Feature Extension Layout]]
- [[concepts/editions-design-features|Protobuf Editions Design: Features]]
- [[concepts/editions-life-of-a-featureset|Editions: Life of a Featureset]]

## 相关实体
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- "The following topics are in this repository:" — [[sources/editions-readme|editions-readme]]
- "Editions Feature Visibility (editions-feature-visibility.md)" — [[sources/editions-readme|editions-readme]]