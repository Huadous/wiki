---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"]
tags: [term]
aliases:
  - "DescriptorPool"
---


# Descriptor Pool

## 定义
Descriptor Pool 是用于在内存中构建并查询 FileDescriptor 的核心数据结构。protoc 在解析 `.proto` 文件时，会先把内容构建进一个 Descriptor Pool。在 Editions 的特性解析流程中，Descriptor Pool 是特性（Feature）解析的关键场所：默认情况下它只解析全局特性（global features）与 C++ 特性（C++ features），因为底层运行时是 C++ 运行时。

## 关键特征
- 作为内存中构建与查询 [[concepts/FeatureSet|FeatureSet]] 相关描述符的核心数据结构，由 protoc 在解析 `.proto` 时构建
- 默认仅解析全局特性与 C++ 特性（C++ 运行时的默认行为）
- 提供可扩展接口，允许 C++ 代码生成器替换参与解析的特性集
- 支持在运行时直接构建 descriptor，无需依赖 protoc

## 应用
- **特性解析的核心场所**：所有 [[concepts/FeatureSet|FeatureSet]] 解析都发生在 Descriptor Pool 中，决定了哪些生成器特性可见
- **多语言生成器适配**：通过新增方法替换参与解析的特性集，使非 C++ 生成器（如 Java、Python 等）能正确获得各自生成器对应的特性
- **运行时构建 descriptor**：解决在运行时直接构建描述符的场景下无法依赖 protoc 的问题，扩展了 descriptor 的使用方式

## 相关概念
- [[concepts/FeatureSet|FeatureSet]]
- [[concepts/Feature Resolution|Feature Resolution]]
- [[concepts/CodeGenerator|CodeGenerator]]
- [[concepts/Edition Defaults|Edition Defaults]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/descriptor.proto|descriptor.proto]]

## 来源提及
- "There are also still the issue of descriptor pools that need to be able to build descriptors at runtime." — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]
- "By default, DescriptorPool will only resolve the global features and the C++ features (since this is the C++ runtime)." — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]