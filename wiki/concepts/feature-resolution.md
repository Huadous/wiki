---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-legacy-syntax-editions]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
tags:
  - "method"
aliases:
  - "feature resolution"
  - "功能解析"
---

## Related Concepts
- [[concepts/FeatureSet|FeatureSet]]
- [[concepts/Feature Inference|Feature Inference]]
- [[concepts/Bootstrapping|Bootstrapping]]
- [[concepts/Serialized Descriptors|Serialized Descriptors]]
- [[concepts/Legacy Syntax Editions|Legacy Syntax Editions]]
- [[concepts/Edition Defaults|Edition Defaults]]
- [[concepts/Editions|Editions]]
- [[concepts/Descriptor Pool|Descriptor Pool]]
- [[concepts/Hyrum's Law|Hyrum's Law]]

## Related Entities
- [[entities/descriptor.proto|descriptor.proto]]
- [[entities/protoc|protoc]]

## Mentions in Source

> **Source: [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]**
> - "In order to avoid blocking edition zero for that long, we may need fallbacks in protoc for the case where feature resolution *fails*."
> - "If the file is proto2/proto3, failure should result in a fallback to the existing hardcoded defaults."
> - "Editions: Life of a FeatureSet"（作为 Feature Resolution 所关联的 FeatureSet 生命周期阶段名称）

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "Feature resolution - The process of applying the algorithm laid out in Protobuf Editions Design: Features."
> - "The flaw that all of these design documents suffer from is that protoc can't be the universal source-of-truth for feature resolution under the original design."