---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-editions-life-of-a-featureset]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
tags:
  - "term"
aliases:
  - "Unresolved features"
  - "未解析特性"
---

## Related Concepts
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/resolved-features|Resolved Features]]
- [[concepts/source-features|Source Features]]
- [[concepts/runtime-features|Runtime Features]]
- [[concepts/option-retention|Option Retention]]
- [[concepts/feature-set|FeatureSet]]
- [[concepts/editions-feature-visibility|Editions Feature Visibility]]
- [[concepts/hyrums-law|Hyrum's Law]]

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/editions|Editions]]

## Mentions in Source
- **Unresolved features** - The features a user has explicitly set on their descriptors in the `.proto` file. These have not gone through feature resolution and are a minimal representation that require more knowledge to be useful. — [[sources/editions-editions-life-of-a-featureset]]

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "Unresolved features represent a clear foot-gun for users, that could also cause issues for us. Since they share the same type as resolved features, it's not always easy to tell the two apart."
> - "If people have easy access to unresolved features though, we can expect a lot of Hyrum's law issues slowing down these large-scale changes."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - No directly relevant information