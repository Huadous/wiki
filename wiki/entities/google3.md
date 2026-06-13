---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-group-migration-issues|editions-group-migration-issues]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "other"
aliases:
  - "Google monorepo"
  - "google3 codebase"
  - "Google3 内部代码库"
---

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/protocol-buffers|Protocol Buffers]]

## Related Concepts
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/group-fields|Group fields]]
- [[concepts/delimited-encoding|Delimited encoding]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/packed-encoding|packed encoding]]
- [[concepts/optional-keyword|optional keyword]]
- [[concepts/legacy-required|LEGACY_REQUIRED]]

## Mentions in Source

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "It was determined that this only affected a handful of protos in google3, and could probably be manually fixed as-needed."
> - "Java's handling changes the story significantly, since over 50% of protos in google3 produce generated Java code."

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "Migration will require deleting every instance of `optional` in proto files in google3, of which there are 385,236."
> - "Users explicitly enabled packed fields 12.3k times, but only explicitly disable it 200 times."