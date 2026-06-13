---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/implementing_proto3_presence]]"]
tags: [term]
aliases:
  - "proto3 Wrapper Types"
  - "wrapper types"
  - "Wrapper Types"
---


# proto3 wrapper types

## 定义
proto3 wrapper types 是一组定义在 `wrappers.proto` 中的特殊消息类型（如 `Int32Value`、`StringValue`、`BoolValue` 等），它们将基础标量类型包装为消息类型，从而在 proto3 中实现字段存在性（field presence）的判断。在 proto3 `optional` 特性被引入之前，wrapper types 是 proto3 中唯一受支持的存在性实现机制。

## 关键特征
- 在 `wrappers.proto` 中预定义，常见成员包括 `DoubleValue`、`FloatValue`、`Int64Value`、`Int32Value`、`UInt64Value`、`UInt32Value`、`BoolValue`、`StringValue`、`BytesValue`。
- 将标量字段包装为 message 类型，使得该字段可以区分"未设置"与"设置为零值"两种状态。
- 在 proto3 中曾是**唯一**受支持的字段存在性（presence）实现机制。
- 用户反馈指出 wrapper types 存在**效率**问题（额外的消息封装带来序列化与内存开销）以及**可用性**问题（API 冗长、需要在标量与包装类型之间转换等）。
- 正是上述两类问题推动了 proto3 `optional` 字段特性的引入，使字段存在性成为标量字段的内建能力。

## 应用
- 在 proto3 `optional` 特性出现之前的版本中，需要区分"字段未设置"与"字段设置为默认值"时使用 wrapper types。
- 在需要与 proto2 互操作、或在某些仍依赖消息语义的场景下，作为兼容性手段继续使用。
- 文档中常被作为反例引用，用以说明为何 proto3 引入了更轻量的 `optional` 字段存在性机制。

## 相关概念
- [[concepts/field-presence|Field Presence]]
- [[concepts/proto3|proto3]]
- [[concepts/proto3-optional-fields|proto3 optional fields]]

## 相关实体
- (无)

## 来源提及
- "The proto3 wrapper types were previously the only supported presence mechanism for proto3." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- "Users have pointed to both efficiency and usability issues with the wrapper types." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]