---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [standard]
aliases:
  - "Behavior-Preserving Edition Upgrades"
  - "保持行为的版本升级"
---


# Behavior-Preserving Editions

## 定义
Behavior-Preserving Editions（保持行为的版本）是 Protobuf Editions 系统的一项设计原则，规定将一个 proto 文件从一个 edition 升级到另一个 edition 时，相对于最新的 proto 语言而言，绝不应破坏其行为。该原则被视为当前 edition 设计的一个"良好副作用"（nice consequence），因为它将 edition 演进与破坏性变更分离，使得团队只需跟踪一套版本方案（即 OSS 发布版本）。

## 关键特征
- **行为保持性**：edition 升级保证不改变 proto 文件相对于当前 proto 语言的运行时行为。
- **与破坏性变更解耦**：editions 本身不引入破坏性变更，破坏性变更独立于 edition 机制。
- **单一版本方案**：只需跟踪 OSS 版本的发布节奏，无需同时维护多套版本机制。
- **潜在权衡**：若将 feature 的生命周期与特定 edition 绑定（即"feature 移除绑定到 edition"），则 edition 升级可能变为破坏性变更，因为升级到的 edition 可能已经移除了某些已废弃的 feature。这是该设计建议需要正视的核心张力，也是偏离当前设计的主要代价之一。

## 应用
- **Edition 升级迁移**：开发者在将 proto 文件从旧 edition（如 Edition 2023）升级到新 edition 时，无需担心行为变更，只需关注语法/特性差异。
- **版本演进规划**：Protobuf 团队在设计新 edition 时，可以安全地引入新特性而不破坏现有用户。
- **破坏性变更隔离**：所有真正的破坏性变更通过独立的 OSS 发布版本管理，清晰区分了"演进"与"破坏"两条轨道。
- **设计决策权衡分析**：在为 feature 生命周期与 edition 耦合提案做评估时，需衡量是否愿意放弃 behavior-preserving 升级这一保证。

## 相关概念
- [[concepts/editions|Editions]]
- [[concepts/feature-removal|Feature Removal]]
- [[concepts/forward-compatibility|Forward Compatibility]]
- [[concepts/backward-compatibility|Backward Compatibility]]

## 相关实体
（暂无相关实体）

## 来源提及
- "This system does have the nice consequence that behavior-preserving editions upgrades can always be performed (with respect to the most current proto language)." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
- "It separates editions from breaking changes, and means that we only need to worry about one versioning scheme (our OSS release)." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]