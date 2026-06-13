---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]"]
tags: [term]
aliases:
  - "LEGACY_BEST_EFFORT"
  - "Legacy Best Effort"
---


# LEGACY_BEST_EFFORT

## 定义
`LEGACY_BEST_EFFORT` 是 [[concepts/json_format feature|json_format feature]] 的三个可能状态之一，代表一种兼容性行为：字段会验证正确性但不验证唯一性，冲突的 JSON 映射会触发 protoc 警告而非错误。该状态与当前 proto2 行为一致，或对应 proto3 设置了 `deprecated_legacy_json_field_conflicts` 选项的情况。由于该行为本质上属于需要被消除的未定义行为，文档建议未来通过平行工作予以移除。

## 关键特征
- 字段验证正确性，但不验证唯一性
- 冲突的 JSON 映射会触发 protoc 警告而非错误
- 与当前 proto2 行为一致
- 在 proto3 中，对应设置了 `deprecated_legacy_json_field_conflicts` 选项的情况
- 本质上属于需要被消除的未定义行为，文档建议未来移除
- 该状态下仍允许 JSON 的解析与序列化

## 应用
- 作为 [[concepts/json_format feature|json_format feature]] 的状态选项之一，用于在 [[entities/Protobuf|Protobuf]] Editions 中控制 JSON 字段冲突的处理策略
- 用于维持与 proto2 现有行为的向后兼容
- 在 proto3 中作为 [[concepts/deprecated_legacy_json_field_conflicts|deprecated_legacy_json_field_conflicts]] 开启时的对应行为
- 在 [[concepts/JSON Field Name Conflicts|JSON Field Name Conflicts]] 场景下，提供宽松的兼容性处理（仅警告而非报错）

## 相关概念
- [[concepts/ALLOW|ALLOW]]
- [[concepts/DISALLOW|DISALLOW]]
- [[concepts/deprecated_legacy_json_field_conflicts|deprecated_legacy_json_field_conflicts]]
- [[concepts/json_format feature|json_format feature]]
- [[concepts/JSON Field Name Conflicts|JSON Field Name Conflicts]]

## 相关实体
- [[entities/Protobuf|Protobuf]]

## 来源提及
- `LEGACY_BEST_EFFORT` - Fields will be validated for correctness, but not for uniqueness. — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]
- This will be consistent with the current proto2 behavior, or proto3 where `deprecated_legacy_json_field_conflicts` is set. — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]