---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-protobuf-editions-design-features.md]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
tags:
  - "method"
aliases:
  - "特性继承"
  - "Feature Inheritance"
  - "inheritance"
---

## Related Concepts

- [[concepts/Features|Features]] — 特性系统的整体框架
- [[concepts/Editions|Editions]] — 版本管理机制
- [[concepts/Field Presence|Field Presence]] — 字段存在性特性
- [[concepts/Target Attributes|Target Attributes]] — 继承机制应用的目标属性
- [[concepts/Options Attributes|Options Attributes]] — `target` 与 `retention` 属性设计提案中定义的 option 属性机制

## Related Entities

- [[entities/protobuf-team|protobuf-team]] — Protobuf 设计团队
- [[entities/protobuf-runtime|protobuf-runtime]] — Protobuf 运行时
- [[entities/editions-what-are-protobuf-editions|Protobuf Editions]] — 该机制所属的版本系统

## Mentions in Source

> **Source: [[sources/editions-what-are-protobuf-editions|Protobuf Editions 介绍文档]]**
> - "This is called feature inheritance, and applies recursively."
> - "Inheritance is intended to allow us to factor frequently-occurring feature declarations, minimizing clutter during migrations."
> - "If a syntax entity's lexical parent has a particular value for a feature, then the child has the same value, unless the feature has a new value specified on the child, explicitly."

> **Source: [[sources/editions-protobuf-editions-design-features|Protobuf Editions Features Design]]**
> - "To support inheritance, we will specify a single `Features` message that extends every kind of option"
> - "At the implementation level, feature inheritance is exactly the behavior of `MergeFrom`"

> **Source: [[sources/editions-protobuf-design-options-attributes|Protobuf Editions Options Attributes Design]]**
> - "In the initial design `target` was serving the dual purpose of identifying the semantic entity, and also the granularity of inheritance for features."
> - "Features will be able to be set on both the `FILE` level and their semantic entity."