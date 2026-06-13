---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [method]
aliases:
  - "DescriptorPool::MergeFeatures"
  - "MergeFeatures API"
---


# MergeFeatures

## 定义
MergeFeatures 是 protobuf 中 [[concepts/descriptor-pool|DescriptorPool]] 上用于获取已解析 FeatureSet 的 C++ API 方法。该方法返回的 [[concepts/feature-set|FeatureSet]] 对象相对于当前生成的池（generated pool）已经完全解析，即应用了所有 edition 默认值和继承合并。该方法的引入是为了让 C++ 生成器能够以更清晰的契约获取已解析特性，而无需依赖导入语句去发现生成器特性扩展。其语义是：调用 MergeFeatures 得到的 FeatureSet 是相对于当前池中可见特性集合的完整解析结果，不会出现部分解析状态。

## 关键特征
- 是 [[concepts/descriptor-pool|DescriptorPool]] 上的 C++ API 方法，用于获取已解析的 FeatureSet
- 返回的 FeatureSet 相对于当前 generated pool 已完全解析
- 自动应用所有 edition 默认值与继承合并规则
- 调用结果不会出现部分解析（partially resolved）状态
- 不再要求调用方通过解析 imports 来发现 generator 特性扩展
- 为 C++ 代码生成器提供清晰的特性解析契约

## 应用
- C++ 代码生成器在生成代码时获取目标特性的完整解析结果
- 在 [[concepts/editions|Editions]] 体系中解析与 generated pool 相关的 generator features
- 替代旧的"通过导入语句抓取特性"的工作方式
- 在生成器需要理解目标 [[concepts/feature-set|FeatureSet]] 的完整视图时直接调用

## 相关概念
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/resolved-features|Resolved Features]]
- [[concepts/generator-features|Generator Features]]
- [[concepts/global-features|Global Features]]
- [[concepts/descriptor-pool|Descriptor Pool]]

## 相关实体
- [[entities/feature-set|FeatureSet]]
- [[entities/descriptor-pool|DescriptorPool]]
- [[entities/codegenerator|CodeGenerator]]

## 来源提及
- "We've decided that there's no longer any reason to scrape the imports for features, but we *could* scrape the generated pool for them. This essentially means that when you call `MergeFeatures` to get a `FeatureSet`, the returned set is fully resolved *with respect to the current generated pool*." — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]