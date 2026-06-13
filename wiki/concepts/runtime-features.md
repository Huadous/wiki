---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-editions-life-of-a-featureset]]"
  - "[[protobuf/editions-editions-feature-extension-layout.md]]"
tags:
  - "term"
aliases:
  - "运行时特性"
  - "Runtime Features"
  - "Runtime Implementation Features"
  - "运行时特性"
  - "Runtime Features"
---

## Description
运行时特性（Runtime Features）是 FeatureSet 在经过选项保留策略之后呈现给运行时的最终形态，既包含已解析特性，也包含未解析特性，由运行时在执行 protobuf 消息时直接消费，并作为动态消息决策的依据。在功能扩展布局的讨论中，存在一种被称为"Runtime Implementation Features"的替代方案，主张将 Features 按运行时实现（如 C++、Java、Python、upb 等）划分，每个实现各自维护一套独立的特性集合。这种划分方式与 Editions 之前可表达的行为范围最为一致，例如 Protobuf Python 用户在使用不同的底层实现时需要分别设置 `features.(pb.cpp).<feature>` 与 `features.(pb.upb).<feature>` 等特性。然而，该方案的缺点是用户难以判断应该使用哪个实现对应的特性集，并且缺乏对语言/实现组合的独立控制能力，可能使迁移过程更加困难。

## Related Concepts
- [[concepts/FeatureSet]]
- [[concepts/Option Retention]]
- [[concepts/Source Features]]
- [[concepts/Resolved Features]]
- [[concepts/Unresolved Features]]
- [[concepts/Dynamic Messages]]
- [[concepts/Feature Extension]]
- [[concepts/Generator Features]]
- [[concepts/Shared Implementations]]
- [[concepts/utf8_validation]]

## Related Entities
- [[entities/FileDescriptorProto]]

## Mentions in Source

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "**Runtime features** - The features available to runtimes after option retention has been applied. These can be either resolved or unresolved."

> **Source: [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]**
> - "Features would be per-runtime implementation as originally described in \"Editions Zero Feature: utf8_validation.\""
> - "For example, Protobuf Python users would set different features depending on the backing implementation (e.g. `features.(pb.cpp).<feature>`, `features.(pb.upb).<feature>`)."