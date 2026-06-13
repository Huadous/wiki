---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/editions-stricter-schemas-with-editions.md]]"
  - "[[protobuf/editions-README.md]]"
tags:
  - "method"
aliases:
  - "Editions 收紧 Schema 备忘录"
  - "Stricter Schemas via Editions"
  - "Editions Ratchet Pattern"
---

## Description

Stricter Schemas with Editions 是一份关于 Editions 框架下如何强化 Schema 校验与约束的设计备忘录。它探讨了通过 Editions 机制对 Protocol Buffers 的模式定义施加更严格的规则,以减少歧义、提升跨语言兼容性和安全性。该方法采用了"为每个语言角落(language corner)引入独立 feature" 的 Feature-per-lint 模型,而非一次性制定全局规则。其 Ratchet 翻转机制利用 feature 的取值通过 edition 的逐代演进由 `true` 翻转为 `false`,形成"棘轮式"单向收紧,不允许回退放宽,从而实现渐进式迁移,不一次性破坏既有 `.proto` 文件。文档明确指出这是一份使用用例备忘录(memo),而非正式的设计文档,且作为 [[protobuf/editions-README|editions-README]] 设计文档库的一部分,属于历史性设计资料,其核心理念与 Edition Zero 的多项特性(如枚举闭合性)以及 Feature Extension Layout 紧密关联。

## Related Concepts

- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/feature-gating|Feature gating]]
- [[concepts/protobuf|Protobuf]]
- Edition Zero Features
- Editions: Feature Extension Layout
- Edition Zero Feature: Enum Field Closedness

## Related Entities

- [[entities/mcy|mcy]]
- Protocol Buffers
- Protobuf Editions

## Mentions in Source

> **Source: [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]**
> - "This document describes several such corners in the language, and how we might use Editions to fix them (spoiler: we'll add a feature for each one and then ratchet the features)."
> - "This is primarily a memo on a use-case for Editions, and not a design doc per se."

> **Source: [[sources/editions-readme|editions-readme]]**
> - "The following topics are in this repository:"
> - "*   [Stricter Schemas with Editions](stricter-schemas-with-editions.md)"
> - "This directory contains historical design documents that describe plans for implementing Protobuf Editions."