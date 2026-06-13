---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"]
tags: [product]
aliases:
  - "Protochangifier tool"
  - "protochangifier"
---


# Protochangifier

## 基本信息
- Type: product
- Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]

## 描述
Protochangifier 是 Protobuf Editions 大规模变更（large-scale change）工作流中所引用的一个工具，其产出是一个 `ProtoChangeSpec`，用以描述如何清理一个 `.proto` 文件。它被用作三种不同操作的输出格式：features GC（计算需要在元素上设置的最小 feature 集合）、editions adopter（将 proto2/proto3 文件升级到最新的 edition）以及 editions upgrader（将处于 editions 模式的文件升级到 `protoc` 已知的最新 edition）。Protochangifier 被描述为一个 OSS 工具，旨在简化执行大规模迁移的 robots 与 beavers 的工作，并且在 adopter 与 upgrader 的场景下，其输出的 `ProtoChangeSpec` 会隐式地运行 features GC。

## 相关实体
- [[entities/protoc|protoc]]

## 相关概念
- [[concepts/protochangespec|ProtoChangeSpec]]
- [[concepts/features-gc|Features GC]]
- [[concepts/editions-adopter|Editions adopter]]
- [[concepts/editions-upgrader|Editions upgrader]]
- [[concepts/large-scale-change|Large-scale Change]]

## 来源提及
- "This will produce a Protochangifier `ProtoChangeSpec` that describes how to clean up the file." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]
- "It will emit this information as a `ProtoChangeSpec`, implicitly running features GC." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]
- "Again, this emits a features GC'd `ProtoChangeSpec`." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]