---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-life-of-an-edition.md]]"]
tags: [organization]
aliases:
  - "Google Busy Beavers"
  - "Busy Beavers"
---


# Busy Beavers

## 基本信息
- Type: organization
- Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]

## 描述
Busy Beavers 是 Google 内部对专门执行大规模代码变更（Large-scale Changes, LSC）工程师的一种非正式称呼。在 [[sources/editions-life-of-an-edition|editions-life-of-an-edition]] 文档中关于 Edition Zero 迁移的上下文中提到，手动升级使用 `FileDescriptorProto` 中 `syntax` 字段的代码将很可能由 Busy Beavers 或少数 [[entities/protobuf-team|protobuf-team]] 成员来完成（"furnished with appropriate stimulants (coffee, diet mountain dew, etc)"）。这个术语生动地凸显了在 Google 这样庞大的单一代码库中推行大规模迁移工作的资源密集性——需要专门的人员投入以确保更改的全面落地。Busy Beavers 在开源生态中没有直接的对应物，因为开源社区缺乏类似的集中化执行机制来强制推行横跨整个生态的大规模变更。

## 相关实体
- [[entities/protobuf-team|protobuf-team]]
- [[entities/mcy|@mcy]]

## 相关概念
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/the-oss-story|The OSS Story]]

## 来源提及
- "This will likely be a manual large-scale change performed either by Busy Beavers or a handful of protobuf-team members furnished with appropriate stimulants (coffee, diet mountain dew, etc)." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]
- "Once we have migrated 95% of callers of `syntax`, we will mark all accessors of that field in various languages as deprecated." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]