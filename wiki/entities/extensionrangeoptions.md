---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]"]
tags: [other]
aliases:
  - "ExtensionRangeOptions message type"
---


# ExtensionRangeOptions

## 基本信息
- Type: other
- Source: [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]

## 描述
ExtensionRangeOptions 是定义在 `descriptor.proto` 中的一个具体消息类型，用于承载应用于 protobuf 扩展范围（extension range）的选项。其内部 `Metadata` 字段是讨论保留期（retention）属性的关键案例：源文档指出，如果该 `Metadata` 字段被标注为 `SOURCE` 保留期而非默认的 `RUNTIME` 保留期，则可实现显著的二进制大小节省，因为扩展的元数据主要被代码生成器和 protoc 所使用，而非运行时。此前这种行为是针对单个字段进行特殊处理的，但该方案缺乏良好的可扩展性；因此保留期属性需要直接在 [[entities/FieldOptions|FieldOptions]] 层级提供一种通用、可扩展的机制。ExtensionRangeOptions 作为一个具体的、现实的示例，论证了为什么保留期属性应当被纳入通用的 FieldOptions 设计，而不是仅仅作为 editions 特性来使用。它与 [[concepts/retention|Retention]] 和 [[concepts/options-attributes|Options Attributes]] 概念紧密相关。

## 相关实体
- [[entities/FieldOptions|FieldOptions]]

## 相关概念
- [[concepts/retention|Retention]]
- [[concepts/options-attributes|Options Attributes]]

## 来源提及
- "significant savings in binary sizes could be realized if `ExtensionRangeOptions::Metadata` had only `SOURCE` retention." — [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]
- "Previously, we have specifically special-cased this behavior on a per-field basis, which does work but does not provide good extensibility." — [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]