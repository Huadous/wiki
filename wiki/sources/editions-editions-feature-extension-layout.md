---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-editions-feature-extension-layout.md]]"
tags: [Protobuf Editions, Editions Zero, Feature Extension, Runtime Implementation Features, Generator Features, Nested Features, utf8_validation, Polyglot, Shared Implementations, FeatureSet, Migrate to bytes, legacy_closed_enum]
aliases: ["Editions 功能扩展布局方案", "Feature Extension Layout"]
---

# Editions: Feature Extension Layout - Summary

## 来源
- Original file: [[protobuf/editions-editions-feature-extension-layout.md]]
- Ingested: 2026-06-13

## 核心内容
本文档（批准于2023-08-23）由 [[entities/mkruskal-google|mkruskal-google]] 与 [[entities/zhangskz|zhangskz]] 撰写，针对 [[concepts/protobuf-editions|Protobuf Editions]] 中功能扩展（[[concepts/feature-extension|Feature Extension]]）应归属于语言、代码生成器还是运行时实现这一未明确的问题展开讨论。以 [[concepts/utf8_validation|utf8_validation]] 功能为例，文档指出该功能在 Python 的三种实现之间行为不一致，且 C++ 还存在"hint"行为，因此归属决策尤为关键。文档详细评估了四种替代方案——[[concepts/runtime-implementation-features|Runtime Implementation Features]]、[[concepts/generator-features|Generator Features]]、[[concepts/migrate-to-bytes|Migrate to bytes]] 与 [[concepts/nested-features|Nested Features]]，并在 [[concepts/polyglot|Polyglot]] 与 [[concepts/shared-implementations|Shared Implementations]] 两个维度上权衡利弊。最终建议暂缓决策，采用方案二（Generator Features），因为目前只有两种行为且其中一种无歧义，团队可在后续版本中收集更多边界情况后重新建模功能，从而在保持初始实现简单的同时保留未来灵活性。

## 关键实体
- [[entities/mkruskal-google|mkruskal-google]]：本文档作者之一，参与 Protobuf Editions 功能扩展归属策略的设计。
- [[entities/zhangskz|zhangskz]]：本文档共同作者，负责评估 utf8_validation 等功能的归属策略。
- [[entities/upb|upb]]：Google 开发的 C 语言 protobuf 运行时实现库，作为多种语言（Python、Ruby、PHP 等）的共享后端实现，是讨论共享实现与多语言场景问题的核心实体。

## 关键概念
- [[concepts/protobuf-editions|Protobuf Editions]]：通过全局 features proto 扩展支持细粒度功能的标准化机制。
- [[concepts/editions-zero|Editions Zero]]：Editions 系统的首个发布版本，本文档决策为其推行而制定。
- [[concepts/feature-extension|Feature Extension]]：扩展全局 features proto 以添加非 protobuf 团队拥有功能的机制。
- [[concepts/runtime-implementation-features|Runtime Implementation Features]]：方案一，主张功能按运行时实现（C++、Java、Python、upb）划分。
- [[concepts/generator-features|Generator Features]]：推荐方案（方案二），主张功能仅按代码生成器（protoc plugin）划分。
- [[concepts/nested-features|Nested Features]]：方案四，允许共享功能集消息但不作全局 FeatureSet 的扩展。
- [[concepts/migrate-to-bytes|Migrate to bytes]]：方案三，将不强制 utf8 的字段迁移到 bytes 类型。
- [[concepts/utf8_validation|utf8_validation]]：Editions Zero 引入的字符串 UTF-8 验证控制功能，是本文档讨论的核心动机。
- [[concepts/polyglot|Polyglot]]：多语言场景下共享运行时应遵循哪一套功能集的问题。
- [[concepts/shared-implementations|Shared Implementations]]：upb、C++ 等被多种语言共享使用的后端实现。
- [[concepts/featureset|FeatureSet]]：Editions 系统中功能归属的根结构。
- [[concepts/legacy_closed_enum|legacy_closed_enum]]：Java 与 C++ 的已有功能扩展，作为归属问题讨论的无歧义参考点。

## 要点
- Protobuf Editions 的功能扩展归属问题涉及语言、代码生成器和运行时实现三个维度，原计划未明确应归属哪一方。
- utf8_validation 功能在 Python 的三种实现（pure python、Python/C++、Python/upb）之间行为不一致，是促使本文档讨论的核心动机。
- 文档评估了四种替代方案，每种方案在多语言场景、共享实现和迁移难度上各有权衡，其中 Migrate to bytes 方案因 O(10M) proto2 字段的迁移成本被否决。
- 最终推荐方案二（Generator Features）：仅按代码生成器划分功能，允许对共享实现在不同目标语言中进行独立控制。
- Polyglot（多语言）与 Shared Implementations（共享实现）是当前已存在的严重问题：所有 proto2 字符串和许多 proto3 字符串在不同语言之间完全不安全，切换运行时实现可能导致微妙且危险的行为变化。