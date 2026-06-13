---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-stricter-schemas-with-editions]]"]
tags: [method]
aliases:
  - "Feature gating"
  - "特性开关迁移机制"
  - "feature flag"
---


# Feature gating

## 定义
Feature gating 是一种迁移机制,通过引入形如 `feature.relax_identifier_rules`、`feature.keywords_as_identifiers`、`feature.allow_enum_aliases`、`features.allow_unused_imports` 等布尔 feature(默认值为 true),在后续 edition 中将其切换为 false,从而触发对应的严格性检查。该机制为每条 lint 设计了一条平滑、可控、可分阶段的迁移路径。

## 关键特征
- 引入布尔型 feature 开关(如 `feature.relax_identifier_rules`),可用于任意实体
- 开关默认值为 true,代表当前行为保持宽松
- 在未来的 edition 中将该开关切换为 false,触发对应的严格性检查
- 同一机制贯穿多条 lint(标识符规则、关键字处理、枚举别名、未使用 import 等)
- 与 Rust 语言 editions 中"关键字先以 context keyword 形态存在,再在下一 edition 提升为正式保留字"的迁移哲学相通
- 为用户提供了分阶段、可控的迁移路径,避免一次性强制升级

## 应用
- [[concepts/Protobuf Editions|Protobuf Editions]] 中多条严格性规则的平滑迁移
- 标识符规则收紧:从 `feature.relax_identifier_rules=true` 逐步过渡到 false,拒绝不符合新约束的标识符
- 关键字处理:从 `feature.keywords_as_identifiers=true` 过渡到 false,使部分 context keyword 升级为正式保留字
- 枚举别名策略演进:通过 `feature.allow_enum_aliases` 控制是否允许 enum value alias
- import 卫生检查:通过 `features.allow_unused_imports` 逐步引入未使用 import 警告
- 为任何希望在不破坏现有代码的前提下引入新严格性规则的场景提供通用迁移框架

## 相关概念
- [[concepts/Protobuf Editions|Protobuf Editions]]
- [[concepts/Stricter Schemas with Editions|Stricter Schemas with Editions]]
- [[concepts/Reserved keywords|Reserved keywords]]

## 相关实体
- [[entities/Protocol Buffers|Protocol Buffers]]

## 来源提及
- "To migrate, we would introduce a bool feature `feature.relax_identifier_rules`, which can be applied to any entity. When set, it would cause the compiler to reject `.proto` files which contain identifiers that don't match the above constraints. It would default to true and would switch to false in a future edition." — [[sources/editions-stricter-schemas-with-editions]]