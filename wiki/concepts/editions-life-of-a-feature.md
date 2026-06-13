---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [standard]
aliases:
  - "Editions Life of a Feature"
  - "Editions: Life of a Feature 愿景"
---


# Editions: Life of a Feature

## 定义

**Editions: Life of a Feature** 是 *Life of an Edition* 的替代性设计愿景（alternate vision），试图为特性（features）与版本（editions）之间的交互施加**更严格的约束**（tighter constraints）。该文档未对外公开（not available externally），但被现行设计文档视为重要的理论先驱：它预测了当前面临的许多核心问题，并提出了可能的解决方案，启发了在特性上引入 `edition_introduced`、`edition_deprecated`、`edition_removed` 等字段生命周期选项的设计思路。

## 关键特征

- **替代性愿景**：与 [[sources/editions-life-of-an-edition|Life of an Edition]] 并行存在的另一种设计构想，而非增量修订。
- **强约束模型**：主张在特性与版本之间建立显式且严格的绑定关系，而非宽松的版本兼容模型。
- **特性生命周期显式化**：提出为每个特性标注引入、废弃、移除的版本边界，使特性的可获得性在 schema 层即可追溯。
- **问题前瞻性**：在多数问题尚未公开浮现时即预测了其走向，并给出了对应解决路径。
- **非公开文档**：仅在内部流传，其理念通过后续文档（如 [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]）被部分采纳与引用。
- **设计范式转变**：体现了从"宽松的版本兼容模型"向"显式特性生命周期管理"的范式转变。

## 应用

- 作为 [[sources/editions-life-of-an-edition|Life of an Edition]] 的对照与补充，为 Editions 设计中关于"特性何时可用、何时应被弃用"的争论提供理论起点。
- 启发 [[sources/editions-edition-lifetimes|editions-edition-lifetimes]] 中字段级别的 `edition_introduced`、`edition_deprecated`、`edition_removed` 等生命周期选项的提出。
- 为 [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]] 等后续文档中 FeatureSet 生命周期管理提供思路。
- 推动 [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]] 中"收紧 schema"方向的设计原则。
- 与 [[concepts/feature-lifetimes|Feature Lifetimes]]、[[concepts/feature-support|FeatureSupport]] 等概念共同构成 Protobuf Editions 的特性治理理论基础。

## 相关概念

- [[concepts/life-of-an-edition|Life of an Edition]]
- [[concepts/feature-lifetimes|Feature Lifetimes]]
- [[concepts/edition-lifetimes|Edition Lifetimes]]
- [[concepts/feature-support|FeatureSupport]]

## 相关实体

- [[entities/protobuf|Protobuf]]

## 来源提及

- *Editions: Life of a Feature* (not available externally) is an alternate vision to *Life of an Edition*, which tries to put tighter constraints on how features and editions interact. — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
- It also predicted many of the problems we face now, and proposes a possible solution. — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]