---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/features.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
  - "[[protobuf/editions-edition-naming.md]]"
tags:
  - "term"
aliases:
  - "open enum"
  - "开放式枚举"
---

## Related Concepts
- [[concepts/closed-enum|Closed Enum]]
- [[concepts/feature|Feature]]
- [[concepts/proto3|Proto3]]
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/edition-2024|Edition 2024]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/enum-field-closedness|Enum Field Closedness]]
- [[concepts/legacy-treat-enum-as-closed|Legacy Treat Enum As Closed]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]

## Mentions in Source
> **Source: [[sources/editions-what-are-protobuf-editions]]**
> - "whether values not specified in an enum go into unknown fields vs producing an enum value outside of the bounds of the specified values in the .proto file (i.e., so-called closed and open enums) will be controlled by feature.enum = OPEN or feature.enum = CLOSED."

> **Source: [[sources/features]]**
> - "OPEN: Open enums parse out of range values into their fields directly."
> - "This feature sets the behavior for how enum values that aren't contained within the defined set are handled. See Enum Behavior for more information on open and closed enums."

> **Source: [[sources/editions-edition-zero-features]]**
> - "An **open enum** does not have this restriction, and is just an `int32` field with well-known values."
> - "*open* enums will parse out of range values into their fields directly."
> - "In proto3, `enum` values are open and the first `enum` value must be zero."

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness]]**
> - "All enums treated as open"
> - "we don't want to add more special cases"

> **Source: [[sources/editions-edition-naming]]**
> - "Ideally, this would be an open enum to avoid ever having the edition thrown into the unknown field set."
> - "However, since it needs to exist in `descriptor.proto`, we won't be able to make it open until the end of our edition zero migration."