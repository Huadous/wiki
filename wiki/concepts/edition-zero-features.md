---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme|editions-readme]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-java-lite-for-editions.md]]"
  - "[[protobuf/editions-editions-feature-extension-layout.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
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
Editions Zero Features 构成了 Editions 体系首发阶段所支持的最小特性集合，核心目标是在不破坏 `MessageInfo` 当前编码格式的前提下，引入按语言或按作用域（如 FILE、FIELD）组织的特性开关机制，从而收敛 proto2 与 proto3 之间长期存在的行为差异。该特性集至少包含六项核心 feature：字段存在性（`features.field_presence`）、遗留封闭枚举（`java.legacy_closed_enum`）、枚举类型（`features.enum_type`）、重复字段编码（`features.repeated_field_encoding`）、字符串字段校验（`features.string_field_validation`）以及消息编码（`features.message_encoding`）。

文档同时提议向 Edition Zero Features 中新增 `legacy_treat_enum_as_closed` 特性，定义其 retention 为 RUNTIME，并允许作用于 FILE 与 FIELD 目标。Edition 2023 作为其后续版本将默认把该特性设为 `false`，而 proto2 则隐式视为 `true`，由此支持从遗留语法到 Editions 的渐进式迁移路径；该特性属于 [[concepts/enum-field-closedness|Enum Field Closedness]] 范畴。当从 syntax 迁移到 edition zero 时，Prototiller 需要知晓所有被使用的语言以保证升级是一个 trivial change，这也意味着 language-scoped features 的存在会直接影响迁移工具的能力边界。

在向后兼容方面，Editions Zero 尽量复用 Java Lite 已有的字段条目位（field entry bits）来表示这些 resolved features，针对 Java Lite 中现存的、读取 `is_proto3` 的语法用法，未来将迁移使用这些 bits 来表达，以保证 Editions 路径与遗留路径在编码层面的统一；若未来需要新增非 Editions Zero 的 features，或要在 message-level 表达 features，则必须升级 `MessageInfo` 编码格式。

在功能扩展布局（Feature Extension Layout）方面，团队倾向于在初始实现中保持尽可能简单——即采用方案二 Generator Features，将功能扩展的复杂度推迟到能够基于真实使用反馈再做决策的阶段，因为后续 editions 拥有较大的自由度来重新建模 features。

## Related Concepts
- [[concepts/what-are-protobuf-editions|What are Protobuf Editions?]]
- [[concepts/protobuf-editions-design-features|Protobuf Editions Design: Features]]
- [[concepts/edition-zero-converged-semantics|Edition Zero: Converged Semantics]]
- [[concepts/edition-zero-json-handling|Edition Zero: JSON Handling]]
- [[concepts/edition-features|Feature]]
- [[concepts/global-features|Global features]]
- [[concepts/language-scoped-features|Language-scoped features]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/feature-extension-layout|Feature Extension Layout]]
- [[concepts/generator-features|Generator Features]]
- [[concepts/enum-field-closedness|Enum Field Closedness]] *(to be created if not existing — referenced via [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]])*

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/prototiller|Prototiller]] *(to be created if not existing — referenced via [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]])*

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

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "This document proposes adding an additional feature to Edition Zero Features, specified as the following .proto fragment:"
> - "When migrating from syntax to edition zero, Prototiller will need to know all used languages to make the upgrade a trivial change"