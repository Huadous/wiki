---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme|Protobuf Editions 设计文档索引]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-edition-naming.md]]"
  - "[[protobuf/editions-edition-evolution.md]]"
  - "[[protobuf/editions-edition-lifetimes.md]]"
tags:
  - "standard"
aliases:
  - "Edition 命名规范"
  - "Edition Naming Rules"
---

## Description
Edition Naming 是 Protobuf Editions 体系中的核心设计决策文档之一，确立了一套由 Protobuf 团队自有定义、更加严格的版本命名方案。该文档的诞生源于对早期提案的反思与简化——许多最初围绕 Editions 的构想，在 Edition Naming 中被进一步收紧和明确化。此外，Edition Naming 还做出了一个重要决定：放弃"补丁版本"（patch edition）这一概念，理由是 Editions 在前后兼容性上始终是无缝的，因此不需要单独的补丁级别。这一简化直接影响了后续关于特性生命周期和版本生命周期的设计思路，使 Editions 演进模型更加清晰和一致。

## Related Concepts
- [[concepts/life-of-an-edition|Life of an Edition]]
- [[concepts/editions|Editions]]
- [[concepts/edition-patches|Edition Patches]]
- [[concepts/edition-lifetimes|Edition Lifetimes]]
- [[concepts/featureset-lifecycle|FeatureSet Lifecycle]]

## Related Entities
- [[entities/protobuf|Protobuf]]

## Mentions in Source
> **Source: [[sources/editions-edition-naming|editions-edition-naming]]**
> - "Many of the ideas around editions have since been simplified in [Edition Naming](edition-naming.md), where we opted for a stricter naming scheme owned and defined by us." — [[sources/editions-edition-naming|editions-edition-naming]]
> - "In [Edition Naming](edition-naming.md) we decided to drop the idea of "patch" editions, because editions were always forward and backward compatible." — [[sources/editions-edition-naming|editions-edition-naming]]

> **Source: [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]**
> - "Many of the ideas around editions have since been simplified in [Edition Naming](edition-naming.md), where we opted for a stricter naming scheme owned and defined by us." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
> - "In [Edition Naming](edition-naming.md) we decided to drop the idea of "patch" editions, because editions were always forward and backward compatible." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]