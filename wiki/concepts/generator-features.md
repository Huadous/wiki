---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [term]
aliases:
  - "Generator Features"
  - "生成器特性"
---


# Generator Features

## 定义
生成器特性（Generator Features）是 `FeatureSet` 的扩展，由特定的运行时或生成器所拥有。它们通常与特定语言相关，例如 C++ 生成器特性、Java 生成器特性等，用于让各语言的代码生成器声明和处理自己特有的行为开关。

## 关键特征
- **归属特定生成器**：每种语言或运行时拥有自己的生成器特性，区别于全局共享的特性。
- **依赖 imports 发现机制**：生成器特性依赖于文件的 import 来使 `protoc` 能够发现它们；如果用户没有为某个生成器特性添加对应的 import，`protoc` 将无法发现该特性。
- **可发现性问题**：正是由于上述依赖关系，生成器特性在 Editions 体系中面临"用户未 import 则不可见"的核心问题。
- **建议的注册模式**：文档推荐每种语言定义自己的 `features.proto` 文件，并在生成器中完成注册，确保所有相关组件都能获取到必要的特性。

## 应用
- **多语言代码生成**：在 Protocol Buffers Editions 体系下，C++、Java、Python 等不同语言的生成器通过各自的生成器特性控制语言专属的编码或运行时行为。
- **FeatureSet 扩展**：作为 `FeatureSet` 的扩展点，允许各运行时和生成器在统一框架下定义自有特性。
- **特性注册与分发**：配合 import 机制，使 `protoc` 在编译时能收集到所有相关语言/运行时声明的生成器特性。

## 相关概念
- [[concepts/feature-set|FeatureSet]]
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/global-features|Global Features]]
- [[concepts/source-features|Source Features]]
- [[concepts/runtime-features|Runtime Features]]
- [[concepts/edition-defaults|Edition Defaults]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/code-generator|CodeGenerator]]

## 来源提及
- **Generator features** - Extensions of `FeatureSet` owned by a specific runtime or generator. — [[sources/editions-editions-life-of-a-featureset]]
- For generator features though, we depend on [imports to make them discoverable](protobuf-editions-design-features.md#specification-of-an-edition). — [[sources/editions-editions-life-of-a-featureset]]