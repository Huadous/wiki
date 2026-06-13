---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/features]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
tags:
  - "standard"
aliases:
  - "Protocol Buffers version 3"
  - "protobuf 3"
  - "proto3 语法"
---

## Description
Proto3 于2016年发布，是 Protocol Buffers 语言发展中的重要里程碑。它大幅简化了 proto2 的语法，移除了 `required` 字段和自定义默认值等容易引发兼容性问题的特性，强制要求所有字段使用更安全的默认行为。然而，这次激进的语言变更（`syntax = "proto3"`）也导致了 Protobuf 生态系统的分裂，不同项目被迫维护两套不兼容的语法版本。文件首行必须通过 `syntax = "proto3"` 显式声明 proto3，否则编译器默认假定使用 proto2。在 proto3 中，标量字段默认采用隐式存在（implicit presence）语义，除非显式标记为 `optional`；而消息类型字段自动具有字段存在性（field presence），这一行为与 Edition 2023+ 的 IMPLICIT 默认设置不同。`enum` 类型的 `allow_alias` 默认设置为开放（OPEN）。proto3 的 `repeated` 字段默认使用 packed 编码，提高了序列化效率；同时 `repeated` 标量数值类型也默认采用 packed 编码。proto3 引入了两种 singular 字段模式：optional 和 implicit，并推荐使用 `optional` 关键字标注字段以获得与 protobuf editions 和 proto2 的最大兼容性。

关于 `optional` 字段的存在性跟踪功能，proto3 的支持经历了一个逐步启用的过程：在 v3.12.0 之前，需要使用 `--experimental_allow_proto3_optional` 编译标志才能为 proto3 的 optional 字段启用显式存在性跟踪；自 v3.15.0 版本起，该功能默认启用。基本类型（数值、字符串、字节、枚举）的 singular proto3 字段若被标记为 `optional`，则具有与 proto2 一致的显式存在性（explicit presence）。此外，proto3 还要求所有枚举类型必须包含一个映射到 0 的枚举值（通常命名为 `UNKNOWN` 或 `_UNKNOWN`），作为未知枚举值的默认表示。

在内部实现层面，proto3 之所以选择默认不追踪字段存在性，是因为它已经在 descriptor 层面对 singular 字段使用了 `LABEL_OPTIONAL` 标签 —— 大量现有的反射代码已经假设 proto3 中 `LABEL_OPTIONAL` 不携带存在性信息，因此不能简单地复用 proto2 的 `LABEL_OPTIONAL` 描述符语义来表示存在性。作为早期版本，proto3 的语法和语义被 [[concepts/protobuf-editions|Protobuf Editions]] 体系所继承和扩展，通过 [[entities/prototiller|Prototiller]] 工具可以将其转换为 Edition 2024 文件且无行为变化。在 Editions 模式下，proto2 和 proto3 中原本存在的所有功能都将继续可用，而原本不可调和的那少数差异将作为 Features 统一表达。当前 proto3 仍被广泛使用，但 Protobuf 团队推荐新项目使用 Editions 体系以获得更灵活的字段特性控制，避免重复 proto2/proto3 分裂的历史教训。

## Related Concepts
- [[concepts/proto2|Proto2]]
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/edition-2024|Edition 2024]]
- [[concepts/features-field_presence|features.field_presence]]
- [[concepts/features-enforce_naming_style|features.enforce_naming_style]]
- [[concepts/features-default_symbol_visibility|features.default_symbol_visibility]]
- [[concepts/feature-setting-scope|Feature setting scope]]
- [[concepts/proto-file|.proto file]]
- [[concepts/field-number|Field number]]
- [[concepts/serialization|Serialization]]
- [[concepts/backward-compatibility|Backward compatibility]]
- [[concepts/forward-compatibility|Forward compatibility]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/field|Field]]
- [[concepts/cardinality|Field cardinality]]
- [[concepts/message|Message]]
- [[concepts/field-presence|Field presence]]
- [[concepts/no-presence-discipline|No presence discipline]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/packed-encoding|Packed encoding]]
- [[concepts/reserved|Reserved]]
- [[concepts/features|Features]]
- [[concepts/edition-zero|Edition Zero]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/prototiller|Prototiller]]
- [[entities/grpc|gRPC]]
- [[entities/google|Google]]
- [[entities/c++|C++]]
- [[entities/codegeneratorresponse|CodeGeneratorResponse]]
- [[entities/protocol-buffers-v3-12-0|Protocol Buffers v3.12.0]]
- [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]]

## Mentions in Source

> **Source: [[sources/overview|overview]]**
> - "In proto2 and proto3, you can also specify if the field is optional."
> - "In proto3, setting a field to optional changes it from implicit presence to explicit presence."
> - "For more information about the options available, see the language guide for proto2, proto3, or edition 2023."

> **Source: [[sources/features|features]]**
> - "Default behavior per syntax/edition: proto3 -> EXPORT_ALL"
> - "proto3 -> OPEN (for enum_type)"
> - "proto3 -> IMPLICIT (for field_presence) unless the field has the optional label"
> - "This feature doesn't impact proto3 files, so this section doesn't have a before and after of a proto3 file."

> **Source: [[sources/proto3,proto3]]**
> - "It covers the proto3 revision of the protocol buffers language."
> - "The first line of the file specifies that you're using the proto3 revision of the protobuf language spec."
> - "syntax 'proto3'"
> - "In proto3, there are two types of singular fields: optional and implicit."
> - "In proto3, repeated fields of scalar numeric types use packed encoding by default."
> - "Covers how to use the proto3 revision of the Protocol Buffers language in your project."
> - "The first line of the file specifies that you're using the proto3 revision of the protobuf language spec."
> - "For information on the proto2 syntax, see the Proto2 Language Guide"

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "The last radical change to Protobuf (syntax = "proto3";) split the ecosystem."
> - "proto3-style non-optional singular fields could allow non-zero defaults."
> - "In editions mode, everything that was possible in `proto2` and `proto3` will be possible, and the handful of irreconcilable differences will be expressed as features."

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "Proto3 Fields marked `optional` will track presence like proto2, while fields without any label (known as "singular fields"), will continue to omit presence information."
> - "Proto3 descriptors already use `LABEL_OPTIONAL` for proto3 singular fields, which do not track presence."

> **Source: [[sources/field_presence|field_presence]]**
> - "Singular proto3 fields of basic types (numeric, string, bytes, and enums) which are defined with the optional label have explicit presence, like proto2 (this feature is enabled by default as release 3.15)."
> - "This table outlines whether presence is tracked for fields in proto3 APIs (both for generated APIs and using dynamic reflection)."