---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/features.md]]"
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

## Related Entities

- [[entities/protocol-buffers|Protocol Buffers]]

## Mentions in Source

> **Source: [[sources/editions-what-are-protobuf-editions]]**
> - "whether values not specified in an enum go into unknown fields vs producing an enum value outside of the bounds of the specified values in the .proto file (i.e., so-called closed and open enums) will be controlled by feature.enum = OPEN or feature.enum = CLOSED."

> **Source: [[sources/features]]**
> - "OPEN: Open enums parse out of range values into their fields directly."
> - "This feature sets the behavior for how enum values that aren't contained within the defined set are handled. See Enum Behavior for more information on open and closed enums."