---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [standard]
aliases:
  - "feature_support"
  - "FeatureSupport 元数据"
---


# FeatureSupport

## 定义
FeatureSupport 是 [[sources/editions-edition-lifetimes|editions-edition-lifetimes]] 文档建议在 `FieldOptions` 中新增的一组字段选项结构，用于编码每个特性（feature）的生命周期信息。它由四个字段组成：`edition_introduced`（特性引入版本）、`edition_deprecated`（特性弃用版本）、`deprecation_warning`（弃用警告文本）和 `edition_removed`（特性删除版本）。

## 关键特征
- 包含四个字段：引入版本、弃用版本、弃用警告文本、删除版本
- 作为 `FieldOptions` 中的扩展选项存在，与特性规范绑定
- 由 [[entities/protoc|protoc]] 编译器与运行时共同读取与解释
- 用于在编译期与运行期表达特性的引入、弃用与删除三个阶段
- 与 [[concepts/Feature-Lifetimes|Feature Lifetimes]] 设计理念紧密耦合

## 应用
- 特性生命周期验证：[[entities/protoc|protoc]] 根据 `edition_introduced` 校验特性是否在当前 edition 中可用
- 弃用警告触发：运行时检测到 `edition_deprecated` 命中后输出 `deprecation_warning` 文本
- 已删除特性拦截：当用户使用的 edition ≥ `edition_removed` 时，禁止对已删除特性进行覆盖
- 为 [[concepts/FeatureSet|FeatureSet]] 与 [[concepts/Edition-Lifetimes|Edition Lifetimes]] 提供细粒度的元数据支撑
- 在 [[concepts/EDITION-LEGACY|EDITION_LEGACY]] 迁移至新 edition 的过程中辅助行为兼容判定

## 相关概念
- [[concepts/Feature-Lifetimes|Feature Lifetimes]]
- [[concepts/EDITION-LEGACY|EDITION_LEGACY]]
- [[concepts/FeatureSet|FeatureSet]]
- [[concepts/Edition-Lifetimes|Edition Lifetimes]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "We recommend adding four new field options to be used in feature specifications: `edition_introduced`, `edition_deprecated`, `deprecation_warning`, and `edition_removed`." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]