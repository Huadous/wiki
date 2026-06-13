---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [method]
aliases:
  - "默认占位符方案"
  - "Default Placeholders Proposal"
---


# Default Placeholders

## 定义
Default Placeholders（默认占位符方案）是一项在 Protobuf Editions 设计中被考虑、但最终被否决的替代性设计方案。该方案的核心思路是让 [[entities/protoc|protoc]] 继续负责核心特性（core features）及已导入语言层级特性（imported language features）的解析与传播，但同时在 [[sources/features|FeatureSet]] 中引入一种"占位符"字段，用于指示某个生成器特性（generator feature）应当回退到其所在 Edition 的默认值。借助这一机制，各语言插件只需维护一份较小的"Edition 到默认 FeatureSet"映射工具，即可避免重复实现整套特性解析算法。典型的代码模式形如：优先读取 `getUtf8Validation()` 的显式设置值，若未设置则查阅当前 Edition 的默认值。

## 关键特征
- **部分解析策略**：protoc 仍负责传播与解析核心特性及已导入的语言特性，但对未导入的生成器特性则植入占位符标记，由各插件按 Edition 默认值自行处理。
- **轻量化插件责任**：插件作者无需重写整个特性解析流程，仅需提供一份从 Edition 到默认 FeatureSet 的小型映射工具。
- **占位符与显式值共存**：同一份 FeatureSet 中可能出现"已被 protoc 完全解析"的特性与"待插件回退到默认值"的占位符特性混合并存的情况。
- **示例回退模式**：插件代码形如 `getUtf8Validation()`——若显式设置则采用，否则回退至当前 Edition 的默认取值。

## 应用
该方案最初面向 Protobuf Editions 生命周期中 FeatureSet 解析流程的简化：希望降低各语言插件在特性传播与默认值选择上的实现负担，使其不必复制 protoc 已有的解析算法。然而由于方案本身存在结构性缺陷，最终未被采纳，详见"关键特征"延伸出的拒绝理由。

## 相关概念
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/edition-defaults|Edition Defaults]]
- [[concepts/generator-features|Generator Features]]
- [[concepts/global-features|Global Features]]
- [[concepts/descriptor-pool|Descriptor Pool]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "Protoc continues to propagate and resolve core features and imported language level features. For language level features that protoc does not know about (that is, not imported), a core placeholder feature indicating that the default for a given edition should be respected can be propagated." — [[sources/editions-editions-life-of-a-featureset]]

## 备注：方案被否决的原因
尽管 Default Placeholders 在表面上看似能简化插件实现，但提案讨论中识别出以下关键缺陷，导致其被否决：

1. **descriptor proto 仍然膨胀**：仍需在 `FeatureSet` 描述符中新增占位符字段及其相关元信息，descriptor proto 并未因此瘦身。
2. **混合语义造成困惑**：同一份 FeatureSet 中同时存在"完全解析后的特性值"与"占位符待回退的特性"，对调试者与插件作者而言语义含混、状态不统一。
3. **代码体积与内存开销未消除**：占位符字段本身及其传递逻辑仍需在运行时维护，无法规避原有的代码体积与内存成本。
4. **无法惠及 descriptor pool 用户**：对于绕过 protoc、直接使用 descriptor pool 读取元数据的工具链（如反射库、动态消息库），占位符机制完全不可见，无法帮助它们获得正确的 Edition 默认行为。