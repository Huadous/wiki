---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
tags:
  - "term"
aliases:
  - "已解析特性"
  - "Resolved Features"
---

## Related Concepts
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/unresolved-features|Unresolved Features]]
- [[concepts/edition-defaults|Edition Defaults]]
- [[concepts/hyrums-law|Hyrum's Law]]
- [[concepts/feature-set|FeatureSet]]
- [[concepts/editions-feature-visibility|Editions Feature Visibility]]
- [[concepts/descriptor-api|Descriptor API]]

## Related Entities
- [[entities/editions|Editions]]

## Mentions in Source
> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "**Resolved features** - Features that have gone through feature resolution, with defaults and inheritance applied. These are the only feature sets that should be used to make decisions."
> - "Resolved feature sets will never be publicly exposed"

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "While runtime decisions *should* be made based on the data in these protos, their struct-like nature makes them very rigid."
> - "We *expect* that people are only making decisions based on resolved features, and therefore that Prototiller transformations are behavior-preserving (despite changing the unresolved features)."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "No directly relevant information"