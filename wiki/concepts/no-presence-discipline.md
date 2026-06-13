---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/field_presence|field_presence]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
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

## Related Concepts
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/field-presence|Field presence]]
- [[concepts/wire-format|Wire format]]
- [[concepts/open-enum|Open enum]]
- [[concepts/proto3|proto3]]
- [[concepts/proto2|proto2]]

## Related Entities
- [[entities/protocol-buffers-v3-15-0|protobuf v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|protobuf v3.12.0]]

## Mentions in Source
- "The no presence discipline relies upon the field value itself to make decisions at (de)serialization time, while the explicit presence discipline relies upon the explicit tracking state instead." — [[sources/field_presence|field_presence]]
- "Under the no presence discipline, the default value is synonymous with 'not present' for purposes of serialization." — [[sources/field_presence|field_presence]]

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "`IMPLICIT` - the field has *no presence* discipline. The default value is not serialized onto the wire (even if it is explicitly set)."
> - "`IMPLICIT` fields behave much like proto3 implicit fields: they cannot have custom defaults and are ignored on submessage fields."

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "such enums can have nonzero defaults, which proto3 does not support due to implicit presence."