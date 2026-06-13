---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/features]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
  - "[[protobuf/features.md]]"
  - "[[protobuf/editions.md]]"
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
tags:
  - "standard"
aliases:
  - "proto2"
  - "Protocol Buffers version 2"
  - "Protobuf 2"
---

## Related Concepts
- [[concepts/proto3|proto3]]
- [[concepts/edition-2024|edition-2024]]
- [[concepts/edition-2023|edition-2023]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]
- [[concepts/feature-inference|Feature Inference]]
- [[concepts/edition-proto2|EDITION_PROTO2]]
- [[concepts/field-cardinality|field-cardinality]]
- [[concepts/forward-compatibility|forward-compatibility]]
- [[concepts/backward-compatibility|backward-compatibility]]
- [[concepts/serialization|serialization]]
- [[concepts/proto-file|proto-file]]
- [[concepts/field-number|field-number]]
- [[concepts/features-field_presence|features-field_presence]]
- [[concepts/features-default_symbol_visibility|features-default_symbol_visibility]]
- [[concepts/optional|optional]]
- [[concepts/message|message]]
- [[concepts/field-presence|field-presence]]
- [[concepts/features|Features]]
- [[concepts/groups|groups]]
- [[concepts/packed|packed]]
- [[concepts/required|required]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/wire-format-compatibility|Wire Format Compatibility]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/editions-upgrader|Editions upgrader]]
- [[concepts/editions-adopter|Editions adopter]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/google|google]]
- [[entities/protoc|protoc]]
- [[entities/prototiller|prototiller]]
- [[entities/c++|C++]]
- [[entities/protobuf-team|Protobuf team]]
- [[entities/mkruskal-google|mkruskal-google]]

## Mentions in Source

> **Source: [[sources/overview|overview]]**
> - "When defining .proto files, you can specify cardinality (singular or repeated). In proto2 and proto3, you can also specify if the field is optional."
> - "For more information about the options available, see the language guide for proto2, proto3, or edition 2023."

> **Source: [[sources/features|features]]**
> - "Default behavior per syntax/edition: proto2 -> EXPORT_ALL"
> - "proto2 -> CLOSED (for enum_type)"
> - "proto2 -> EXPLICIT (for field_presence)"
> - "The following code sample shows a proto2 file: syntax "proto2""
> - "shows how to override the default behaviors so that your proto definition files act like proto2 or proto3 files."
> - "The following code sample shows a proto2 file: syntax = "proto2""
> - "proto2 CLOSED"

> **Source: [[sources/editions|editions]]**
> - "If no edition syntax is specified, the protocol buffer compiler will assume you are using proto2."
> - "Proto2 required fields that have been migrated to editions will also use the field_presence feature, but set to LEGACY_REQUIRED"

> **Source: [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]]**
> - "The first edition (colloquially known as "Edition Zero") will use features to unify proto2 and proto3 (Edition Zero Features)."
> - "There will be a large period of time during which `protoc` is able to consume `proto3`, `proto2`, and editions files."
> - "The protobuf team will provide a tool that upgrades `proto2` and `proto3` files to edition zero in a fully compatible way."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "Tooling that can take a `proto2` or `proto3` file and add `edition = "2023";` and `option features.* = ...;` as appropriate, so that each file retains its original behavior."
> - "Running `protoc --upgrade-edition -I... file.proto` figure out how to update `file.proto` from `proto2` or `proto3` to the latest edition, adding features as necessary."
> - "We also need to track down and upgrade (by hand) any code that is using the value of `syntax`."

> **Source: [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]**
> - "Since early in the design process, we've discussed the possibility of making proto2 and proto3 "special" editions"
> - "While the original plan was to keep editions and syntax orthogonal, that naively means we'd be supporting two very different codebases."
> - "If the file is proto2/proto3, failure should result in a fallback to the existing hardcoded defaults."