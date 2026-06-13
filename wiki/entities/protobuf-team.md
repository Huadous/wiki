---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-edition-zero-converged-semantics.md]]"
tags:
  - "organization"
aliases:
  - "Protocol Buffers team"
  - "Protobuf 团队"
---

## Related Entities
- [[entities/google|Google]]
- [[entities/protoc|protoc]]
- [[entities/protobuf-runtime|protobuf-runtime]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/perezd|@perezd]]
- [[entities/haberman|@haberman]]
- [[entities/descriptor-proto|descriptor.proto]]

## Related Concepts
- [[concepts/features|Features]]
- [[concepts/editions|Editions]]
- [[concepts/large-scale-change|Large-Scale Change (LSC)]]
- [[concepts/feature-lifecycle|Feature Lifecycle]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/semantic-patch|Semantic Patch]]
- [[concepts/schema-producer|Schema Producer]]
- [[concepts/edition-proclamation|Edition Proclamation]]
- [[concepts/total-ordering-of-editions|Total Ordering of Editions]]
- [[concepts/converged-semantics|Converged Semantics]]
- [[concepts/edition-keyword|edition keyword]]
- [[concepts/features-option|features option]]
- [[concepts/proto2-proto3|proto2/proto3]]

## Mentions in Source
> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
- "This document reflects the approximate consensus of protobuf-team members who have been developing Protobuf Editions, but please beware: many open questions remain."
- "As stewards of the Protobuf language, we believe this is the best way to get rid of features that were a good idea at the time, but which history has shown to have had poor outcomes."
- "We will partner with use-cases that are known risks for migration, such as storage providers, to minimize toil and disruption on all sides."

> **Source: [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]]**
- "The protobuf team will provide a tool that upgrades `proto2` and `proto3` files to edition zero in a fully compatible way."
- "Protobuf team will investigate adding support for semantic patches when it addresses Bazel rules."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
- "Edition numbers are announced by protobuf-team, but not necessarily defined by us."
- "protobuf-team does not define editions, it only proclaims them."
- "We promise to proclaim an edition once per calendar year, even if first-party backends will not use it."

> **Source: [[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]**
- "The Protobuf Team has been exploring potential facilities for introducing breaking API and semantic changes."
- "Doing this in lockstep with the introduction of editions provides the protobuf team with a few valuable outcomes:"