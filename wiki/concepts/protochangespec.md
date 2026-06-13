---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"]
tags: [term]
aliases:
  - "Proto Change Spec"
  - "Protochangifier ProtoChangeSpec"
---


# ProtoChangeSpec

## 定义
ProtoChangeSpec 是 protoc 工具链中用于描述如何修改 `.proto` 文件的输出格式，由 Protochangifier 系统定义和消费，作为大规模变更（Large-scale Change）工具链中各工具之间的中间表示（Intermediate Representation）。

## 关键特征
- 由 Protochangifier 系统定义并消费，是一种中间表示格式
- 用于描述对源 `.proto` 文件的修改操作
- 允许工具链各组件之间解耦，便于构建更多定制的内部工具
- 具体格式内容定义在 Protochangifier 系统中，文档未详细展开

## 应用
- **Features GC**：通过发出 ProtoChangeSpec 来描述对源文件的清理操作
- **Editions adopter**：以 ProtoChangeSpec 形式描述将 `.proto` 文件升级到 Editions 所需进行的修改
- **Editions upgrader**：使用 ProtoChangeSpec 表示从旧版本到 Editions 的升级变更
- 作为大规模变更工具链中各工具间共享的中间表示

## 相关概念
- [[concepts/Features-GC|Features GC]]
- [[concepts/Editions-adopter|Editions adopter]]
- [[concepts/Editions-upgrader|Editions upgrader]]
- [[concepts/Large-scale-Change|Large-scale Change]]
- [[concepts/Protochangifier|Protochangifier]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "This will produce a Protochangifier ProtoChangeSpec that describes how to clean up the file." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]
- "It will emit this information as a ProtoChangeSpec, implicitly running features GC." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]