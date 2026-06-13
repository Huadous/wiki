---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/field_presence.md]]"
tags:
  - Field presence
  - No presence discipline
  - Explicit presence discipline
  - Wire format
  - proto2
  - proto3
  - Oneof
  - Hazzer methods
  - Default value
  - JSON
  - Merging
  - Repeated fields
  - Map fields
  - Unknown fields
  - Forward and backward compatibility
  - Dynamic reflection
  - '`optional` label'
  - Packed repeated field
  - Named-field mapping formats
  - Tag-value stream
  - Self-delimiting values
  - Last one wins rule
  - Change-compatibility
  - Empty length-delimited values
  - Clear methods
  - UNKNOWN enumerator
  - '`--experimental_allow_proto3_optional` flag'
aliases: ["Application note: Field presence", "protobuf 字段存在性应用笔记"]
---

# 应用笔记：字段存在性 - Summary

## 来源
- Original file: [[protobuf/field_presence.md]]
- Ingested: 2026-06-13

## 核心内容
本应用笔记系统介绍了 [[entities/protocol-buffers|Protocol Buffers]] 中[[concepts/field-presence|字段存在性（field presence）]] 的概念与实践，涵盖两种核心机制：[[concepts/no-presence-discipline|无存在性模式]]（API 仅存储字段值，默认值等同于未设置）与[[concepts/explicit-presence-discipline|显式存在性模式]]（API 同时存储字段值与设置状态，可通过 [[concepts/hazzer-methods|hazzers]] 与 [[concepts/clear-methods|clear 方法]] 操作）。文档对比了 [[concepts/proto2|proto2]]（默认显式存在）与 [[concepts/proto3|proto3]]（默认无存在性）的行为差异，说明 proto3 可通过 `[[concepts/`optional`-label|optional]]` 标签为基本类型字段启用显式存在性。同时分析了 [[concepts/wire-format|wire format]]、[[entities/textformat|TextFormat]] 与 [[concepts/json|JSON]] 三种序列化格式在存在性语义上的不同表现，并讨论了 [[concepts/merging|merging]] 行为、字段默认值处理及变更兼容性，并附有 C++、Java、Python、Go 等多语言代码示例。

## 关键实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/textformat|TextFormat]]
- [[entities/fieldmask|FieldMask]]
- [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|Protocol Buffers v3.12.0]]

## 关键概念
- [[concepts/field-presence|字段存在性]]
- [[concepts/no-presence-discipline|无存在性模式]]
- [[concepts/explicit-presence-discipline|显式存在性模式]]
- [[concepts/wire-format|线缆格式]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]
- [[concepts/oneof|oneof]]
- [[concepts/hazzer-methods|hazzers]]
- [[concepts/default-value|默认值]]
- [[concepts/json|JSON]]
- [[concepts/merging|合并]]
- [[concepts/repeated-fields|repeated fields]]
- [[concepts/map-fields|map fields]]
- [[concepts/unknown-fields|unknown fields]]
- [[concepts/forward-and-backward-compatibility|向前和向后兼容性]]
- [[concepts/dynamic-reflection|动态反射]]
- [[concepts/`optional`-label|`optional` 标签]]
- [[concepts/packed-repeated-field|packed encoding]]
- [[concepts/named-field-mapping-formats|named-field mapping 格式]]
- [[concepts/tag-value-stream|tag-value stream]]
- [[concepts/self-delimiting-values|自定界值]]
- [[concepts/last-one-wins-rule|"最后一个胜出"规则]]
- [[concepts/change-compatibility|变更兼容性]]
- [[concepts/empty-length-delimited-values|空 length-delimited 值]]
- [[concepts/clear-methods|clear 方法]]
- [[concepts/unknown-enumerator|UNKNOWN enumerator]]
- [[concepts/`-experimental_allow_proto3_optional`-flag|`--experimental_allow_proto3_optional` 标志]]

## 要点
- Protocol Buffers 字段存在性有两种主要模式：**无存在性**（仅存储字段值，默认值即未设置）与**显式存在性**（同时存储字段值与设置状态）。
- **proto2** 默认采用[[concepts/explicit-presence-discipline|显式存在性]]，几乎所有 singular 字段均跟踪存在性；**proto3** 默认采用[[concepts/no-presence-discipline|无存在性]]，但可通过 `optional` 标签为基本类型字段启用显式存在性。
- proto3 的 `optional` 显式存在性功能自 **v3.15.0** 起默认启用；v3.12.0 到 v3.15.0 之间需使用 [[concepts/`-experimental_allow_proto3_optional`-flag|`--experimental_allow_proto3_optional`]] 标志。
- [[concepts/wire-format|wire format]] 仅表示"已存在"的字段，不包含"不存在"信息；[[entities/textformat|TextFormat]] 在语义上接近 wire format，而 [[concepts/json|JSON]] 可通过 `null` 值表示"已定义但不存在"的字段。
- [[concepts/repeated-fields|repeated fields]] 与 [[concepts/map-fields|map fields]] **不**跟踪显式存在性：空集合与未设置之间无 API 级别区分。
- 在无存在性模式下，[[concepts/merging|merging]] 操作会跳过默认值，无法通过合并将字段更新为默认值，通常需要借助 [[entities/fieldmask|FieldMask]] 等外部机制。
- 在显式存在性语义下，应使用 `has_foo`（[[concepts/hazzer-methods|hazzer]]）查询状态，使用 `clear_foo`（[[concepts/clear-methods|clear 方法]]）取消设置，而非通过赋值为默认值来模拟。
- [[concepts/oneof|oneof]] 字段在 proto2 和 proto3 中均暴露存在性信息，遵循 [[concepts/last-one-wins-rule|"最后一个胜出"]] 规则；其 wire format 可能包含多个属于同一 oneof 的 (tag, value) 对。
- proto3 要求所有 enum 类型必须有映射到 0 的枚举值（习惯上命名为[[concepts/unknown-enumerator|UNKNOWN]]），若 0 不在合法值域内，则此默认行为在功能上等效于显式存在性。
- 将字段在显式存在性与无存在性之间切换在 wire format 上属于[[concepts/change-compatibility|二进制兼容变更]]，但消息的序列化表示可能不同；若客户端依赖显式存在性，经由另一版本的客户端 round-trip 可能产生有损结果。