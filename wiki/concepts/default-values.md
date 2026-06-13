---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/proto3]]"
  - "[[protobuf/field_presence.md]]"
tags:
  - "term"
aliases:
  - "默认值"
  - "零值"
  - "Default Values"
  - "Default value"
  - "默认值"
  - "零值"
  - "Default Values"
---

## Description
Default Values 是 Protocol Buffers proto3 中定义的核心规则——当字段未被用户显式设置时，访问该字段将返回一个与类型对应的默认值。不同字段类型的默认值各有规定：数值类型默认为 0，枚举类型默认为零值枚举器（zero-valued enumerator），字符串、字节和 repeated 字段默认为零长度值，message 类型默认为语言相关的 null 值。

Default Values 的行为与字段存在性（field presence）规则密不可分，二者共同决定消息的序列化与合并语义。在 proto3 的 _no presence_ 规则下，默认值在序列化意义上等同于"未设置"——该字段不会被写入线格式中，也不会参与 merge-from 操作，因此接收方无法区分"显式设置为零值"与"从未设置"两种情况，这一设计有效节省了带宽和存储空间。在 _explicit presence_ 规则下（即 `optional` 字段），即使字段被显式赋值为默认值，该值也会被序列化到线格式中，接收方可据此区分字段的存在状态。

值得注意的是，proto3 中消息类型（message fields）字段默认即具有存在性语义：当消息未被设置时返回默认的空消息，其行为与 `optional` 字段一致，而与隐式标量字段不同。

## Related Concepts
- [[concepts/field-presence|field-presence]]
- [[concepts/scalar-types|scalar-types]]
- [[concepts/field-cardinality|field-cardinality]]

## Related Entities
- [[entities/Protocol-Buffers|Protocol Buffers]]

## Mentions in Source
- "the field is unset, and will return the default value. It will not be serialized to the wire." — [[sources/proto3|proto3]]
- "the field is set to the default (zero) value. It will not be serialized to the wire." — [[sources/proto3|proto3]]

> **Source: [[sources/field_presence|field_presence]]**
> - "For numeric types, the default is 0."
> - "For enums, the default is the zero-valued enumerator."
> - "For strings, bytes, and repeated fields, the default is the zero-length value."
> - "Under the _no presence_ discipline, the default value is synonymous with 'not present' for purposes of serialization."