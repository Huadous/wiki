---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "method"
aliases:
  - "Protobuf OSS Strategy"
  - "开源策略"
  - "The OSS Story"
  - "Protobuf OSS Strategy"
  - "开源策略"
---

## Description
OSS Strategy 是 Protocol Buffers 团队针对开源生态环境的迁移推广策略，其背景在于 Google 内部可以依靠全局审批（global approvals）和"行政大棒"（bureaucratic sticks）来强制推动大规模变更，但 OSS 环境既无审批机构（no "global approval" or "TAP" for OSS），也缺乏强制力，因此必须另辟蹊径。该策略的核心理念是"胡萝卜加大棒"：用破坏性变更作为推动力（the only stick we have is breaking changes），用新特性作为吸引力（the only carrots we can offer are new features）。在执行层面，团队需要"export"内部的大规模变更到开源生态中，以避免 Editions 割裂生态（have any hope of editions not splitting the ecosystem）。

具体策略包括多个层面：通过 protoc 诊断和编辑器集成温和引导用户进入新 edition；为第三方后端（如 Apple 的 Swift）设计有吸引力的迁移路径；提供 Google 级迁移工具（如 features GC 以及 editions adopter/upgrader）；明确告知破坏性变更政策。沟通规划同样至关重要，文档明确参考了 Go 的 `go fix`、Rust 的 `rustfix`，以及 Carbon 团队关于"升级是生活常态"的公开表态，强调发布迁移指南、提供公开迁移工具（如 `proto2`/`proto3` -> `edition` migrator）以及为第三方代码生成器提供支持的必要性。

## Related Concepts
- [[concepts/Edition|Edition]]
- [[concepts/Feature Lifecycle|Feature Lifecycle]]
- [[concepts/Incremental Migration|Incremental Migration]]
- [[concepts/Feature Deprecation Window|Feature Deprecation Window]]
- [[concepts/Edition Proclamation|Edition Proclamation]]
- [[concepts/Large-scale Change|Large-scale Change]]
- [[concepts/Feature Lifetime|Feature Lifetime]]
- [[concepts/Edition Zero|Edition Zero]]
- [[concepts/Features GC|Features GC]]
- [[concepts/Editions Adopter|Editions Adopter]]
- [[concepts/Editions Upgrader|Editions Upgrader]]

## Related Entities
- [[entities/protobuf-team|protobuf-team]]
- [[entities/Google|Google]]
- [[entities/protoc|protoc]]
- [[entities/Carbon|Carbon]]

## Mentions in Source
> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "We want to share a variant of this document with the OSS community."
> - "We plan to publish migration guides and, where feasible, any migration tooling, such as the `proto2`/`proto3` -> `edition` migrator."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "We need to export our large-scale changes into open source to have any hope of editions not splitting the ecosystem. It is impossible to do this the way we do large-scale changes in our internal codebase, where we have global approvals and a finite but nonzero supply of bureaucratic sticks to motivate reluctant users."
> - "In OSS, we have neither of these things. The only stick we have is breaking changes, and the only carrots we can offer are new features. There is no \"global approval\" or \"TAP\" for OSS."