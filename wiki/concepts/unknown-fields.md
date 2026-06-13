---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/field_presence]]"
  - "[[brpc/json2pb.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
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
---

## Description
Unknown fields 是 Protocol Buffers 为实现向前兼容而设计的一种机制。当消息接收方的 proto 定义中缺少发送方传来的某个字段时，该字段的内容不会被丢弃，而是作为 unknown fields 存储在消息对象中；当消息被序列化时，这些 unknown fields 会被重新写入 wire format，从而在中间节点实现数据透传，待接收方升级 proto 定义后再正常解析。在 proto2 API 中，即使 wire format tag 被识别（例如枚举字段的 tag），若值无法被当前消息定义解释（例如枚举值超出有效范围），API 也不会直接返回该值，而是将其作为 unknown fields 存储。

Editions 提案进一步明确了 unknown fields 在 closed enum 语义下的关键作用：当解析 closed enum 时遇到不在已知值集合中的 enum 值，会被存入未知字段集而非丢弃；而 open enum 则直接将超出范围的值解析到对应字段。该机制也带来与"并行数组"（parallel arrays）场景的交互问题——一个被移入未知字段集的 enum 值会出现在字段集末尾，从而破坏并行数组之间的索引对齐。文档还指出 repeated closed enum 的解析与序列化过程会因将未知值移至末尾而改变原始顺序。

此外，protobuf 对枚举开放性的判定并非仅取决于字段定义，还可能取决于字段的使用方式。这意味着在某些语言实现中，即使 proto 定义层面未明确指定封闭性（如 proto3 消息引用 proto3 枚举），该枚举在运行时也可能被当作 closed 处理：未知的 enum 值（如 `1: 2` 中的 `2`）不会进入该 enum 字段，而是以 VARINT wire type 存入 `UnknownFieldSet`。这一行为可通过 Protoscope 等工具直接观察到 `UnknownFieldSet` 中出现对应 VARINT 值来验证。

然而，unknown fields 的完整支持受限于 protobuf 消息定义中字段的"数字标识"（即 field number，如 `required int32 foo = 3` 中的 `3`）。当一个 protobuf 不认识某个字段时，其 proto 中必然没有对应的数字标识，因此无法在结构上插入该 unknown fields。这一限制在 json2pb 等转换工具中体现得尤为明显：unknown_fields 与 JSON 之间的双向转换目前均未实现。

针对 json2pb 中无法传递 unknown fields 的问题，实践中可考虑两种方案：一是确保被 JSON 访问的服务的 proto 文件保持最新，从而避免透传需求（但在前端 proxy 类服务中可能不现实）；二是在 protobuf 中定义一个名为 `unknown_json_fields` 的特殊透传字段，在解析时进行特殊处理，使 unknown fields 能以该字段为载体进行转发——但此方案修改面广且对性能有一定影响。

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

## Related Entities
- [[entities/protocol-buffers-v3-15-0|protobuf v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|protobuf v3.12.0]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/brpc|brpc]]
- [[entities/json2pb|json2pb]]
- [[entities/protoscope|Protoscope]]

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