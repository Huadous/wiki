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
  - "[[protobuf/editions-edition-zero-features.md]]"
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
Protobuf Editions 是 Protobuf 语言为安全演进而设计的版本机制。与传统 `proto2`/`proto3` 语法将一组固定语义绑定到 syntax 声明上不同，editions 模型将语义行为解构为一系列独立的 features，每个 feature 在该 edition 中具有一个默认值，schema 作者可以在文件级、字段级、枚举级等不同粒度上覆盖这些默认行为。一个 edition 形式上就是一组带有默认值的 features 的集合。

Editions Zero（即 Edition 2023）是第一个具体的 edition，它定义了一组核心 features（如 `features.field_presence`、`features.enum_type` 等）及其默认值，标志着 Protobuf 进入无 `syntax` 声明的新时代。后续的 edition 2024 在此基础上进一步演进。Editions 机制的设计目标是允许 Protobuf 在不破坏现有 schema 的前提下逐步收紧或放松语言规则——新增的约束通常通过新增一个 feature 并在后续 edition 中将其默认值"ratchet"为更严格的值来实现，例如为新关键字引入 `feature.xxx_is_a_keyword` 特性并将其切换为强制启用。

为了防止旧版运行时加载"过新"的描述符，editions 引入了 Minimum Required Edition 概念作为"毒丸"机制。editions 同时支持通过全局 features proto 的扩展来实现非 protobuf 团队拥有的第三方 features。editions 的生命周期被设计为支持大规模语言变更（large-scale change），通过 edition proclamation 等机制完成语义迁移。历史遗留的 proto2/proto3 文件可以通过 Legacy Syntax Editions 映射到对应的 edition 行为，Prototiller 则负责 syntax 到 edition 之间的转换。

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
> - "No directly relevant information"

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "Edition Zero Features defines the \"first edition\" of the brave new world of no-`syntax` Protobuf."
> - "For the purposes of this document, we will use the syntax described in Features as Custom Options, since it is the prevailing consensus among those working on editions."