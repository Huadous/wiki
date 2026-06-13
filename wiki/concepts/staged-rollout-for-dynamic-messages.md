---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [method]
aliases:
  - "Staged Rollout"
  - "渐进式动态消息发布策略"
---


# Staged Rollout for Dynamic Messages

## 定义
Staged Rollout for Dynamic Messages 是一种分阶段实施特性解析（[[concepts/Feature-Resolution|Feature Resolution]]）的策略，旨在让尚不支持完整运行时特性解析的语言（如 Java Lite 等）也能先支持 [[concepts/Editions|Editions]]，同时为后续的长期优化保留迁移路径。该策略要求代码生成器（[[entities/CodeGenerator|CodeGenerator]]）在初期将序列化后的已解析源特性（[[concepts/Resolved-Features|Resolved Features]]）直接嵌入生成的代码中，并使用 `raw_features` 字段（计划最终删除）携带未解析特性（[[concepts/Unresolved-Features|Unresolved Features]]）用于反射。只要每个描述符都提供了完全解析的特性，[[concepts/Dynamic-Messages|Dynamic Messages]] 依然可以在该方案下正常使用；待运行时实现完整的特性解析后，可删除冗余的已解析字段，仅保留未解析字段。

## 关键特征
- **双轨并存**：生成代码中同时保留已解析特性（供运行时直接使用）与未解析特性（`raw_features` 字段，供反射与动态消息使用）
- **临时兼容字段**：`raw_features` 是计划最终删除的过渡字段，用于在缺少完整运行时解析能力的语言中维持 [[concepts/Dynamic-Messages|Dynamic Messages]] 的工作
- **目标无关性**：只要每个描述符都提供完全解析的 [[concepts/FeatureSet|FeatureSet]]，动态消息即可正常使用，使所有语言都能渐进式迁移至 Editions
- **可演进性**：当运行时实现完整的特性解析后，可移除冗余的已解析字段，仅保留未解析字段，从而降低代码体积与 [[concepts/Resolved-Features|Resolved Features]] 带来的 RAM 开销
- **长期愿景**：支持反射（即需要 [[concepts/FeatureSet|FeatureSet]] 对象）的运行时在远期应将特性解析下推到运行时，以减少代码大小与 RAM 占用，并原生支持动态消息

## 应用
- **缺乏运行时解析能力的语言**：例如 Java Lite 等尚未实现完整运行时 [[concepts/Feature-Resolution|Feature Resolution]] 的语言，可借助该策略先行提供 [[concepts/Editions|Editions]] 支持
- **动态消息的过渡期支持**：在 [[concepts/Source-Features|Source Features]] 与 [[concepts/Runtime-Features|Runtime Features]] 之间尚未打通的阶段，使 [[concepts/Dynamic-Messages|Dynamic Messages]] 仍可基于完全解析的 [[concepts/FeatureSet|FeatureSet]] 正常工作
- **代码体积与 RAM 优化的演进路径**：为后续在不破坏 [[concepts/Dynamic-Messages|Dynamic Messages]] 兼容性的前提下减少冗余字段、缩减生成代码体积与运行时内存占用保留路径

## 相关概念
- [[concepts/Feature-Resolution|Feature Resolution]]
- [[concepts/Resolved-Features|Resolved Features]]
- [[concepts/Unresolved-Features|Unresolved Features]]
- [[concepts/FeatureSet|FeatureSet]]
- [[concepts/Source-Features|Source Features]]
- [[concepts/Runtime-Features|Runtime Features]]
- [[concepts/Dynamic-Messages|Dynamic Messages]]

## 相关实体
- [[entities/CodeGenerator|CodeGenerator]]

## 来源提及
- Long-term, we want to be able to handle feature resolution at run-time for any runtime that supports reflection (and therefore needs FeatureSet objects) to reduce code-size/RAM costs and support dynamic messages. — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]