---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/features]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
tags:
  - "standard"
aliases:
  - "proto2"
  - "Protocol Buffers version 2"
  - "Protobuf 2"
---

## Description
proto2 是 Protocol Buffers 的第二个主要版本，"2"指其发布时的版本号。作为 proto3 之前的主流版本，proto2 提供了比 proto3 更丰富的字段存在性跟踪能力。从历史来看，proto2 主要遵循显式存在性（explicit presence）模式，几乎所有类型的 singular 字段都在生成的 API 中跟踪存在性。proto2 默认的 field_presence 行为为 EXPLICIT，enum_type 默认为 CLOSED，文件级符号可见性默认为 EXPORT_ALL。在 proto2 与 proto3 的对比中，proto2 强调显式的存在性跟踪，而 proto3 在历史上仅暴露无存在性（no presence）语义。值得注意的是，proto3 后续通过引入 `optional` 关键字采用了与 proto2 完全相同的显式存在性语法和语义，从而最小化与 proto2 的差异，并最大化与 proto2 及 Protobuf Editions 的兼容性。如果 .proto 文件未指定 edition 或 syntax，protocol buffer 编译器会默认假定使用 proto2。

## Related Concepts
- [[concepts/proto3|proto3]]
- [[concepts/edition-2024|edition-2024]]
- [[concepts/edition-2023|edition-2023]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/field-cardinality|field-cardinality]]
- [[concepts/forward-compatibility|forward-compatibility]]
- [[concepts/backward-compatibility|backward-compatibility]]
- [[concepts/serialization|serialization]]
- [[concepts/proto-file|proto-file]]
- [[concepts/field-number|field-number]]
- [[concepts/features-field_presence|features-field_presence]]
- [[concepts/features-default_symbol_visibility|features-default_symbol_visibility]]
- [[concepts/optional|optional]]
- [[concepts/message|message]]
- [[concepts/field-presence|field-presence]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/features|Features]]
- [[concepts/groups|groups]]
- [[concepts/packed|packed]]
- [[concepts/required|required]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/google|google]]
- [[entities/protoc|protoc]]
- [[entities/prototiller|prototiller]]
- [[entities/c++|C++]]

## Mentions in Source

> **Source: [[sources/overview|overview]]**
> - "When defining .proto files, you can specify cardinality (singular or repeated). In proto2 and proto3, you can also specify if the field is optional."
> - "For more information about the options available, see the language guide for proto2, proto3, or edition 2023."

> **Source: [[sources/features|features]]**
> - "Default behavior per syntax/edition: proto2 -> EXPORT_ALL"
> - "proto2 -> CLOSED (for enum_type)"
> - "proto2 -> EXPLICIT (for field_presence)"
> - "The following code sample shows a proto2 file: syntax \"proto2\""

> **Source: [[sources/proto3|proto3]]**
> - "For information on the proto2 syntax, see the Proto2 Language Guide."
> - "If no edition or syntax is specified, the protocol buffer compiler will assume you are using proto2."
> - "optional is recommended over implicit fields for maximum compatibility with protobuf editions and proto2."

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "The proto2/proto3 distinction is going away."
> - "Messages with any permutation of features are always interoperable (they can import each other freely and use messages from each other)."
> - "We still have `required` and `group`, `packed` is not everywhere, and string accessors in C++ still return `const std::string&`."
> - "Edition Zero should be viewed as the 'completion' of the union of proto2 and proto3: it contains both syntaxes as subsets (although with different spellings to disambiguate things) as well as new behavior that was previously inexpressible."
> - "Everything expressible today will remain so in Edition Zero."

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "Presence in proto3 uses exactly the same syntax and semantics as in proto2."
> - "The `optional` keyword was chosen to minimize differences with proto2."
> - "If your implementation already supports proto2, a proto3 `optional` field should use exactly the same API and internal implementation as proto2 `optional`."

> **Source: [[sources/field_presence|field_presence]]**
> - "Historically, proto2 has mostly followed explicit presence, while proto3 exposes only no presence semantics."
> - "Singular fields (of all types) track presence explicitly in the generated API."
> - "This table outlines whether presence is tracked for fields in proto2 APIs (both for generated APIs and using dynamic reflection)."