---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence]]"]
tags: [term]
aliases:
  - "self-delimiting wire format values"
  - "自界定值"
  - "Self-delimiting values"
---


# Self-delimiting values

## 定义
Self-delimiting values（自界定值）是 Protocol Buffers wire format 中每个 tagged 值的根本属性：每一个被 tag 标记的值都在其编码中自带长度信息或终止标记，因此解析器在反序列化时无需依赖外部的 schema（.proto 定义）即可确定该值的字节边界。这使得 wire format 本身成为自包含的、可以独立解析的字节流。

## 关键特征
- 每个 tagged 值在编码中携带其自身的长度信息（如 length-delimited 字段的前缀 varint）或具有天然的终止边界（如 varint、fixed32 等类型），解析器无需查表即可定位值的结束位置。
- 解析器可以仅靠 wire format 字节流完成解析，不必提前知晓消息的字段定义，从而天然支持前向与后向兼容的消息定义变更。
- "空"的 length-delimited 值（例如空字符串 `""`、空字节串 `[]`）在 wire format 中是合法的表示：字段被视为"存在"（present），因为它确实出现在了序列化字节流中。
- 在没有显式字段存在性（field presence）跟踪机制的 API 中，一个被反序列化得到空值的 length-delimited 字段可能无法被可靠地重新序列化——因为区分"字段缺失"和"字段为空值"需要额外的存在性位。

## 应用
- 作为 Protocol Buffers wire format 的基础机制，支撑 [[concepts/Wire format|Wire format]] 的自描述性与可独立解析性。
- 与 [[concepts/Forward and backward compatibility|前向与后向兼容性]]直接相关：正是因为每个值自带边界，旧/新版本的解析器才能安全地跳过彼此不认识的新字段。
- 构成 [[concepts/Tag-value stream|Tag-value 流]]结构的核心前提——tag 之后紧跟的 value 自身即可定位边界，无需外部 schema 介入。
- 与 [[concepts/Field presence|字段存在性]]语义紧密耦合：在 proto3 中，一个空 length-delimited 值虽"出现于 wire format"，但若运行时 API 不追踪存在性位，则在重新序列化时可能丢失该字段。

## 相关概念
- [[concepts/Wire format|Wire format]]
- [[concepts/Tag-value stream|Tag-value stream]]
- [[concepts/Forward and backward compatibility|Forward and backward compatibility]]
- [[concepts/Field presence|Field presence]]
- [[concepts/Length-delimited|Length-delimited]]

## 相关实体
（无相关实体）

## 来源提及
- The wire format is a stream of tagged, _self-delimiting_ values. — [[sources/field_presence]]
- "Empty" length-delimited values (such as empty strings) can be validly represented in serialized values: the field is "present," in the sense that it appears in the wire format. — [[sources/field_presence]]