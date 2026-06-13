---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-edition-zero-json-handling]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "standard"
aliases:
  - "json_format feature"
  - "JSON 格式特性"
  - "JSON Format Feature"
  - "features.json_format"
  - "json_format feature"
  - "JSON 格式特性"
  - "JSON Format Feature"
---

## Description
`json_format` 是 [[concepts/edition-zero|Edition Zero]] 引入的用于统一 Proto2 与 Proto3 中 [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]] 处理行为的三态（tri-state）特性，但根据 [[sources/editions-edition-zero-features|editions-edition-zero-features]] 源文档描述，其实际取值为 `ALLOW` 与 `LEGACY_BEST_EFFORT` 两种状态（[[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]] 文档中额外提到了 `DISALLOW`）。其中 `ALLOW` 为默认值，意味着运行时必须支持 JSON 的解析与序列化，并会在 proto 层校验 proto 与 JSON 之间是否存在良好（well-defined）的映射，对应当前的 proto3 行为；`LEGACY_BEST_EFFORT` 则让运行时尽力而为地解析与序列化 JSON，允许 proto 与 JSON 之间存在多对一或一对多等无明确定义的映射关系，主要用于需要该行为的 proto2 文件（例如设置了 `deprecated_legacy_json_field_conflicts` 选项的文件）。该特性主要面向消息（message）和枚举（enum），但为方便使用同时也在文件（file）级别提供。在从 proto2/proto3 迁移至 Editions 的过程中，系统会根据源文件的 `syntax` 与 `deprecated_legacy_json_field_conflicts` 选项自动转换为对应的 `json_format` 值，从而保留原有的 JSON 序列化语义，避免破坏现有客户端。

## Related Concepts
- [[concepts/allow|ALLOW]]
- [[concepts/disallow|DISALLOW]]
- [[concepts/legacy_best_effort|LEGACY_BEST_EFFORT]]
- [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]]
- [[concepts/edition-zero-features|Edition Zero features]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/proto3-syntax|proto3 syntax]]
- [[concepts/proto2-syntax|proto2 syntax]]
- [[concepts/protobuf-editions|Protobuf Editions]]

## Related Entities
- [[entities/edition-zero|Edition Zero]]
- [[entities/protobuf|Protobuf]]

## Mentions in Source
> **Source: [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]**
> - "We recommend adding a new `json_format` feature as part of Edition Zero features."
> - "This feature will target messages and enums, but we will also provide it at the file level for convenience."

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "ALLOW - this means that a runtime must allow JSON parsing and serialization. Checks will be applied at the proto level to make sure that there is a well-defined mapping to JSON."
> - "The default will be `ALLOW`, which maps the to the current proto3 behavior."