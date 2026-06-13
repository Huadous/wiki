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
FeatureSet 是 Protocol Buffers Editions 体系的核心概念，用以统一描述 proto 文件及其描述符所启用的各项功能特性。其生命周期由《Editions: Life of a FeatureSet》文档详述：从给定描述符的特征解析开始，系统根据 proto 文件的 edition 与 feature schema 生成默认 feature set，并进一步在嵌套与扩展场景中进行合并与解析。FeatureSet 既作为全局特性容器存在（global features），也被生成器（generator features）、运行时（runtime features）以及源码（source features）分别消费，并通过 resolved features / unresolved features 的划分反映解析结果的多阶段特征。在 API 设计层面，推荐保守策略——尽可能将 FeatureSet 消息从公共 API 中隐藏，避免暴露 `features()` getter 并在描述符选项中剥离 features，但每个描述符仍会保留两份独立的 features proto，这在 Edition Zero 推广时可能带来性能开销。实现上可通过全局 FeatureSet proto 的扩展（extensions）或定义独立的 feature 消息（如 μpb 的做法）来支撑跨语言复用。值得注意的是，《Editions: Life of a FeatureSet》指出 feature resolution 至少需要在每种支持语言中部分重复实现，而所需的最小操作集是 edition 比较（edition comparison）与 proto 合并（proto merging）——这一决策正是 Edition 命名从宽松字符串转向枚举类型的核心动机，因为枚举可显著简化跨语言的 edition 比较实现。

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
- [[concepts/feature-set|FeatureSet]]
- [[concepts/edition-naming|Edition Naming]]

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/mkruskal-google|mkruskal-google]]
- [[entities/protoc|protoc]]
- [[entities/descriptor-proto|descriptor.proto]]
- [[entities/upb|μpb]]

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