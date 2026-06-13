---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]"]
tags: [term]
aliases:
  - "json_format ALLOW"
  - "ALLOW 状态"
---


# ALLOW

## 定义
`ALLOW` 是 [[concepts/json-format-feature|json_format feature]] 的三个可能状态之一，代表默认行为：字段在 proto 解析时会被完全验证，任何冲突的 JSON 映射都会触发 protoc 错误以保证唯一性。该行为与当前 proto3 的默认行为一致，且不需要运行时更改，因为 JSON 解析/序列化本身是被允许的。在迁移方案中，原 proto2/proto3 文件将根据其配置迁移到 `ALLOW` 或 [[concepts/LEGACY-BEST-EFFORT|LEGACY_BEST_EFFORT]] 状态。

## 关键特征
- **完全验证**：在 proto 解析阶段对字段进行严格验证，确保所有 JSON 映射的冲突能被捕获。
- **编译期错误**：任何冲突的 JSON 映射都会触发 `protoc` 错误，从而保证字段映射的唯一性。
- **零运行时影响**：不需要运行时更改，JSON 解析与序列化在该状态下被允许。
- **行为一致性**：与当前 proto3 的默认行为保持一致。
- **迁移目标之一**：在 proto2/proto3 向 Editions 迁移时，是两个目标状态之一（另一个为 `LEGACY_BEST_EFFORT`）。

## 应用
- 作为 [[concepts/json-format-feature|json_format feature]] 的默认状态，适用于需要严格保证 JSON 字段映射唯一性的场景。
- 在 [[concepts/Editions|Editions]] 迁移过程中，作为原 proto2/proto3 文件的目标状态之一。
- 适用于需要 protoc 编译期验证来防止 [[concepts/JSON-Field-Name-Conflicts|JSON Field Name Conflicts]] 的项目。

## 相关概念
- [[concepts/DISALLOW|DISALLOW]]
- [[concepts/LEGACY-BEST-EFFORT|LEGACY_BEST_EFFORT]]
- [[concepts/json-format-feature|json_format feature]]
- [[concepts/JSON-Field-Name-Conflicts|JSON Field Name Conflicts]]

## 相关实体
- [[entities/Protobuf|Protobuf]]

## 来源提及
- "`ALLOW` - By default, fields will be fully validated during proto parsing. Any conflicting JSON mappings will trigger protoc errors, guaranteeing uniqueness." — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]
- "This will be consistent with the current proto3 behavior. No runtime changes are needed, since we allow JSON parsing/serialization." — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]