---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/features.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "term"
aliases:
  - "open enum"
  - "开放式枚举"
---

## Description
Open Enum 是 Protocol Buffers 中枚举（enum）的开放式行为模式，与 [[concepts/closed-enum|Closed Enum]] 形成对比。其核心特征是不对字段值进行枚举集合范围校验：当序列化或反序列化遇到未在 `.proto` 文件中定义的整数值时，该值会直接存入对应字段，而不会触发未知字段（unknown field）机制。从底层实现角度看，open enum 实际上只是一个带有已知（well-known）值的 `int32` 字段。

在历史演进中，[[concepts/proto3|Proto3]] 语法采用的就是 open enum 行为，但同时附加了一条约束：第一个枚举值必须为零（作为默认值）。在 [[concepts/edition-2023|Edition 2023]] 及后续版本中，枚举的开闭行为通过 [[concepts/feature|feature]] 机制显式控制，即 `feature.enum = OPEN` 或 `feature.enum = CLOSED`，从而将枚举行为与具体的 [[concepts/proto3|Proto3]] 语法解耦。[[concepts/edition-2024|Edition 2024]] 进一步取消了"第一个枚举值必须为零"的限制，允许非零值作为默认枚举值，这是一个之前未明确表达过的新状态。Edition Zero 将 `OPEN` 作为 `features.enum_type` 的默认值，以兼容既有的 proto3 语义。

## Related Concepts
- [[concepts/closed-enum|Closed Enum]]
- [[concepts/feature|Feature]]
- [[concepts/proto3|Proto3]]
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/edition-2024|Edition 2024]]
- [[concepts/edition-zero|Edition Zero]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]

## Mentions in Source
> **Source: [[sources/editions-what-are-protobuf-editions]]**
> - "whether values not specified in an enum go into unknown fields vs producing an enum value outside of the bounds of the specified values in the .proto file (i.e., so-called closed and open enums) will be controlled by feature.enum = OPEN or feature.enum = CLOSED."

> **Source: [[sources/features]]**
> - "OPEN: Open enums parse out of range values into their fields directly."
> - "This feature sets the behavior for how enum values that aren't contained within the defined set are handled. See Enum Behavior for more information on open and closed enums."

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "An **open enum** does not have this restriction, and is just an `int32` field with well-known values."
> - "*open* enums will parse out of range values into their fields directly."
> - "In proto3, `enum` values are open and the first `enum` value must be zero."