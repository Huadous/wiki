---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
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

## Related Concepts
- [[concepts/life-of-an-edition|Life of an Edition]]
- [[concepts/edition-evolution|Edition Evolution]]
- [[concepts/protobuf-editions-design-features|Protobuf Editions Design: Features]]
- [[concepts/editions-feature-visibility|Editions Feature Visibility]]
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/option-retention|Option Retention]]
- [[concepts/global-features|Global Features]]
- [[concepts/generator-features|Generator Features]]
- [[concepts/runtime-features|Runtime Features]]
- [[concepts/source-features|Source Features]]

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/mkruskal-google|mkruskal-google]]
- [[entities/protoc|protoc]]
- [[entities/descriptor-proto|descriptor.proto]]

## Mentions in Source

> **Source: [[sources/editions-readme|editions-readme]]**
> - "The following topics are in this repository:"
> - "[Editions: Life of a Featureset](editions-life-of-a-featureset.md)"

> **Source: [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]**
> - "we recently redesigned editions to be represented as enums ([Edition Naming](edition-naming.md)), and also how edition defaults are propagated to generators and runtimes ([Editions: Life of a FeatureSet](editions-life-of-a-featureset.md))."
> - "We define global feature sets for proto2 and proto3, and try to use those internally instead of checking syntax directly."

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "The features contained directly in FeatureSet as fields."
> - "Feature resolution for a given descriptor starts by using the proto file's edition and the feature schemas to generate the default feature set."