---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
tags:
  - "term"
aliases:
  - "protoc 后端"
  - "代码生成后端"
  - "codegen backends"
  - "Codegen Backend"
  - "protoc 后端"
  - "代码生成后端"
  - "codegen backends"
---

## Description
Protoc backends 是 protoc 编译器架构中的核心组件，每个 backend 专为一种目标编程语言（如 C++、Java、Python）实现代码生成逻辑。在 Protobuf Editions 框架中，backends 被赋予定义语言作用域特征（language-scoped features）的能力，这使得语言特定的行为（例如 C++ 中字符串字段的内存管理方式）可以通过特征进行声明式控制。每个 backend 必须为其支持的每个 edition 版本显式地声明所有特征的默认值，并明确拒绝其无法处理的 edition 版本，这确保了代码生成的安全性和兼容性。值得注意的是，只有代码生成器的所有者才需要掌握特征的传播逻辑，普通用户可以完全忽略底层实现细节。通过这种方式，backends 将特征定义、版本兼容性管理和代码生成逻辑有机地整合在一起，使得 Protobuf 生态能够平滑演进。

## Related Concepts
- [[concepts/Features|Features]]
- [[concepts/Language-scoped features|Language-scoped features]]
- [[concepts/Editions|Editions]]
- [[concepts/Feature Inheritance|Feature Inheritance]]

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protobuf-team|protobuf-team]]
- [[entities/open-source-oss-community|open-source-oss-community]]
- [[entities/c++|C++]]

## Mentions in Source
> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
- "protoc backends, which can specify their own set of language-scoped features, must advertise the defaults for a particular edition that they understand (and reject editions that they don't)." — [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]
- "Codegen backends own the definitions of their features." — [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]
- "Owners of code generators should be the only ones that need to know how to correctly propagate features." — [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]