---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-editions-life-of-a-featureset.md]]"]
tags: [method]
aliases:
  - "C++ Generator Approach"
  - "C++ 生成器策略"
---


# C++ Generators

## 定义
C++ Generators 是指在 Protobuf 中，针对使用 C++ 编写的代码生成器所采用的 Feature 解析策略。由于这些生成器与 C++ 运行时链接，它们可以直接复用既有的 C++ Feature 解析工具，无需重复实现该算法。默认情况下，`DescriptorPool` 仅解析全局 Features 与 C++ Features；通过在 `DescriptorPool` 上新增的方法，可替换用于解析的 C++ Features；而各生成器则通过 `CodeGenerator` 上的虚方法来注册自身的 Features。该方式消除了内置 C++ 生成器以及任何以 C++ 编写的非内置插件中的代码重复问题。

## 关键特征
- 适用于以 C++ 编写的 Protobuf 代码生成器（包括内置生成器与第三方 C++ 插件）。
- 复用现有的 C++ Feature 解析工具，避免算法重复实现。
- 通过 `DescriptorPool` 的新方法实现 C++ Features 的可替换性。
- 借助 `CodeGenerator` 上的虚方法完成各生成器自有 Features 的注册。
- 与 [[concepts/Non-C++ Generators]] 相比，路径更轻量，无需语言间桥接。
- 与 [[concepts/Feature Resolution]] 紧密耦合，依赖其底层机制完成解析。

## 应用
- 解决 Protobuf Editions 体系下不同语言生成器对 Feature 解析的需求差异。
- 简化和统一内置 C++ 代码生成器在 Editions 中的行为。
- 允许第三方 C++ 插件复用与官方生成器一致的 Feature 解析能力。
- 与 [[concepts/Edition Defaults]] 结合，为 C++ 代码生成提供确定性的 Feature 解析结果。
- 减少跨语言 Feature 解析逻辑的维护成本。

## 相关概念
- [[concepts/Non-C++ Generators|Non-C++ Generators]]
- [[concepts/Feature Resolution|Feature Resolution]]
- [[concepts/Descriptor Pool|Descriptor Pool]]
- [[concepts/CodeGenerator|CodeGenerator]]
- [[concepts/Edition Defaults|Edition Defaults]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "Generators written in C++ are in a better position since they don't require any code duplication. They could be given visibility to our existing feature resolution utility to resolve the features themselves." — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]