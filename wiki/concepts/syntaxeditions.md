---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]"]
tags: [term]
aliases:
  - "Syntax::EDITIONS"
  - "EDITIONS 枚举值"
  - "editions syntax"
---


# Syntax::EDITIONS

## 定义
`Syntax::EDITIONS` 是 Protocol Buffers Editions 提案中引入的一个新的 `Syntax` 枚举特殊值。当 `syntax()` API 被弃用后，该值被用作其返回值，以显式打破调用方对返回值的既有预期。它代表一种由 Edition Zero 引入的全新语法模式，区别于传统的 `PROTO2` 和 `PROTO3`。

## 关键特征
- 是一个 `Syntax` 枚举的**特殊返回值**，而非真实存在的 `.proto` 文件中的 `syntax` 声明值。
- 由 Edition Zero 引入，标志着**继 PROTO2 / PROTO3 之后的全新语法模式**。
- 在 `syntax()` API 被弃用后返回，目的是**显式破坏（break）调用方对返回值的不合理预期**。
- 设计上利用了现有调用方的"快速失败"行为：几乎所有未涵盖的 `syntax()` 用例都已经在拒绝两种现有语法之一或在遇到未知 `Syntax` 值时报错，因此返回 `EDITIONS` 后这些代码会按预期失败（即对 editions proto 报错）。
- 推动剩余 `syntax()` 调用方完成**最终迁移**，避免隐式兼容造成的长期技术债。

## 应用
- 用于 `syntax()` API 被弃用之后的过渡阶段，作为占位/显式失败返回值。
- 促使尚未迁移到 Editions 的遗留代码路径在遇到 Editions proto 时产生**显式失败**，而不是返回看似合理的旧值（例如 `PROTO2` / `PROTO3`）。
- 作为 Editions 迁移策略的一部分，与 [[concepts/syntax()-deprecation-migration|syntax() deprecation migration]] 协同推进 protobuf 生态从 `proto2`/`proto3` 到 editions 的过渡。

## 相关概念
- [[concepts/syntax()-deprecation-migration|syntax() deprecation migration]]
- [[concepts/proto2-syntax|proto2 syntax]]
- [[concepts/proto3-syntax|proto3 syntax]]

## 相关实体
- [[entities/Edition-Zero|Edition Zero]]
- [[entities/Protocol-Buffers|Protocol Buffers]]

## 来源提及
- "`syntax()` will return a new special value, `Syntax::EDITIONS`, intended to explicitly break caller expectations about what this function returns." — [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]