---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"]
tags: [term]
aliases:
  - "已解析特性"
  - "Resolved Features"
---


# Resolved Features

## 定义
已解析特性（Resolved Features）是指已经过特性解析（Feature Resolution）算法处理，并应用了默认值（Defaults）与继承关系（Inheritance）之后的特性。每个特性在此状态下都拥有显式的值，是用于做出决策的唯一有效的特性集。换言之，"未解析"的特性集合只是原始声明信息，而"已解析"的特性集合才是运行时可被信任的唯一视图。

## 关键特征
- **经过了完整的解析流程**：包括从继承链向上收集、`Edition Defaults` 填充、显式声明覆盖等步骤。
- **每个特性都有显式的值**：不存在"未指定"或"待定"状态，因此是决策时唯一可用的来源。
- **不应被公开暴露**：文档明确建议已解析特性集永远不应公开暴露，以防止 API 用户依赖于内部实现细节（对抗 Hyrum 定律）。
- **仅在内部使用**：在推荐方案中，所有已解析特性都通过包装器在 protobuf 内部使用；外部代码只能通过运行时帮助函数间接访问。

## 应用
- **运行时决策**：代码在判断某项功能是否启用、采用何种编码方式或兼容性行为时，只应读取已解析特性集中的显式值。
- **Edition 行为统一**：通过继承与默认值机制，保证在不同 `Edition` 下各特性具有一致且可预测的解析结果。
- **内部实现封装**：作为 protobuf 内部的稳定数据载体，配合包装器对外屏蔽解析细节，避免外部 API 暴露随实现演进而变化。

## 相关概念
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/unresolved-features|Unresolved Features]]
- [[concepts/edition-defaults|Edition Defaults]]
- [[concepts/hyrums-law|Hyrum's Law]]

## 相关实体
（暂无相关实体）

## 来源提及
- **Resolved features** - Features that have gone through feature resolution, with defaults and inheritance applied. These are the only feature sets that should be used to make decisions. — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]
- Resolved feature sets will never be publicly exposed — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]