---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-features|editions-edition-zero-features]]"]
tags: [term]
aliases:
  - "LENGTH_PREFIXED encoding"
  - "length-prefixed submessage encoding"
---


# LENGTH_PREFIXED

## 定义
`LENGTH_PREFIXED` 是 Protobuf Editions 中 `features.message_encoding` 特征的默认值，表示将 message 类型字段在线缆上以长度前缀字节块（wire type 2）形式编码的 Protobuf 标准方式。在 Edition Zero 下，该特征的另一个取值 `DELIMITED` 会使 message 字段使用旧的 group 编码（wire types 3/4）。`group` 关键字本身在 editions 中被移除，原先的 `group` 字段会被迁移为嵌套 message 类型，并搭配一个带有 `features.message_encoding = DELIMITED` 标注的单数子消息字段使用。

## 关键特征
- `features.message_encoding` 的默认取值
- 采用标准的 Protobuf 长度前缀编码（wire type 2 的字节块）
- 使 parser 默认统一使用长度前缀编码
- 与 `DELIMITED` 取值互斥，分别对应新旧两种 message 字段编码方式
- 与 Edition Zero 下的 `group` 语法移除方案配合使用

## 应用
- 适用于所有 Protobuf Editions 模式下 message 类型的字段编码
- 取代 proto2 中 `group` 关键字的默认 wire 格式
- 用于统一不同历史编码形式下的解析器行为
- 在将历史 `group` 字段迁移到 editions 时，通过显式设置 `DELIMITED` 来保留原 wire types 3/4 行为

## 相关概念
- [[concepts/features.message_encoding|features.message_encoding]]
- [[concepts/groups|groups]]
- [[concepts/Wire types|Wire types]]
- [[concepts/proto2 syntax|proto2 syntax]]

## 相关实体
- [[entities/Protobuf Editions|Protobuf Editions]]
- [[entities/Features message|Features message]]

## 来源提及
- This feature defaults to `LENGTH_PREFIXED`. The `group` syntax does not exist under editions. — [[sources/editions-edition-zero-features|editions-edition-zero-features]]
- Instead, message-typed fields that have `features.message_encoding = DELIMITED` set will be encoded as groups (wire type 3/4) rather than byte blobs (wire type 2). — [[sources/editions-edition-zero-features|editions-edition-zero-features]]