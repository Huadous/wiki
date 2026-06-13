---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-edition-lifetimes.md]]"
tags: [Edition Lifetimes, Feature Lifetimes, Edition Zero, Edition 2023, Edition 2024, EDITION_LEGACY, FeatureSupport, FeatureSet, Dynamic Messages, Editions, Edition Patches, Edition Naming, Life of an Edition, Editions: Life of a Feature, Protobuf Editions Design: Features, Editions Feature Visibility, Backward Compatibility, Forward Compatibility, FeatureSetEditionDefault, Behavior-Preserving Editions, Edition Support Window, Reflection-Based Validation, Deprecation Warning, Garbage Collection, Edition Upgrade, Predictability, Validation Layer]
aliases: ["Protobuf Editions - Edition Lifetimes", "Editions: Feature & Edition Lifecycle Design"]
---

# Edition Lifetimes - Summary

## 来源
- Original file: [[protobuf/editions-edition-lifetimes.md]]
- Ingested: 2026-06-13

## 核心内容
本文档是 [[entities/protobuf|Protobuf]] 项目在 [[concepts/edition-zero|Edition Zero]] 完成后对其版本（Edition）与特性（Feature）生命周期管理的重新审视与设计提案。文档指出当前的 [[concepts/editions|Editions]] 系统与特性几乎相互独立——每个 Edition 仅是所有特性的默认值集合，用户可在任意版本中覆盖任何已发布特性的值。这种设计在仅有 [[concepts/edition-2023|Edition 2023]] 一个版本时运作良好，但当引入新版本和新特性时会产生旧二进制无法识别新特性、特性弃用/删除缺乏清晰策略等问题。文档核心建议为特性规范新增四个字段选项（`edition_introduced`、`edition_deprecated`、`deprecation_warning`、`edition_removed`）以及新的占位版本 [[concepts/edition_legacy|EDITION_LEGACY]]，将特性生命周期与具体版本绑定，使库行为更可预测，并强烈建议在 [[concepts/edition-2024|Edition 2024]] 发布前尽快落地。

## 关键实体
- [[entities/protobuf|Protobuf]]：项目主体，OSS 与 google3 双发布线
- [[entities/protoc|protoc]]：执行特性生命周期验证的核心编译器
- [[entities/google3|google3]]：Google 内部单体仓库，旧二进制可存在长达六个月
- [[entities/upb|upb]]：对反射式验证性能敏感的 C/C++ 运行时
- [[entities/new-string-apis|New String APIs]]：暴露 Editions 缺陷的真实案例项目
- [[entities/string_type|string_type]]：作为案例驱动本文设计的具体特性

## 关键概念
- [[concepts/edition-lifetimes|版本生命周期]]：每个 Edition 从引入到弃用/删除的完整周期
- [[concepts/feature-lifetimes|特性生命周期]]：通过四个新字段选项显式编码
- [[concepts/featuresupport|FeatureSupport]]：编码特性生命周期元数据的字段选项结构
- [[concepts/edition_legacy|EDITION_LEGACY]]：作为"无限过去"占位的特殊版本
- [[concepts/featureset|FeatureSet]] 与 [[concepts/featureseteditiondefault|FeatureSetEditionDefault]]：动态消息运行时验证的数据结构
- [[concepts/dynamic-messages|动态消息]] 与 [[concepts/validation-layer|运行时验证层]]：protoc 之外的额外检查机制
- [[concepts/reflection-based-validation|反射式验证]]：被否定的备选方案（性能问题）
- [[concepts/behavior-preserving-editions|行为保持型版本升级]]：可能因新设计而变成潜在破坏性变更
- [[concepts/edition-support-window|版本支持窗口]]：protoc 与插件声明的 Edition 支持范围
- [[concepts/edition-patches|版本补丁]]：因前向/后向兼容假设变化而重新引入的应急机制
- [[concepts/predictability|可预测性]]：将特性生命周期与版本绑定的主要收益
- [[concepts/deprecation-warning|弃用警告]]：特性弃用时 protoc 发出的自定义提示
- [[concepts/garbage-collection|代码清理]]：与版本支持窗口强绑定的特性相关代码移除能力
- [[concepts/backward-compatibility|向后兼容性]] 与 [[concepts/forward-compatibility|向前兼容性]]：新设计所改变的原有假设
- [[concepts/edition-upgrade|版本升级]]：可能成为潜在破坏性变更的操作
- [[concepts/edition-naming|Edition Naming]]：本文参考的更严格命名方案
- [[concepts/life-of-an-edition|Life of an Edition]]：本文作为基础的早期设计文档
- [[concepts/editions-life-of-a-feature|Editions: Life of a Feature]]：与 Life of an Edition 对立的替代愿景
- [[concepts/protobuf-editions-design-features|Protobuf Editions Design: Features]]：本文参考的原始设计文档
- [[concepts/editions-feature-visibility|Editions Feature Visibility]]：支撑补丁可行性论证的相关决策

## 要点
- 当前 Protocol Buffers 中 Editions 与 Features 几乎相互独立，每个 Edition 仅是所有 Feature 默认值的集合，该设计在仅有 2023 一个版本时运作良好，但无法应对多版本演进。
- 文档建议在 Feature 规范中新增四个字段：`edition_introduced`、`edition_deprecated`、`deprecation_warning`、`edition_removed`，将特性生命周期绑定到具体版本。
- 文档建议新增 [[concepts/edition_legacy|EDITION_LEGACY]] 作为"无限过去"占位版本，标记早于特性引入时的 noop 默认行为。
- 强烈建议在 [[concepts/edition-2024|Edition 2024]] 发布前尽快实施该方案，因为 2024 中新增的任何特性将默认可在 2023 中使用，增加验证复杂度。
- 动态消息运行时验证推荐方案是在 [[concepts/featureseteditiondefault|FeatureSetEditionDefault]] 中新增 `overridable_features` 和 `fixed_features` 两个字段，运行时通过简单合并与断言完成特性窗口检查，无需反射式遍历。
- 由于特性生命周期与版本绑定，[[concepts/edition-upgrade|版本升级]]可能变成潜在的破坏性变更；但这与 [[entities/google3|google3]] 中删除特性所需的烧除工作并无本质区别。
- 因假设发生变化（版本不再完全前向/后向兼容），文档重新引入 [[concepts/edition-patches|补丁版本（edition_patch）]] 概念作为应急修复机制。