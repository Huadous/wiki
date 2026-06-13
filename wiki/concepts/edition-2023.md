---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/features]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/features.md]]"
  - "[[protobuf/editions.md]]"
  - "[[protobuf/editions-stricter-schemas-with-editions.md]]"
  - "[[protobuf/editions-README.md]]"
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
  - "[[protobuf/editions-protobuf-editions-design-features.md]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
  - "[[protobuf/editions-minimum-required-edition.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
  - "[[protobuf/editions-editions-feature-extension-layout.md]]"
  - "[[protobuf/editions-edition-zero-json-handling.md]]"
tags:
  - "standard"
aliases:
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "Protobuf Editions"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "edition 2023"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "Protobuf Editions"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "Edition 2023"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "Protobuf Editions"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "edition 2023"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "Protobuf Editions"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "Protobuf editions"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "Protobuf Editions"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "edition 2023"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "Protobuf Editions"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "Edition 2023"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "Protobuf Editions"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "edition 2023"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
  - "Protobuf Editions"
  - "proto edition 2023"
  - "2023 edition"
  - "Protobuf 2023 语言版本"
---

## Description
Protobuf editions 项目用「editions」来允许 Protobuf 随时间安全地演进，核心机制是「features」——每个 edition 形式上就是一组带有默认值的 feature（如 `enum_type`、`field_presence`）。文件首行以 `edition "2023"` 这样的声明取代了 `syntax = "proto2"/"proto3"`，且 edition 声明必须是文件中第一个非空、非注释的行。editions 体系同时引入了 [[concepts/featureset|FeatureSet]]、[[concepts/feature-gating|Feature gating]]、[[concepts/options-attributes|Options Attributes]] 与 [[concepts/fieldoptions|FieldOptions]] 等基础设施，允许语言绑定基于 options 构建自定义 feature。设计上还存在 [[concepts/feature-inheritance|feature-inheritance]] 机制，并通过扩展全局 features proto 来支持非 protobuf team 拥有的「targeted features」。演进过程需要 [[concepts/large-scale-change|large-scale-change]] 式的迁移，并配套 [[concepts/minimum-required-edition|Minimum Required Edition]] 作为「poison pill」来阻断过老的运行时加载「过新」的描述符。[[concepts/edition-proclamation|Edition Proclamation]] 描述了某个 edition 的发布流程；[[concepts/legacy-syntax-editions|Legacy Syntax Editions]] 则关注如何让旧语法平滑过渡到新版本。Editions 的另一个核心目的是收紧历史遗留的语法角落（[[concepts/stricter-schemas-with-editions|Stricter Schemas with Editions]]），例如通过新增 `feature.xxx_is_a_keyword` 之类的 feature，并在新 edition 中将其默认值从 true 切到 false，以 [[concepts/semantic-patch|Semantic Patch]] 方式渐进收紧校验。Editions 强调 [[concepts/wire-format-compatibility|Wire Format Compatibility]]，因此设计必须兼顾 [[concepts/backward-compatibility|backward-compatibility]] 与 [[concepts/forward-compatibility|forward-compatibility]]，并由 [[concepts/schema-producer|Schema Producer]] 与 [[concepts/schema-consumer|Schema Consumer]] 共同遵守。Edition Zero 是 editions 体系的首个里程碑，用以统一 proto2 与 proto3；其推进过程中曾因 JSON 字段名冲突的遗留问题（[[concepts/json-format-feature|json_format feature]]）而被阻塞——这迫使 json_format 被设计为三态特性（ALLOW / DISALLOW / LEGACY_BEST_EFFORT），以便在保持 wire format 兼容的前提下推进 editions 发布。Edition 2023 默认 `STYLE_LEGACY`，并新增了 `enum_type`、`field_presence` 等 feature；`features-default_symbol_visibility` 默认 `EXPORT_ALL`，同时 `features-enforce_naming_style`、`features-field_presence` 等功能持续迭代。

## Related Concepts
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/feature|Feature]]
- [[concepts/edition|Edition]]
- [[concepts/feature-inheritance|feature-inheritance]]
- [[concepts/rust-editions|Rust editions]]
- [[concepts/carbon|Carbon]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]
- [[concepts/field-cardinality|field-cardinality]]
- [[concepts/proto-file|proto-file]]
- [[concepts/backward-compatibility|backward-compatibility]]
- [[concepts/forward-compatibility|forward-compatibility]]
- [[concepts/features-default_symbol_visibility|features-default_symbol_visibility]]
- [[concepts/features-enforce_naming_style|features-enforce_naming_style]]
- [[concepts/features-field_presence|features-field_presence]]
- [[concepts/google-protobuf-any|google-protobuf-any]]
- [[concepts/edition-2024|Edition 2024]]
- [[concepts/features-enum_type|features.enum_type]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/message-type|Message Type]]
- [[concepts/reserved-keywords|Reserved keywords]]
- [[concepts/feature-gating|Feature gating]]
- [[concepts/stricter-schemas-with-editions|Stricter Schemas with Editions]]
- [[concepts/wire-format-compatibility|Wire Format Compatibility]]
- [[concepts/semantic-patch|Semantic Patch]]
- [[concepts/schema-producer|Schema Producer]]
- [[concepts/schema-consumer|Schema Consumer]]
- [[concepts/options-attributes|Options Attributes]]
- [[concepts/custom-options|Custom Options]]
- [[concepts/fieldoptions|FieldOptions]]
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/edition-proclamation|Edition Proclamation]]
- [[concepts/immolation-of-required|Immolation of `required`]]
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/delimited-encoding|Delimited encoding]]
- [[concepts/group-fields|Group fields]]
- [[concepts/json-format-feature|json_format feature]]
- [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]]
- [[concepts/json-format-allow|json_format ALLOW]]
- [[concepts/json-format-disallow|json_format DISALLOW]]
- [[concepts/json-format-legacy-best-effort|json_format LEGACY_BEST_EFFORT]]

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/protoc|protoc]]
- [[entities/grpc|grpc]]
- [[entities/google|google]]
- [[entities/prototiller|prototiller]]
- [[entities/rust|rust]]
- [[entities/bazel|bazel]]
- [[entities/protobuf-team|protobuf team]]
- [[entities/kfm|@kfm]]
- [[entities/mcy|@mcy]]
- [[entities/mkruskal-google|@mkruskal-google]]
- [[entities/joshua-humphries|Joshua Humphries]]

## Mentions in Source

> **来源: overview**
> - "The following shows an example message edition '2023'."
> - "For more information about the options available, see the language guide for proto2, proto3, or edition 2023."

> **来源: features**
> - "Protobuf Editions features and how they affect protobuf behavior."
> - "This topic provides an overview of the features that are included in the released edition versions. Subsequent editions' features will be added to this topic."
> - "For more information on how editions and features work together to set behavior, see Protobuf Editions Overview"
> - "Edition 2023 defaults to STYLE_LEGACY, so a non-conformant field name is fine:"
> - "edition \"2023\""
> - "Default behavior per syntax/edition: 2023 -> EXPORT_ALL"
> - "Features added in Edition 2023: enum_type, field_presence"
> - "No directly relevant information"

> **来源: editions**
> - "It covers edition 2023 edition 2024 of the protocol buffers language."
> - "The first line of the file specifies that you're using edition 2023 of the protobuf language spec."
> - "edition syntax for proto2/proto3) must be the first non-empty, non-comment line of the file."

> **来源: editions**
> - "No directly relevant information"

> **Source: editions-stricter-schemas-with-editions**
> - "This document describes several such corners in the language, and how we might use Editions to fix them (spoiler: we'll add a feature for each one and then ratchet the features)."
> - "From time to time we may introduce new keywords. The best procedure for doing so is to add a `feature.xxx_is_a_keyword` feature, start it out as true, and then switch it to false in an edition, which would cause it to be treated as a keyword for the purposes of this check."

> **Source: editions-stricter-schemas-with-editions**
> - "No directly relevant information"

> **Source: editions-readme**
> - "This directory contains historical design documents that describe plans for implementing Protobuf Editions."
> - "For an up-to-date overview of this feature of Protocol Buffers, see [Protobuf Editions Overview](https://protobuf.dev/editions/overview/)."
> - "These are purely for historical value and should not be treated as documentation of the current state."

> **Source: editions-README**
> - "No directly relevant information"

> **Source: editions-protobuf-editions-for-schema-producers**
> - "The Protobuf Editions project uses \"editions\" to allow Protobuf to safely evolve over time."
> - "This is primarily accomplished through \"features\"."
> - "No directly relevant information"

> **Source: editions-protobuf-editions-design-features**
> - "The Protobuf Editions project uses \"editions\" to allow Protobuf to safely evolve over time."
> - "An edition is formally a set of \"features\" with a default value per feature."
> - "No directly relevant information"

> **Source: editions-protobuf-design-options-attributes**
> - "The [Protobuf Editions](what-are-protobuf-editions.md) project plans to use [custom options](protobuf-editions-design-features.md) to model features and encourage language bindings to build custom features off options as well."
> - "While the proximal motivation for these options is for use with \"features\" in \"editions\", I believe they provide sufficient general utility that adding them directly to `FieldDescriptorOptions` is warranted."
> - "No directly relevant information"

> **Source: editions-minimum-required-edition**
> - "[Protobuf Editions](what-are-protobuf-editions.md) intends to add the concept of an edition to Protobuf, which will be an approximately-annually incrementing value."
> - "we can use them as a poison pill for old runtimes that try to load descriptors that are \"too new.\""
> - "No directly relevant information"

> **Source: editions-life-of-an-edition**
> - "How to use Protobuf Editions to construct a large-scale change that modifies the semantics of Protobuf in some way."
> - "This document describes how to use the Protobuf Editions mechanism (both editions, themselves, and features) for designing migrations and large-scale changes intended to solve a particular kind of defect in the language."
> - "No directly relevant information"

> **Source: editions-legacy-syntax-editions**
> - "[Edition Zero Features](edition-zero-features.md) lays out our plan for edition 2023, which will unify proto2 and proto3."
> - "A separate issue is how Prototiller will support the conversion of syntax to edition 2023."
> - "No directly relevant information"

> **Source: editions-group-migration-issues**
> - "The problem under edition 2023 is that we've removed the generation of synchronized synthetic messages from the language."
> - "Nerf Delimited Encoding in 2023 is the quickest path forward to unblock the release of edition 2023."
> - "No directly relevant information"

> **Source: [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]**
> - "[What are Protobuf Editions](what-are-protobuf-editions.md) lays out a plan for allowing for more targeted features not owned by the protobuf team."
> - "It uses extensions of the global features proto to implement this."
> - "No directly relevant information"

> **Source: [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]**
> - "While we had hoped to unify these before Protobuf editions launched, we ended up blocked by some internal use-cases."
> - "This issue is now blocking the editions launch, since we can't represent this behavior with the current set of Edition Zero features."