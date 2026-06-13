---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-stricter-schemas-with-editions]]"]
tags: [term]
aliases:
  - "Implicit string concatenation"
  - "隐式字符串拼接"
---


# Implicit string concatenation

## 定义
Implicit string concatenation(隐式字符串拼接)指 Protocol Buffers(protobuf)语言允许在任何可出现带引号字符串的位置,将两个或多个相邻的字符串字面量在语法层面隐式拼接为一个字符串的特性,例如 `option foo = "bar " "baz";` 等价于 `"bar baz"`。该特性源自类 C 语言(如 C、C++)的字符串字面量拼接传统,被沿用到了 protobuf 的词法/语法规则中。

## 关键特征
- 适用于所有允许出现带引号字符串的位置,包括 `option` 取值、`reserved` 字段名/值、`extend` 消息名等多个语法场景。
- 拼接发生在解析阶段,不依赖运行时操作,等价于在源文件中写成一个字符串。
- 容易因遗漏分隔符而产生歧义:文档指出的真实故障案例是 `reserved "foo" "bar";` 被解析为 `reserved "foobar";`,而非两条独立的 reserved 项。
- 与 [[concepts/feature-gating|Feature gating]] 机制配合,通过 `features.concatenate_adjacent_strings` 特性开关进行治理。
- 默认行为为 `true`(允许隐式拼接),提案建议在后续 [[sources/editions|Editions]] 中将其切换为 `false`,以降低语言解析复杂度并消除潜在歧义。

## 应用
- 在 [[sources/editions|Editions]] 设计中,被视作需要收紧的语言特性之一,提议通过 feature gate(`features.concatenate_adjacent_strings`)逐步禁用。
- 用于诊断历史 `reserved` 声明相关的解析与 lint 告警问题,例如两个字符串之间漏掉逗号时的合并错误。
- 在 [[sources/editions-stricter-schemas-with-editions|Editions 收紧 Schema 备忘录]]中作为示例,论证 Editions 在减少解析歧义和增强 schema 严格性方面的价值。

## 相关概念
- [[concepts/feature-gating|Feature gating]]
- [[concepts/reserved-keywords|Reserved keywords]]

## 相关实体
- [[entities/protobuf|Protobuf]]

## 来源提及
- "Protobuf will implicitly concatenate two adjacent strings in any place it allows quoted strings, e.g. `option foo = "bar " "baz;`. This has caused interesting problems around `reserved` in the past, if a comma is omitted: `reserved "foo" "bar";` is `reserved "foobar";`." — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]