---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition]]"]
tags: [product]
aliases:
  - "go fix tool"
  - "Go fix"
---


# go fix

## 基本信息
- Type: product
- Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]

## 描述
go fix 是 Go 编程语言提供的一个自动化代码重构工具，用于以编程方式将 Go 代码从一个旧版本迁移到新版本。它是 Go 生态中处理大规模语言演进时采用的标志性工具，能够自动完成 API 重命名、语法更新等迁移工作。本源文档在讨论 Protobuf Editions 迁移策略时，明确将 go fix 列为 Protobuf 应借鉴的先例之一，与 Rust 生态中的 [[entities/rustfix|rustfix]] 并列。该工具体现了通过自动化工具显著降低升级成本的核心思想，是 [[concepts/the-oss-story|The OSS Story]] 中推动大规模变更（[[concepts/large-scale-change|Large-scale Change]]）时希望复用的成功经验。文中特别强调 Protobuf 在设计 Editions upgrader（[[concepts/editions-upgrader|Editions upgrader]]）以及处理 Features GC（[[concepts/features-gc|Features GC]]）相关迁移问题时，应向 Go 的 go fix 学习。

## 相关实体
- [[entities/rustfix|rustfix]]

## 相关概念
- [[concepts/the-oss-story|The OSS Story]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/features-gc|Features GC]]
- [[concepts/editions-upgrader|Editions upgrader]]

## 来源提及
- We should lean in on lessons learned by Go (see: their `go fix` tool) and Rust (see: their `rustfix` tool); Rust in particular has an editions/epoch mechanism like we do; they also have feature gates, but those are not the same concept as *our* features. — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]