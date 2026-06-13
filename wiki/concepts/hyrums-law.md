---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"]
tags: [theory]
aliases:
  - "海勒姆定律"
  - "Hyrum's Law"
---


# Hyrum's Law

## 定义
Hyrum's Law 指出，当一个 API 的用户数量足够多时，他们便会开始依赖 API 的每一个实现细节，即使这些细节并未在契约中明确。该定律揭示了 API 演进过程中的一种常见现象：用户基数越大，任何内部实现细节都越有可能被外部代码隐式依赖，从而使这些细节事实上成为不可变更的契约。

## 关键特征
- 描述 API 实际行为与文档契约之间的隐性依赖关系
- 用户数量是触发该定律的关键变量：用户越多，依赖面越广
- 一旦用户基数达到临界点，任何内部调整都可能被既有用户绑定为不可变行为
- 即使契约中未明确说明的内部实现细节，也会受到约束
- 本质上是对 API 演进成本和兼容性的一种悲观观察

## 应用
在 Protobuf Editions 的 FeatureSet 设计中，Hyrum's Law 被用作重要的设计依据：为了让内部实现细节不被用户绑定为不可变行为，公开 API 仅向用户暴露未解析的 FeatureSet，而已解析的 FeatureSet 仅在内部以包装类的形式访问。这样即使内部对 FeatureSet 的解析逻辑或表示方式进行调整，也不会影响用户可见的 API 行为，从而在内部演进时保持外部行为的稳定性。这一策略同时也适用于 codegen 变更和运行时辅助函数等间接暴露方式。

## 相关概念
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/featureset|FeatureSet]]

## 相关实体
无

## 来源提及
- "Users will only be exposed to them indirectly, via codegen changes or runtime helper functions, in order to avoid Hyrum's law cementing every decision we make about them." — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]