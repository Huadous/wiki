---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme|editions-readme]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-java-lite-for-editions.md]]"
  - "[[protobuf/editions-editions-feature-extension-layout.md]]"
tags:
  - "standard"
aliases:
  - "Edition Zero 特性集"
  - "Edition 0 Features"
  - "Edition 0 特性"
  - "Editions Zero Features"
  - "Edition Zero 特性集"
  - "Edition 0 Features"
  - "Edition 0 特性"
  - "Editions Zero"
  - "Edition Zero 特性集"
  - "Edition 0 Features"
  - "Edition 0 特性"
  - "Editions Zero Features"
  - "Edition Zero 特性集"
  - "Edition 0 Features"
  - "Edition 0 特性"
---

## Description
Editions Zero Features 构成了 Editions 体系首发阶段所支持的最小特性集合，至少包含六项核心 feature：字段存在性（`features.field_presence`）、遗留封闭枚举（`java.legacy_closed_enum`）、枚举类型（`features.enum_type`）、重复字段编码（`features.repeated_field_encoding`）、字符串字段校验（`features.string_field_validation`）以及消息编码（`features.message_encoding`）。该特性集的设计哲学强调向后兼容：Editions Zero 的目标是尽量不破坏 `MessageInfo` 的当前编码格式，即尽量复用 Java Lite 已有的字段条目位（field entry bits）来表示这些 resolved features。文档明确指出，未来若需要新增非 Editions Zero 的 features，或要在 message-level 表达 features，则必须升级 `MessageInfo` 编码格式；与此同时，针对 Java Lite 中现存的、读取 `is_proto3` 的语法用法，未来将迁移使用这些 bits 来表达，以保证 Editions 路径与遗留路径在编码层面的统一。

在功能扩展布局（Feature Extension Layout）方面，相关决策是为支持 Editions Zero 的发布而制定的。文档指出，团队可以在 Editions Zero 的推行过程中持续收集更多需要功能扩展的边界情况，这些信息也将为后续版本对 features 的重新建模提供依据。由于后续 editions 拥有较大的自由度来重新建模 features，因此倾向于在初始实现中保持尽可能简单——即采用方案二 Generator Features，将功能扩展的复杂度推迟到能够基于真实使用反馈再做决策的阶段。

## Related Concepts
- [[concepts/what-are-protobuf-editions|What are Protobuf Editions?]]
- [[concepts/protobuf-editions-design-features|Protobuf Editions Design: Features]]
- [[concepts/edition-zero-converged-semantics|Edition Zero: Converged Semantics]]
- [[concepts/edition-zero-json-handling|Edition Zero: JSON Handling]]
- [[concepts/edition-features|Feature]]
- [[concepts/global-features|Global features]]
- [[concepts/language-scoped-features|Language-scoped features]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/feature-extension-layout|Feature Extension Layout]] *(to be created if not existing — referenced via [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]])*
- [[concepts/generator-features|Generator Features]] *(to be created if not existing — referenced via [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]])*

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]

## Mentions in Source

> **Source: [[sources/editions-readme|editions-readme]]**
> - "[Edition Zero Features](edition-zero-features.md)"
> - "The following topics are in this repository:"

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "Next, we will introduce the features defined in [Edition Zero Features](edition-zero-features.md)."
> - "We will then implement tooling that can take a `proto2` or `proto3` file and add `edition = \"2023\";` and `option features.* = ...;` as appropriate, so that each file retains its original behavior."

> **Source: [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]**
> - "Fortunately, we already have corresponding bits for most Editions Zero Features in the corresponding `MessageInfo` field entry encoding."
> - "We will move existing remaining syntax usages reading `is_proto3` to use these bits."

> **Source: [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]**
> - "We may encounter more edge cases that require feature extensions (and give us more information) during the rollout of edition zero."
> - "We also have a lot of freedom to re-model features in later editions, so keeping the initial implementation as simple as possible seems best (i.e. Alternative 2)."