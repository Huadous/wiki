---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-protobuf-design-options-attributes.md]]"
tags: [Options Attributes, Target Attributes, Retention, FieldOptions, Custom Options, OptionTargetType, FeatureRetention, Java annotations, Feature inheritance]
aliases: ["Protobuf Editions Options Attributes Design", "target 与 retention 属性设计提案"]
---

# Protobuf Design: Options Attributes - Summary

## 来源
- Original file: [[protobuf/editions-protobuf-design-options-attributes.md]]
- Ingested: 2026-06-13

## 核心内容
本设计文档由 [[entities/@kfm|@kfm]]（GitHub: fowles）撰写并于 2022-08-26 批准，是 [[entities/protobuf-editions|Protobuf Editions]] 项目的一部分。提案在 [[entities/descriptor-proto|descriptor.proto]] 的 [[concepts/fieldoptions|FieldOptions]] 中直接新增两个属性：`target`（通过 [[concepts/optiontargettype|OptionTargetType]] 枚举指定选项可应用的语义实体，如 FILE、MESSAGE、FIELD、ENUM 等）和 `retention`（通过 [[concepts/featureretention|FeatureRetention]] 枚举控制选项是否保留在运行时描述符中，RUNTIME 为默认，SOURCE 则须从生成描述符中剥离以减小二进制体积）。两者的设计灵感均直接借鉴 [[concepts/java-annotations|Java 注解]]的同名概念。经讨论后，`target` 被精炼为仅指定语义实体，与[[concepts/feature-inheritance|特性继承]]粒度解耦。文档还讨论了[[concepts/custom-options|自定义选项]]、[[entities/protoc|protoc]] 中硬编码行为等替代方案，最终选择直接在 FieldOptions 中添加字段的方案。

## 关键实体
- [[entities/@kfm|@kfm]]：提案作者
- [[entities/protobuf-editions|Protobuf Editions]]：本设计的所属项目
- [[entities/protoc|protoc]]：负责验证 target 放置合法性及剥离 SOURCE 类选项
- [[entities/descriptor-proto|descriptor.proto]]：target 和 retention 属性添加的目标文件
- [[entities/extensionrangeoptions|ExtensionRangeOptions]]：retention 属性的重要应用场景
- [[entities/features|Features]]：Editions 中使用 target/retention 的示例消息

## 关键概念
- [[concepts/options-attributes|Options Attributes]]：本提案引入的 target 与 retention 属性统称
- [[concepts/target-attributes|Target Attributes]]：通过 OptionTargetType 指定选项语义实体
- [[concepts/retention|Retention]]：通过 FeatureRetention 控制描述符保留级别
- [[concepts/fieldoptions|FieldOptions]]：承载 target 和 retention 的字段选项消息
- [[concepts/custom-options|Custom Options]]：被拒绝的替代实现方案
- [[concepts/optiontargettype|OptionTargetType]]：target 属性的取值枚举
- [[concepts/featureretention|FeatureRetention]]：retention 属性的取值枚举
- [[concepts/java-annotations|Java 注解]]：target 与 retention 命名的设计灵感来源
- [[concepts/feature-inheritance|Feature inheritance]]：从 target 中解耦的继承粒度问题

## 要点
- 提案在 [[concepts/fieldoptions|FieldOptions]] 中添加 `target` 和 `retention` 两个属性，灵感来自 [[concepts/java-annotations|Java 注解]]的同名概念
- `target` 通过 [[concepts/optiontargettype|OptionTargetType]] 枚举指定选项可应用的语义实体（FILE、MESSAGE、FIELD、ENUM 等），未指定时允许应用于任何实体
- `retention` 通过 [[concepts/featureretention|FeatureRetention]] 枚举（RUNTIME/SOURCE）控制选项是否保留在运行时描述符中，SOURCE 选项必须从生成描述符中剥离以减小二进制体积
- 经讨论，`target` 被精炼为仅指定语义实体，与[[concepts/feature-inheritance|继承粒度]]解耦；使用 `optional` 而非 `repeated` 以保留未来扩展空间
- 考虑过的替代方案包括：使用[[concepts/custom-options|自定义选项]]（"We Must Go Deeper"）、在 [[entities/protoc|protoc]] 中硬编码行为、允许基于 target 语义位置的层级继承，以及维持现状
- 原始批准提案与最终实现存在差异：retention 枚举无 UNKNOWN 类型、枚举定义在顶层而非嵌套、枚举值无作用域前缀、target 枚举曾有 STREAM 条目