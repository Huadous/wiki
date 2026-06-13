---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/features]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/features.md]]"
  - "[[protobuf/editions.md]]"
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "standard"
aliases:
  - "2024 edition"
  - "Editions 2024"
  - "Edition Zero"
  - "2024 edition"
  - "Editions 2024"
  - "edition 2024"
  - "2024 edition"
  - "Editions 2024"
  - "Edition Zero"
  - "2024 edition"
  - "Editions 2024"
---

## Description
Protobuf Editions 是 Protocol Buffers 语言演进的下一阶段，其核心目标是将 proto2 与 proto3 的语义统一在新的"editions"语法之下。[[concepts/edition-zero|Edition Zero]] 被设计为 proto2 与 proto3 的"完成版"，可对任意 .proto 文件进行机械迁移而保持行为不变；[[concepts/edition-2023|Edition 2023]] 与 [[concepts/edition-2024|Edition 2024]] 随后引入并逐步强化了各项 [[concepts/feature|Feature]]，例如 [[concepts/field-presence|Field Presence]]、[[concepts/features-field_presence|features-field_presence]]、[[concepts/closed-enum|Closed Enum]]、[[concepts/open-enum|Open Enum]]、[[concepts/features-default_symbol_visibility|features-default_symbol_visibility]] 与 [[concepts/features-enforce_naming_style|features-enforce_naming_style]] 等。[[concepts/editions-life-of-an-edition|Life of an Edition]] 文档将这次迁移描述为一次独特的大规模变更：它"不改变任何行为，仅修改大量现有语法的拼写方式"，需先手动迁移使用 `syntax` 字段值的代码，待 95% 调用方迁移完成后再弃用相应访问器，然后通过 [[entities/protoc|protoc]] 工具链将 proto2/proto3 文件自动改写为带 `edition = "2023";` 与对应 `features.*` 选项的 editions 文件。整个迁移过程依赖 [[concepts/.proto-file|.proto file]] 的向后兼容特性，并保证 [[concepts/wire-format-compatibility|Wire Format Compatibility]] 不被破坏，从而让 [[concepts/proto2|proto2]] 与 [[concepts/proto3|proto3]] 用户在零行为差异的前提下逐步进入 editions 时代。

## Related Concepts
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/edition-2024|Edition 2024]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/features-field_presence|features-field_presence]]
- [[concepts/features-default_symbol_visibility|features-default_symbol_visibility]]
- [[concepts/features-enforce_naming_style|features-enforce_naming_style]]
- [[concepts/feature|Feature]]
- [[concepts/closed-enum|Closed Enum]]
- [[concepts/open-enum|Open Enum]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/.proto-file|.proto file]]
- [[concepts/wire-format-compatibility|Wire Format Compatibility]]

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/protoc|protoc]]
- [[entities/protobuf-team|protobuf-team]]
- [[entities/protobuf-editions|Protobuf Editions]]

## Mentions in Source

> **Source: [[sources/features|features]]**
> - "EXPORT_ALL: This is the default prior to Edition 2024."
> - "Edition 2024 defaults to STYLE2024, so an override is needed to keep the non-conformant field name:"
> - "edition \"2024\""
> - "Default behavior per syntax/edition: 2024 -> EXPORT_TOP_LEVEL"
> - "Introduced in Edition 2024, this feature enables strict naming style enforcement as defined in the style guide to ensure protos are round-trippable by default."
> - "Added in: Edition 2024"

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "The first edition of Protobuf Editions, the so-called 'edition zero', will effectively be a 'proto4' that introduces the new syntax, and merges the semantics of proto2 and proto3."
> - "Edition Zero is designed in such a way that we can mechanically migrate an arbitrary .proto file from either proto2 or proto3 with no behavioral changes."
> - "Edition Zero should be viewed as the 'completion' of the union of proto2 and proto3"

> **Source: [[sources/editions|editions]]**
> - "It covers edition 2023 edition 2024 of the protocol buffers language."
> - "No directly relevant information"

> **Source: [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]]**
> - "The first edition (colloquially known as \"Edition Zero\") will use features to unify proto2 and proto3"
> - "In order to unify proto2 and proto3, \"Edition Zero\" is taking an opinionated stance on which choices are good and bad, by choosing \"good\" defaults and requiring explicit requests for the \"bad\" semantics"
> - "No directly relevant information"

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "We need to get the ecosystem into the \"editions\" syntax. This migration is probably unique because we are not changing any behavior, just the spelling of a bunch of things."
> - "We will then introduce the features defined in Edition Zero Features. We will then implement tooling that can take a proto2 or proto3 file and add edition = \"2023\"; and option features.* = ...; as appropriate, so that each file retains its original behavior."