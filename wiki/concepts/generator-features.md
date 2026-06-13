---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-editions-life-of-a-featureset]]"
  - "[[protobuf/editions-editions-feature-extension-layout.md]]"
tags:
  - "term"
aliases:
  - "Generator Features"
  - "生成器特性"
---

## Related Concepts
- [[concepts/feature-set|FeatureSet]]
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/global-features|Global Features]]
- [[concepts/source-features|Source Features]]
- [[concepts/runtime-features|Runtime Features]]
- [[concepts/edition-defaults|Edition Defaults]]
- [[concepts/feature-extension|Feature Extension]]

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/code-generator|CodeGenerator]]

## Mentions in Source
- **Generator features** - Extensions of `FeatureSet` owned by a specific runtime or generator. — [[sources/editions-editions-life-of-a-featureset]]
- For generator features though, we depend on [imports to make them discoverable](protobuf-editions-design-features.md#specification-of-an-edition). — [[sources/editions-editions-life-of-a-featureset]]

> **Source: [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]**
> - "Features would be per-generator only (i.e. each protoc plugin would own one set of features)."
> - "For example, all Python implementations would share the same set of features (e.g. `features.(pb.python).<feature>`). However, certain features could be targeted to specific implementations (e.g. `features.(pb.python).upb_utf8_validation` would only be used by Python/upb)."