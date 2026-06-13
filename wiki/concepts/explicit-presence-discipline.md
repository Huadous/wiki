---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence|field_presence]]"]
tags: [method]
aliases:
  - "显式存在性模式"
  - "Explicit Presence"
  - "显式存在性"
---


# Explicit presence discipline

## 定义
显式存在性模式（Explicit presence discipline）是一种字段存在性跟踪机制，其中生成的 API 不仅存储字段的值，还显式地存储该字段是否被设置（set）的状态。在这种模式下，代码能够区分"字段未被设置"与"字段被设置为默认值"这两种不同的语义状态。

## 关键特征
- 生成的 API 同时跟踪字段值与字段是否被设置的状态
- 提供 has_foo（hazzers）方法用于判断字段是否已被显式设置
- 提供 clear_foo 方法用于清除字段的设置状态
- 显式设置的值始终会被序列化，即使其值与默认值相同
- 是 [[concepts/proto2|proto2]] 的默认存在性行为
- 在 [[concepts/proto3|proto3]] 中需要通过 `optional` 标签显式启用（自 [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]] 起默认启用 optional 支持）
- 使用时需更加小心，因为"未设置"、"设置为默认值"等不同状态可能具有不同的语义含义

## 应用
- 需要精确区分"未设置"与"默认零值"的场景，例如部分更新（partial update）操作
- 使用 [[entities/fieldmask|google.protobuf.FieldMask]] 对消息进行有针对性的字段更新
- 需要可靠地检测客户端是否显式提供了某个字段值（如配置合并、覆盖检测等）
- proto3 中需要表达"字段不存在"语义的接口设计
- 与 [[concepts/No presence discipline|No presence discipline]]（隐式存在性模式）形成对比，用于在序列化效率与语义精度之间做权衡

## 相关概念
- [[concepts/No presence discipline|No presence discipline]]
- [[concepts/Field presence|Field presence]]
- [[concepts/Hazzer methods|Hazzer methods]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]

## 来源提及
- "explicit presence, where the API also stores whether or not a field has been set." — [[sources/field_presence|field_presence]]
- "Explicit presence discipline: Explicitly set values are always serialized, including default values." — [[sources/field_presence|field_presence]]
- "The explicit presence discipline relies upon the explicit tracking state instead." — [[sources/field_presence|field_presence]]