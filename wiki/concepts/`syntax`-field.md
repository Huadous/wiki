---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"]
tags: [term]
aliases:
  - "FileDescriptorProto.syntax"
  - "proto syntax declaration"
  - "syntax field"
---


# `syntax` field

## 定义
`syntax` field 是 `FileDescriptorProto` 中的一个字段,用于在 `.proto` 文件中声明 proto2 或 proto3 语法(例如 `syntax = "proto2";` 或 `syntax = "proto3";`)。Protobuf Editions 的设计目标正是取代这一声明方式。由于 Editions 是用不同写法表达相同行为,一旦生态开始采用 Editions,`syntax` 字段的值便不再能可靠地作为行为指示器。

## 关键特征
- 表示 `.proto` 文件中 proto2/proto3 语法声明的字符串字段
- Editions 是其行为等价但拼写不同的替代方案
- 在 Editions 生态过渡期,其值无法可靠地反映实际行为语义
- 迁移工作需要 95% 的使用率才能将访问器标记为 deprecated
- 此次迁移仅改变拼写而不改变行为,完成时将构成 breaking change
- 被描述为一种独特的大规模变更,需要人工逐处追踪和升级

## 应用
- Protobuf 编译器(protoc)解析 `.proto` 文件时识别语法版本
- 工具链、代码生成器和反射库通过该字段判断文件采用的语法
- 在 Editions 迁移阶段,作为需要被识别、追踪和替换的旧式行为标识

## 相关概念
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/edition|Edition]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]
- [[concepts/file-descriptor-proto|FileDescriptorProto]]
- [[concepts/large-scale-change|Large-scale Change]]

## 相关实体
No related entities

## 来源提及
- "We also need to track down and upgrade (by hand) any code that is using the value of `syntax`." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]
- "This will likely be a manual large-scale change performed either by Busy Beavers or a handful of protobuf-team members furnished with appropriate stimulants (coffee, diet mountain dew, etc)." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]