---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-naming|editions-edition-naming]]"]
tags: [standard]
aliases:
  - "Calendar Versioning"
  - "日历版本"
  - "calver"
---


# Calver

## 定义
Calver（Calendar Versioning，日历版本）是一种使用日历日期（如年份）作为版本号的版本命名方案。在 Protobuf Editions 的命名讨论中，由于 Edition 的命名形式（如 2023）看起来像 calver 数字，团队曾错误地将修订版本称为「补丁版本」（patch editions），暗示它们是对早期版本的 bug 修复。

## 关键特征
- 版本号基于日历日期（通常是年份），例如 `2023`、`2024`
- 版本号外观呈纯数字形式，容易被误认为可比较的递增序号
- 当使用日期作为版本标识时，后续的「修订」容易被误解为「补丁」（即对前一版本的 bug 修复），而实际意图是新的特性集合
- 为避免这种命名混淆，Protobuf 倾向于采用不显式包含修订概念的 Edition 枚举方案

## 应用
- 许多软件项目（如 Ubuntu `22.04`、IntelliJ IDEA `2023.1`、GitHub `2021`）使用 Calver 命名发行版本
- 在 Protobuf Editions 设计的语境中，Calver 的命名形式（年份）正是促使设计者选择非数字、显式枚举式命名的原因之一
- 区分「基于时间的发布」与「基于修复的补丁」是版本命名策略中的关键考量

## 相关概念
- [[concepts/edition|Edition]]
- [[concepts/edition-naming|Edition Naming]]

## 相关实体
无

## 来源提及
- the fact that editions look like calver numbers has led to us calling revisions 'patch editions', which suggests that they're bug fixes to an earlier one. — [[sources/editions-edition-naming|editions-edition-naming]]
- Doesn't look like calver, avoiding that confusion — [[sources/editions-edition-naming|editions-edition-naming]]