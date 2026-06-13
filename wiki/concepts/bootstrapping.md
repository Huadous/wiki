---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-minimum-required-edition|editions-minimum-required-edition]]"]
tags: [phenomenon]
aliases:
  - "Compiler Bootstrapping"
  - "自举问题"
  - "Bootstrapping"
---


# Bootstrapping

## 定义
在描述符（descriptor）版本管理的语境下，Bootstrapping（自举）指一种挑战：当 Protobuf 编译器 `protoc` 发布新版本时，需要确保该新版本的编译器仍然能够编译其自身的内部 schema（如 `descriptor.proto` 以及其他编译器内部使用的 schema），即便这些 schema 已经开始使用更新的特性。这是编译器演化过程中必须解决的核心工程问题。

## 关键特征
- **自指性需求**：编译器必须能够编译用于描述其自身功能的 schema，这是自举（bootstrapping）的核心要求。
- **新特性引入风险**：如果在 `descriptor.proto` 或其他内部 schema 中立即采用新特性，那么较旧版本的编译器将无法编译这些 schema，从而破坏自举链。
- **与版本化策略紧密耦合**：不同的版本管理方案（如 Epochs 方案 vs. Minimum Required Edition 方案）会直接影响自举问题是否出现，以及其严重程度。
- **渐进式采纳**：通过延迟内部 schema 对新特性的采纳，可以保证旧版编译器仍可编译当前 schema，从而避免自举失败。

## 应用
- **Protobuf 编译器演化**：`protoc` 在引入新的 Editions 特性时，必须保证其内部 schema（如 `descriptor.proto`）不会立即迁移到这些新特性，否则会导致较旧版本编译器无法编译 `protoc` 自身。
- **版本管理方案评估**：在评估不同的描述符版本化方案（如 Epochs 方案与 Minimum Required Edition 方案）时，自举问题是一个关键考量因素。
- **内部 schema 的兼容性维护**：决定编译器内部 schema 在何时以及如何采用新特性，以维持编译器的自举能力。

## 相关概念
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/epochs-for-descriptor-proto|Epochs for `descriptor.proto`]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/descriptor-proto|descriptor.proto]]

## 来源提及
- "Epochs for `descriptor.proto`" (not available externally) describes a potential issue with bootstrapping. — [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]
- It is not the case here: minimum edition is only incremented once a particular file uses a new feature. — [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]