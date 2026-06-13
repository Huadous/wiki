---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme|editions-readme]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-edition-lifetimes.md]]"
tags:
  - "term"
aliases:
  - "Editions 特性可见性"
  - "Editions Feature Visibility"
---

## Description
Editions Feature Visibility 是一项面向 Protobuf Editions 生态的设计原则，旨在通过在公共 API 层隐藏 edition 概念本身来降低使用者的认知负担。该决策主张采取保守策略：尽量将 `FeatureSet` 协议类型隐藏在运行时与插件的内部实现中，使其不作为面向用户的稳定 API 出现。一旦 edition 在绝大多数用户路径中不再可见，针对旧版 edition 发布补丁（例如通过 `edition_patch` 字段）并将补丁机制推广到各语言的 protoc 插件，其工程代价与兼容性风险都会显著下降。配合"补丁不引入或移除特性、也不更改特性默认值"的约束，`protoc` 与各插件可以始终使用它们所知的最新补丁号来表示对应 edition，从而让 edition 的生命周期管理更加平滑。这项设计也与 [[concepts/feature-set-protos|FeatureSet]] 的内部化使用以及 [[concepts/resolved-features|Resolved Features]] / [[concepts/unresolved-features|Unresolved Features]] 的概念分层紧密相关。

## Related Concepts
- [[concepts/editions-feature-extension-layout|Editions: Feature Extension Layout]]
- [[concepts/editions-design-features|Protobuf Editions Design: Features]]
- [[concepts/editions-life-of-a-featureset|Editions: Life of a Featureset]]
- [[concepts/feature-set-protos|FeatureSet]]
- [[concepts/resolved-features|Resolved Features]]
- [[concepts/unresolved-features|Unresolved Features]]
- [[concepts/descriptor-api|Descriptor API]]
- [[concepts/hyrums-law|Hyrum's Law]]
- [[concepts/editions|Editions]]
- [[concepts/edition-patches|Edition Patches]]
- [[concepts/edition-naming|Edition Naming]]

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/upb|μpb]]
- [[entities/protobuf|Protobuf]]

## Mentions in Source

> **Source: [[sources/editions-readme|editions-readme]]**
> - "The following topics are in this repository:"
> - "Editions Feature Visibility (editions-feature-visibility.md)"

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "This is a much more targeted document laying out how features should be treated by runtimes."
> - "We recommend a conservative approach of hiding all `FeatureSet` protos from public APIs whenever possible."

> **Source: [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]**
> - "given that we've hidden the edition from most users ([Editions Feature Visibility](editions-feature-visibility.md)) it shouldn't be too bad."
> - "As long as patches never introduce or remove features or change their defaults, protoc and plugins can always use the latest patch they know about to represent that edition."