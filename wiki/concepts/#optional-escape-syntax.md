---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-stricter-schemas-with-editions.md]]"]
tags: [term]
aliases:
  - "hash-optional syntax"
  - "keyword escape syntax"
  - "#optional 转义语法"
---


# `#optional` 转义语法

## 定义
`#optional` 是一种用于将关键字转义为标识符的语法机制。它由 [[sources/editions-stricter-schemas-with-editions|Stricter Schemas with Editions]] 提案引入，目的是在逐步将关键字变为真正保留字的过程中，为仍需使用关键字作为标识符的场景（例如字段名 `optional`）提供向后兼容路径。

## 关键特征
- **作用域限制**：该语法**只允许在关键字上使用**，不能用于非关键字标识符
- **不需要 feature gating**：与其他可能影响兼容性的提案不同，`#optional` 语法本身无需通过 feature flag 门控，可以直接引入
- **设计动机**：当前 Protobuf 允许关键字作为标识符，导致解析复杂性增加；同时关键字遮蔽行为在规范中并未被明确规定，转义语法可解决此类二义性
- **过渡性机制**：随着关键字逐渐升级为真正的保留字，`#optional` 为现有代码提供平滑迁移路径

## 应用
- 当字段名为关键字（如 `optional`、`stream` 等）但仍需在消息定义中作为标识符使用时，通过 `#optional` 前缀显式声明其为转义后的标识符
- 在 [[sources/editions-stricter-schemas-with-editions|Stricter Schemas with Editions]] 所描述的逐步收紧的 Schema 策略下，提供向后兼容的过渡手段
- 帮助解析器明确区分"关键字语义"与"作为标识符使用的关键字"，避免遮蔽（shadowing）行为带来的歧义

## 相关概念
- [[concepts/reserved-keywords|Reserved keywords]]
- [[concepts/feature-gating|Feature gating]]
- [[concepts/identifier-naming-conventions|Identifier naming conventions]]
- [[concepts/protobuf-editions|Protobuf Editions]]

## 相关实体
- [[entities/stricter-schemas-with-editions|Stricter Schemas with Editions]]
- [[entities/protobuf|Protobuf]]

## 来源提及
- "Additionally, we introduce the syntax `#optional` for escaping a keyword as an identifier. This may *only* be used on keywords, and not non-keyword identifiers." — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]
- "The `#optional` syntax would not need to be feature-gated." — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]