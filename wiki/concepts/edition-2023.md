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
---

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

> **Source: [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]**
> - "The [Protobuf Editions](what-are-protobuf-editions.md) project plans to use [custom options](protobuf-editions-design-features.md) to model features and encourage language bindings to build custom features off options as well."
> - "While the proximal motivation for these options is for use with \"features\" in \"editions\", I believe they provide sufficient general utility that adding them directly to `FieldDescriptorOptions` is warranted."
> - "No directly relevant information"