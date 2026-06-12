---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/features]]"]
tags: [term]
aliases:
  - "Scope levels"
  - "Feature scope"
  - "特性设置作用域"
---


# Feature setting scope

## 定义
Feature setting scope 是 Protobuf Editions 中定义 feature 可应用层次的术语，将代码结构分为四个级别：file-level（文件级）、non-nested（非嵌套：消息、枚举、服务）、nested（嵌套：oneof、嵌套消息、枚举）和 lowest-level（最低级：字段、扩展、枚举值、扩展范围、方法）。每个 feature 只能应用于特定的 scope，下层设置会覆盖上层设置，形成层次化的特性配置模型。

## 关键特征
- **四层分级体系**：从文件级到最低级，共有四个明确的 scope 层次，覆盖 Protobuf 定义中所有元素类型。
- **继承与覆盖机制**：下层 scope 设置可以覆盖上层 scope 的设置，未设置的元素继承上级作用域的配置。
- **scope 约束性**：每个 feature 只能应用于其定义的 scope 范围内，如 `features.field_presence` 可应用于 file 和 field 级别，但不能应用于其他层级。
- **语义精确性**：scope 决定了 feature 设置的影响范围及其可被覆盖的层级关系，确保配置的直观性和一致性。

## 应用
- **文件级默认配置**：在 `.proto` 文件顶部设置文件级别 feature，为整个文件提供默认行为。例如设置 `features.default_symbol_visibility` 为文件级，控制文件内所有符号的默认可见性。
- **消息/枚举/服务级覆盖**：在消息、枚举或服务定义内部覆盖文件级的 feature 设置，实现局部定制。例如在特定消息内覆盖 `features.field_presence` 设置。
- **嵌套结构细化**：在嵌套消息、枚举或 oneof 内部进一步覆盖配置，实现更精细的控制。
- **字段/枚举值级精细化**：在最低级直接为字段、枚举值等元素应用特定 feature 设置，提供最大粒度的配置能力。

## 相关概念
- [[concepts/features-field_presence|features.field_presence]]
- [[concepts/features-default_symbol_visibility|features.default_symbol_visibility]]
- [[concepts/features-enforce_naming_style|features.enforce_naming_style]]

## 相关实体
- [[entities/protocol-buffers|protobuf]]

## 来源提及
- "Feature settings apply at different levels: File-level: These settings apply to all elements (messages, fields, enums, and so on) that don't have an overriding setting. Non-nested: Messages, enums, and services can override settings made at the file level. They apply to everything within them (message fields, enum values) that aren't overridden, but don't apply to other parallel messages and enums. Nested: Oneofs, messages, and enums can override settings from..." — [[protobuf/features|features]]