---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]"]
tags: [phenomenon]
aliases:
  - "多语言运行时场景"
  - "Polyglot Runtime Scenario"
---


# Polyglot

## 定义
Polyglot 在 Protobuf Editions 设计讨论中，指的是同一个运行时实现（例如 upb 或 C++ 运行时）被多种编程语言共同使用时，所面临的运行时行为一致性问题。其核心难点在于：当一个运行时被多语言共享时，应当遵循哪一套功能集（feature set）作为运行时行为的标准。文档指出，这一问题在当下已十分严峻——所有 proto2 字符串以及许多 proto3 字符串在不同语言之间的互通是完全不安全的。

## 关键特征
- **多语言共享运行时**：指 upb、C++ 等运行时被多种语言客户端共同依赖与使用
- **功能集归属不明确**：缺乏清晰规范规定运行时行为应遵循哪一套功能集
- **跨语言安全隐患**：proto2 字符串及大量 proto3 字符串在不同语言间存在完全不安全的互通风险
- **影响功能扩展决策**：是讨论功能扩展应当归属到哪个层级时的关键考量因素

## 应用
- 在 Protobuf Editions 的功能扩展布局设计中，作为评估新功能归属运行时还是 schema 的核心依据
- 指导共享实现（如 upb）在多语言场景下的行为一致性策略制定
- 帮助识别并解决跨语言字符串处理中的安全性与兼容性问题

## 相关概念
- [[concepts/shared-implementations|Shared Implementations]]
- [[concepts/runtime-implementation-features|Runtime Implementation Features]]

## 相关实体
- 无相关实体

## 来源提及
- **Polyglot** - it's not clear how upb or C++ runtimes should behave in multi-language situations. Which feature sets do they consider for runtime behaviors? — [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]
- *Note: this is already a serious issue today, where all proto2 strings and many proto3 strings are completely unsafe across languages.* — [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]