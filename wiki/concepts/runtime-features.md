---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [term]
aliases:
  - "运行时特性"
  - "Runtime Features"
---


# Runtime Features

## 定义
运行时特性（Runtime Features）是指在选项保留策略（Option Retention）应用之后，运行时可见的特性集合。这些特性可以是已解析的（resolved），也可以是未解析的（unresolved）。运行时特性由运行时在执行 protobuf 消息时使用，包括用于动态消息（Dynamic Messages）决策的特性。

## 关键特征
- 在选项保留策略（Option Retention）应用之后才对运行时可见
- 存在两种状态：已解析（Resolved）特性与未解析（Unresolved）特性
- 由运行时在执行 protobuf 消息时直接使用
- 包含用于动态消息（Dynamic Messages）决策的特性
- 运行时需要为全局特性和生成器特性都提供默认值，以支持动态消息
- 缺失的特性覆盖应引用某个共享的默认对象，以减少 RAM 开销
- 每个运行时都需要所有已解析运行时特性和所有未解析运行时特性

## 应用
- 作为 FeatureSet 生命周期中的最终输出，供运行时消费
- 指导运行时的消息执行与序列化/反序列化行为
- 为动态消息机制提供特性决策依据
- 通过共享默认对象的方式优化内存占用

## 相关概念
- [[concepts/FeatureSet]]
- [[concepts/Option Retention]]
- [[concepts/Source Features]]
- [[concepts/Resolved Features]]
- [[concepts/Unresolved Features]]
- [[concepts/Dynamic Messages]]

## 相关实体
- [[entities/FileDescriptorProto]]

## 来源提及
- **Runtime features** - The features available to runtimes after option retention has been applied. These can be either resolved or unresolved. — [[sources/editions-editions-life-of-a-featureset]]