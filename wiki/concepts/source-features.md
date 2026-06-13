---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [term]
aliases:
  - "源特性"
  - "Source Features"
---


# Source Features

## 定义
源特性（Source Features）是指在选项保留策略（Option Retention）应用之前，protoc 和生成器（Code Generator）可见的特性。这些特性对应于源代码中嵌入的可用信息，处于特性生命周期中的关键状态阶段。源特性可以是已解析的（resolved）或未解析的（unresolved）特性，是文档定义的四个特性分类之一，与全局特性、生成器特性、运行时特性并列。

## 关键特征
- 出现在选项保留策略应用之前的阶段，对应 protoc 与生成器可见的特性集合
- 既可以处于已解析状态，也可以处于未解析状态
- 与源代码中嵌入的可用信息直接对应，是特性生命周期的初始可见形态
- 在 [[concepts/FeatureSet|FeatureSet]] 生命周期的四个特性分类中占据关键位置，与 [[concepts/resolved-features|Resolved Features]]、[[concepts/unresolved-features|Unresolved Features]]、[[concepts/runtime-features|Runtime Features]] 等状态存在流转关系
- 其取值范围受 [[concepts/option-retention|Option Retention]] 策略约束，是后续保留与解析过程的输入

## 应用
- 源代码被 [[entities/protoc|protoc]] 编译时，由解析器从 `.proto` 文件及扩展中收集得到的初始特性集合
- 在 [[entities/CodeGenerator|Code Generator]] 执行代码生成逻辑时，作为其读取并处理特性的数据来源
- 与 [[entities/FileDescriptorProto|FileDescriptorProto]] 等描述符对象协同工作，为生成器提供生成目标代码所需的元信息
- 作为 [[concepts/option-retention|Option Retention]] 机制的输入，决定哪些特性最终被保留、传递或丢弃
- 在 Protobuf Editions 的 [[concepts/FeatureSet|FeatureSet]] 生命周期中，作为特性流转的起点，与 [[sources/editions-editions-life-of-a-featureset|FeatureSet 生命周期设计]] 直接对应

## 相关概念
- [[concepts/feature-set|FeatureSet]]
- [[concepts/option-retention|Option Retention]]
- [[concepts/runtime-features|Runtime Features]]
- [[concepts/resolved-features|Resolved Features]]
- [[concepts/unresolved-features|Unresolved Features]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/code-generator|CodeGenerator]]
- [[entities/file-descriptor-proto|FileDescriptorProto]]

## 来源提及
- **Source features** - The features available to protoc and generators, before option retention has been applied. These can be either resolved or unresolved. — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]