---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
tags:
  - "term"
aliases:
  - "语言特性"
  - "语言作用域特性"
  - "language-scoped features"
  - "Language-scoped Feature"
  - "语言特性"
  - "语言作用域特性"
  - "language-scoped features"
---

## Description

Language-scoped features 是 Protobuf Editions 为实现语言特定定制而设计的核心机制。由于 features 本质上是 Protobuf 扩展（extensions），每个语言后端（如 C++、Java、Go、Rust 等）都可以在其独立的命名空间内定义专有的 feature，例如 `features.(pb.cpp).string_type` 控制 C++ 后端的生成字符串类型。这种设计赋予了语言后端完全的所有权——从 feature 的语义定义、默认值设定到验证逻辑均由后端自主管理，不受其他语言影响。例如，`[ctype = CORD]` 这一历史遗留语法可以被更清晰地重构为 `[features.(pb.cpp).string_type = CORD]`，使其成为语言作用域 edition 的一部分。同时，由于遵循统一的 editions 生命周期管理规则，各语言后端可以在共享的版本框架下独立演进其特性，实现细粒度的文件、消息、字段级控制，而不会破坏整体跨语言生态的兼容性。

## Related Concepts

- [[concepts/features|Features]]
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/editions|Editions]]

## Related Entities

- [[entities/protobuf-team|protobuf-team]]
- [[entities/protoc|Protoc]]
- [[entities/c++|C++]]

## Mentions in Source

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "Because features can be extensions, language backends can specify **language-scoped** features. For example, `[ctype = CORD]` could instead be phrased as `[features.(pb.cpp).string_type = CORD]`."
> - "Codegen backends own the definitions of their features."