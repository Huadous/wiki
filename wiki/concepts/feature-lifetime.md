---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"]
tags: [term]
aliases:
  - "transient features"
  - "feature lifespan"
---


# Feature lifetime

## 定义
Feature lifetime（功能生命周期）指的是 Protobuf Editions 系统中功能的短暂性本质：功能被设计为随着迁移的推进，从原始默认值逐步翻转为期望默认值，然后被移除。任何引入功能的迁移都应该计划最终在内部代码库和开源代码中弃用并移除该功能，通常需要多年的时间跨度。

## 关键特征
- **暂时性**：功能是过渡性的，最终会被移除，而非永久保留在系统中
- **默认值翻转**：功能具有原始默认值（original default）和期望默认值（desired default），随着生态系统迁移的进展而逐步切换
- **多为 bool 或 enum**：由于需要在两个值之间翻转，大多数功能会以布尔或枚举形式呈现
- **多年期规划**：从引入到移除通常需要多年时间跨度
- **移除是破坏性变更**：功能的移除不强制绑定到特定的 edition，但在开源代码中必须批量放入破坏性版本中，并提前一年公告

## 应用
- **功能迁移规划**：在引入新功能时同时制定长期的弃用与移除路线图
- **默认值渐进迁移**：通过逐步翻转功能的默认值，引导整个生态系统从旧行为过渡到新行为
- **破坏性版本管理**：将开源代码中的功能移除操作归批到破坏性发布版本，并提前一年发出公告
- **代码库维护**：协调内部代码库与开源代码库中功能的弃用与删除节奏

## 相关概念
- [[concepts/Feature|Feature]]
- [[concepts/Large-scale Change|Large-scale Change]]
- [[concepts/Edition Proclamation|Edition Proclamation]]

## 相关实体
无相关实体。

## 来源提及
- In general, features should have an *original default* and a *desired default*: features are intended to gradually flip from one value to another throughout the ecosystem as migrations progress. This is not always true, but this means most features will be bools or enums. — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]