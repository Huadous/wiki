---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/editions-stricter-schemas-with-editions]]"
  - "[[protobuf/editions-stricter-schemas-with-editions.md]]"
tags:
  - "method"
aliases:
  - "Protobuf name resolution"
  - "Protobuf 名称解析"
  - "Go-style name resolution in Protobuf"
  - "Go-style name resolution"
  - "Protobuf name resolution"
  - "Protobuf 名称解析"
  - "Go-style name resolution in Protobuf"
---

## Description
Name resolution in Protobuf 描述了一套用于解析 .proto 文件中各类符号（消息、枚举、字段类型等）的规则。当前的 Protobuf 沿用了 C++ 风格的复杂子集匹配机制，连原作者都承认其"比我们（Protobuf）的还更复杂"。本文档提出用 Go 风格的解析规则取代之：每个名称只能是单标识符或完整限定名（fully-qualified name）。当名称为单标识符时，它必须解析为当前文件顶层定义的类型，或在字段类型位置解析为当前消息内嵌套定义的 message/enum（不适用于扩展字段）。与 Go 不同的是，Protobuf 出于"在大型包（如 Go 运行时）中很难追踪符号定义位置"的考虑，禁止在未完全限定的情况下从其他包中查找符号。文档还提议禁止 `.foo.Bar` 这种以点开头的相对引用形式，仅在不含 `package` 声明的文件中保留为兼容例外。该迁移通过 `features.use_cpp_style_name_resolution` 特性从 true 切换到 false 实现，并结合严格标识符名称支持，利用大小写区分消息根与包根，从而进一步简化解析逻辑。

## Related Concepts
- [[concepts/feature-gating|Feature gating]]
- [[concepts/identifier-naming-conventions|Identifier naming conventions]]
- [[concepts/nonempty-package|Nonempty package]]
- [[concepts/protobuf-editions|Protobuf Editions]]

## Related Entities
- [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|Protocol Buffers v3.12.0]]

## Mentions in Source

> **Source: [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]**
> - "Right now, Protobuf defines a complicated name resolution scheme that involves matching subsets of names inspired by that of C++ (which is even more complicated than ours!)."
> - "Instead, we should require that every name be either a single identifier OR fully-qualified."