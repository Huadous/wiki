---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [term]
aliases:
  - "deprecation_warning"
  - "特性弃用警告"
---


# Deprecation Warning

## 定义
Deprecation Warning 是 Protobuf Editions 文档中推荐在 feature 规范（feature specification）中新增的四个字段选项之一，与 `edition_introduced`、`edition_deprecated`、`edition_removed` 并列使用。它用于描述当一个 feature 进入弃用窗口时 protoc 应向用户发出的自定义提示信息。该字段独立于通用的 `deprecated` 选项，允许 feature 维护者写入诸如 "Feature do_something will be removed in edition 2027" 的具体迁移提醒。

## 关键特征
- **生命周期元数据之一**：与 `edition_introduced`、`edition_deprecated`、`edition_removed` 共同构成完整的特性生命周期元数据，使特性弃用成为一个可被显式建模与传达的过程。
- **自定义提示内容**：feature 维护者可自由填写具体的迁移提醒文本，而非依赖通用 `deprecated` 标记。
- **触发条件明确**：当 proto 文件的 edition 落在 `edition_deprecated` 之后但仍在 `edition_removed` 之前，且用户对被弃用特性进行了覆盖（override）时，protoc 触发该警告而非错误。
- **与通用 deprecated 区分**：作为字段级别的专用选项，独立于通用的 `deprecated` 字段存在。

## 应用
- 在 Protobuf Editions 的 feature 规范中标注弃用提示信息，例如提醒用户某特性将在特定 edition 中被移除。
- 为 proto 文件作者提供迁移引导，使其在特性仍可用期间收到明确的升级提示。
- 与 `edition_introduced` / `edition_deprecated` / `edition_removed` 协同使用，记录特性从引入、弃用到移除的完整时间线。

## 相关概念
- [[concepts/FeatureSupport|FeatureSupport]]
- [[concepts/Feature Lifetimes|Feature Lifetimes]]
- [[concepts/Edition Deprecation|Edition Deprecation]]
- [[concepts/Feature Removal|Feature Removal]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/Edition 2023|Edition 2023]]
- [[entities/Edition 2024|Edition 2024]]

## 来源提及
- "We recommend adding four new field options to be used in feature specifications: `edition_introduced`, `edition_deprecated`, `deprecation_warning`, and `edition_removed`. This will allow every feature to specify the edition it was introduced in, the edition it became deprecated in, when we expect to remove it (deprecation warnings), and the edition it actually becomes removed in." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]