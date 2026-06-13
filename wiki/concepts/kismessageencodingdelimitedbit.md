---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-java-lite-for-editions]]"]
tags: [term]
aliases:
  - "kIsMessageEncodingDelimitedBit"
  - "0x1100"
---


# kIsMessageEncodingDelimitedBit

## 定义
kIsMessageEncodingDelimitedBit 是在备选方案中提出的一个新编码位，其十六进制值为 0x1100。该位用于编码 `features.message_encoding = DELIMITED` 特性，作为将 DELIMITED 消息字段直接编码为 `MESSAGE` 类型（而非 `GROUP` 类型）的替代方案。

## 关键特征
- 十六进制取值为 0x1100，是一个在现有编码中未被使用的位
- 作为 `MessageInfo` 编码方案的一部分，被用来标识一个消息字段应使用 DELIMITED 编码
- 该位会被传递给 [[concepts/MessageSchema|MessageSchema]]，使其能够将设置了该位的消息当作 [[concepts/Group encoding|Group]] 进行解析/序列化
- 由于需要在多处处理 group 行为，该方案被作者评价为不够理想

## 应用
- 用于在 Protobuf Editions 中支持 `features.message_encoding = DELIMITED` 特性
- 作为在 [[entities/Java Lite|Java Lite]] 中实现 DELIMITED 消息编码的备选技术方案
- 通过 MessageInfo 编码将这些 DELIMITED 消息字段编码为正常的消息字段形式

## 相关概念
- [[concepts/features.message_encoding]]
- [[concepts/DELIMITED message encoding|DELIMITED 消息编码]]
- [[concepts/MessageInfo]]
- [[concepts/MessageSchema]]
- [[concepts/Group encoding|Group 编码]]

## 相关实体
- [[entities/Java Lite|Java Lite]]

## 来源提及
- "Alternatively, we could encode `features.message_encoding = DELIMITED` as-is as type `MESSAGE`." — [[sources/editions-java-lite-for-editions]]
- "The `MessageInfo` encoding would encode these as a normal message field, using an unused (0x1100) bit as `kIsMessageEncodingDelimitedBit`." — [[sources/editions-java-lite-for-editions]]