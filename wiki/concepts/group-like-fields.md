---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-group-migration-issues|editions-group-migration-issues]]"]
tags: [term]
aliases:
  - "group-like fields"
  - "group-like"
---


# Group-like fields

## 定义
Group-like fields 是 Smooth Extension 方案中定义的概念性字段类别，指同时满足以下三个条件的字段：具有 DELIMITED 编码、类型对应于其所在消息直接嵌套的子消息、名称对应于其类型名的小写形式。Proto2 中的所有 group 都会自动满足此定义，因此会保留原有的 proto2 行为。

## 关键特征
- 编码方式为 DELIMITED（定界编码）
- 字段类型为所在消息直接嵌套的子消息
- 字段名称为其类型名称的小写形式
- 由于第 2 和第 3 个条件以及禁止重复字段名的规则，可以保证代码生成和文本编码中不会出现符号冲突

## 应用
- 作为 Protobuf Editions 迁移过程中区分传统 group 行为与新增显式 `group` 关键字字段的判定依据
- 用于识别和保留 proto2 中已有 group 字段在 Editions 下的兼容行为
- 为代码生成器和文本格式编码器提供无歧义的命名与符号映射规则

## 相关概念
- [[concepts/smooth-extension|Smooth Extension]]
- [[concepts/group-fields|Group fields]]
- [[concepts/delimited-encoding|Delimited encoding]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/edition-2023|Edition 2023]]

## 来源提及
- We would define a "group-like" concept, which applies to all fields which: Have `DELIMITED` encoding, Have a type corresponding to a nested message directly under its containing message, Have a name corresponding to its lowercased type name. — [[sources/editions-group-migration-issues|editions-group-migration-issues]]
- Note that proto2 groups will always be "group-like." — [[sources/editions-group-migration-issues|editions-group-migration-issues]]