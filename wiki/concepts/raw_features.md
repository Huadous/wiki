---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [term]
aliases:
  - "raw_features 字段"
  - "raw features field"
---


# raw_features

## 定义
`raw_features` 是 Protobuf Editions 特性集（FeatureSet）生成代码（gencode）中的一个字段，用作动态消息（Dynamic Messages）分阶段迁移策略中的过渡机制。在尚无法将特性解析（feature resolution）完全迁移到运行时的生成器中，`raw_features` 字段被用于同时承载未解析的（unresolved）特性，以便在反射（reflection）阶段使用。该字段被明确标注为"最终应被删除"（should eventually be deleted），其目标是在特性解析完全迁移至运行时后，gencode 中仅嵌入未解析的特性。

## 关键特征
- 作为 Protobuf Editions 特性集生成代码中的一个字段，序列化为 gencode 的一部分
- 承担动态消息特性解析迁移过程中的过渡角色
- 在反射（reflection）场景中承载未解析的源特性
- 与已解析的（resolved）源特性序列化结果并列嵌入 gencode
- 被设计为临时性字段，最终目标是在特性解析完全迁移至运行时后将其删除
- 移除后，gencode 将仅包含未解析的特性

## 应用
- 适用于 Protobuf Editions 中动态消息的代码生成流程
- 用于在生成器无法将特性解析完全迁移到运行时的过渡阶段
- 支持运行时通过反射机制访问原始（未解析）的特性集
- 作为 Protobuf Editions 特性集生命周期中迁移策略的一部分

## 相关概念
- [[concepts/Staged Rollout for Dynamic Messages]]
- [[concepts/Resolved Features]]
- [[concepts/Unresolved Features]]
- [[concepts/Dynamic Messages]]

## 相关实体
（无相关实体）

## 来源提及
- "Here, the generator would embed the serialized resolved source features into the gencode along with the rest of the options. We would use the `raw_features` field (which should eventually be deleted) to also include the unresolved features for reflection." — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]