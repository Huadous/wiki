---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/field_presence]]"
  - "[[brpc/json2pb.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
  - "[[protobuf/editions-edition-naming.md]]"
tags:
  - "term"
aliases:
  - "unknown field"
  - "Unknown Fields"
  - "Unknown fields处理"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown field set"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown fields处理"
  - "unknown field"
  - "Unknown Fields"
  - "UnknownFieldSet"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown fields处理"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown field set"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown fields处理"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown Field Set"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown fields处理"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown field set"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown fields处理"
  - "unknown field"
  - "Unknown Fields"
  - "UnknownFieldSet"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown fields处理"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown field set"
  - "unknown field"
  - "Unknown Fields"
  - "Unknown fields处理"
  - "unknown field"
  - "Unknown Fields"
---

## Related Concepts
- [[concepts/wire-format|Wire format]]
- [[concepts/field-presence|Field presence]]
- [[concepts/json-protobuf-conversion|JSON-protobuf转换规则]]
- [[concepts/closed-enum|Closed enum]]
- [[concepts/open-enum|Open enum]]
- [[concepts/parallel-arrays|Parallel arrays]]
- [[concepts/features-enum-type|features.enum_type]]
- [[concepts/unknownfieldset|UnknownFieldSet]]
- [[concepts/proto3-enum|proto3 enum]]
- [[concepts/enum-field-closedness|Enum Field Closedness]]
- [[concepts/edition-enum|Edition enum]]

## Related Entities
- [[entities/protocol-buffers-v3-15-0|protobuf v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|protobuf v3.12.0]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/brpc|brpc]]
- [[entities/json2pb|json2pb]]
- [[entities/protoscope|Protoscope]]
- [[entities/descriptor-proto|descriptor.proto]]

## Mentions in Source
> **Source: [[sources/field_presence|field_presence]]**
> - "Out-of-range values are not returned for enum fields in generated proto2 APIs."
> - "However, out-of-range values may be stored as _unknown fields_ in the API, even though the wire-format tag was recognized."

> **Source: [[sources/json2pb|json2pb]]**
> - "unknown_fields → json目前不支持，未来可能支持。"
> - "这也是unknown_fields的key。当一个protobuf不认识某个字段时，其proto中必然不会有那个数字，所以没办法插入unknown_fields。"
> - "确保被json访问的服务的proto文件最新。这样就不需要透传了，但越前端的服务越类似proxy，可能并不现实。"

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "closed enums will store enum values that are out of range in the unknown field set"
> - "an unknown enum value from a parallel array will be placed in the unknown field set and the arrays will cease being parallel"

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "we will find that it is not present, and that there is a VARINT of value 2 in the UnknownFieldSet."
> - "This is because Protobuf sometimes implements the openness of an enum by its usage, *not* its definition."

> **Source: [[sources/editions-edition-naming|editions-edition-naming]]**
> - "Ideally, this would be an open enum to avoid ever having the edition thrown into the unknown field set."
> - "However, since it needs to exist in `descriptor.proto`, we won't be able to make it open until the end of our edition zero migration."
> - "No directly relevant information"