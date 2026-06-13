---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme|editions-readme]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
tags:
  - "standard"
aliases:
  - "Enum Field Closedness"
  - "Edition Zero Feature: Enum Field Closedness"
  - "枚举字段闭合性"
  - "legacy_treat_enum_as_closed"
  - "Enum Field Closedness"
  - "Edition Zero Feature: Enum Field Closedness"
  - "枚举字段闭合性"
---

## Related Concepts
- [[concepts/edition-zero-features|Edition Zero Features]]
- [[concepts/stricter-schemas-with-editions|Stricter Schemas with Editions]]
- [[concepts/protobuf-editions-for-schema|Protobuf Editions for Schema Producers]]
- [[concepts/feature-settings-for-editions|Feature Settings for Editions]]
- [[concepts/editions-language-guide|Protocol Buffers Editions 语言指南]]
- [[concepts/application-note-field-presence|Application note: Field presence]]
- [[concepts/open-enum|Open Enum]]
- [[concepts/proto3-enum|proto3 enum]]
- [[concepts/unknown-field-set|UnknownFieldSet]]
- [[concepts/legacy-treat-enum-as-closed|legacy_treat_enum_as_closed]]
- [[concepts/enum-field-closedness|Enum Field Closedness]]
- [[concepts/field-descriptor|FieldDescriptor]]
- [[concepts/edition-2023|Edition 2023]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/prototiller|Prototiller]]
- [[entities/mcy|@mcy]]

## Mentions in Source

> **Source: [[sources/editions-readme|editions-readme]]**
> - "The following topics are in this repository:"
> - "*   [Edition Zero Feature: Enum Field Closedness](edition-zero-feature-enum-field-closedness.md)"
> - "These are purely for historical value and should not be treated as documentation of the current state."

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "It turns out we misunderstood a critical corner-case of proto3 enums."
> - "This is because Protobuf sometimes implements the openness of an enum by its usage, *not* its definition."
> - "optional bool legacy_treat_enum_as_closed = ??? [retention = RUNTIME, target = FILE, target = FIELD];"
> - "Edition 2023 would set this to false by default, and proto2 would treat it as implicitly true."