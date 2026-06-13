---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]"]
tags: [term]
aliases:
  - "上下文关键字"
  - "contextual reserved words"
---


# Contextual keywords

## 定义
Contextual keywords（上下文关键字）是一种解析策略，指关键字仅在特定语法上下文中被保留为关键字，而在其他上下文中可以作为普通标识符使用。文档明确引用 Rust 语言作为参考，Rust 社区强烈反对上下文关键字（因为它会使解析器复杂化），因此新关键字通常先作为上下文关键字引入，然后在下一个 Rust edition 中才被提升为完全保留字。文档建议 Protobuf 借鉴相同的演进策略：当需要引入新关键字时，先在语法中作为上下文关键字使用（前提是不会产生歧义），然后通过 `feature.xxx_is_a_keyword` 特性，在未来的 edition 中将其切换为真正的保留字。

## 关键特征
- 关键字身份与语法上下文绑定：同一词在某些语法位置是保留字，在其他位置则是合法标识符。
- 解析器需要区分使用场景，因此会引入额外的解析复杂度，这也是 Rust 社区反对此策略的主要原因。
- 提供向后兼容的演进路径：新关键字可以"软着陆"，避免在已发布的 schema 中产生大量破坏性变更。
- 与 [[concepts/Reserved keywords|保留字]]形成渐进关系：上下文关键字是引入完全保留字的过渡阶段。
- 通常与 [[concepts/Feature gating|特性开关（Feature gating）]]机制配合使用，以便在后续 edition 中完成最终切换。

## 应用
- 作为 Protobuf Editions 引入新关键字的演进策略：在不会产生歧义的语法位置先以上下文关键字形式加入新关键字，最大限度减少对现有用户的破坏。
- 配合 `feature.xxx_is_a_keyword` 特性门控，将新关键字在未来 edition 中提升为完全保留字，参照 Rust edition 的演进模式。
- 配合 [[concepts/optional-escape-syntax|optional 转义语法]]等过渡机制，为 Protobuf [[entities/Protobuf|Protobuf]] 在不破坏既有 schema 的前提下扩展语法提供一种折中手段。

## 相关概念
- [[concepts/Reserved keywords|保留字]]
- [[concepts/Protobuf Editions|Protobuf Editions]]
- [[concepts/Feature gating|Feature gating]]
- [[concepts/optional-escape-syntax|optional escape syntax]]

## 相关实体
- [[entities/Protobuf|Protobuf]]

## 来源提及
- "Rust provides guidance here: they really hate contextual keywords since it complicates the parser, so keywords start out as contextual and become properly reserved in the next Rust edition." — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]