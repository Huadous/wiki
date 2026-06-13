---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]"]
tags: [method]
aliases:
  - "嵌套功能"
  - "Shared Feature Set Messages"
---


# Nested Features

## 定义
Nested Features 是 Protobuf Editions 功能扩展布局方案中讨论的第四种替代方案，主张允许共享功能集消息（shared feature set messages）。例如 upb 可以定义一个功能消息，但不将其作为全局 `FeatureSet` 的扩展，而是让使用 upb 的语言将其作为字段使用，以便实现更细粒度的控制。

## 关键特征
- **共享功能集消息**：允许定义可被多个生成器或语言共享使用的功能消息结构。
- **非全局扩展**：所定义的功能消息不作为全局 `FeatureSet` 的扩展，而是嵌入到具体语言/工具的上下文中。
- **更细粒度的语言级控制**：使用方语言可以将功能消息作为字段使用，从而获得更精确的控制粒度。
- **明确性高于方案一和方案二**：比前两种方案在功能归属与作用域表达上更加明确。
- **可能导致过度明确**：作为潜在缺点，可能过于显式，导致 proto 拥有者不得不复制大量功能定义。

## 应用
- **多语言 Protobuf 代码生成**：当不同语言（如 upb、其他运行时）对功能集有差异化需求时，可通过 Nested Features 方案避免将所有功能塞入全局 `FeatureSet`。
- **功能集作用域分离**：将通用功能消息与具体语言/工具特有的功能消息分离，降低全局 `FeatureSet` 的复杂度。
- **Editions 功能扩展机制设计**：作为 Editions 功能扩展布局方案的候选之一，供设计决策权衡。

## 相关概念
- [[concepts/feature-extension|Feature Extension]]
- [[concepts/generator-features|Generator Features]]
- [[concepts/featureset|FeatureSet]]

## 相关实体
（无相关实体）

## 来源提及
- "Another option is to allow for shared feature set messages. For example, upb would define a feature message, but *not* make it an extension of the global `FeatureSet`." — [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]
- "Maybe too explicit? Proto owners would be forced to duplicate a lot of features" — [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]