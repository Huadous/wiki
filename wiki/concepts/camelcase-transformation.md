---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-json-handling]]"]
tags: [method]
aliases:
  - "CamelCase转换"
  - "Proto CamelCase 转换"
  - "CamelCase Naming Convention"
---


# CamelCase transformation

## 定义
CamelCase transformation 是 [[entities/Protobuf|Protobuf]] 默认的字段名到 JSON 名的转换机制。该机制将每个 proto 字段名（如 `my_field_name`）转换为 CamelCase 格式（如 `myFieldName`），作为 proto 字段在 JSON 序列化/反序列化时所使用的默认名称。

## 关键特征
- **默认转换机制**：在未显式指定其他选项时，CamelCase 转换是 proto 字段名映射到 JSON 字段名的默认行为。
- **合法性保证**：转换结果在 JSON 中保证是合法的标识符名称。
- **非唯一性**：转换结果并不保证唯一性，多个不同的 proto 字段名（如 `my_field_name` 和 `MyFieldName`）可能映射到同一 JSON 名（如 `myFieldName`）。
- **冲突根源**：这种非唯一性是 [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]] 问题的主要根源之一。
- **可被覆盖**：可以通过 [[concepts/json-name-field-option|json_name field option]] 为单个字段显式指定 JSON 名，从而绕过默认的 CamelCase 转换行为。

## 应用
- **proto 字段的 JSON 序列化**：在 Protocol Buffers 将消息序列化为 JSON 时，默认采用 CamelCase transformation 将每个 proto 字段名转换为对应的 JSON 字段名。
- **proto 字段的 JSON 反序列化**：在从 JSON 数据反序列化为 proto 消息时，CamelCase transformation 用于将 JSON 字段名解析回 proto 字段。
- **跨语言互操作**：JSON 是语言无关的数据交换格式，CamelCase 命名风格更符合 JavaScript/TypeScript 等前端语言的命名约定，便于 Web 端消费 protobuf 数据。

## 相关概念
- [[concepts/json-name-field-option|json_name field option]]
- [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]]
- [[concepts/json-format-feature|json_format feature]]

## 相关实体
- [[entities/Protobuf|Protobuf]]

## 来源提及
- "Today, by default, we transform each field name to a CamelCase name that will always be valid, but not necessarily unique in JSON."（目前，默认情况下，我们将每个字段名转换为一个 CamelCase 名称，该名称在 JSON 中始终是合法的，但并不保证唯一。） — [[sources/editions-edition-zero-json-handling]]
- "We also support a `json_name` field option to override this for JSON parsing/serialization."（我们还支持 `json_name` 字段选项，用于在 JSON 解析/序列化时覆盖此默认行为。） — [[sources/editions-edition-zero-json-handling]]