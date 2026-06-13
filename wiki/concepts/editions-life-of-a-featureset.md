---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-editions-feature-extension-layout.md]]"
  - "[[protobuf/editions-edition-naming.md]]"
  - "[[protobuf/editions-edition-lifetimes.md]]"
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
- [[concepts/resolved-features|Resolved Features]]
- [[concepts/unresolved-features|Unresolved Features]]
- [[concepts/descriptor-api|Descriptor API]]
- [[concepts/feature-extension|Feature Extension]]
- [[concepts/nested-features|Nested Features]]
- [[concepts/edition-naming|Edition Naming]]
- [[concepts/proto-merging|Proto Merging]]
- [[concepts/edition-comparison|Edition Comparison]]
- [[concepts/dynamic-messages|Dynamic Messages]]
- [[concepts/feature-lifetime|Feature Lifetime]]
- [[concepts/featuresupport|FeatureSupport]]

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/mkruskal-google|mkruskal-google]]
- [[entities/protoc|protoc]]
- [[entities/descriptor-proto|descriptor.proto]]
- [[entities/upb|μpb]]
- [[entities/featureseteditiondefault|FeatureSetEditionDefault]]

## Mentions in Source

> **Source: editions-readme**
> - "The following topics are in this repository:"
> - "[Editions: Life of a Featureset](editions-life-of-a-featureset.md)"

> **Source: editions-legacy-syntax-editions**
> - "we recently redesigned editions to be represented as enums ([Edition Naming](edition-naming.md)), and also how edition defaults are propagated to generators and runtimes ([Editions: Life of a FeatureSet](editions-life-of-a-featureset.md))."
> - "We define global feature sets for proto2 and proto3, and try to use those internally instead of checking syntax directly."

> **Source: editions-editions-life-of-a-featureset**
> - "The features contained directly in FeatureSet as fields."
> - "Feature resolution for a given descriptor starts by using the proto file's edition and the feature schemas to generate the default feature set."

> **Source: editions-editions-feature-visibility**
> - "We recommend a conservative approach of hiding all `FeatureSet` protos from public APIs whenever possible. This means that there should be no public `features()` getter, and that features should be stripped from any descriptor options."
> - "Every descriptor is going to contain two separate features protos, and it's likely this will end up getting expensive as we roll out edition zero."

> **Source: editions-editions-feature-extension-layout**
> - "It uses extensions of the global features proto to implement this."
> - "Another option is to allow for shared feature set messages. For example, upb would define a feature message, but *not* make it an extension of the global `FeatureSet`."

> **Source: editions-edition-naming**
> - "One of the decisions in Editions: Life of a FeatureSet was that feature resolution would, at least partially, need to be duplicated across every supported language."
> - "As discussed in Life of a FeatureSet, the minimal operations we need to duplicate are edition comparison and proto merging."

> **Source: editions-edition-lifetimes**
> - "Specifically, we will add two new `FeatureSet` fields to `FeatureSetEditionDefault` in addition to the existing `features` field."
> - "overridable_features - The default values that users **are** allowed to override in a given edition"

> **Source: editions-edition-lifetimes**
> - "No directly relevant information"