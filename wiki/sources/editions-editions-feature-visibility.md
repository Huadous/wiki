---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/editions-edition-lifetimes.md]]"
tags:
  - "FeatureSet"
  - "Editions Feature Visibility"
  - "Resolved Features"
  - "Unresolved Features"
  - "Descriptor API"
  - "Hyrum's Law"
  - "Large-scale Change"
  - "edition zero"
  - "proto2"
  - "proto3"
  - "Conformance test"
  - "Descriptor"
  - "Reflection"
aliases:
  - "Editions Feature Visibility"
  - "Feature Visibility for Editions"
---

## 来源
- Original file: [[protobuf/editions-editions-feature-visibility.md]]
- Ingested: 2026-06-13

## 核心内容
本文档由 mkruskal-google 撰写，于 2023 年 9 月 8 日获批，作为姊妹文档 [[concepts/editions-life-of-a-featureset|editions-life-of-a-featureset]] 的补充，专门探讨 [[entities/editions|Protocol Buffers Editions]] 中，feature 应如何从运行时暴露给用户的问题。作者指出，将解析后的 [[concepts/featureset|FeatureSet]] protos 直接暴露给用户会引发两大隐患：resolved features 的结构化特性阻碍内部重构，[[concepts/unresolved-features|unresolved features]] 与 [[concepts/resolved-features|resolved features]] 共享同一类型，容易被误用，可能在年度 edition 迁移时引发意外崩溃。文中以 UTF8 验证、`packed` 特性建模、descriptor 内存优化及 [[concepts/large-scale-change|年度 LSC]] 等案例佐证。推荐采取保守策略：隐藏所有 [[concepts/featureset|FeatureSet]] protos，并通过 [[concepts/descriptor-api|descriptor]] 上的辅助方法（如 `has_presence`、`requires_utf8_validation`）封装 feature 行为。反射场景是唯一例外，需保留 unresolved features 以忠实还原原始 proto。文档还讨论了 Google 内外执行难度差异，以及 [[entities/μpb|μpb]] 作为非完整运行时的特殊定位。

## 关键实体
- [[entities/editions|Protocol Buffers Editions]]：feature-based 模式的核心项目，团队承诺每年向 Google 内部推广至少 80%
- [[entities/μpb|μpb]]：运行时实现而非完整运行时，可自由暴露 features
- [[entities/prototiller|Prototiller]]：Google 内部 proto-to-proto 转换工具，其行为保持性是 LSC 成功的关键

## 关键概念
- [[concepts/editions-feature-visibility|Editions Feature Visibility]]：本文档提出的设计标准，保守隐藏 FeatureSet protos
- [[concepts/featureset|FeatureSet]]：表示一组 feature 的 proto 类型，是本文核心讨论对象
- [[concepts/resolved-features|Resolved Features]]：经 Editions 规则处理后的 feature，是运行时决策的依据
- [[concepts/unresolved-features|Unresolved Features]]：proto 文件直接指定的 feature，是用户易误用的 foot-gun
- [[concepts/descriptor-api|Descriptor API]]：运行时描述 proto 元数据的接口层，推荐方案要求剥离其 features 字段
- [[concepts/descriptor|Descriptor]]：承载 FeatureSet 的容器，用户访问 feature 的入口
- [[concepts/reflection|Reflection]]：唯一保留 unresolved features 的位置，用于忠实还原原始 proto
- [[concepts/hyrums-law|Hyrum's Law]]：API 用户依赖所有可观察行为的工程现象，本文档两次援引以论证隐藏 features 的必要性
- [[concepts/large-scale-change|Large-scale Change]]：Google 内部大规模变更机制，Editions 年度迁移依赖之
- [[concepts/edition-zero|edition zero]]：Editions 初始版本，保留所有 [[concepts/proto2|proto2]]/[[concepts/proto3|proto3]] 行为
- [[concepts/conformance-test|Conformance test]]：保障各语言 feature 行为一致性的测试方法

## 要点
- **推荐方案**：保守地隐藏所有 [[concepts/featureset|FeatureSet]] protos，不提供公共 `features()` getter，并在 `options()` getter 中将 features 字段置空，转而通过 [[concepts/descriptor|descriptor]] 上的辅助方法暴露 feature 行为
- **两大核心顾虑**：resolved features 的 proto 结构与底层行为不一一对应，阻碍内部重构；unresolved features 与 resolved features 共享类型，存在被误用的 foot-gun，可能在 edition 升级时意外崩溃
- **反射是唯一例外**：`CopyTo`、`DebugString` 等 [[concepts/reflection|reflection]] 方法需忠实还原原始 proto 文件，因此应保留 unresolved features
- **执行层面**：无法在 Google 外部强制约束，但 Google 内部应更严格执行，因为 [[concepts/large-scale-change|大规模迁移]] 的成本主要由 Google 承担
- **μpb 的特殊定位**：作为运行时实现而非完整运行时，可自由暴露 features，由上层包装语言运行时负责剥离
- **推荐方案的代价**：每个语言都要重复实现高层 feature 行为（可能需要 [[concepts/conformance-test|conformance test]] 保证一致性）；`options()` 不再严格 1:1 反映 proto 文件，违背既有惯例
- **设计原则**：增加新 API 容易，移除既有 API 困难，因此保持保守可在未来需要时灵活放开
- **Prototiller 的关键作用**：其行为保持性（behavior-preserving）使得 [[concepts/large-scale-change|LSC]] 可以在不破坏运行时代码的前提下更新 proto 文件的内部表示形式

## 补充信息
- 来源文件 [[protobuf/editions-edition-lifetimes|editions-edition-lifetimes]]：未提供与本主题直接相关的信息