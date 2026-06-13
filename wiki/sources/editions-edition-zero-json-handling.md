---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-edition-zero-json-handling.md]]"
tags: [JSON Field Name Conflicts, json_format feature, ALLOW, DISALLOW, LEGACY_BEST_EFFORT, proto2, proto3, json_name field option, deprecated_legacy_json_field_conflicts, CamelCase transformation]
aliases: ["Edition Zero: JSON Handling", "Edition Zero JSON Handling Proposal"]
---

# Edition Zero: JSON Handling - Summary

## 来源
- Original file: [[protobuf/editions-edition-zero-json-handling.md]]
- Ingested: 2026-06-13

## 核心内容

本文档是 [[entities/edition-zero|Edition Zero]] 系列中关于 JSON 处理的设计提案，由 [[entities/mkruskal-google|mkruskal-google]] 于 2023 年 5 月 10 日撰写并获批。文档针对当前 [[entities/protobuf|Protobuf]] 中 [[concepts/proto2|proto2]] 与 [[concepts/proto3|proto3]] 在 [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]] 处理上的行为差异提出统一方案：建议在 [[entities/edition-zero|Edition Zero]] 中新增三态 [[concepts/json_format-feature|json_format feature]]，分别为 [[concepts/allow|ALLOW]]（完全验证，对应 proto3）、[[concepts/disallow|DISALLOW]]（禁止 JSON 编码并禁用验证）和 [[concepts/legacy_best_effort|LEGACY_BEST_EFFORT]]（尽力而为，对应 proto2）。该提案同时规定 [[concepts/allow|ALLOW]] 消息不得嵌套 [[concepts/disallow|DISALLOW]] 类型的树形约束，并规划了从 proto2/proto3 迁移时根据 [[concepts/deprecated_legacy_json_field_conflicts|deprecated_legacy_json_field_conflicts]] 选项自动映射到对应状态的路径。该问题是 [[entities/protobuf-editions|protobuf editions]] 发布的阻碍因素之一。

## 关键实体

- [[entities/mkruskal-google|mkruskal-google]]：本设计文档作者
- [[entities/protobuf|Protobuf]]：Google 开发的序列化机制
- [[entities/edition-zero|Edition Zero]]：Protobuf editions 的初始版本
- [[entities/protobuf-editions|protobuf editions]]：Protobuf 新一代版本化特性体系
- [[entities/protocolbuffersprotobuf|protocolbuffers/protobuf]]：Protobuf 官方 GitHub 仓库
- [[entities/protoc|protoc]]：Protobuf 编译器，JSON 冲突检测的执行点

## 关键概念

- [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]]：推动本提案的核心现象
- [[concepts/json_format-feature|json_format feature]]：本提案建议新增的三态特性
- [[concepts/allow|ALLOW]]：完全验证模式，对应 proto3 默认行为
- [[concepts/disallow|DISALLOW]]：禁止 JSON 编码模式
- [[concepts/legacy_best_effort|LEGACY_BEST_EFFORT]]：兼容性尽力而为模式，对应 proto2
- [[concepts/proto2|proto2]]：Protobuf 第二版语法
- [[concepts/proto3|proto3]]：Protobuf 第三版语法
- [[concepts/json_name-field-option|json_name field option]]：覆盖默认 JSON 名的字段选项
- [[concepts/deprecated_legacy_json_field_conflicts|deprecated_legacy_json_field_conflicts]]：用于禁用 proto3 严格 JSON 冲突检查的选项
- [[concepts/camelcase-transformation|CamelCase transformation]]：Protobuf 默认字段名到 JSON 名的转换机制

## 要点

- proto2 与 proto3 在 JSON 字段名冲突处理上行为不一致：proto3 严格验证唯一性并报错，proto2 采用尽力而为方式允许非 1:1 映射
- 建议在 [[entities/edition-zero|Edition Zero]] 中引入三态 [[concepts/json_format-feature|json_format feature]]：[[concepts/allow|ALLOW]]（proto3 风格）、[[concepts/disallow|DISALLOW]]（禁止 JSON 编码）、[[concepts/legacy_best_effort|LEGACY_BEST_EFFORT]]（proto2 风格）
- [[concepts/allow|ALLOW]] 消息不能在其消息树任何位置包含 [[concepts/disallow|DISALLOW]] 类型（包括扩展字段），违反时由 [[entities/protoc|protoc]] 产生编译错误
- [[concepts/disallow|DISALLOW]] 提供了一种不涉及 schema 更改的 [[concepts/legacy_best_effort|LEGACY_BEST_EFFORT]] 替代方案，运行时将拒绝任何 JSON 解析或序列化操作
- 从 proto2/proto3 迁移到 Edition Zero 时，会根据 `syntax` 和 [[concepts/deprecated_legacy_json_field_conflicts|deprecated_legacy_json_field_conflicts]] 选项的值自动决定映射到 [[concepts/allow|ALLOW]] 或 [[concepts/legacy_best_effort|LEGACY_BEST_EFFORT]]
- [[concepts/legacy_best_effort|LEGACY_BEST_EFFORT]] 被视为需要消除的未定义行为，但保留以兼容现有内部用例
- 该特性适用于消息、枚举和文件级别；文档同时分析了 Dual State、Default to DISALLOW 和 Do Nothing 等替代方案