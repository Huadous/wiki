---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"]
tags: [method]
aliases:
  - "双向插件通信"
  - "Bidirectional Plugin Communication"
---


# Bidirectional Plugins

## 定义
Bidirectional Plugins（双向插件）是一种用于解决 protoc 与其各语言插件之间**功能可见性（feature visibility）**问题的备选方案。其核心思路是改变 protoc 与插件之间单向的调用流程：在插件被调度执行之前，先由插件主动向 protoc 声明自身所关心的功能（features），随后 protoc 在派发请求之前**预先完全解析（fully resolve）**所有 FeatureSet，再将解析后的结果连同请求一起发送给插件。这种双向握手可以避免每个插件各自重复实现特性解析逻辑。

## 关键特征
- **双向通信模式**：与传统的"protoc 单向派发 → 插件被动接收"不同，protoc 与插件之间需要预先完成一次特性声明握手。
- **插件主动声明依赖**：插件在收到完整请求前，先告知 protoc 自己需要哪些 features。
- **protoc 端集中解析**：所有 FeatureSet 的解析与合并集中在 protoc 中完成，再下发给插件。
- **消除重复实现**：插件侧不再需要各自复制一份特性解析代码，显著减少跨语言代码重复。
- **可扩展到前置校验**：未来可在此基础上让插件预先声明所需的最低 edition（minimum required editions），在派发前完成兼容性检查。
- **未解决运行时开销**：该方案不解决运行时代码体积与内存开销问题，且对 descriptor pool 这类完全绕过 protoc 的场景无能为力。

## 应用
- 解决 protoc 及其官方语言插件（cpp、java、python、go 等）在 editions 特性解析上的代码重复问题。
- 作为 Protobuf Editions 设计讨论中，对"每插件各自解析 features"方案的备选提案。
- 未来可基于该机制实现插件对 edition 兼容性的前置声明与校验。

## 相关概念
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/generator-features|Generator Features]]
- [[concepts/codegenerator|CodeGenerator]]
- [[concepts/descriptor-pool|Descriptor Pool]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- Since the generators know the features they care about, we could have some kind of bidirectional communication between protoc and the plugins. The plugin would start by telling protoc the features it wants added, and then protoc would be able to fully resolve all feature sets before sending them off. — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]