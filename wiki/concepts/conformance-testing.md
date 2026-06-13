---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
tags:
  - "method"
aliases:
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
  - "Conformance tests"
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
  - "Conformance test"
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
  - "Conformance tests"
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
  - "conformance test"
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
  - "Conformance tests"
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
  - "Conformance test"
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
  - "Conformance tests"
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
---

## Related Concepts
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/group-fields|Group Fields]] *(implied by group migration context — link deferred until page exists)*
- [[concepts/smooth-extension|Smooth Extension]] *(implied by Smooth Extension 方案 — link deferred until page exists)*
- [[concepts/text-format|Text Format]] *(implied by text-format 往返行为 — link deferred until page exists)*
- [[concepts/feature-visibility|Feature Visibility]] *(implied by Editions Feature Visibility 上下文 — link deferred until page exists)*
- [[concepts/open-enum|Open Enum]] *(implied by Enum Field Closedness 上下文 — link deferred until page exists)*
- [[concepts/enum-field-closedness|Enum Field Closedness]] *(implied by Edition Zero 枚举封闭性上下文 — link deferred until page exists)*
- [[concepts/legacy-treat-enum-as-closed|legacy_treat_enum_as_closed]] *(implied by 过渡期逐语言演进策略 — link deferred until page exists)*
- [[concepts/edition-zero-features|Edition Zero Features]] *(implied by edition zero features 落地实践 — link deferred until page exists)*

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/protocol-buffers|Protocol Buffers]]

## Mentions in Source

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "Code duplication means that we need a test strategy for making sure everyone stays conformant."
> - "Our current conformance tests provide a good model for accomplishing this, even though they don't quite fit the problem (they're designed for parsing/serialization)."

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "We also have conformance tests locking down the positive path here (i.e. using the message name round-trip)."
> - "The negative path (i.e. failing to accept the field name) doesn't have a conformance test, but C++/Java/Python all agree and there's no known case that doesn't."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "Requires duplicating high-level feature behaviors across every language. For example, `has_presence` will need to be implemented identically in every language. We will likely need some kind of conformance test to make sure these all agree."
> - "This has already been done for edition zero features (e.g. `has_presence`, `requires_utf8_validation`, etc), and we should continue this model."

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "Define the official behavior to be \"Enums open-ness should be defined by the definition of the enum.\" Add a conformance test for this behavior. Use per language features to eventually converge implementations that are out of conformance."
> - "Given the wide variety of behavior in different languages, a singular global setting will always leave some of our languages in the lurch. As such, we will use per language features to allow each language to control its own evolution while we define the \"correct" behavior."

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "No directly relevant information"