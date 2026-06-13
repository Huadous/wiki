---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-protobuf-editions-design-features.md]]"
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
  - "Language-Specific Features"
  - "语言特性"
  - "语言作用域特性"
  - "language-scoped features"
  - "Language-scoped Feature"
  - "语言特性"
  - "语言作用域特性"
  - "language-scoped features"
---

## Description

Language-scoped features 是 Protobuf Editions 为实现语言特定定制而设计的核心机制，其实现基础是利用 protobuf 的 extension 机制在 `descriptor.proto` 的 Features 消息中按语言预留扩展号（如 extensions 1000 用于 C++，extensions 1001 用于 Java），从而保持核心 Features 消息的精简。由于 features 本质上是 Protobuf 扩展（extensions），每个语言后端（如 C++、Java、Go、Rust 等）都可以在其独立的命名空间内定义专有的 feature，并通过 `import` 引入对应的 `features_cpp.proto` 等语言级 features 文件来自动发现这些功能字段，例如 `features.(pb.cpp).string_field_type` 控制 C++ 后端的生成字符串类型。这种设计赋予了语言后端完全的所有权——从 feature 的语义定义、默认值设定到验证逻辑均由后端自主管理，不受其他语言影响。同时，第三方代码生成器只要在 `descriptor.proto` 中预留一个扩展号，就可以借助 editions 系统实现各自的特性演进。例如，`[ctype = CORD]` 这一历史遗留语法可以被更清晰地重构为 `[features.(pb.cpp).string_type = CORD]`，使其成为语言作用域 edition 的一部分。由于遵循统一的 editions 生命周期管理规则，各语言后端可以在共享的版本框架下独立演进其特性，实现细粒度的文件、消息、字段级控制，而不会破坏整体跨语言生态的兼容性。

## Related Concepts

- [[concepts/features|Features]]
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/editions|Editions]]
- [[concepts/custom-options|Custom Options]]

## Related Entities

- [[entities/protobuf-team|protobuf-team]]
- [[entities/protoc|Protoc]]
- [[entities/c++|C++]]

## Mentions in Source

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "Because features can be extensions, language backends can specify **language-scoped** features. For example, `[ctype = CORD]` could instead be phrased as `[features.(pb.cpp).string_type = CORD]`."
> - "Codegen backends own the definitions of their features."

> **Source: [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]**
> - "We will use extensions to manage features specific to individual code generators."
> - "This will allow third-party code generators to use editions for their own evolution as long as they reserve a single extension number in `descriptor.proto`."