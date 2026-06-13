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
  - "Large-Scale Change"
  - "大规模变更"
  - "Large-scale Change"
  - "Large-Scale Change"
  - "大规模变更"
---

## Description
LSC 是 Google 在庞大代码库中执行系统性、可控语义修改的核心方法论，其设计目标是让 Protobuf 之类的语言特性演进能够以自动化、可审计的方式贯穿整个代码库。LSC 的核心是自动化执行，能够对代码库中成千上万个文件进行批量修改，遵循统一的模板以确保所有变更具有一致性和可重复性，便于审计和回滚。每一次 LSC 都遵循相同的标准化流程：先引入新特性 → 在新 edition 中将该特性设为新的默认值 → 等待生态系统迁移 → 最终移除旧特性（破坏性变更）。这种流程使 LSC 在无操作（no-op）迁移场景中效率极高，例如将 feature 设置从显式改为默认值的操作几乎不需要人工介入。文档列举了多种大规模变更模板作为示例，涵盖不同的变更层级：Edition Zero（无功能变更的纯语法迁移）、Immolation of `required`（功能性的特性迁移）、`absl::string_view` Accessors（生成 API 变更）、Group-Encoded Messages（线协议优化），共同说明 LSC 是一种可复用、可组合的迁移框架。

## Related Concepts
- [[concepts/Feature|Feature]]
- [[concepts/Edition|Edition]]
- [[concepts/Edition Zero|Edition Zero]]
- [[concepts/Immolation of required|Immolation of required]]

## Related Entities
- [[entities/Google|Google]]
- [[entities/Protobuf Editions|Protobuf Editions]]
- [[entities/protoc|protoc]]

## Mentions in Source

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "Undesirable features will be LSC'd away, using the same template as any other feature/edition migration."
> - "The migration to edition "2025" across google will move very fast as it is a no-op."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "How to use Protobuf Editions to construct a large-scale change that modifies the semantics of Protobuf in some way."
> - "The following are sketches of large-scale change designs for feature changes we would like to execute, presented as example use-cases."