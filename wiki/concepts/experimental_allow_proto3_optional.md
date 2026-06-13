---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/implementing_proto3_presence|implementing_proto3_presence]]"
  - "[[protobuf/field_presence.md]]"
tags:
  - "term"
aliases:
  - "--experimental_allow_proto3_optional flag"
  - "experimental_allow_proto3_optional"
  - "protoc experimental_allow_proto3_optional"
  - "`--experimental_allow_proto3_optional` flag"
  - "--experimental_allow_proto3_optional flag"
  - "experimental_allow_proto3_optional"
  - "protoc experimental_allow_proto3_optional"
---

## Description
`--experimental_allow_proto3_optional` 是 [[entities/protoc|protoc]] 编译器中的一个命令行参数，核心作用是允许在 proto3 `.proto` 文件中处理带有 `optional` 标签的字段，从而启用显式存在（explicit presence）追踪。在 [[entities/protocol-buffers-v3-12-0|protobuf v3.12.0]] 引入 proto3 `optional` 特性至 [[entities/protocol-buffers-v3-15-0|protobuf v3.15.0]] 的过渡期之间，传入此标志是让 proto3 singular basic 类型字段获得 `optional` 显式存在语义的必要条件；若不传入，[[entities/protoc|protoc]] 会拒绝编译并报错 `This file contains proto3 optional fields, but --experimental_allow_proto3_optional was not set.`。该实验性门控原本计划在后续版本中移除——按计划是 protobuf 3.13（约 2020 年中），具体取决于社区反馈。该标志的存在反映了显式存在功能从实验特性到正式默认行为的演进轨迹：自 [[entities/protocol-buffers-v3-15-0|protobuf v3.15.0]] 起，proto3 消息的 presence tracking 成为默认行为，开发者不再需要显式传入此标志。文档的"How to enable _explicit presence_ in proto3"章节明确将其列为启用步骤之一，指出至少需要 [[entities/protoc|protoc]] v3.15，或者 v3.12 配合此标志使用。

## Related Concepts
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/explicit-presence|Explicit presence]]
- [[concepts/field-presence|Field presence]]
- [[concepts/optional-label|optional label]]

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/protocol-buffers-v3-12-0|Protocol Buffers v3.12.0]]
- [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]]

## Mentions in Source

> **Source: [[sources/implementing_proto3_presence]]**
> - "If you try to run `protoc` on a file with proto3 `optional` fields, you will get an error because the feature is still experimental:"
> - "test.proto: This file contains proto3 optional fields, but --experimental_allow_proto3_optional was not set."

> **Source: [[sources/field_presence]]**
> - "Presence tracking for proto3 messages is enabled by default since v3.15.0 release, formerly up until v3.12.0 the `--experimental_allow_proto3_optional` flag was required when using presence tracking with protoc."
> - "Run `protoc` (at least v3.15, or v3.12 using `--experimental_allow_proto3_optional` flag)."