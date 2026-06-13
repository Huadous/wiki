---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/implementing_proto3_presence|implementing_proto3_presence]]"]
tags: [term]
aliases:
  - "--experimental_allow_proto3_optional flag"
  - "experimental_allow_proto3_optional"
  - "protoc experimental_allow_proto3_optional"
---


# --experimental_allow_proto3_optional

## 定义
`--experimental_allow_proto3_optional` 是 [[entities/protoc|protoc]]（Protocol Buffers 编译器）提供的一个命令行标志（flag）。在 proto3 中 `optional` 字段仍处于实验性阶段时（即 protobuf 3.12 前后），该标志用于显式告知编译器允许处理包含 proto3 `optional` 字段的 `.proto` 文件。若未传入此标志，[[entities/protoc|protoc]] 会拒绝编译并报错。

## 关键特征
- 是 [[entities/protoc|protoc]] 的命令行参数，启用后允许编译包含 proto3 `optional` 字段的 proto 文件。
- 在 proto3 `optional` 特性尚未正式发布（GA）期间作为临时性的"实验门控"机制存在。
- 文档提供了两种绕过该检查的方式：
  1. 显式传入 `--experimental_allow_proto3_optional` 标志。
  2. 在 `.proto` 文件的文件名或其所在目录名中包含子串 `test_proto3_optional`。
- 若不满足上述任一条件，[[entities/protoc|protoc]] 会输出错误：`This file contains proto3 optional fields, but --experimental_allow_proto3_optional was not set.`
- 该实验性门控原本计划在后续版本中移除——按计划是 protobuf 3.13（约 2020 年中），具体取决于社区反馈。

## 应用
- 在 protobuf 3.12 时代编译包含 proto3 `optional` 字段的 `.proto` 文件时，作为临时性编译开关使用。
- 与 [[concepts/proto3-optional-fields|proto3 optional fields]] 特性配合使用，是该特性在 GA 之前的必要编译条件。

## 相关概念
- [[concepts/proto3-optional-fields|proto3 optional fields]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "If you try to run `protoc` on a file with proto3 `optional` fields, you will get an error because the feature is still experimental:" — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- "test.proto: This file contains proto3 optional fields, but --experimental_allow_proto3_optional was not set." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]