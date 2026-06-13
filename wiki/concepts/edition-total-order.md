---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-minimum-required-edition|editions-minimum-required-edition]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-edition-evolution.md]]"
tags:
  - "method"
aliases:
  - "Edition 全序比较"
  - "edition_less_than"
  - "Edition Total Order"
  - "Total Ordering of Editions"
  - "Edition 全序比较"
  - "edition_less_than"
  - "Edition Total Order"
---

## Related Concepts
- [[concepts/edition|Edition]]
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/edition-proclamation|Edition Proclamation]]
- [[concepts/build-horizon|Build Horizon]]
- [[concepts/backend-features|Backend Features]]
- [[concepts/protobuf-features|Protobuf Features]]

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protoc|protoc]]

## Mentions in Source
> **Source: [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]**
> - "Less than" is defined per the edition total order given in [Life of an Edition](life-of-an-edition.md). To restate it, it is the following algorithm:

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - However, protobuf-team does not define editions, it only proclaims them. Third-party backends are responsible for changing defaults across editions. To minimize the amount of synchronization, we introduce a total order on editions.
> - The total order is thus: the edition string is split on '.'. Each component is then ordered by a.len < b.len && a < b. This ensures that 9 < 10, for example.

> **Source: [[sources/editions-edition-evolution|editions-edition-evolution]]**
> - We propose defining a *total order* on editions. This means that a backend can pick the default not by looking at the edition, but by asking "is this proto older than this edition, where I introduced this default?"
> - The total order is thus: the edition string is split on `'.'`. Each component is then ordered by `a.len < b.len && a < b`. This ensures that `9 < 10`, for example.