---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]"]
tags: [term]
aliases:
  - "DISALLOW json_format"
  - "DISALLOW 模式"
---


# DISALLOW

## 定义
`DISALLOW`是 Protobuf Editions 中`json_format` feature 的三个可能状态之一。它是一种新模式，用于显式禁止 JSON 编码并禁用所有与 JSON 映射相关的验证。当在顶层消息上设置该特性时，所有运行时会拒绝对该消息进行任何 JSON 解析或序列化操作。这提供了一种不涉及 schema 更改的`LEGACY_BEST_EFFORT`替代方案。

## 关键特征
- 属于`json_format` feature 的三种合法状态之一（与`ALLOW`、`LEGACY_BEST_EFFORT`并列）
- 显式禁止 JSON 编码行为，禁用所有与 JSON 映射相关的验证逻辑
- 在顶层消息上设置后，所有运行时会拒绝对该消息进行任何 JSON 解析或序列化操作
- 作为`LEGACY_BEST_EFFORT`的替代方案，无需修改 schema 即可达到禁止 JSON 编码的目的
- 设计约束：`ALLOW`消息不能在其消息树中任何位置包含`DISALLOW`类型，包括扩展字段，否则会导致编译错误
- 是一种新引入的显式语义模式，并非通过隐式推断得到

## 应用
- 在 Protobuf Editions（特别是 Edition Zero）中用于明确声明某消息不支持 JSON 编码
- 当某个消息需要完全禁止 JSON 解析与序列化时，作为最严格的 JSON 处理策略
- 为需要明确禁止 JSON 转换的使用场景提供比`LEGACY_BEST_EFFORT`更清晰的语义
- 在消息树中防止`DISALLOW`与`ALLOW`混合使用，确保 JSON 处理策略的一致性

## 相关概念
- [[concepts/ALLOW|ALLOW]]
- [[concepts/LEGACY_BEST_EFFORT|LEGACY_BEST_EFFORT]]
- [[concepts/json_format feature|json_format feature]]
- [[concepts/JSON Field Name Conflicts|JSON Field Name Conflicts]]

## 相关实体
- [[entities/Protobuf|Protobuf]]

## 来源提及
- `DISALLOW` - Alternatively, we will ban JSON encoding and disable all validation related to JSON mappings. — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]
- All runtimes will fail to parse or serialize any messages to/from JSON when this feature is set on the top-level messages. — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]