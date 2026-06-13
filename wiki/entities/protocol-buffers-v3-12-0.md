---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence]]"]
tags: [event]
aliases:
  - "protobuf v3.12.0"
  - "v3.12.0 release"
  - "Protocol Buffers v3.12.0"
---


# Protocol Buffers v3.12.0

## 基本信息
- Type: event
- Source: [[sources/field_presence]]

## 描述
Protocol Buffers v3.12.0 是 Protocol Buffers 历史上的一个关键版本节点，在 [[sources/field_presence|field_presence]] 应用文档中作为显式存在追踪（explicit presence）功能的早期实验性支持阶段被提及。在 v3.12.0 时代，开发者必须通过 `--experimental_allow_proto3_optional` 这一 protoc 命令行标志才能在 proto3 中为 singular basic 类型字段启用显式存在追踪。该版本标志着 explicit presence 功能从无到有的最初引入，而后续的 [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]] 则把它升级为默认行为。文档在指导用户启用显式存在时，将 v3.12.0 与 `--experimental_allow_proto3_optional` 标志捆绑提及，表明这是一种过渡性的实验配置。

## 相关实体
- [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]]

## 相关概念
- [[concepts/experimental-allow-proto3-optional-flag|--experimental_allow_proto3_optional flag]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]

## 来源提及
- "Presence tracking for proto3 messages is enabled by default since v3.15.0 release, formerly up until v3.12.0 the `--experimental_allow_proto3_optional` flag was required when using presence tracking with protoc." — [[sources/field_presence]]
- "Run `protoc` (at least v3.15, or v3.12 using `--experimental_allow_proto3_optional` flag)." — [[sources/field_presence]]