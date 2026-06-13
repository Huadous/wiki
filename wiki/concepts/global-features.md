---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-life-of-an-edition]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
tags:
  - "term"
aliases:
  - "global feature"
  - "proto.Features"
  - "Global Feature"
  - "global feature"
  - "proto.Features"
---

## Related Concepts
- [[concepts/language-scoped-features|Language-scoped features]]
- [[concepts/feature|Feature]]
- [[concepts/edition-proclamation|Edition Proclamation]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/generator-features|Generator Features]]
- [[concepts/runtime-features|Runtime Features]]
- [[concepts/source-features|Source Features]]
- [[concepts/smooth-extension|Smooth Extension]]
- [[concepts/legacy-group-handling|Legacy group handling]]

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/descriptor-proto|descriptor.proto]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/edition-2023|Edition 2023]]

## Mentions in Source

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "Global features, which are the fields of `proto.Features`. In this document, we refer to them as `features.<name>`, e.g. `features.enum`."

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "Global features, which are the features contained directly in `FeatureSet` as fields. These apply to the protobuf language itself, rather than any particular runtime or generator."
> - "For global features, there's of course no issue (protoc has a bootstrapping setup for `descriptor.proto` and always knows the global feature set)."

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "Global Feature is a good long-term mitigation for tech debt we're leaving behind with Smooth Extension."
> - "The simplest answer here is to introduce a new global message feature `legacy_group_handling` to control all the changes we'd like."