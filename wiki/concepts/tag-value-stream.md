---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence|field_presence]]"]
tags: [term]
aliases:
  - "tagged-value stream"
  - "tagged-value stream formats"
---


# Tag-value stream

## 定义
Tag-value stream 是 protobuf wire format 的本质描述——一个由 tagged、self-delimiting 值组成的流。它是 Protocol Buffers 二进制序列化的核心抽象：序列化后的 wire format 仅包含"存在"字段的值，不携带任何关于"不存在"字段的信息。Tag-value stream 格式与 named-field mapping 格式（如 TextFormat 和 JSON）在正确性要求上有所不同，后者通常更为严格。

## 关键特征
- **Tagged**：每个值都附带一个字段编号（field number）与 wire type 组合而成的 tag，用于标识该值属于哪个字段。
- **Self-delimiting**：每个值在编码上都是自定界的，无需外部元数据即可独立解析。
- **仅编码"存在"字段**：序列化输出中不包含未设置字段的任何信息，"absence" 是通过"不存在"来表达的。
- **字段追加语义**：对于 repeated 字段，多个同名 tag-value 对会在解析时按顺序追加到该字段。
- **Oneof 的"last one wins"语义**：在同一 oneof 分组中，后出现的 tag-value 对会覆盖之前出现的同组值。
- **正确性要求较宽松**：相比 named-field mapping 格式（如 TextFormat、JSON），tag-value stream 对输入的严格性要求更低。

## 应用
- **Protobuf 二进制 wire format 的核心抽象**：所有 protobuf 二进制序列化本质上都是 tag-value stream，决定了字段存在性、字段顺序无关性以及 repeated 追加、oneof 最后写入胜出等行为。
- **字段存在性（field presence）语义的解释基础**：在 wire format 层面，"字段是否存在"完全取决于流中是否出现对应的 tag-value 对；这是 proto3 可选字段、implicit presence vs explicit presence 等讨论的底层依据。
- **与 named-field 格式的对比**：当与 TextFormat、JSON 等以"字段名 → 值"为映射单位的格式比较时，tag-value stream 的"无字段即为不存在"特性使得这些文本格式可以更严格地校验未知字段、类型不匹配等输入。

## 相关概念
- [[concepts/wire-format|Wire format]]
- [[concepts/self-delimiting-values|Self-delimiting values]]
- [[concepts/named-field-mapping-formats|Named-field mapping formats]]
- [[concepts/textformat|TextFormat]]

## 相关实体
- （无相关实体）

## 来源提及
- "These formats have correctness requirements of their own, and are generally stricter than _tagged-value stream_ formats." — [[sources/field_presence|field_presence]]
- "However, TextFormat more closely mimics the semantics of the wire format, and does, in certain cases, provide similar semantics (for example, appending repeated name-value mappings to a repeated field)." — [[sources/field_presence|field_presence]]