---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "organization"
aliases:
  - "Protocol Buffers team"
  - "Protobuf 团队"
---

## Description
protobuf-team 是 Google 内部负责开发与维护 Protobuf 生态系统的团队，也是 Protobuf Editions 的核心推动者。作为 Protobuf 语言的"stewards"（管理者），该团队主导移除历史上产生过不良后果的特性，并与存储提供商等高风险迁移用例合作以减少双方负担。同时，团队承诺提供将 `proto2` 和 `proto3` 文件完全兼容地升级到 edition zero 的工具。

在 Editions 的生命周期管理中，protobuf-team 扮演"宣告者"而非"定义者"的角色：版本号（edition numbers）由该团队宣布，但具体版本的定义可能并非由其完成。团队承诺每个日历年至少宣告一个 edition，即使 first-party backends 暂时不会使用该版本，以此保证 Editions 时间线的连续性与有序推进。

## Related Entities
- [[entities/google|Google]]
- [[entities/protoc|protoc]]
- [[entities/protobuf-runtime|protobuf-runtime]]
- [[entities/protobuf-editions|Protobuf Editions]]

## Related Concepts
- [[concepts/features|Features]]
- [[concepts/editions|Editions]]
- [[concepts/large-scale-change|Large-Scale Change (LSC)]]
- [[concepts/feature-lifecycle|Feature Lifecycle]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/semantic-patch|Semantic Patch]]
- [[concepts/schema-producer|Schema Producer]]
- Edition Proclamation
- Total Ordering of Editions

## Mentions in Source
> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
- "This document reflects the approximate consensus of protobuf-team members who have been developing Protobuf Editions, but please beware: many open questions remain."
- "As stewards of the Protobuf language, we believe this is the best way to get rid of features that were a good idea at the time, but which history has shown to have had poor outcomes."
- "We will partner with use-cases that are known risks for migration, such as storage providers, to minimize toil and disruption on all sides."

> **Source: [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]]**
- "The protobuf team will provide a tool that upgrades `proto2` and `proto3` files to edition zero in a fully compatible way."
- "Protobuf team will investigate adding support for semantic patches when it addresses Bazel rules."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
- "Edition numbers are announced by protobuf-team, but not necessarily defined by us."
- "protobuf-team does not define editions, it only proclaims them."
- "We promise to proclaim an edition once per calendar year, even if first-party backends will not use it."