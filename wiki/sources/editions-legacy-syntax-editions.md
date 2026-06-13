---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-legacy-syntax-editions.md]]"
tags: [Legacy Syntax Editions, proto2, proto3, Edition 2023, FeatureSet, Feature Inference, Feature Resolution, Bootstrapping, Serialized Descriptors]
aliases: ["Legacy Syntax Editions Proposal", "遗留语法 Editions 提案"]
---

# Legacy Syntax Editions - Summary

## 来源
- Original file: [[protobuf/editions-legacy-syntax-editions.md]]
- Ingested: 2026-06-13

## 核心内容
本文档由 [[entities/mkruskal-google|mkruskal-google]] 于 2023-09-08 批准，探讨了是否应将 [[concepts/proto2|proto2]] 和 [[concepts/proto3|proto3]] 视为 [[concepts/legacy-syntax-editions|特殊 editions]] 纳入 protobuf editions 系统的统一枚举体系。提案建议新增 `EDITION_PROTO2 = 998` 和 `EDITION_PROTO3 = 999` 两个枚举值，与 `EDITION_2023 = 1000` 并列，由 parser 拒绝显式的 `edition = "proto2"` / `edition = "proto3"` 声明，但内部像处理其他 edition 一样处理它们。该方案的核心动机是统一语法与 editions 的代码基础设施，避免维护两套代码库，并通过 [[concepts/feature-resolution|Feature Resolution]] 与 [[concepts/feature-inference|Feature Inference]] 实现行为对齐。

## 关键实体
- [[entities/mkruskal-google|mkruskal-google]] — 文档作者与推动者
- [[entities/prototiller|Prototiller]] — 负责将 proto2/proto3 转换至 editions 的工具
- [[entities/descriptor-proto|descriptor.proto]] — 自描述协议，其序列化快照带来兼容性约束

## 关键概念
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]] — 核心提案，将 proto2/proto3 设为特殊 edition
- [[concepts/proto2|proto2]] — 遗留语法版本一（EDITION_PROTO2 = 998）
- [[concepts/proto3|proto3]] — 遗留语法版本二（EDITION_PROTO3 = 999）
- [[concepts/edition-2023|Edition 2023]] — editions 系统首个正式版本（EDITION_2023 = 1000）
- [[concepts/featureset|FeatureSet]] — 将 edition 默认值传播至 generators 和 runtimes 的核心抽象
- [[concepts/feature-inference|Feature Inference]] — 从 proto2/proto3 语法推断 features 的方法
- [[concepts/feature-resolution|Feature Resolution]] — 根据 edition/syntax 确定 feature 实际生效值的过程
- [[concepts/bootstrapping|Bootstrapping]] — 引导构建机制，是 feature resolution 运行的前提
- [[concepts/serialized-descriptors|Serialized Descriptors]] — 预序列化的 descriptor 快照，需要保持向后兼容

## 要点
- 提案建议将 [[concepts/proto2|proto2]] 与 [[concepts/proto3|proto3]] 作为 `EDITION_PROTO2 = 998`、`EDITION_PROTO3 = 999` 纳入统一枚举体系，与 `EDITION_2023 = 1000` 并列
- 核心动机是统一语法与 editions 代码基础设施，避免维护两套独立代码库，并改善 [[concepts/feature-resolution|Feature Resolution]] 的测试覆盖率
- [[concepts/feature-inference|Feature Inference]] 包含关键映射规则：`required` → `LEGACY_REQUIRED`、`proto3 optional` → `EXPLICIT` presence、`group` → `DELIMITED` 编码、`enforce_utf8` → `PACKED`/`EXPANDED` 切换
- 需要解决 [[concepts/bootstrapping|引导构建]] 问题以让 feature resolution 能在 proto2/proto3 中运行，C++ 需将默认值 check in 至代码，其他语言可通过 genrules 动态处理
- 由于生态系统中存在大量预序列化的 [[entities/descriptor-proto|descriptor.proto]] 快照，protoc 需在 feature resolution 失败时提供 fallback，回退至硬编码默认值
- 该方案使 [[entities/prototiller|Prototiller]] 迁移工具能获得更丰富的 proto2/proto3 行为信息，从而更好地支持向 [[concepts/edition-2023|Edition 2023]] 的迁移