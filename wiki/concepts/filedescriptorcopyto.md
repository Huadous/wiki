---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [method]
aliases:
  - "FileDescriptor::CopyTo 方法"
  - "CopyTo"
---


# FileDescriptor::CopyTo

## 定义
FileDescriptor::CopyTo 是 protobuf C++ 描述符 API（Descriptor API）中的一个方法，其核心职责是将 `FileDescriptor` 序列化为 `FileDescriptorProto` 时输出一组 **unresolved runtime features**（未经过特性解析的运行时特性）。在生成代码时，这些未解析的运行时特性会经过选项保留（option retention）剥离后转换为 unresolved source features，并嵌入到生成的代码中供运行时使用。该方法在推荐的 Editions 方案中行为保持不变，是 descriptor proto 在外部通信中始终保持未解析形式这一关键设计点的实现基础。

## 关键特征
- **方法签名与职责**：属于 `FileDescriptor` 类，将描述符对象复制（序列化）到 `FileDescriptorProto` 中。
- **输出未解析特性**：序列化 `FileDescriptorProto` 时，输出的是 unresolved runtime features（未经过特性解析的运行时特性），而非已解析的最终特性。
- **应用选项保留策略**：输出已经过选项保留（option retention）剥离处理，去除了不必要的属性。
- **Editions 兼容**：在推荐的 Editions 方案中行为保持不变，确保前后一致性。
- **代码嵌入**：经选项保留剥离后的 unresolved source features 最终嵌入到生成的代码（gencode）中，供运行时直接使用。
- **架构设计意义**：保证 descriptor proto 在外部通信链路中始终保持未解析形式，有效减少序列化体积和内存占用。

## 应用
- **代码生成器（CodeGenerator）实现**：生成器读取 `FileDescriptorProto` 中的 unresolved features，将其作为 unresolved source features 嵌入到生成代码中。
- **运行时特性加载**：运行时通过读取嵌入在 gencode 中的 unresolved source features 来构建运行时 `FeatureSet`，避免重复进行特性解析。
- **跨进程/跨语言通信**：在 descriptor proto 跨进程或跨语言传递时，传输的是未解析形式，减少网络传输和内存开销。
- **Editions 迁移场景**：在从 proto2/proto3 向 Editions 迁移时，`CopyTo` 的稳定行为保证了现有生成器和工具链的兼容性。

## 相关概念
- [[concepts/unresolved-features|Unresolved Features]]
- [[concepts/runtime-features|Runtime Features]]
- [[concepts/source-features|Source Features]]
- [[concepts/option-retention|Option Retention]]
- [[concepts/codegenerator|CodeGenerator]]

## 相关实体
- [[entities/filedescriptorproto|FileDescriptorProto]]
- [[entities/featureset|FeatureSet]]

## 来源提及
- The `FileDescriptor::CopyTo` method will continue to output unresolved runtime features, which will become unresolved source features after option retention stripping (which generators should already be doing), for embedding in the gencode for runtime use. — [[sources/editions-editions-life-of-a-featureset]]