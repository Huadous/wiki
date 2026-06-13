---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence|field_presence]]"]
tags: [field]
aliases:
  - "named-field formats"
  - "textual protobuf formats"
---


# Named-field mapping formats

## 定义
Named-field mapping formats 是 protobuf 的可读文本表示形式，与基于 tag-value stream 的二进制 wire format 相区别。其中最显著的两类是 TextFormat（由生成消息的 `DebugString` 方法产生）和 JSON。

## 关键特征
- 以人类可读的文本形式表示 protobuf 消息，而非二进制的 tag-value stream 形式
- 具有自身的正确性要求，通常比 tag-value stream 格式更严格
- TextFormat 在语义上更接近 wire format：例如重复字段的多个名-值映射会被追加保留
- JSON 是更严格的格式，无法有效表达 wire format 或 TextFormat 中的某些语义
- JSON 元素语义上是无序的，因此不适合表示依赖顺序的 protobuf 语义

## 应用
- 用于调试与日志输出（如生成消息的 `DebugString` 方法输出 TextFormat）
- 跨语言、跨平台的数据交换与接口描述（JSON 在 Web 与 REST 场景中尤为常见）
- 配置文件、数据持久化以及需要人工阅读或编辑 protobuf 消息的场景

## 相关概念
- [[concepts/textformat|TextFormat]]
- [[concepts/wire-format|Wire format]]
- [[concepts/tag-value-stream|Tag-value stream]]
- [[concepts/json|JSON]]

## 相关实体
- 无相关实体

## 来源提及
- "Protobufs can be represented in human-readable, textual forms. Two notable formats are TextFormat (the output format produced by generated message `DebugString` methods) and JSON." — [[sources/field_presence|field_presence]]
- "These formats have correctness requirements of their own, and are generally stricter than _tagged-value stream_ formats." — [[sources/field_presence|field_presence]]