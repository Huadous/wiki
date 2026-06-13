---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]"]
tags: [term]
aliases:
  - "OptionTargetType"
  - "TargetType 枚举"
---


# OptionTargetType

## 定义
OptionTargetType 是 Protobuf Editions 提案中定义在 `FieldOptions` 内部的枚举类型，用于规定 `target` 属性可取的合法取值，从而限定 `Target Attributes` 所引用的具体 schema 元素种类。

## 关键特征
- 枚举定义位于 `FieldOptions` 内部，作为 `target` 字段的类型约束。
- 包含以下枚举值：
  - `TARGET_TYPE_UNKNOWN` (0) — 视为缺省（absent）
  - `TARGET_TYPE_FILE` (1)
  - `TARGET_TYPE_EXTENSION_RANGE` (2)
  - `TARGET_TYPE_MESSAGE` (3)
  - `TARGET_TYPE_FIELD` (4)
  - `TARGET_TYPE_ONEOF` (5)
  - `TARGET_TYPE_ENUM` (6)
  - `TARGET_TYPE_ENUM_VALUE` (7)
  - `TARGET_TYPE_SERVICE` (8)
  - `TARGET_TYPE_METHOD` (9)
- 最初批准的提案中，枚举值并未添加作用域前缀（如 `TARGET_TYPE_` 之外的命名空间限定）。
- 早期提案版本中曾包含 `STREAM` 条目，但因相关语法被移除而最终从枚举中删除。

## 应用
- 在 Protobuf Editions 模式下，与 `target` 属性配合使用，指明某条 `Target Attributes` 规则所引用的目标 schema 元素（如文件、消息、字段、服务等）的种类。
- 由编译器（如 [[entities/protoc|protoc]]）在解析与校验 `Target Attributes` 时使用，以确保 `target` 指向的实体类型与声明一致。
- 与 [[concepts/feature-retention|FeatureRetention]] 等基于 `FieldOptions` 的机制共同构成 Editions 的元信息层。

## 相关概念
- [[concepts/target-attributes|Target Attributes]]
- [[concepts/field-options|FieldOptions]]
- [[concepts/feature-retention|FeatureRetention]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- `TARGET_TYPE_UNKNOWN` will be treated as absent. — [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]
- The enum values did not have a scoping prefix. — [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]