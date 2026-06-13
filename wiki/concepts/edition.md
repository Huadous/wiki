---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/features.md]]"
tags:
  - "term"
aliases:
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "Editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "Rust editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "Editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "Protocol Buffers Editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "Editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "Rust editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "Editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
  - "editions"
  - "language edition"
  - "protobuf edition"
  - "Proto编辑器版本"
---

## Description
Editions 是 Google 为 Protobuf 设计的新一代模式定义机制，采用年份编号（如 2023、2024）来标识版本，每个版本定义了 protoc 及其后端所理解的特性的默认值集合。与传统的 proto2/proto3 硬编码行为不同，Editions 引入了特性设置（feature settings）的概念，允许用户在文件级、非嵌套级（non-nested level）、嵌套级（nested level）和最低层级（lowest level）等不同作用域中覆盖默认行为，从而提供更灵活、可演进且不会破坏现有模式的配置方式。

Editions 的设计直接借鉴自 [[entities/rust|Rust]] 的 editions 机制——Rust 将语言演进内建为核心设计的一部分，Protobuf 也采用了类似思路。每个新版本会引入新的特性并调整默认值，使整个生态系统能够持续向前演进，同时保持向后兼容。当 .proto 文件未指定 edition 或 syntax 时，[[entities/protoc|protoc]] 编译器默认假设使用 proto2。

特性设置按作用域层级生效：文件级（file-level）的设置将应用于所有未自行覆盖的元素（包括消息、字段、枚举等），而更细粒度的作用域允许在特定元素上覆盖默认值。例如 `field_presence`、`default_symbol_visibility`、`enforce_naming_style`、`enum_type` 等都是 Editions 中可配置的典型特性。

## Related Concepts
- [[concepts/field-presence|field_presence feature]]
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/features|Features]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/edition-2024|Edition 2024]]
- [[concepts/default-symbol-visibility|features.default_symbol_visibility]]
- [[concepts/enforce-naming-style|features.enforce_naming_style]]
- [[concepts/enum-type|features.enum_type]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/carbon|Carbon]]
- [[entities/rust|rust]]
- [[entities/prototiller|Prototiller]]

## Mentions in Source
> **来源: [[sources/editions|editions]]**
> - "The first line of the file specifies that you’re using edition 2023 of the protobuf language spec."
> - "It covers edition 2023 and edition 2024 of the protocol buffers language."
> - "If no edition or syntax is specified, the protocol buffer compiler will assume you are using proto2."

> **来源: [[sources/proto3|proto3]]**
> - "For information on editions syntax, see the Protobuf Editions Language Guide"
> - "If no edition / syntax is specified, the protocol buffer compiler will assume you are using proto2"

> **来源: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "An edition is a collection of defaults for features understood by protoc and its backends."
> - "Editions change only the defaults of features and do not otherwise introduce new behavior."
> - "Editions allow us to ratchet the ecosystem forward."
> - "Directly inspired by Rust editions."
> - "Rust has built language evolution via editions into its core design."
> - "Editions are year-numbered, although we have defined a breakout in case we need multiple editions in a particular year."
> - "Editions are year-numbered, and each edition defines a set of default values for the various features that protoc and its backends understand."

> **来源: [[sources/features|features]]**
> - "This topic provides an overview of the features that are included in the released edition versions. Subsequent editions' features will be added to this topic."
> - "Feature settings apply at different levels: File-level: These settings apply to all elements (messages, fields, enums, and so on) that don't have an overriding setting."