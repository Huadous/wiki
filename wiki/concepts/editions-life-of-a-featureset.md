---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
tags:
  - "method"
aliases:
  - "Editions: Life of a Featureset"
  - "特性集生命周期"
  - "Life of a Featureset"
  - "FeatureSet"
  - "Editions: Life of a Featureset"
  - "特性集生命周期"
  - "Life of a Featureset"
---

## Description
Editions: Life of a Featureset 聚焦于 FeatureSet 这一 Editions 的核心抽象单元，描述特性从提出、设计、实现、测试到发布的完整生命周期，并规定特性在后续 Edition 中如何演进、修改或被废弃。该文档详细说明了 edition 默认值如何通过 FeatureSet 机制传播到 generators 和 runtimes，从而取代原先直接检查语法的做法。在 Legacy Syntax Editions 提案中，这一机制被应用于 proto2/proto3——通过定义全局 feature set 来统一处理遗留语法，使代码无需直接判断语法版本。该机制还支持在 bootstrapping 场景下将默认值直接嵌入代码中。该概念与 [[concepts/life-of-an-edition|Life of an Edition]] 相辅相成，分别从特性级别和 Edition 级别两个维度描述 Editions 的演进机制。

## Related Concepts
- [[concepts/life-of-an-edition|Life of an Edition]]
- [[concepts/edition-evolution|Edition Evolution]]
- [[concepts/protobuf-editions-design-features|Protobuf Editions Design: Features]]
- [[concepts/editions-feature-visibility|Editions Feature Visibility]]
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/mkruskal-google|mkruskal-google]]

## Mentions in Source

> **Source: [[sources/editions-readme|editions-readme]]**
> - "The following topics are in this repository:"
> - "[Editions: Life of a Featureset](editions-life-of-a-featureset.md)"

> **Source: [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]**
> - "we recently redesigned editions to be represented as enums ([Edition Naming](edition-naming.md)), and also how edition defaults are propagated to generators and runtimes ([Editions: Life of a FeatureSet](editions-life-of-a-featureset.md))."
> - "We define global feature sets for proto2 and proto3, and try to use those internally instead of checking syntax directly."