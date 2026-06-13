---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]"]
tags: [standard]
aliases:
  - "Options Attributes"
  - "Options 属性设计"
  - "target and retention attributes"
---


# Options Attributes

## 定义
Options Attributes 指在 Protobuf Editions 设计提案中提出的两个新属性——`target` 和 `retention`——用于扩展 Protobuf 的选项（options）系统。`target` 指定某个选项可以应用到的语义实体（如 message、field、enum 等），`retention` 控制该选项在运行时描述符（descriptor）中的保留策略。这两个属性被提议直接添加到 `FieldDescriptorOptions` 中，对非选项字段表现为 no-op。其设计灵感直接来自 Java 注解中的 `@Target` 与 `@Retention` 概念。

## 关键特征
- 包含两个核心属性：`target` 与 `retention`
- `target` 用于声明选项可应用的目标语义实体（与 [[concepts/Target Attributes|Target Attributes]] 相关）
- `retention` 用于控制选项在运行时描述符中的可见性与保留策略（与 [[concepts/Retention|Retention]] 和 [[concepts/FeatureRetention|FeatureRetention]] 相关）
- 提议将这两个属性直接挂载在 `FieldDescriptorOptions` 上（与 [[concepts/FieldOptions|FieldOptions]] 相关）
- 对普通（非选项）字段而言是 no-op，不会影响非选项字段的语义
- 与 [[concepts/OptionTargetType|OptionTargetType]] 共同构成自定义选项的类型与作用域约束体系
- 设计语义借鉴自 Java 注解的 target / retention 模型

## 应用
- 规范 [[concepts/Custom Options|Custom Options]] 的作用范围：使 schema 作者能精确声明某个自定义选项可标注到 message、field、enum、service 等哪一类实体
- 控制自定义选项的运行时可见性：通过 `retention` 区分选项仅在源码/编译期生效，还是同时进入运行时反射/descriptor
- 增强 Protobuf Editions 中描述符（descriptor）的元数据表达力，减少自定义选项的歧义使用
- 配合 `protoc`（参见 [[entities/protoc|protoc]]）实现更严格的选项校验，避免误用
- 属于 [[entities/Protobuf Editions|Protobuf Editions]] 演进中描述符元数据标准化的重要一环（设计文档见 [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]）

## 相关概念
- [[concepts/Target Attributes|Target Attributes]]
- [[concepts/Retention|Retention]]
- [[concepts/FieldOptions|FieldOptions]]
- [[concepts/Custom Options|Custom Options]]
- [[concepts/FeatureRetention|FeatureRetention]]
- [[concepts/OptionTargetType|OptionTargetType]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/Protobuf Editions|Protobuf Editions]]

## 来源提及
- "A proposal to create target and retention attributes to support." — [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]
- "This design proposed the specific addition of `target` and `retention` attributes for options as well as their suggested meaning." — [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]