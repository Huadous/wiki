---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [method]
aliases:
  - "使用生成池方案"
  - "Generated Pool Approach"
---


# Use Generated Pool for C++ Generators

## 定义
Use Generated Pool for C++ Generators 是一种为 C++ 编写的生成器（generators）提供特性发现（feature discovery）能力的方法。该方案最初是原始提案的一部分，后被重构进推荐方案中。其核心思路是放弃从 `import` 语句中抓取特性扩展，改为从生成池（generated pool）中发现特性：当调用 `MergeFeatures` 获得 `FeatureSet` 时，返回的集合相对于当前生成池而言是已完全解析的。这种方式让 `protoc` 在插件或内置生成器进程中重建描述符时自动包含所有链接进来的生成器特性。

## 关键特征
- **从生成池发现特性**：不再依赖 `import` 语句来抓取特性扩展，而是基于生成池（generated pool）进行特性发现。
- **完全解析的 `FeatureSet`**：调用 `MergeFeatures` 返回的 `FeatureSet` 相对于当前生成池而言是已完全解析的，特性的解析永远不会是部分的。
- **自动包含链接特性**：当 `protoc` 在插件或内置生成器进程中重建描述符时，会自动包含所有链接进来的生成器特性。
- **无需代码重复**：C++ 编写的生成器无需任何代码重复，可直接复用现有的特性解析工具。
- **隐式副作用**：依赖全局变量（生成池）来传递特性信息，可能带来非显式的副作用和意外行为。
- **测试不友好**：使用全局变量导致在测试场景中不便于隔离与控制。
- **对 DescriptorPool 用户不友好**：该方案对直接使用 `DescriptorPool` 的用户而言并不直观。

## 应用
- **C++ 内置生成器**：用于 `protoc` 自带的 C++ 代码生成器，使其在生成代码时自动获取所有链接生成器的特性。
- **C++ 插件式生成器**：用于基于 `protoc` 插件机制运行的 C++ 生成器，避免重复实现特性解析逻辑。
- **描述符重建过程**：在 `protoc` 进程或插件进程中重建 `FileDescriptorProto` 描述符时，确保 `FeatureSet` 的完整性与一致性。
- **特性链接场景**：当多个生成器互相链接特性时，借助生成池统一暴露可用特性，避免手动同步。

## 相关概念
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/descriptor-pool|Descriptor Pool]]
- [[concepts/generator-features|Generator Features]]
- [[concepts/bootstrapping|Bootstrapping]]
- [[concepts/c-generators|C++ Generators]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/code-generator|CodeGenerator]]
- [[entities/descriptor-pool|Descriptor Pool]]
- [[entities/file-descriptor-proto|FileDescriptorProto]]

## 来源提及
- "Generators written in C++ are in a better position since they don't require any code duplication. They could be given visibility to our existing feature resolution utility to resolve the features themselves." — [[sources/editions-editions-life-of-a-featureset]]