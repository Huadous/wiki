---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence]]"]
tags: [event]
aliases:
  - "protobuf v3.15.0"
  - "v3.15.0 release"
  - "Protocol Buffers 3.15.0"
---


# Protocol Buffers v3.15.0

## 基本信息
- Type: event
- Source: [[sources/field_presence]]

## 描述
Protocol Buffers v3.15.0 是 [[entities/Protocol Buffers v3.12.0|Protocol Buffers v3.12.0]] 之后 Protocol Buffers 项目的一个重要发布版本。该版本的关键意义在于将 proto3 中的 [[concepts/explicit-presence-discipline|显式存在]]（explicit presence）追踪功能从实验性支持提升为默认启用，即从 v3.15.0 开始，proto3 消息中的显式存在追踪不再需要额外的命令行开关。文档明确指出，要使用显式存在功能，运行 `protoc` 时至少需要 v3.15 版本，而 v3.12.0 则需要配合 `--experimental_allow_proto3_optional` 标志才能启用相同功能。该版本因此成为 proto3 字段存在性语义演进中的一个重要分水岭，确立了 [[concepts/optional-label|`optional` 标签]]与 [[concepts/field-presence|字段存在性]]在 proto3 中的默认行为。

## 相关实体
- [[entities/Protocol Buffers v3.12.0]]

## 相关概念
- [[concepts/explicit-presence-discipline]]
- [[concepts/optional-label]]
- [[concepts/field-presence]]

## 来源提及
- "Presence tracking for proto3 messages is enabled by default since v3.15.0 release, formerly up until v3.12.0 the `--experimental_allow_proto3_optional` flag was required when using presence tracking with protoc." — [[sources/field_presence]]
- "Run `protoc` (at least v3.15, or v3.12 using `--experimental_allow_proto3_optional` flag)." — [[sources/field_presence]]
- "this feature is enabled by default as release 3.15" — [[sources/field_presence]]