---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
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

## Related Entities

- [[entities/protobuf-team|protobuf-team]] — Protobuf 设计团队
- [[entities/protobuf-runtime|protobuf-runtime]] — Protobuf 运行时
- [[entities/editions-what-are-protobuf-editions|Protobuf Editions]] — 该机制所属的版本系统

## Mentions in Source

> **Source: [[sources/editions-what-are-protobuf-editions|Protobuf Editions 介绍文档]]**
> - "This is called feature inheritance, and applies recursively."
> - "Inheritance is intended to allow us to factor frequently-occurring feature declarations, minimizing clutter during migrations."
> - "If a syntax entity's lexical parent has a particular value for a feature, then the child has the same value, unless the feature has a new value specified on the child, explicitly."