---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/features]]"
  - "[[sources/editions]]"
  - "[[sources/proto3]]"
tags:
  - "term"
aliases:
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field_presence feature"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field presence"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
  - "field_presence feature"
  - "字段存在性特性"
  - "field presence feature"
  - "features.field_presence"
---

## Related Concepts
- [[concepts/edition|edition]]
- [[concepts/optional|optional]]
- [[concepts/field-cardinality|field cardinality]]
- [[concepts/implicit-field|implicit field]]
- [[concepts/features-default_symbol_visibility|features-default_symbol_visibility]]
- [[concepts/features-enforce_naming_style|features-enforce_naming_style]]
- [[concepts/packed-encoding|packed-encoding]]

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/protoc|protoc]]
- [[entities/prototiller|prototiller]]
- [[entities/google|google]]

## Mentions in Source
> **Source: [[sources/features|features]]**
> - "This feature sets the behavior for tracking field presence, or the notion of whether a protobuf field has a value."
> - "Values available: LEGACY_REQUIRED, EXPLICIT, IMPLICIT."
> - "LEGACY_REQUIRED: The field is required for parsing and serialization."
> - "After running Prototiller, the equivalent code might look like this:"

> **Source: [[sources/editions|editions]]**
> - "Proto3 implicit fields that have been migrated to editions will use the field_presence feature set to the IMPLICIT value."
> - "Proto2 required fields that have been migrated to editions will also use the field_presence feature, but set to LEGACY_REQUIRED."

> **Source: [[sources/proto3|proto3]]**
> - "An optional field is in one of two possible states: the field is set, and contains a value that was explicitly set or parsed from the wire... the field is unset, and will return the default value."
> - "In proto3, message-type fields already have field presence. Because of this, adding the optional modifier doesn't change the field presence for the field."
> - "If the field is not a message, it has two states: the field is set to a non-default (non-zero) value... the field is set to the default (zero) value."
> - "The field is set to the default (zero) value. It will not be serialized to the wire. In fact, you cannot determine whether the default (zero) value was set or parsed from the wire or not provided at all."

> **Source: [[sources/proto3|proto3]]** (no directly relevant information)