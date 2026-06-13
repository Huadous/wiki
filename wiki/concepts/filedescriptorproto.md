---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-minimum-required-edition]]"]
tags: [term]
aliases:
  - "FileDescriptorProto 消息类型"
  - "FileDescriptorProto message"
---


# FileDescriptorProto

## 定义
`FileDescriptorProto` 是 Protobuf 中用于描述一个 `.proto` 文件元数据的消息类型，定义于 `descriptor.proto` 中。该消息类型包含了 `.proto` 文件的各种描述性信息，例如文件中的消息、字段、服务等定义。在《最低必需版本机制》提案中，计划在 `FileDescriptorProto` 中新增一个 `optional string minimum_required_edition = ...;` 字段，与现有的 `edition` 字段并列存在，用于记录加载此描述符所需的最低 edition 版本。

## 关键特征
- 定义于 `descriptor.proto` 中，是 Protobuf 自描述机制的核心消息类型之一
- 用于承载 `.proto` 文件的完整元数据信息
- 包含 `edition` 字段，用于标识该 `.proto` 文件所使用的 edition
- 提案新增 `optional string minimum_required_edition` 字段，与 `edition` 字段并列
- `minimum_required_edition` 字段记录加载该描述符所需的最低 edition 版本
- 所有 Protobuf 运行时在加载描述符时都需校验自身支持的 edition 是否满足 `minimum_required_edition` 的要求

## 应用
- 作为 Protobuf 反射（reflection）机制的基石，允许运行时获取 `.proto` 文件的结构化元数据
- 在 protoc 等编译器工具中用于序列化和传递 `.proto` 文件的描述信息
- 在《最低必需版本机制》提案中，作为承载 `minimum_required_edition` 字段的载体，实现运行时的版本兼容性检查
- 支持运行时根据 `FileDescriptorProto` 中的 edition 信息决定是否能够正确加载该描述符

## 相关概念
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/descriptor.proto|descriptor.proto]]
- [[concepts/edition|Edition]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/protobuf|Protobuf]]

## 来源提及
- "We propose adding a new field to `FileDescriptorProto`:`optional string minimum_required_edition = ...;`" — [[sources/editions-minimum-required-edition]]
- "This field would exist alongside the `edition` field, and would have the following semantics:" — [[sources/editions-minimum-required-edition]]