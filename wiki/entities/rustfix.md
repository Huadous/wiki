---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "product"
aliases:
  - "rustfix tool"
  - "cargo fix"
---

## Description
rustfix 是 Rust 编程语言提供的一款自动化代码迁移工具，可通过 `cargo fix` 子命令在 Cargo 项目中执行。其核心能力是协助开发者将 crate 从一个 [[entities/rust-editions|Rust Editions]] 升级到另一个 edition，从而降低跨 edition 升级的人工成本。

根据 Rust 的设计要求，每次 edition 的变更都*必须*附带一份可由 rustfix 执行的迁移计划——这是一项硬性约束，旨在保证旧代码库能够以机器可读、可重复的方式迁移至新 edition。rustfix 因此被视为 Protobuf 设计 [[concepts/editions-proclamation|Edition Proclamation]] 与大规模迁移机制时的重要先例。

rustfix 在角色定位上与 Go 语言的 [[entities/go-fix|go fix]] 工具类似，二者都是为编程语言的大规模版本迁移提供自动化辅助，并被 Protobuf 的 OSS 迁移策略明确列为值得借鉴的先例，因为它体现了"升级是开发生命周期的一部分"这一理念。与 Protobuf 计划采取的更激进迁移节奏不同，Rust 承诺对所有过往 edition 永久支持，这使其迁移故事相对宽松：用户可以长期停留在旧 edition 而无需立即升级。Protobuf 在调研中正是借由这种对比，反思自身在 [[concepts/large-scale-change|Large-scale Change]] 中应如何在「宽松对待旧版本」与「推动用户快速迁移」之间做出设计取舍。

## Related Entities
- [[entities/rust-editions|Rust Editions]]
- [[entities/go-fix|go fix]]

## Related Concepts
- [[concepts/the-oss-story|The OSS Story]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/editions-proclamation|Edition Proclamation]]
- [[concepts/features-gc|Features GC]]

## Mentions in Source
- `rustfix` (runnable on Cargo projects via `cargo fix`), a tool that can upgrade crates to a new edition. Edition changes are *required* to come with a migration plan to enable `rustfix`. — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "Rust does ship with `rustfix` (runnable on Cargo projects via `cargo fix`), a tool that can upgrade crates to a new edition."
> - "We should lean in on lessons learned by Go (see: their `go fix` tool) and Rust (see: their `rustfix` tool)"
> - "Rust in particular has an editions/epoch mechanism like we do; they also have feature gates, but those are not the same concept as *our* features."