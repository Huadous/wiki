---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-edition-zero-json-handling.md]]"]
tags: [term]
aliases:
  - "json_name field option"
  - "json_name 选项"
---


# json_name field option

## 定义
`json_name` 是 Protobuf 中的一个字段级选项（field option），用于在 JSON 解析与序列化过程中覆盖默认的 CamelCase 字段名转换规则，使开发者能够显式指定该字段在 JSON 表示中所使用的名称。

## 关键特征
- **字段级选项**：作为 `FieldOptions` 扩展作用于单个 proto 字段，而非整个消息或文件。
- **覆盖默认转换**：默认情况下，Protobuf 使用 CamelCase 转换规则将 proto 字段名映射为 JSON 字段名；`json_name` 可对此进行显式覆盖。
- **冲突根源**：若多个 proto 字段通过 `json_name`（或经 CamelCase 转换后）映射到相同的 JSON 名称，便会触发 [[concepts/JSON Field Name Conflicts|JSON Field Name Conflicts]]。
- **proto2 与 proto3 行为差异**：
  - proto2 仅在两个冲突字段**均**显式设置了 `json_name` 时，才在解析阶段报错。
  - proto3 则在 proto 解析时即严格检查所有冲突，无论文段是否设置了 `json_name`。

## 应用
- 在需要与现有 JSON API 保持兼容的场景中，通过 `json_name` 将 proto 字段映射为不同的 JSON 名称（例如保留下划线命名或沿用遗留命名）。
- 在 Editions 设计中，作为评估 JSON 兼容性与收紧 Schema 检查的关键选项之一，参见 [[sources/editions-stricter-schemas-with-editions|Stricter Schemas with Editions]]。
- 配合 [[concepts/deprecated_legacy_json_field_conflicts|deprecated_legacy_json_field_conflicts]] 选项使用，以在过渡期内容忍历史遗留的 JSON 名称冲突。
- 与 [[concepts/json_format feature|json_format feature]]（Editions 中的 JSON 特性）联合定义消息在 JSON 序列化时的字段命名行为。

## 相关概念
- [[concepts/JSON Field Name Conflicts|JSON Field Name Conflicts]]
- [[concepts/CamelCase transformation|CamelCase transformation]]
- [[concepts/deprecated_legacy_json_field_conflicts|deprecated_legacy_json_field_conflicts]]
- [[concepts/json_format feature|json_format feature]]

## 相关实体
- [[entities/Protobuf|Protobuf]]

## 来源提及
- "We also support a `json_name` field option to override this for JSON parsing/serialization." — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]
- "Proto2 files will only fail to parse if both of the conflicts fields have `json_name` set" — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]