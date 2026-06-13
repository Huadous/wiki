---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [term]
aliases:
  - "Editions Predictability"
  - "可预测性"
---


# Predictability

## 定义
Predictability（可预测性）在来源文档中被描述为将 feature 生命周期与具体 edition 绑定这一策略所带来的核心收益。该策略明确了库的 support contract（支持合约），并降低了用户跟踪 feature 演进所需的认知负担。

## 关键特征
- **Edition 行为稳定保证**：处于特定 edition 的 proto 文件在以下两种情况之外，不会观察到任何行为变化：
  1. 在 editions 框架之外进行了 breaking change（破坏性变更）；
  2. proto 文件所使用的 edition 被 drop（废弃）。
- **Edition 间平滑升级保证**：只要用户避免使用已 deprecated（弃用）的 feature，就可以在不进行任何修改的情况下升级到下一个 edition。
- **支持合约明确化**：通过将 feature lifetime 与 edition lifetime 绑定，让库的兼容性承诺对用户更加清晰透明。

## 应用
- 作为 Protobuf Editions 框架下，评估「将 feature 生命周期绑定到具体 edition」这一设计策略优劣的核心指标。
- 帮助库的使用者判断：在什么条件下升级 edition 是安全的，以及在什么条件下会触发破坏性变更。
- 为库维护者提供契约式承诺的依据，规范 breaking change 的引入时机与方式。

## 相关概念
- [[concepts/edition-lifetimes|Edition Lifetimes]]
- [[concepts/feature-lifetimes|Feature Lifetimes]]
- [[concepts/behavior-preserving-editions|Behavior-Preserving Editions]]
- [[concepts/edition-upgrade|Edition Upgrade]]
- [[concepts/deprecation-warning|Deprecation Warning]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/protobuf|Protobuf]]

## 来源提及
- The main win with this strategy is that it clarifies our guarantees and makes our library more predictable. — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
- We can guarantee that a proto file at a specific edition will not see any behavioral changes unless we: 1. Make a breaking change outside the editions framework. 2. Drop the edition the proto file uses. — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]