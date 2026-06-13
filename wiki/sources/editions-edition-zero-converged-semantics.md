---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-edition-zero-converged-semantics.md]]"
tags: [Converged Semantics, edition keyword, features option, syntax keyword deprecation, Language-specific features, Semantic features, proto2/proto3, Rust editions, Implied behavior, Base features, Feature scope hierarchy, Large deployment feature management]
aliases: ["Edition Zero 提案", "Converged Semantics Design Doc"]
---

# Edition Zero: Converged Semantics - 摘要

## 来源
- Original file: [[protobuf/editions-edition-zero-converged-semantics.md]]
- Ingested: 2026-06-13

## 核心内容
本文档《Edition Zero: Converged Semantics》由 [[entities/protobuf-team|Protobuf Team]] 的 [[entities/@perezd|@perezd]] 与 [[entities/@haberman|@haberman]] 共同撰写，于 2021-10-07 获得批准。文档的核心目标是设计 [[entities/edition-zero|Edition Zero]] —— protobuf 的第一个 edition 版本，通过在 IDL 中引入 [[concepts/edition-keyword|`edition` 关键字]] 来统一 [[concepts/proto2proto3|proto2/proto3]] 的长期语义差异。选定 edition 后将默认启用 [[concepts/converged-semantics|融合语义]]，同时用户可通过新增的 [[concepts/features-option|`features` 选项]] 细粒度地选择退出不兼容特性，以回退到原有的 proto2 或 proto3 行为。文档还讨论了在 [[entities/descriptor-proto|descriptor.proto]] 中跨多个描述符层级暴露 features 字段的方案、language-specific 与 semantic 两类特性的区分、逐步弃用 `syntax` 关键字的策略，以及将 [[concepts/rust-editions|Rust editions]] 作为先例参考的合理性。

## 关键实体
- [[entities/protobuf-team|Protobuf Team]] —— 文档的提出方与设计主体
- [[entities/@perezd|@perezd]] —— 文档合著者
- [[entities/@haberman|@haberman]] —— 文档合著者
- [[entities/edition-zero|Edition Zero]] —— 文档所描述的设计对象
- [[entities/protoc|protoc]] —— 唯一解析 protobuf IDL 的实现
- [[entities/descriptor-proto|descriptor.proto]] —— 承载 `features` 选项的描述符定义文件

## 关键概念
- [[concepts/converged-semantics|Converged Semantics]] —— proto2/proto3 融合后的统一默认语义
- [[concepts/edition-keyword|`edition` 关键字]] —— 用于声明文件语义版本基线的新关键字
- [[concepts/features-option|`features` 选项]] —— 在 `descriptor.proto` 中新增的可重复字符串集合
- [[concepts/syntax-keyword-deprecation|syntax keyword deprecation]] —— 引入 edition 后对 `syntax` 关键字的弃用策略
- [[concepts/language-specific-features|Language-specific features]] —— 仅影响特定语言生成 API 的特性
- [[concepts/semantic-features|Semantic features]] —— 跨语言影响 protobuf 数据模型行为的特性
- [[concepts/proto2proto3|proto2/proto3]] —— 即将被 editions + features 取代的粗粒度历史模型
- [[concepts/rust-editions|Rust editions]] —— 作为先例参考的 Rust edition 机制
- [[concepts/implied-behavior|Implied behavior]] —— `syntax` 关键字隐式捆绑的特性集
- [[concepts/base-features|Base features]] —— 每个 edition 默认激活的整套特性
- [[concepts/feature-scope-hierarchy|Feature scope hierarchy]] —— `features` 可声明的描述符层级
- [[concepts/large-deployment-feature-management|Large deployment feature management]] —— 用于缓解大型项目迁移复杂度的补充机制

## 要点
- 在 protobuf IDL 中引入 [[concepts/edition-keyword|`edition` 关键字]]，用于声明文件及其内容所遵循的语义版本基线
- 在 [[entities/descriptor-proto|descriptor.proto]] 中新增 [[concepts/features-option|`features` 选项]]，定义为可重复字符串集合，可使用 `-` 前缀 opt-out 特性或不带前缀 opt-in 特性
- [[entities/edition-zero|Edition Zero]] 默认启用 proto2 与 proto3 的 [[concepts/converged-semantics|融合语义]]，用户可按需选择退出不兼容特性以回退到原有 proto2/proto3 行为
- 特性分为 [[concepts/language-specific-features|Language-specific features]]（仅影响特定语言生成 API）与 [[concepts/semantic-features|Semantic features]]（影响跨语言数据模型行为）两大类
- 建议在引入 [[concepts/edition-keyword|`edition` 关键字]] 后逐步 [[concepts/syntax-keyword-deprecation|弃用 `syntax` 关键字]]；当二者共存时 `edition` 优先
- 修订 [[entities/descriptor-proto|descriptor.proto]] 的侵入性远高于仅修改 IDL 本身，需谨慎处理下游 C++ `google::protobuf::Descriptor` API 等使用者
- 将 [[concepts/rust-editions|Rust editions]] 列为 editions + features 模型在工业界的成功先例
- [[concepts/implied-behavior|`syntax` 关键字隐式捆绑特性]] 是造成用户困惑的重要根源，Editions + Features 模型旨在将其显式化