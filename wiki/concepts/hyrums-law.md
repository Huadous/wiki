---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-edition-naming.md]]"
tags:
  - "theory"
aliases:
  - "海勒姆定律"
  - "Hyrum's Law"
---

## Related Concepts
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/unresolved-features|Unresolved Features]]
- [[concepts/editions-feature-visibility|Editions Feature Visibility]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/edition-naming|Edition Naming]]
- [[concepts/edition-enum|Edition enum]]

## Related Entities
无

## Mentions in Source
> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "Users will only be exposed to them indirectly, via codegen changes or runtime helper functions, in order to avoid Hyrum's law cementing every decision we make about them."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "If people have easy access to unresolved features though, we can expect a lot of Hyrum's law issues slowing down these large-scale changes."
> - "Deciding to loosen this in the future would be a bit awkward for `options()`. If we stop stripping it, people will suddenly start seeing a new field and Hyrum's law might result in breakages."

> **Source: [[sources/editions-edition-naming|editions-edition-naming]]**
> - "There's also a very real Hyrum's law risk when we permit an infinite number of edition names that we never expect to exist in practice."
> - "Leaves us open to Hyrum's law and unexpected abuse"