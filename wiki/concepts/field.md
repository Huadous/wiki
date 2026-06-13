---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [term]
aliases:
  - "字段 (Field)"
  - "protobuf字段"
  - "message field"
---


# 字段

## 定义
字段是 Protocol Buffers 消息定义中的基本组成单元。每个字段拥有名称、数据类型、唯一的字段编号，并可选的基数修饰符（如 optional、repeated、map）。字段是线格式（wire-format）中数据序列化和反序列化的基础标识单位。

## 关键特征
- **名称**：每个字段有一个语义化的名称，用于代码生成和可读性。
- **类型**：字段类型可以是标量类型（如 int32、string）、枚举类型或其他消息类型。
- **字段编号**：每个字段必须有一个介于 1 到 536,870,911 之间的唯一编号，该编号在消息中不可重复，是线格式中的核心标识符，发布后不可更改。
- **基数修饰符**：字段可以标记为 `optional`（可选）、`repeated`（重复）、或 `map`（映射），影响序列化行为和语义。
- **线格式唯一性**：字段编号是线格式中识别字段的唯一标识，必须保证全局唯一。

## 应用
- **消息定义**：在 `.proto` 文件中定义业务数据结构，如用户信息、订单详情等。
- **数据序列化**：通过字段编号实现高效编码和解码，用于网络传输或持久化存储。
- **协议演化**：利用保留字段编号和可选字段实现前后向兼容的消息格式。
- **API 设计**：在 gRPC 和 Protobuf 服务中定义请求与响应的数据结构。

## 相关概念
- [[concepts/field-number|字段编号]]
- [[concepts/field-cardinality|字段基数]]
- [[concepts/message|消息]]
- [[concepts/wire-format|线格式]]

## 相关实体
- [[entities/protoscope|protoscope]]
- [[entities/thrift|thrift]]

## 来源提及
- "Each field has a name and a type." — [[sources/proto3|proto3]]
- "You must give each field in your message definition a number between 1 and 536,870,911 with the following restrictions: The given number must be unique among all fields for that message." — [[sources/proto3|proto3]]
- "Singular fields can appear more than once in wire-format bytes." — [[sources/proto3|proto3]]