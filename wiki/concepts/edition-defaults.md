---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]"]
tags: [method]
aliases:
  - "EditionDefault"
  - "版本默认值算法"
---


# Edition Defaults

## 定义
版本默认值（Edition Defaults）是本提案提出的算法，用于构建特定版本（edition）在特定 `.proto` 文件上下文中的特性（features）默认值集合。该算法通过 `EditionDefault` 子消息以及 `edition_defaults` extension 机制实现，使每个版本能够为各个特性字段提供确定性的默认值。

## 关键特征
- **算法流程明确**：构造新的 `Features feats`；对每个字段，按 `edition` 排序 `edition_defaults` 选项；通过二分搜索找到当前版本之前或相等的最新版本；根据字段类型确定 `feats` 中的值；并对所有可见的 `extensions` 执行相同算法。
- **语言作用域特性通过 imports 发现**：在当前 `.proto` 文件上下文中，仅通过 `imports` 引入的特性才会被发现并参与默认值的计算。
- **每个值都明确设置**：算法会显式地为每个特性字段赋值，从而能够正确地拒绝那些针对更旧版本编写的、缺少必要特性声明的文件。
- **支持未来版本文件**：通过 `edition` 标志参数，该算法允许尚未发布或较新版本的文件被读取，而不会立即拒绝。
- **基于二分搜索实现**：在 `defaults` 集合中使用二分搜索定位到 `current` 版本之前或相等的最新 `edition_defaults` 条目，确保查找效率。

## 应用
- 在 Protobuf Editions 编译器中，为给定的 `current` 版本与 `foo.proto` 文件上下文生成完整的特性默认值集合。
- 用于在 `.proto` 文件缺失或省略部分特性声明时，回退到版本所定义的默认行为，从而保持向前与向后兼容。
- 在处理 `imports` 引入的扩展（extensions）时，统一地为可见扩展构造其特性默认值。
- 作为 Editions 特性继承（[[concepts/feature-inheritance|Feature Inheritance]]）机制的基础，使较低版本声明的特性值在更高版本中可被继承或覆盖。

## 相关概念
- [[concepts/editions|Editions]]
- [[concepts/features|Features]]
- [[concepts/feature-inheritance|Feature Inheritance]]

## 相关实体
- [[entities/protobuf-editions|Protobuf Editions]]

## 来源提及
- "To build the edition defaults for a particular edition `current` in the context of a particular file `foo.proto`, we execute the following algorithm —" — [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]
- "Binsearch for the latest edition in `defaults` that is earlier or equal to `current`." — [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]