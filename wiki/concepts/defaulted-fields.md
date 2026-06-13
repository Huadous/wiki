---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-features|editions-edition-zero-features]]"]
tags: [term]
aliases:
  - "defaulted field"
  - "default value field"
---


# defaulted fields

## 定义
`defaulted` 是 proto3 中与 `required` 对应的字段规约概念。在 proto3 中，`defaulted` 字段不允许自定义默认值；并且对于消息类型（message-typed）字段，`defaulted` 是 `optional` 的同义词。proto2 中不存在 `defaulted` 这一概念。

## 关键特征
- proto3 引入的关键字概念，proto2 中没有此概念
- 与 proto2 的 `required` 关键字在语义上对偶
- 不允许在 `defaulted` 字段上自定义默认值
- 对消息类型字段而言，`defaulted` 等价于 `optional`
- 在 Editions 设计过程中，曾在 alternatives 中讨论过允许 `required`/`optional` 并将 `defaulted` 引入为真正的关键字
- 最终方案选择完全消除这些关键字，转而使用基于 features 的注解系统

## 应用
- 在 proto3 语法体系中表达字段规约语义，与 `required`/`optional` 形成对照
- 在 Protobuf Editions 设计的 alternatives 讨论阶段，作为评估字段存在性（field presence）表达方式的备选方案出现
- 与 Edition Zero 的 features 设计（EXPLICIT presence 等）形成对比，展示了从关键字语法向 features 注解系统的迁移路径

## 相关概念
- [[concepts/required-keyword|required keyword]]
- [[concepts/optional-keyword|optional keyword]]
- [[concepts/proto3-syntax|proto3 syntax]]
- [[concepts/explicit-presence|EXPLICIT presence]]

## 相关实体
（无相关实体）

## 来源提及
- Required. Proto2 has `required` but not `defaulted`; Proto3 has `defaulted` but not `required`. Proto3 also does not allow custom defaults on `defaulted` fields, and on message-typed fields, `defaulted` is a synonym for `optional`. — [[sources/editions-edition-zero-features|editions-edition-zero-features]]