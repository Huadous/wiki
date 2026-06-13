---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"]
tags: [term]
aliases:
  - "group encoding feature"
  - "group_encoded"
---


# features.group_encoded

## 定义
`features.group_encoded` 是 Protobuf Editions 中的一种 wire-format 功能（特性），用于消息字段（message field）。它通过使用 group（以 end-marker 界定边界的 submessage）格式来替代传统的 length-prefixed message 格式，从而实现更高效的编码和解码。该特性是一个大规模变更模板（large-scale change template）的核心：第一步先修改解析器（parsers），使其在反序列化器（deserializer）中同时接受 group 编码和 length-prefixed 编码作为同义格式；第二步在经过多年的 soak period（浸泡期）之后，再将 `features.group_encoded` 添加到代码库中的各个消息字段上。在 editions 中，group 实际上并不作为独立的实体存在；它们只是设置了 `features.group_encoded` 的消息。

## 关键特征
- 是一种 wire-format 级别的特性，针对消息字段的编码效率进行优化
- 使用 end-marker-delimited submessage（group）格式，相较 length-prefixed message 格式在编码和解码时开销更低
- 属于大规模变更（large-scale change）的核心，必须分多阶段实施：先让解析器同时支持新旧两种格式，再经过长时间 soak period 后才全面启用
- 在 editions 中，group 并非独立概念，而是带有 `features.group_encoded` 标志的普通消息
- 启用时需要反序列化器能够同时识别 group 与 length-prefixed 两种编码，保证向后与向前兼容性

## 应用
- 在 Protobuf Editions 中对消息字段启用更高效的 group 编码格式，以降低序列化/反序列化的计算开销
- 作为大规模 wire-format 演进策略的一部分：先在反序列化端实现双格式兼容，再逐步在生产 schema 中推广启用
- 适用于对编码/解码性能敏感且能接受多年迁移窗口的 Protobuf 使用场景

## 相关概念
- [[concepts/Feature|Feature]]
- [[concepts/Large-scale Change|Large-scale Change]]
- [[concepts/Global features|Global features]]

## 相关实体
无相关实体

## 来源提及
- "It turns out that encoding and decoding groups (end-marker-delimited submessages) is cheaper than handling length-prefixed messages." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]