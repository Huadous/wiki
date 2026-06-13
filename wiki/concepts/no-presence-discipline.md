---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/field_presence|field_presence]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "method"
aliases:
  - "No presence discipline"
  - "无存在性模式"
  - "implicit presence"
  - "IMPLICIT presence"
  - "No presence discipline"
  - "无存在性模式"
  - "implicit presence"
---

## Description
No presence discipline 是 Protocol Buffers 字段存在性管理的两种基本范式之一，其核心特征是生成的 API 不暴露任何 hasbit 或显式存在性跟踪状态——仅有字段值被存储。在这种模式下，默认值与"不存在"在序列化时完全等价：未被设置的字段不会被序列化输出，即使该默认值是被显式设置的也不会进入 wire format。该模式是 proto3 中未使用 `optional` 标签的标量字段的默认行为，也是 Editions 体系中 `IMPLICIT` 字段存在性的语义基础。

在 Editions 框架下，`IMPLICIT` 字段被明确规定"行为与 proto3 implicit 字段高度一致"：它们不能拥有自定义默认值，并且当字段类型为子消息（submessage）时，IMPLICIT 字段在合并（merge）操作中会被忽略。此外，当一个 IMPLICIT 字段是 enum 类型时，该 enum 必须是 open 状态——这可以通过将 enum 定义在 `syntax = proto3` 文件中实现，也可以通过 `features.enum_type = OPEN` 在字段层级传递性地设置。值得注意的是，Editions 设计过程中曾考虑允许 IMPLICIT 字段拥有自定义默认值，但该方案后被划去，决定保持与 proto3 完全一致以提升跨版本兼容性。

## Related Concepts
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/field-presence|Field presence]]
- [[concepts/wire-format|Wire format]]
- [[concepts/open-enum|Open enum]] *(如已存在，否则保留现有链接)*

## Related Entities
- [[entities/protocol-buffers-v3-15-0|protobuf v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|protobuf v3.12.0]]
- *(Editions 体系作为 `IMPLICIT` 的新载体尚无独立实体页面，故暂不新增)*

## Mentions in Source
- "The no presence discipline relies upon the field value itself to make decisions at (de)serialization time, while the explicit presence discipline relies upon the explicit tracking state instead." — [[sources/field_presence|field_presence]]
- "Under the no presence discipline, the default value is synonymous with 'not present' for purposes of serialization." — [[sources/field_presence|field_presence]]

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "`IMPLICIT` - the field has *no presence* discipline. The default value is not serialized onto the wire (even if it is explicitly set)."
> - "`IMPLICIT` fields behave much like proto3 implicit fields: they cannot have custom defaults and are ignored on submessage fields."