---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"]
tags: [method]
aliases:
  - "Non-C++ Generator Approach"
  - "Non-C++ Generators Strategy"
---


# Non-C++ Generators

## 定义
Non-C++ Generators（非 C++ 代码生成器）是指在 Protobuf Editions 体系中，用 C++ 以外语言（如 Java、Python 等）编写的代码生成器。这类生成器无法直接复用 C++ 的特性解析工具（feature resolution utility），因此必须自行复制大量的特性解析逻辑。它们从 protoc 的 `GeneratorRequest` 中只能接收到尚未解析（unresolved）的特性，需要独立完成选项保留剥离（retention stripping）和 Edition 默认值（edition defaults）的解析工作。

## 关键特征
- 不能直接调用 C++ 的 feature resolution utility，只能依赖 protoc 通过 `GeneratorRequest` 提供未解析的原始特性数据
- 需要自行复制 retention 剥离与 edition default 解析等核心逻辑，开发与维护成本较高
- 为降低重复实现成本，提案建议将一份由 feature protos 派生的 `EditionFeatureDefaults` 序列化 proto 作为公共资源打包，供所有生成器和运行时嵌入使用，从而避免在运行时通过反射遍历 feature schema
- 对于不需要运行时访问特性的非 C++ 生成器，双向插件通信（bidirectional plugin communication）是一种可能更简单的替代方案
- 与 [[concepts/cpp-generators|C++ Generators]] 相比，需要在生成器侧承担原本由 C++ 工具链完成的工作

## 应用
- 使用 Java 编写的 protoc 插件代码生成器（如 protobuf-javalite 相关工具链）
- 使用 Python 编写的 protoc 插件代码生成器
- 任何需要遵循 Editions 规范、但运行时不依赖 C++ 反射能力的第三方 protoc 插件
- 在 [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]] 等迁移方案中，作为需要重新实现 feature resolution 路径的典型场景

## 相关概念
- [[concepts/cpp-generators|C++ Generators]]
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/edition-defaults|Edition Defaults]]
- [[concepts/bidirectional-plugins|Bidirectional Plugins]]
- [[concepts/option-retention|Option Retention]]

## 相关实体
- [[entities/generatorrequest|GeneratorRequest]]

## 来源提及
- "As we've shown above, non-C++ generators are already in a situation where they'd need to duplicate *some* of the feature resolution logic. With this solution, they'd need to duplicate much more of it." （如我们上面所示，非 C++ 生成器已经处于必须复制*部分*特性解析逻辑的境地。采用此方案后，它们将需要复制更多的此类逻辑。） — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]