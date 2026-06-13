---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme|Protobuf Editions 设计文档索引]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "standard"
aliases:
  - "Edition 命名规范"
  - "Edition Naming Rules"
---

## Related Concepts
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/edition-evolution|Edition Evolution]]
- [[concepts/life-of-an-edition|Life of an Edition]]
- [[concepts/total-ordering-of-editions|Total Ordering of Editions]]
- [[concepts/edition-proclamation|Edition Proclamation]]
- [[concepts/protobuf-editions|Protobuf Editions]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protobuf-editions|Protobuf Editions]]

## Mentions in Source
> **Source: [[sources/editions-readme|Protobuf Editions 设计文档索引]]**
> - "The following topics are in this repository:"
> - "[Edition Naming](edition-naming.md)"
> - "This directory contains historical design documents that describe plans for implementing Protobuf Editions."

> **Source: [[sources/editions-life-of-an-edition|Life of an Edition]]**
> - "(**Note:** The above edition ordering is updated in [Edition Naming](edition-naming.md).)"
> - "The total order is thus: the edition string is split on `'.'`. Each component is then ordered by `a.len < b.len && a < b`. This ensures that `9 < 10`, for example."

> **Source: [[sources/editions-life-of-an-edition|Life of an Edition]]**
> - No directly relevant information