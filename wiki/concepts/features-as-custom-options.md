---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-features|editions-edition-zero-features]]"]
tags: [method]
aliases:
  - "Features-as-options syntax"
  - "features-as-options"
---


# Features as Custom Options

## 定义
Features as Custom Options 是 Protobuf Editions Zero 中用于表达 feature flag 的语法方案。该方案将所有 feature 以字段的形式集中声明在一个单独的 `Features` 消息中，并借助 Protobuf 已有的 custom options 机制承载这些字段。该语法被描述为从事 Editions 工作的各方之间的主流共识，因为它天然支持 enum 类型的 feature，并能无缝接入现有的 options 体系。

## 关键特征
- **统一的消息载体**：所有 feature 都作为字段挂在单一的 `Features` 消息上，而不是分散在各处。
- **基于 custom options**：借助 Protobuf 既有的 custom options 机制承载 feature 字段定义，无需引入新的语法或运行时结构。
- **支持 enum 类型 feature**：天然允许 feature 字段使用 enum 类型，从而表达多档可选状态（如字段存在性策略、编码方式等）。
- **运行时保留**：`Features` 上的 feature 字段以 `retention = RUNTIME` 标注，确保在运行时仍可读取。
- **显式 `target` 标注**：每个 feature 字段通过 `target` 注解限定其作用范围（如目标类型或目标实体）。
- **语法形态已定，命名仍可微调**：语法载体本身是 settled 的；具体 feature 字段的名称（如 `features.field_presence`、`features.enum_type`）则被明确定义为 "matter of bikeshedding"（细节打磨范畴）。

## 应用
- 作为 Edition Zero 文档说明 feature 时的标准语法，方便在原型设计阶段统一讨论和示例化。
- 用以在 Protobuf Editions 中表达多种 feature flag，例如：
  - [[concepts/features-field-presence|features.field_presence]] — 字段存在性策略
  - [[concepts/features-enum-type|features.enum_type]] — enum 值类型相关 feature
  - [[concepts/features-repeated-field-encoding|features.repeated_field_encoding]] — repeated 字段编码方式
  - [[concepts/features-string-field-validation|features.string_field_validation]] — 字符串字段校验
  - [[concepts/features-message-encoding|features.message_encoding]] — 消息编码方式
  - [[concepts/features-json-format|features.json_format]] — JSON 格式相关 feature
- 作为后续讨论 [[concepts/Field option attributes|Field option attributes]]（`target` 与 `retention`）时的承载示例。

## 相关概念
- [[concepts/Field option attributes|Field option attributes]]
- [[concepts/features-field-presence|features.field_presence]]
- [[concepts/features-enum-type|features.enum_type]]
- [[concepts/features-repeated-field-encoding|features.repeated_field_encoding]]
- [[concepts/features-string-field-validation|features.string_field_validation]]
- [[concepts/features-message-encoding|features.message_encoding]]
- [[concepts/features-json-format|features.json_format]]

## 相关实体
- [[entities/Features-message|Features message]]
- [[entities/Protobuf-Editions|Protobuf Editions]]

## 来源提及
- For the purposes of this document, we will use the syntax described in *Features as Custom Options*, since it is the prevailing consensus among those working on editions, and allows us to have enum-typed features. — [[sources/editions-edition-zero-features|editions-edition-zero-features]]
- The exact names for the features are a matter of bikeshedding. — [[sources/editions-edition-zero-features|editions-edition-zero-features]]