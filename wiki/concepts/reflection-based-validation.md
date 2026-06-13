---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [method]
aliases:
  - "Reflection-Based Validation"
  - "reflection-based algorithm"
---


# Reflection-Based Validation

## 定义
Reflection-Based Validation 是一种用于在 Protobuf 运行时中校验动态消息（Dynamic Messages）的替代方案。它通过运行时反射（runtime reflection）遍历描述符树（descriptor tree），并对照当前所使用的 edition 来检查 feature lifetime 约束。该方法在源文档中被提出作为"Full Validation for Dynamic Messages"（动态消息的完整校验）的备选方案。

## 关键特征
- **基于运行时反射**：依赖 runtime reflection 遍历 descriptor tree 实现校验逻辑
- **后置校验**：仅在 build 之后（post-build）生效，无法在编译期捕获问题
- **跨语言代码重复**：相同的反射算法需要在每一种支持动态消息的语言运行时中重复实现
- **性能开销**：在 upb 等运行时中存在明显的性能顾虑（Performance concerns, especially in upb）
- **与 protoc 校验重叠**：重复了 protoc 已有的校验逻辑，但比 protoc 的检查宽松得多（substantially more permissive than protoc's checks）
- **易于理解和测试**：相比其他方案更容易理解，也更容易进行测试

## 应用
- 用于 Protobuf 各种语言运行时（如 upb 等）对动态消息进行 feature lifetime 约束的校验
- 作为 protoc 直接使用预合并默认值 IR（位于 [[concepts/FeatureSetEditionDefault|FeatureSetEditionDefault]]）进行校验这一推荐方案的备选方案
- 适用于需要防止任何 feature lifetime 违反跨语言场景的运行时校验需求

## 相关概念
- [[concepts/dynamic-messages|Dynamic Messages]]
- [[concepts/featureseteditiondefault|FeatureSetEditionDefault]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/featuresupport|FeatureSupport]]

## 相关实体
- [[entities/upb|upb]]
- [[entities/protobuf|Protobuf]]
- [[entities/protoc|protoc]]

## 来源提及
- Any runtime that supports dynamic messages should have reflection, and the same reflection-based algorithm will need to be duplicated everywhere. — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
- Performance concerns, especially in upb — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]