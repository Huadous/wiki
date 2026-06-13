---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-group-migration-issues|editions-group-migration-issues]]"]
tags: [other]
aliases:
  - "Google monorepo"
  - "google3 codebase"
  - "Google3 内部代码库"
---


# google3

## 基本信息
- Type: other
- Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]

## 描述
google3 是 Google 内部的单体代码仓库（monorepo），在该来源文档中被作为衡量 protobuf 代码生成影响范围的关键基准出现。文档指出，google3 中超过 50% 的 proto 文件会产生 Java 生成代码，因此 Java 对 [[concepts/group-fields|group 字段]]的处理方式变更对项目影响最大。与此同时，google3 中只有少数 proto 文件受到 Dart V1 行为变更的影响，可按需手动修复。google3 是评估 [[concepts/edition-2023|Edition 2023]] 迁移风险与决策权衡的核心参考代码库，其内部统计直接影响了不同语言代码生成器的优先级与迁移策略。

## 相关实体
No related entities

## 相关概念
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/group-fields|Group fields]]
- [[concepts/delimited-encoding|Delimited encoding]]

## 来源提及
- "It was determined that this only affected a handful of protos in google3, and could probably be manually fixed as-needed." — [[sources/editions-group-migration-issues|editions-group-migration-issues]]
- "Java's handling changes the story significantly, since over 50% of protos in google3 produce generated Java code." — [[sources/editions-group-migration-issues|editions-group-migration-issues]]