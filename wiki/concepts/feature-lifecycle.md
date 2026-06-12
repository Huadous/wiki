---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
tags:
  - "method"
aliases:
  - "特性生命周期"
  - "特性演化流程"
---

## 相關概念
- [[concepts/Features]]
- [[concepts/Editions]]
- [[concepts/Feature Inheritance]]
- [[concepts/Language-scoped features]]
- [[concepts/LSC|LSC]]

## 相關實體
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protoc|Protoc]]
- [[entities/protobuf-team|protobuf-team]]

## 來源提及

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
- "Edition "2025" creates features.(pb.cpp).opaque_repeated_fields with a default value of false."
- "Edition "2027" switches the default of features.(pb.cpp).opaque_repeated_fields to true."
- "The key point to note here is that any `.proto` file that does not use deprecated features has a no-op upgrade from one edition to the next and we will provide tools to effect that upgrade."
- "Internal users will be migrated centrally before a feature is deprecated. External users will have the full window of the Google migration as well as the deprecation window to upgrade their own code."