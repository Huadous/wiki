---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition]]"]
tags: [standard]
aliases:
  - "年度版本发布节奏"
  - "Edition release schedule"
  - "annual edition release"
---


# Edition proclamation cadence

## 定义
Edition proclamation cadence（版本宣告节奏）是由 protobuf-team 制定的、关于多久宣告一次新 Protobuf Editions 的策略规范。该规范承诺：即便没有第一方后端（first-party backend）立即采用，每年也会宣告一个新的版本；在紧急情况下可通过 `Y.1`、`Y.2` 等修订编号追加补丁版本；同时文档还提到未来将根据经验积累，制定允许第三方按个案申请非计划内版本升级的指引。

## 关键特征
- **年度发布承诺**：protobuf-team 承诺每个日历年度至少宣告一次新的 Edition，即便没有第一方后端计划使用该版本。
- **紧急补丁机制**：在发生紧急情况时，可通过 `Y.1`、`Y.2` 等次级编号追加修订版本号。
- **与全序关系相互制约**：由于后端必须等到 protobuf-team 宣告下一个编号后才能开始观测该版本，因此宣告节奏决定了整个生态中默认值翻转（default values flipping）的最小时间粒度。
- **第三方申请预留空间**：文档明确表示将逐步制定相关准则，使第三方能够基于个案申请非计划内的版本升级（unscheduled edition bumps）。
- **政策属性**：这是 Editions 生命周期中的一项官方政策（policy），属于 protobuf-team 对外发布的承诺与约束。

## 应用
- **默认值变更节奏控制**：决定字段默认值（field defaults）等破坏性或兼容性变更在生态中能够生效的最快速度。
- **后端迁移规划**：第一方后端团队据此安排对各 Edition 的支持与切换时间表。
- **第三方维护者协同**：为使用 Protobuf 的下游项目（语言实现、代码生成器、生态工具等）提供稳定的年度预期，以便规划兼容性工作。
- **紧急情况下的快速响应**：在出现严重缺陷或安全问题时，借助 `Y.1`、`Y.2` 修订机制在不打破年度节奏的前提下及时发布修复。

## 相关概念
- [[concepts/edition-proclamation|Edition Proclamation]]
- [[concepts/total-ordering-of-editions|Total Ordering of Editions]]
- [[concepts/edition|Edition]]
- [[concepts/breaking-changes-policy|Breaking changes policy]]

## 相关实体
无相关实体。

## 来源提及
- "We promise to proclaim an edition once per calendar year, even if first-party backends will not use it." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]
- "In the event of an emergency (whatever that means), we can proclaim a `Y.1`, `Y.2`, and so on." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]