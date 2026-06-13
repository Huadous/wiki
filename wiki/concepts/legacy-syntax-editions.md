---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
tags:
  - "term"
aliases:
  - "遗留语法 Edition"
  - "Legacy Syntax Editions"
---

## Description
Legacy Syntax Editions 是 Protobuf Editions 体系为实现向后兼容性而提出的核心迁移方案。该方案建议在 editions 枚举中新增两个特殊值 `EDITION_PROTO2 = 998` 和 `EDITION_PROTO3 = 999`，将 proto2 和 proto3 视为特殊的 edition；parser 会拒绝 proto 文件中的 `edition = "proto2"` 和 `edition = "proto3"` 声明，但内部会像处理其他 edition 一样处理它们。其核心目标是统一语法与 editions 的代码基础设施，避免维护两套不同的代码库，从而提高测试覆盖率并简化 runtimes 实现。在生态层面，Legacy Syntax Editions 保护了既有 proto2/proto3 schema 的投资，使工具链（如编译器、运行时）能够正确识别和转换遗留语法的语义，并在不破坏现有 API 与数据兼容性的前提下，允许用户逐步采用 Editions 特性。它与 Edition Lifetimes、Minimum Required Edition、FeatureSet、Feature Inference 等机制协同，共同保障迁移过程的可行性。

## Related Concepts
- [[concepts/edition-lifetimes|Edition Lifetimes]]
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/editions-group-migration-issues|Editions: Group Migration Issues]]
- [[concepts/edition-evolution|Edition Evolution]]
- [[concepts/feature-inference|Feature Inference]] *(待确认页面存在性，建议在有对应概念页时链接)*
- [[concepts/feature-set|FeatureSet]] *(待确认页面存在性，建议在有对应概念页时链接)*

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/mkruskal-google|mkruskal-google]] *(待确认页面存在性)*
- [[entities/prototiller|Prototiller]] *(待确认页面存在性)*

## Mentions in Source
> **Source: [[sources/editions-readme]]**
> - "The following topics are in this repository:"
> - "[Legacy Syntax Editions](legacy-syntax-editions.md)"

> **Source: [[sources/editions-legacy-syntax-editions]]**
> - "We recommend adding two new special editions to our current set"
> - "These will be treated the same as any other edition, except in our parser which will reject `edition = \"proto2\"` and `edition = \"proto3\"` in proto files."