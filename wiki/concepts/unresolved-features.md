---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [term]
aliases:
  - "Unresolved features"
  - "未解析特性"
---


# Unresolved Features

## 定义
Unresolved Features（未解析特性）是用户在 `.proto` 文件中显式设置在描述符（descriptor）上的特性，尚未经过特性解析（feature resolution）处理。它是一种最小化的表示形式，需要结合更多上下文知识才能被有效使用。

## 关键特征
- 由用户在 `.proto` 文件中显式声明，存储于描述符之上
- 尚未经过 feature resolution 流程，是特性的原始、最小化表示
- 需要结合目标 Edition 的默认特性集以及继承规则才能解析为完整语义
- 在 protoc、生成器与运行时之间共享时只需传递最少量的信息，显著降低 RAM 与代码大小成本
- 各组件（protoc、generator、runtime）独立完成各自的解析逻辑，避免重复实现

## 应用
- **protoc → GeneratorRequest 传递**：protoc 将完整的未解析特性集随 `GeneratorRequest` 发送给代码生成器，由生成器自行解析并应用保留策略（retention）进行剥离
- **跨组件共享**：作为 protoc、生成器与运行时之间共享的公共数据载体，减少冗余存储与重复计算
- **特性生命周期起点**：是 FeatureSet 生命周期的初始形态，经解析后转化为 Source Features、Resolved Features，最终衍生为 Runtime Features

## 相关概念
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/resolved-features|Resolved Features]]
- [[concepts/source-features|Source Features]]
- [[concepts/runtime-features|Runtime Features]]
- [[concepts/option-retention|Option Retention]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- **Unresolved features** - The features a user has explicitly set on their descriptors in the `.proto` file. These have not gone through feature resolution and are a minimal representation that require more knowledge to be useful. — [[sources/editions-editions-life-of-a-featureset]]