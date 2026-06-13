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
  - "[[protobuf/editions-group-migration-issues.md]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-edition-zero-json-handling.md]]"
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
  - "edition zero"
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
Edition Zero is the foundational release of Protobuf Editions, conceived as the "completion" of the union of proto2 and proto3. It introduces a new syntax in which a `.proto` file declares `edition = "...";` and opts into behavior via explicit `features.*` settings rather than scattered language-level knobs. Crucially, Edition Zero is engineered so that any existing proto2 or proto3 file can be mechanically migrated to Edition Zero with no behavioral change — it does not alter runtime semantics, only the spelling and organization of declarations.

Beyond the syntactic unification, Edition Zero takes an opinionated stance: it selects "good" defaults and requires explicit opt-in for legacy "bad" semantics, gradually steering the ecosystem toward stricter, more round-trippable schemas. For example, Edition 2024 defaults to `STYLE2024` (enforcing naming style) and to `EXPORT_TOP_LEVEL` for symbol visibility, while older `EXPORT_ALL` behavior requires an override.

The release of Edition Zero, however, was not purely a matter of designing the syntax and feature set. It was originally hoped that proto2 and proto3 could be fully unified before Editions launched, but the team was blocked by certain internal use-cases — most notably the divergent behavior between proto2 and proto3 when handling JSON field-name conflicts. The proposed resolution is to unify these behaviors into a future-facing `json_format` feature as part of Edition Zero, so that conflicting semantics can be expressed explicitly per file instead of being silently inherited from the legacy syntax. This JSON-handling proposal sits alongside the broader Edition Zero featureset concerns (UTF-8 validation modeling, dual features protos in descriptors, migration tooling) that the team is working through.

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
- [[concepts/featureset|FeatureSet]]
- [[concepts/closed-enum|Closed Enum]]
- [[concepts/open-enum|Open Enum]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/.proto-file|.proto file]]
- [[concepts/wire-format-compatibility|Wire Format Compatibility]]
- [[concepts/json-format-feature|json_format feature]]
- [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]]

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/protoc|protoc]]
- [[entities/protobuf-team|protobuf-team]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/mkruskal-google|mkruskal-google]]

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
> - "No directly relevant information"

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "We'd likely have to wait until edition 2024"
> - "It allows us to release editions in a reasonable state, where we can fix these issues and release a more functional DELIMITED feature in 2024."
> - "No directly relevant information"

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "We've bounced back and forth on how UTF8 validation should be modeled as a feature. None of the proposals resulted in any functional changes, since edition zero preserves all proto2/proto3 behavior, the question was just about what features should be used to control them."
> - "every descriptor is going to contain two separate features protos, and it's likely this will end up getting expensive as we roll out edition zero."
> - "No directly relevant information"

> **Source: [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]**
> - "While we had hoped to unify these before Protobuf editions launched, we ended up blocked by some internal use-cases."
> - "The goal here is to unify these behaviors into a future-facing feature as part of edition zero."