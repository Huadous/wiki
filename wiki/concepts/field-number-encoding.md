---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/proto3]]"]
tags: [term]
aliases:
  - "field number wire size"
  - "字段号编码"
---


# Field Number Encoding

## 定义
Field Number Encoding（字段号编码）描述了 Protocol Buffers 线格式（wire format）中字段号（field number）占用的字节大小与其数值之间的关系。它规定不同范围的字段号在线格式序列化时分别占用不同长度的字节空间。

## 关键特征
- 字段号取值范围为 1 至 536,870,911，因为 32 位空间中有 3 个比特位被保留用于指定字段的线格式类型（如 wire type）。
- 字段号 1 至 15：编码后仅占用 1 个字节。
- 字段号 16 至 2047：编码后占用 2 个字节。
- proto3 指南建议将最频繁设置的字段使用 1 至 15 范围内的字段号，以最小化线格式开销。
- 字段号越大，编码后所占用的线格式空间越多，因此字段号的选择会直接影响序列化消息的体积。

## 应用
- 在 `.proto` 文件中为消息字段分配字段号时，应优先将高频字段分配到 1–15 范围内。
- 在对性能敏感或消息体量较大的场景下（如流式 RPC、海量数据传输），通过合理选择字段号减少编码开销。
- 在评估 Protocol Buffers 消息体积与网络传输成本时，作为重要的编码规则参考。

## 相关概念
- [[concepts/Field Number|Field Number]]
- [[concepts/Wire Format|Wire Format]]
- [[concepts/packed encoding|packed encoding]]

## 相关实体
无相关实体。

## 来源提及
- "You should use the field numbers 1 through 15 for the most-frequently-set fields. Lower field number values take less space in the wire format." — [[sources/proto3|proto3]]
- "For example, field numbers in the range 1 through 15 take one byte to encode. Field numbers in the range 16 through 2047 take two bytes. You can find out more about this in Protocol Buffer Encoding." — [[sources/proto3|proto3]]