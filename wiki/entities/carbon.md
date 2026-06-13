---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "project"
aliases:
  - "Carbon programming language"
  - "Carbon语言"
---

## Description
Carbon 是由 Google 主导开发的实验性编程语言项目，其核心设计理念强调"演化优先"（evolution as a core precept），将语言的持续演化能力作为预先设计目标，包含兼容性保证与迁移路径定义等机制。Carbon 的版本演化机制并非简单的语言特性叠加，而是从根本上保障语言能够平滑演进，这一思路与 Protobuf Editions 所追求的目标高度一致。在 Protobuf Editions 的开源策略制定中，Carbon 团队的公开沟通方式被视为值得借鉴的先例（prior art），尤其是在传达"升级是日常事实"这一信息方面。该文档建议在 Protobuf 面向外部观察者时，借鉴 Carbon 的沟通经验，以形成 Google 在语言/协议演化议题上统一一致的对外口径。

## Related Entities
- [[entities/google|Google]] — Carbon 的主导开发者
- [[entities/protobuf-editions|Protobuf Editions]] — 受 Carbon 演化理念影响的项目，两者设计理念相似；Protobuf 团队将 Carbon 的公开沟通策略作为开源战略的参考先例

## Related Concepts
- [[concepts/rust-editions|Rust editions]] — Carbon 演化机制的设计参考
- [[concepts/editions|Editions]] — 语言/协议版本演化模式的广义概念
- [[concepts/large-scale-change|Large-scale Change]] — 与 Carbon 演化理念相关的概念
- [[concepts/edition-zero|Edition Zero]] — 与 Carbon 演化理念相关的概念

## Mentions in Source
> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
- "Carbon has a similar philosophy"
- "For example, Carbon is heavily focused on evolution as a core precept"
- "Rust has built language evolution via editions into its core design."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
- "We should also lean on the Carbon team's public messaging about upgrading being a fact of life, to provide a unified Google front on the matter from the view of observers."