---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-json-handling]]"]
tags: [standard]
aliases:
  - "json_format feature"
  - "JSON 格式特性"
  - "JSON Format Feature"
---


# json_format feature

## 定义
`json_format` 是本文档建议在 [[concepts/edition-zero|Edition Zero]] 中新增的一个三态（tri-state）特性，用于统一 Proto2 和 Proto3 中 JSON 字段名冲突（JSON Field Name Conflicts）的处理行为。该特性可以取三个枚举值：`ALLOW`、`DISALLOW` 或 `LEGACY_BEST_EFFORT`，分别对应不同的 JSON 编码与验证语义。

## 关键特征
- **三态取值**：
  - `ALLOW`：完全验证 JSON 编码与字段名的一致性（对应 proto3 行为）。
  - `DISALLOW`：禁止 JSON 编码并禁止所有相关验证。
  - `LEGACY_BEST_EFFORT`：验证正确性但不验证唯一性，冲突仅发出警告（对应 proto2 行为）。
- **多层级声明**：该特性在消息（message）、枚举（enum）和文件（file）级别均可用，但主要面向消息和枚举。
- **迁移兼容**：从 proto2/proto3 迁移至 Editions 时，会根据源文件的 `syntax` 和 `deprecated_legacy_json_field_conflicts` 选项自动转换为对应的 `json_format` 值。
- **属于 Edition Zero 特性集合**：`json_format` 被列入 Edition Zero 的特性列表，作为 Editions 标准化 JSON 行为的一部分。

## 应用
- 解决 Proto2 与 Proto3 在 JSON 编码时对字段名冲突的不同处理策略。
- 在迁移至 Editions 的过程中，自动保留原有 JSON 序列化语义，避免破坏现有客户端。
- 当某些消息不需要 JSON 支持时，可通过 `DISALLOW` 明确禁用以避免运行时开销或误用。
- 当需要保留宽松的、向后兼容的 JSON 行为时，可选择 `LEGACY_BEST_EFFORT`。

## 相关概念
- [[concepts/allow|ALLOW]]
- [[concepts/disallow|DISALLOW]]
- [[concepts/legacy_best_effort|LEGACY_BEST_EFFORT]]
- [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]]
- [[concepts/edition-zero-features|Edition Zero features]]

## 相关实体
- [[entities/edition-zero|Edition Zero]]
- [[entities/protobuf|Protobuf]]

## 来源提及
- "We recommend adding a new `json_format` feature as part of Edition Zero features." — [[sources/editions-edition-zero-json-handling]]
- "This feature will target messages and enums, but we will also provide it at the file level for convenience." — [[sources/editions-edition-zero-json-handling]]