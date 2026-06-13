---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]"]
tags: [method]
aliases:
  - "ManifestSchemaFactory.newSchema()"
  - "newSchema()"
---


# ManifestSchemaFactory.newSchema()

## 定义
ManifestSchemaFactory.newSchema() 是 Java Lite 中负责将 [[concepts/MessageInfo|MessageInfo]] 转换为 [[concepts/Schema|Schema]] 的工厂方法。在向 Editions 迁移的背景下，该方法被明确列为需要修改的代码位置之一，以允许处理 extensions 类型的消息，从而使其与 Editions 兼容。

## 关键特征
- 属于 Java Lite 运行时中 [[concepts/Schema|Schema]] 构建流程的入口方法
- 输入为 [[concepts/MessageInfo|MessageInfo]]，输出为 [[concepts/Schema|Schema]]
- 在 Editions 迁移中需要扩展以支持 extensions 类型消息
- 与 `MessageSchema.getSerializedSize`、`MessageSchema.writeTo`、`MessageSchema.mergeFrom`、`DescriptorMessageInfoFactory.convert()` 并列，构成 Editions 兼容性修改的工作清单
- 所在代码路径中存在基于 syntax（proto2/proto3）分支的重复逻辑，是 Editions 迁移中需要统一为基于 feature bit（如 [[concepts/is_proto3-bit|is_proto3 bit]]）单一分支的目标之一

## 应用
- Java Lite 在运行时根据 [[concepts/MessageInfo|MessageInfo]] 元数据生成对应的 [[concepts/Schema|Schema]] 实例，用于后续的序列化与反序列化
- 在 Editions 迁移中，作为允许 extensions 类型消息通过 [[concepts/Schema|Schema]] 构建流水线的关键改造点
- 与 [[concepts/DescriptorMessageInfoFactory.convert()|DescriptorMessageInfoFactory.convert()]] 等方法协同，完成从 Descriptor 到 [[concepts/MessageInfo|MessageInfo]] 再到 [[concepts/Schema|Schema]] 的转换链路

## 相关概念
- [[concepts/MessageSchema]]
- [[concepts/MessageInfo]]
- [[concepts/DescriptorMessageInfoFactory.convert()]]
- [[concepts/is_proto3-bit]]

## 相关实体
- [[sources/java-lite|Java Lite]]

## 来源提及
- "ManifestSchemaFactory.newSchema() | MessageInfo -> Schema | Allow extensions for editions." — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]
- "There are several places that branch on syntax into separate proto2/proto3 codepaths. These generally duplicate a lot of code and should be unified into a single syntax-agnostic code path branching on the relevant feature bits." — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]