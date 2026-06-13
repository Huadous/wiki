---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/json2pb|json2pb]]"]
tags: [method]
aliases:
  - "map entry编码"
  - "JSON Map Encoding"
---


# JSON map编码

## 定义
JSON map编码是 [[sources/json2pb|json2pb]] 中处理 protobuf map 的一种特殊编码机制。它通过 repeated message 来模拟 JSON map：当一个 repeated message 同时满足"包含名为 key 的 string 类型字段且 tag 为 1"、"包含名为 value 的字段且 tag 为 2"、"不包含其他字段"这三个条件时，该 repeated message 会被识别为 json map。

## 关键特征
- **基于 repeated message 模拟 map**：JSON map 编码的核心实现方式是利用满足特定结构约束的 repeated message 来表示 map 结构。
- **三条件判定机制**：必须同时满足以下条件才被视作 json map：
  - 包含一个名为 `key` 的字段，类型为 string，tag 为 1；
  - 包含一个名为 `value` 的字段，tag 为 2；
  - 不包含其他字段。
- **与 protobuf 3.x 的 map 二进制兼容**：由于该编码方式与 protobuf 3.x 中 map 的二进制表示兼容，3.x 中定义的 map 字段通过 pb2json 转换时也会被正确地转化为 json map。
- **可被显式打破**：如果不希望某个 repeated message 被视作 map，可以通过以下方式打破上述条件：
  - 添加额外字段，例如 `optional int32 this_message_is_not_map_entry = 3`；
  - 交换 key 与 value 的 tag 值。

## 应用
- 在 [[sources/json2pb|json2pb]] 中将 protobuf 消息转换为 JSON 格式时，正确处理 protobuf 3.x 的 map 类型字段。
- 实现 JSON 与 protobuf 之间的双向转换时，保持 map 类型的语义一致性。
- 为不希望被当作 map 处理的 repeated message 提供显式打破匹配的机制。

## 相关概念
- [[concepts/json-protobuf转换规则|JSON-protobuf转换规则]]
- [[concepts/repeated字段JSON编码|repeated字段JSON编码]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/json2pb|json2pb]]
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- 满足如下条件的repeated MSG被视作json map — [[sources/json2pb|json2pb]]
- MSG包含一个名为key的字段，类型为string，tag为1。MSG包含一个名为value的字段，tag为2。不包含其他字段。 — [[sources/json2pb|json2pb]]
- 与protobuf 3.x中的map二进制兼容，故3.x中的map使用pb2json也会正确地转化为json map。 — [[sources/json2pb|json2pb]]
- 如果不希望某个repeated message被视为map，可以通过添加optional int32 this_message_is_not_map_entry = 3等额外字段或交换key/value的tag值来打破上述条件。 — [[sources/json2pb|json2pb]]