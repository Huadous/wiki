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
  - "[[protobuf/editions-group-migration-issues.md]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-edition-zero-json-handling.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
  - "[[protobuf/editions-cpp-apis-for-edition-zero.md]]"
tags:
  - "standard"
aliases:
  - "proto2"
  - "Protocol Buffers version 2"
  - "Protobuf 2"
  - "proto2 syntax"
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
- [[concepts/smooth-extension|Smooth Extension]]
- [[concepts/text-format|text format]]
- [[concepts/group-like-fields|group-like fields]]
- [[concepts/group-fields|group fields]]
- [[concepts/legacy-best-effort|LEGACY_BEST_EFFORT]]
- [[concepts/json-format-feature|json_format feature]]
- [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]]
- [[concepts/enum-type|enum_type]]
- [[concepts/repeated-field-encoding|repeated_field_encoding]]
- [[concepts/defaulted|defaulted]]
- [[concepts/extensions|extensions]]
- [[concepts/legacy-treat-enum-as-closed|legacy_treat_enum_as_closed]]
- [[concepts/enum-field-closedness|Enum Field Closedness]]
- [[concepts/field-descriptor|FieldDescriptor]]
- [[concepts/file-descriptor|FileDescriptor]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/google|google]]
- [[entities/protoc|protoc]]
- [[entities/prototiller|prototiller]]
- [[entities/c++|C++]]
- [[entities/java|Java]]
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

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "Proto2 splits groups into a synthetic nested message with a type name equivalent to the group specification (required to be capitalized), and a field name that's fully lowercased."
> - "Note that proto2 groups will *always* be 'group-like.'"

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "We've bounced back and forth on how UTF8 validation should be modeled as a feature. None of the proposals resulted in any functional changes, since edition zero preserves all proto2/proto3 behavior, the question was just about what features should be used to control them."

> **Source: [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]**
> - "Today, proto3 fully validates JSON mappings for uniqueness during parsing, while proto2 takes a best-effort approach and allows cases that don't have a 1:1 mapping."
> - "Proto2 files will only fail to parse if both of the conflicts fields have `json_name` set"

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "In proto2, `enum` values are closed and no requirements are placed upon the first `enum` value."
> - "Proto2 has `required` but not `defaulted`; Proto3 has `defaulted` but not `required`."
> - "Groups. Proto2 has groups, proto3 does not."

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "syntax = "proto2";"
> - "proto2 would treat it as implicitly true."
> - "file().syntax() == FileDescriptor::SYNTAX_PROTO2"
> - "the proto compiler rejects proto2-enum-valued fields in proto3 messages, because such enums can have nonzero defaults, which proto3 does not support due to implicit presence."

> **Source: [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]**
> - "existing usage checks `syntax() == PROTO3` to determine if enums are open."
> - "Identifying what proto2/proto3 distinction is being picked up on, among the following: 1. UTF-8 verification on parse (use new API). 2. Closed/open enum (use new API)."