---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]"]
tags: [term]
aliases:
  - "deprecated_legacy_json_field_conflicts"
  - "legacy JSON field conflicts option"
---


# deprecated_legacy_json_field_conflicts

## 定义
`deprecated_legacy_json_field_conflicts` 是 Protocol Buffers proto3 中的一个现有文件级选项（file option），用于关闭 proto3 默认的严格 JSON 字段名冲突检查。启用该选项后，proto3 将退化为类似 proto2 的"尽力而为"（best-effort）行为：当多个字段映射到相同的 JSON 名称时，不再产生编译错误。该选项在 Edition Zero 的 JSON 处理迁移方案中被用作判断目标状态（`ALLOW` 或 `LEGACY_BEST_EFFORT`）的关键依据。

## 关键特征
- 是 proto3 的一个**已存在但被标记为 deprecated 的选项**，仅控制 JSON 编码时的字段名冲突行为。
- 设置为 `true` 时，**禁用** proto3 的严格 JSON 字段名冲突检查，允许多个字段共享同一 JSON 名称（即 `LEGACY_BEST_EFFORT` 行为）。
- 未设置（默认）时，proto3 会对默认 JSON 映射产生的冲突发出**警告**（在严格模式下甚至报错），对应 `ALLOW` 行为。
- 在从 proto2/proto3 迁移到 **Edition Zero** 时，可根据该选项的值推断目标 Edition 应使用的 JSON 冲突目标状态。
- 仅影响 JSON 序列化/反序列化（`json_format` feature），不影响二进制 protobuf 编码。

## 应用
- **Edition Zero 迁移决策**：在把既有 proto2/proto3 文件升级到 Edition Zero 时，根据 `deprecated_legacy_json_field_conflicts` 的取值自动选择 `ALLOW` 或 `LEGACY_BEST_EFFORT` 作为目标状态，保留用户既有的 JSON 兼容性预期。
- **保护历史 JSON 消费者**：当 schema 中存在因历史原因而映射到相同 JSON 字段名的多个字段时，启用该选项可避免在升级 proto 版本时引入破坏性变更。
- **平滑过渡到 Editions**：作为 proto3 → Editions 的过渡桥梁，使得不同 JSON 冲突策略的 schema 都能正确映射到 Edition Zero 中的等价状态。

## 相关概念
- [[concepts/proto3|proto3]]
- [[concepts/LEGACY_BEST_EFFORT|LEGACY_BEST_EFFORT]]
- [[concepts/ALLOW|ALLOW]]
- [[concepts/json_format-feature|json_format feature]]
- [[concepts/JSON-Field-Name-Conflicts|JSON Field Name Conflicts]]

## 相关实体
- [[entities/Protobuf|Protobuf]]

## 来源提及
- Disabled by `deprecated_legacy_json_field_conflicts` option — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]
- We will still warn for default json mapping conflicts if `deprecated_legacy_json_field_conflicts` isn't set — [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]