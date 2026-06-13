---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]"]
tags: [term]
aliases:
  - "FieldDescriptorOptions"
  - "FieldOptions message type"
---


# FieldOptions

## 定义
FieldOptions 是 Protocol Buffers 在 `descriptor.proto` 中定义的标准选项消息类型，用于承载字段（field）级别的选项配置。在 [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]] 提案中，`target` 和 `retention` 属性被提议直接添加到 `FieldOptions` 中（提案文档中也将其称为 `FieldDescriptorOptions`，两者指代同一概念）。提案明确说明，虽然最初动机是为 Protobuf Editions 中的 features 服务，但由于这些属性具有通用效用，因此选择将其作为内建字段添加到 `FieldOptions` 而非通过自定义选项（custom options）实现。文档中给出了 `message FieldOptions` 的结构示例，其中包含 `optional OptionTargetType target = 17;` 的字段定义。

## 关键特征
- 属于 Protobuf 内建的标准选项消息类型，定义于 `descriptor.proto` 中
- 用于承载字段级别的选项配置，是字段描述符（FieldDescriptor）的元数据容器
- 提案中 `target` 字段的 tag 编号为 17，类型为 `OptionTargetType`（可选项）
- 同时容纳了与 Editions features 相关的通用属性（如 `target` 和 `retention`）
- 可通过自定义选项（custom options）扩展，等价方案可通过扩展机制实现

## 应用
- 在 Protobuf Editions 中作为字段级别的内建选项载体，与 [[concepts/Options Attributes|Options Attributes]] 配合使用
- 承载 [[concepts/Target Attributes|Target Attributes]]（`target`）和 [[concepts/Retention|Retention]] 等字段级配置
- 作为 [[concepts/Custom Options|Custom Options]] 的替代或补充机制，承载通用属性而无需额外扩展定义
- 在 [[entities/Protobuf Editions|Protobuf Editions]] 体系中定义字段的 [[concepts/FeatureRetention|FeatureRetention]] 等特性
- 与 [[concepts/OptionTargetType|OptionTargetType]] 枚举类型协同工作，指定选项的目标作用域

## 相关概念
- [[concepts/Options Attributes]]
- [[concepts/Target Attributes]]
- [[concepts/Retention]]
- [[concepts/Custom Options]]
- [[concepts/OptionTargetType]]
- [[concepts/FeatureRetention]]

## 相关实体
- [[entities/Protobuf Editions]]
- [[entities/protoc]]

## 来源提及
- "I believe they provide sufficient general utility that adding them directly to `FieldDescriptorOptions` is warranted." — [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]
- "Rather than building `retention` and `target` directly as fields of `FieldOptions`, we could use custom options to define an equivalent thing." — [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]