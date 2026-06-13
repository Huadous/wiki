---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
tags:
  - "method"
aliases:
  - "EditionDefault"
  - "版本默认值算法"
---

## Related Concepts
- [[concepts/editions|Editions]]
- [[concepts/features|Features]]
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/feature-resolution|Feature Resolution]] *(referenced in source)*
- [[concepts/featureset|FeatureSet]] *(referenced in source)*

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protoc|protoc]] *(referenced in source)*

## Mentions in Source

> **Source: [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]**
> - "To build the edition defaults for a particular edition `current` in the context of a particular file `foo.proto`, we execute the following algorithm —"
> - "Binsearch for the latest edition in `defaults` that is earlier or equal to `current`."

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "the calculation of edition defaults is by far the most complicated piece of feature resolution"
> - "Editions: Runtime Feature Set Defaults was a follow-up attempt to specifically handle the default feature sets of an edition."
> - "No directly relevant information"