---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition]]"]
tags: [term]
aliases:
  - "global feature"
  - "proto.Features"
---


# Global features

## 定义
Global features（全局特性）是 Protobuf Editions 系统中的两类特性之一，由 `proto.Features` 的字段定义，在文档中以 `features.<name>`（例如 `features.enum`）的形式引用。它们是一类不绑定到特定语言的特性定义。

## 关键特征
- 由 `proto.Features` 的字段定义，在文档中统一以 `features.<name>` 形式引用
- 与语言无关（language-agnostic），因此必须被清晰且显著地记录
- 定义一个 global feature 需要修改 `descriptor.h`，改动相对重量级
- 还需要在 `Descriptor` 包装类中添加辅助方法，以避免使用者自行解析继承关系

## 应用
- 作为 Protobuf Editions 设计中特性的基础分类之一，与 language-scoped features 共同构成完整的特性体系
- 用于在 Edition 演进过程中引入跨语言生效的功能开关

## 相关概念
- [[concepts/language-scoped-features|Language-scoped features]]
- [[concepts/feature|Feature]]
- [[concepts/edition-proclamation|Edition Proclamation]]

## 相关实体
无相关实体。

## 来源提及
- Global features, which are the fields of `proto.Features`. In this document, we refer to them as `features.<name>`, e.g. `features.enum`. — [[sources/editions-life-of-an-edition]]