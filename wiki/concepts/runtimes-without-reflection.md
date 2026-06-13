---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [term]
aliases:
  - "无反射能力的运行时"
  - "Non-Reflection Runtimes"
---


# Runtimes Without Reflection

## 定义
**Runtimes Without Reflection**（无反射能力的运行时）指的是 Protobuf 中不支持反射（reflection）或动态消息（dynamic messages）功能的运行时实现，例如 Java lite 和 ObjC。这类运行时通常采用特殊的代码生成策略，将它们所需的"特性类"信息直接嵌入到生成代码中的自定义对象里，因此并不需要完整的 FeatureSet 对象。

## 关键特征
- **不支持反射与动态消息**：运行时本身不具备通过反射机制在运行时查询类型信息或动态构建消息的能力。
- **特征信息嵌入生成代码**：将运行时所需的"特性类"信息直接内嵌到生成代码（gencode）中的自定义对象，避免依赖运行时的反射机制。
- **无需完整的 FeatureSet 对象**：因特征信息已经在编译期生成代码中固化，运行时不需要持有并解析完整的 FeatureSet。
- **简化特性解析职责划分**：在采用推荐方案时，这些运行时无需在 runtime 端重复实现 feature resolution 逻辑，而由生成器（CodeGenerator）直接把运行时所需的完全解析后的特性值嵌入到生成代码中即可。
- **影响 feature 生命周期设计**：这一分类对特性解析的整体设计有重要影响，因为它简化了部分语言在 feature 生命周期中的职责划分。

## 应用
- **Java lite 运行时**：作为 Android 等资源受限平台的主流 Protobuf 运行时，因其不依赖反射机制，特性信息需在代码生成阶段完成解析。
- **ObjC 运行时**：在 Apple 生态系统中广泛使用，由于语言与平台特性限制，同样采用无反射设计。
- **Editions Feature 生命周期设计**：在 Protobuf Editions 提案的推荐方案下，CodeGenerator 一次性产出完全解析后的特性值嵌入生成代码，运行时无需自行做 feature resolution，从而简化语言实现者的负担。
- **其他受限平台/语言的 Protobuf 实现**：可作为类似运行时（不依赖反射）的设计参考模板。

## 相关概念
- [[concepts/Feature Resolution|Feature Resolution]]
- [[concepts/Dynamic Messages|Dynamic Messages]]
- [[concepts/Edition Defaults|Edition Defaults]]
- [[concepts/Staged Rollout for Dynamic Messages|Staged Rollout for Dynamic Messages]]
- [[concepts/CodeGenerator|CodeGenerator]]

## 相关实体
- [[entities/Java lite|Java lite]]
- [[entities/ObjC|ObjC]]
- [[entities/CodeGenerator|CodeGenerator]]

## 来源提及
- There are various runtimes that do not support reflection or dynamic messages at all (e.g. Java lite, ObjC). They typically embed the "feature-like" information they need directly into custom objects in the gencode. — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]