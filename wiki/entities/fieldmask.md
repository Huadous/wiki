---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence|field_presence]]"]
tags: [product]
aliases:
  - "google.protobuf.FieldMask"
  - "Protobuf FieldMask"
---


# FieldMask

## 基本信息
- Type: product
- Source: [[sources/field_presence|field_presence]]

## 描述
FieldMask 是 [[sources/proto3|Protocol Buffers]] 中的一个标准消息类型（`google.protobuf.FieldMask`），用于表示消息中字段路径的集合。它主要被设计用于支持部分"补丁"（patch）更新操作，使得调用方能够仅指定需要修改的字段路径，而不必发送整个消息。当 [[concepts/no-presence-discipline|No presence discipline]]（即字段存在性未被跟踪）时，仅使用 update patch 无法将字段更新为其默认值，因为默认值在序列化层面与字段缺失无法区分。FieldMask 提供了一种外部机制来解决这一局限，允许在 [[concepts/no-presence-discipline|无显式存在性场景]]下可靠地将字段重置为默认值。在 [[sources/field_presence|field_presence]] 应用笔记中，FieldMask 被引用为该问题的标准解决方案。

## 相关实体
- [[entities/descriptor|Protocol Buffers Descriptor]]（FieldMask 本身即为 protobuf 内置消息类型，其定义位于描述符体系中）

## 相关概念
- [[concepts/no-presence-discipline|No presence discipline]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/field-presence|Field presence]]

## 来源提及
- "Updating to set a default value in this case requires some external mechanism, such as FieldMask." — [[sources/field_presence|field_presence]]