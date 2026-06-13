---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme|editions-readme]]"
  - "[[protobuf/editions-editions-feature-extension-layout.md]]"
tags:
  - "method"
aliases:
  - "Editions 特性扩展布局"
  - "Feature Extension Layout"
  - "Feature Extension"
  - "Editions 特性扩展布局"
  - "Feature Extension Layout"
---

## Description
Editions: Feature Extension Layout（Editions 功能扩展布局）文档聚焦于 Protobuf Editions 体系中特性扩展机制的底层数据结构布局。Protobuf Editions 的目标之一是允许添加非 protobuf 团队拥有的"更具针对性的特性"（more targeted features not owned by the protobuf team），而特性扩展机制正是实现这一目标的关键手段——它通过全局 features proto 的扩展（extensions of the global features proto）来承载这些新增特性。在布局层面，该文档关注特性数据在二进制存储、序列化和内存表示中的组织方式，直接影响 Editions 框架的可扩展性、运行效率以及向前向后兼容性。

该设计文档还需要解决一个核心的归属问题：特性扩展应当归运行时实现所有（如 C++、Java、Python、upb 等不同运行时各自维护独立的功能集），还是仅归代码生成器所有。这一归属策略的选择深刻地影响跨语言实现的一致性——若由运行时各自拥有，则不同语言实现可能演化出不同的特性集合；若仅由生成器拥有，则可以保证多语言和共享实现场景下的行为统一。功能扩展机制的灵活性允许不同实现拥有独立的功能集，但归属策略必须明确以确保行为一致性。该布局与 Editions Feature Visibility（特性可见性）形成互补：前者从内部表示角度定义特性机制，后者从外部暴露角度定义特性机制。

## Related Concepts
- Editions Feature Visibility — 见 [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]
- Protobuf Editions Features Design — 见 [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]
- Editions: Life of a FeatureSet — 见 [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]
- FeatureSet
- Runtime Implementation Features
- Generator Features
- Nested Features
- Protobuf Editions
- Feature Settings for Editions — 见 [[sources/features|features]]

## Related Entities
- [[entities/protocol-buffers-v3-15-0|protocol-buffers-v3-15-0]]
- [[entities/protocol-buffers-v3-12-0|protocol-buffers-v3-12-0]]

## Mentions in Source

> **Source: [[sources/editions-readme|editions-readme]]**
> - "[Editions: Feature Extension Layout](editions-feature-extension-layout.md)"
> - "The following topics are in this repository:"

> **Source: [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]**
> - "[What are Protobuf Editions](what-are-protobuf-editions.md) lays out a plan for allowing for more targeted features not owned by the protobuf team."
> - "It uses extensions of the global features proto to implement this."