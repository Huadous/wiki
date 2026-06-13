---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/encoding]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
tags:
  - "product"
aliases:
  - "protoscope tool"
  - "Protoscope工具"
---

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]] — 核心关联技术
- [[entities/github|GitHub]] — 代码仓库托管平台
- [[entities/prototiller|Prototiller]] — 同类 Protobuf 工具
- [[entities/protoscope|Protoscope]] — 本页对应实体

## Related Concepts
- [[concepts/varint|Varint]] — Protoscope 直接支持的编码概念
- [[concepts/wire-format|Wire format]] — Protoscope 描述的核心对象
- [[concepts/tag-length-value-tlv|Tag-Length-Value (TLV)]] — 底层编码结构基础
- [[concepts/length-delimited-records|Length-delimited records]] — Protoscope 简写形式对应的编码方式
- [[concepts/enum-field-closedness|Enum Field Closedness]] — Protoscope 在该概念验证中被用作演示工具
- [[concepts/unknown-field-set|UnknownFieldSet]] — 当枚举封闭性判定失败时，原始值落入此集合
- [[concepts/proto3-enum|proto3 enum]] — 与封闭性边界问题相关的枚举类型

## Mentions in Source
> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "If we parse the Protoscope value `1: 2` as an `oh.no.Msg`, and look at the value of `oh.no.Msg.enum`, we will find that it is not present, and that there is a VARINT of value `2` in the `UnknownFieldSet`."
> - "`https://github.com/protocolbuffers/protoscope`"