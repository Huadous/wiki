---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]"]
tags: [term]
aliases:
  - "UTF8 validation"
  - "utf-8 validation"
---


# utf8_validation

## 定义
utf8_validation 是 Editions Zero 计划引入的一项新功能（generator feature），用于控制 Protocol Buffers 中 `string` 类型字段的 UTF-8 验证行为。它允许生成代码在序列化与反序列化阶段决定是否对字符串字段执行 UTF-8 合法性校验，从而影响运行时在不同语言实现中的语义一致性。

## 关键特征
- **多实现行为不一致**：在 Python 的三种实现（pure python、Python/C++、Python/upb）之间，UTF-8 验证的默认行为存在差异。
- **C++ 的"hint"行为**：C++ 实现提供一种"hint"模式，即记录错误信息但仍允许无效的 UTF-8 字符串通过。
- **归属复杂性高**：由于其行为横跨生成器与运行时，并涉及多种语言实现间的语义对齐，utf8_validation 的归属（归为 generator feature 还是 runtime implementation feature）成为相关讨论的核心动机。
- **影响方案选择**：utf8_validation 概念的引入是导致"方案三（将 `string` 迁移到 `bytes`）"被否决的主要原因之一。

## 应用
- 在 Protobuf Editions 体系中作为 generator feature 注册，纳入 [[sources/features|features]] 特性集合进行声明与配置。
- 用于解决 `string` 字段在不同语言运行时中 UTF-8 校验行为不一致的问题。
- 在 [[sources/editions-protobuf-editions-design-features|Protobuf Editions Features Design]] 与 [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]] 所述的扩展布局方案中，作为讨论功能归类与运行时语义的典型案例。

## 相关概念
- [[concepts/Protobuf Editions|Protobuf Editions]]
- [[concepts/Editions Zero|Editions Zero]]
- [[concepts/Generator Features|Generator Features]]
- [[concepts/Runtime Implementation Features|Runtime Implementation Features]]

## 相关实体
（无相关实体）

## 来源提及
- "Editions Zero Feature: utf8_validation" (not available externally, though a later version, "Editions Zero: utf8_validation Without Problematic Options" is) is a recent plan to add a new set of generator features for utf8 validation. — [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]