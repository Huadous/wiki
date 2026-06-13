---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-group-migration-issues.md]]"]
tags: [method]
aliases:
  - "Smooth Extension 方案"
  - "平滑扩展方案"
---


# Smooth Extension

## 定义
Smooth Extension 是一种针对 protobuf delimited 编码迁移问题的文档推荐短期解决方案。其核心思路是扩展现有规范以同时覆盖 proto2 和 editions 行为。该方案定义了一个 "group-like" 概念，适用于所有同时满足以下三个条件的字段：具有 DELIMITED 编码、字段类型是嵌套消息、字段名称是其类型名的小写形式。对于 group-like 字段保留 proto2 语义，其他 delimited 字段则按常规字段处理。

## 关键特征
- **group-like 字段判定三条件**：DELIMITED 编码 + 嵌套消息类型 + 字段名为类型名的小写形式
- **语义分层处理**：group-like 字段沿用 proto2 旧语义，其余 delimited 字段按常规 editions 字段处理
- **完全兼容旧行为**：不破坏现有的 proto2 group 用法
- **覆盖大部分新场景**：能够正确处理大部分新的 editions 字段用法
- **避免当前问题场景**：规避已知的 delimited 迁移冲突
- **文本解析器双兼容**：同时接受新旧两种拼写方式，为迁移提供平滑路径
- **依赖运行时协调**：需要协调每个 editions 兼容运行时的更改

## 应用
- 作为 protobuf delimited 编码迁移到 editions 的短期推荐方案
- 为现有 proto2 schema 提供向后兼容的迁移路径
- 在文本解析器层面支持新旧拼写混用，便于渐进式升级
- 作为 editions 运行时需要协调更新的依据方案

## 相关概念
- [[concepts/group-like-fields|Group-like fields]]
- [[concepts/delimited-encoding|Delimited encoding]]
- [[concepts/global-feature|Global Feature]]
- [[concepts/aliases|Aliases]]
- [[concepts/group-fields|Group fields]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/edition-2023|Edition 2023]]

## 来源提及
- "Smooth Extension seems like the best short-term path forward to unblock the delimited migration." — [[sources/editions-group-migration-issues|editions-group-migration-issues]]
- "It mostly solves the problem and doesn't require any new features." — [[sources/editions-group-migration-issues|editions-group-migration-issues]]