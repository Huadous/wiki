---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/style]]"]
tags: [term]
aliases:
  - "字段存在性特征"
  - "LEGACY_REQUIRED 特性集"
  - "Field Presence Feature Set"
---


# Field Presence feature (LEGACY_REQUIRED)

## 定义
Field presence feature 是 Protocol Buffers 中用于控制字段存在性语义的一组特性集。在 proto2 中，`required` 字段曾用于强制要求字段必须在解析时出现；proto3 中移除了 `required` 关键字；在 Editions 2023 中，通过将 `field_presence` 特性设置为 `LEGACY_REQUIRED` 来兼容 proto2 的 `required` 语义。该特性旨在帮助用户在 schema 演化过程中逐步淘汰 `required` 字段。

## 关键特征
- **兼容性桥接**：允许 proto2 中的 `required` 字段迁移到 Editions 2023 后保持原有行为，通过设置 `field_presence` 为 `LEGACY_REQUIRED`。
- **演化友好**：设计初衷是作为过渡方案，支持逐步移除 `required` 字段，因为 `required` 已被证明对长期 schema 演化有害。
- **风格禁忌**：官方风格指南强烈不推荐使用 `required` 字段，建议使用更灵活的 `field_presence` 特性替代。
- **解析行为**：`required` 字段在解析时，如果字段未出现会导致解析失败，而 `LEGACY_REQUIRED` 可保持这一行为以不破坏现有系统。

## 应用
- **proto2 到 Editions 2023 迁移**：当将旧有 proto2 schema 迁移到 Editions 2023 时，对于现有 `required` 字段，可通过设置 `field_presence = LEGACY_REQUIRED` 来保持向后兼容。
- **渐进式废弃**：团队可以先将 `required` 字段标记为 `LEGACY_REQUIRED`，然后逐步通过 schema 变更移除该特性。
- **跨版本兼容**：在混合使用 proto2 和 proto3/protobuf 新版本代码的环境里，有助于减少解析行为差异导致的错误。

## 相关概念
- [[concepts/required-fields|required fields]]
- [[concepts/groups|groups]]
- [[concepts/message-encoding-feature|message_encoding feature]]
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/field-presence|field_presence]]

## 相关实体
- [[entities/protobuf|Protocol Buffers]]

## 来源提及
- "Proto2 required fields that have been migrated to editions 2023 can use the field_presence feature set to LEGACY_REQUIRED to accommodate." — [[protobuf/style|style]]
- "Required fields are a way to enforce that a given field must be set when parsing wire bytes, and otherwise refuse to parse the message." — [[protobuf/style|style]]