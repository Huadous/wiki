---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [method]
aliases:
  - "edition upgrade"
  - "Edition Upgrade"
---


# Edition Upgrade

## 定义
Edition Upgrade（版本升级）是指将一个 proto 文件从较旧 edition 迁移到较新 edition 的过程。在新的设计下，edition 升级有可能成为**破坏性变更**，而非始终保持行为兼容——即任何使用了已被废弃（deprecated）特性的 proto 文件，在将其 edition 升级到该特性已被移除的 edition 时，都可能发生破坏。

## 关键特征
- **可能引入破坏性变更**：与早期"升级永远保持行为等价"的预期不同，升级 edition 后被废弃的特性将不再可用。
- **前置 burndown 要求**：在 google3 等大型 monorepo 中，某项特性被移除之前，必须先完成所有使用该废弃特性的文件的清零（burndown）。
- **白名单豁免机制**：设计上允许通过 allowlist 将特定用户或测试保留在旧 edition 上，从而在推进 monorepo 整体升级时，减小新引入的破坏性影响。
- **生命周期驱动的升级**：与 [[concepts/Feature Lifetimes|Feature Lifetimes]] 和 [[concepts/Edition Lifetimes|Edition Lifetimes]] 直接关联——特性退场会推动 edition 升级的语义收紧。

## 应用
- 在 google3 中执行 [[entities/Edition 2023|Edition 2023]] 向 [[entities/Edition 2024|Edition 2024]] 的批量迁移。
- 在 proto 文件即将使用即将被移除的特性时，安排提前的 edition 升级以避免被遗弃在旧 edition。
- 对关键路径或测试用例使用 allowlist 机制，在不阻塞整体 monorepo 升级的前提下保持其运行在旧 edition。
- 作为 [[concepts/Garbage Collection|Garbage Collection]] 与 [[concepts/Predictability|Predictability]] 策略的执行手段——通过强制 burndown 使平台行为可预测。

## 相关概念
- [[concepts/Behavior-Preserving Editions|Behavior-Preserving Editions]]
- [[concepts/Garbage Collection|Garbage Collection]]
- [[concepts/Predictability|Predictability]]
- [[concepts/Feature Lifetimes|Feature Lifetimes]]
- [[concepts/Edition Lifetimes|Edition Lifetimes]]

## 相关实体
- [[entities/google3|google3]]
- [[entities/Edition 2023|Edition 2023]]
- [[entities/Edition 2024|Edition 2024]]

## 来源提及
- "A consequence of this design is that edition upgrades could now become potentially breaking." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
- "Any proto files using deprecated features could be broken by bumping its edition to one where the feature has been removed." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]