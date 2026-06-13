---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]"]
tags: [method]
aliases:
  - "DescriptorMessageInfoFactory.convert"
  - "Java Lite Descriptor -> MessageInfo 转换方法"
  - "convertProto2/3 统一点"
---


# DescriptorMessageInfoFactory.convert()

## 定义
`DescriptorMessageInfoFactory.convert()` 是 Java Lite 运行时中负责将 `Descriptor` 转换为 `MessageInfo` 的方法。在向 Protobuf Editions 迁移的过程中，该方法的 `convertProto2` 与 `convertProto3` 两条独立分支代码路径需要被统一为单一的 syntax-agnostic 实现，根据相关 feature 位（例如 `is_proto3`）进行分支判断。

## 关键特征
- 属于 Java Lite 运行时层的方法，负责从 `Descriptor` 生成 `MessageInfo`
- 当前实现按 proto2 / proto3 syntax 分裂为两条独立路径（`convertProto2`、`convertProto3`），存在大量重复代码
- 是"unify non-feature syntax usages"任务中列出的关键统一位置之一
- 与 [[concepts/getSerializedSize-unification|getSerializedSize]]、[[concepts/writeTo-unification|writeTo]]、[[concepts/mergeFrom-unification|mergeFrom]] 等方法并列，属于 Editions 迁移中需要统一的多处分支代码路径之一
- 统一后将根据 feature 位（例如 `is_proto3`）进行条件分支，从而消除 syntax 维度的硬编码分支

## 应用
- 在 Java Lite 中将 `Descriptor` 元数据转换为运行时所需的 `MessageInfo`，是消息反射与序列化基础设施的关键步骤
- 配合 [[concepts/MessageInfo|MessageInfo]] 提供 schema 信息给序列化、解析、反射访问等下游组件
- Editions 迁移完成后，可消除重复的 proto2/proto3 路径，显著减少 Java Lite 代码体积与维护成本

## 相关概念
- [[concepts/MessageInfo|MessageInfo]]
- [[concepts/ManifestSchemaFactory.newSchema()|ManifestSchemaFactory.newSchema()]]
- [[concepts/is_proto3-bit|is_proto3 bit]]
- [[concepts/ProtoSyntax|ProtoSyntax]]
- [[concepts/getSerializedSize-unification|getSerializedSize（需统一的方法之一）]]
- [[concepts/writeTo-unification|writeTo（需统一的方法之一）]]
- [[concepts/mergeFrom-unification|mergeFrom（需统一的方法之一）]]

## 相关实体
- [[entities/java-lite|Java Lite]]

## 来源提及
- "DescriptorMessageInfoFactory.convert() | Descriptor -> MessageInfo | Unify convertProto2/3" — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]
- "There are several places that branch on syntax into separate proto2/proto3 codepaths. These generally duplicate a lot of code and should be unified into a single syntax-agnostic code path branching on the relevant feature bits."（中文释义：源代码中存在若干处按 syntax 分裂为 proto2/proto3 独立代码路径的位点，它们通常包含大量重复代码，应统一为根据相关 feature 位进行分支的单一 syntax-agnostic 路径。） — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]