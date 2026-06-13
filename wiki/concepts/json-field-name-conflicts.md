---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]"]
tags: [phenomenon]
aliases:
  - "JSON 字段名冲突"
  - "JSON Field Name Conflicts"
---


# JSON Field Name Conflicts

## 定义
JSON Field Name Conflicts（JSON 字段名冲突）是指在 Protobuf 中，由于多个 proto 字段映射到同一个 JSON 字段名而产生的冲突现象。其根源在于默认的 CamelCase 字段名转换机制并不保证唯一性，同时 `json_name` 字段选项允许进一步自定义 JSON 名称，从而可能引入额外的命名冲突。

## 关键特征
- **冲突根源**：默认的 CamelCase 字段名转换不保证全局唯一；`json_name` 选项允许用户自定义 JSON 名称，进一步加剧冲突可能性。
- **proto3 行为**：在编译期因冲突而报错，拒绝生成代码。
- **proto2 行为**：采用尽力而为（best-effort）解析，允许生成代码但产生跨运行时不一致的未定义行为。
- **直接结果**：冲突的映射会产生带有重复键（duplicate keys）的 JSON 输出。
- **设计动因**：该问题正是推动 Edition Zero JSON 处理设计提案的核心动因。

## 应用
- 作为 Edition Zero 中 JSON 处理语义设计的核心问题域。
- 推动 `json_format` feature、`json_name` 字段选项以及 `ALLOW`、`LEGACY_BEST_EFFORT` 等兼容性策略的提出与权衡。
- 为 Protobuf Editions 体系下 JSON 序列化行为的统一与规范化提供依据。

## 相关概念
- [[concepts/json-format-feature|json_format feature]]
- [[concepts/json-name-field-option|json_name field option]]
- [[concepts/ALLOW|ALLOW]]
- [[concepts/LEGACY-BEST-EFFORT|LEGACY_BEST_EFFORT]]

## 相关实体
- [[entities/Protobuf|Protobuf]]

## 来源提及
- "This is laid out in more detail by JSON Field Name Conflicts (not available externally)." — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]
- "Conflicting mappings will produce JSON with duplicate keys" — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]