---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/overview]]"
  - "[[sources/features]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
tags:
  - "standard"
aliases:
  - "Protocol Buffers version 3"
  - "protobuf 3"
  - "proto3 语法"
---

## Description
Proto3 于2016年发布，是 Protocol Buffers 语言发展中的重要里程碑。它大幅简化了 proto2 的语法，移除了 `required` 字段和自定义默认值等容易引发兼容性问题的特性，强制要求所有字段使用更安全的默认行为。然而，这次激进的语言变更（`syntax = "proto3"`）也导致了 Protobuf 生态系统的分裂，不同项目被迫维护两套不兼容的语法版本。在 proto3 中，标量字段默认采用隐式存在（implicit presence）语义，除非显式标记为 `optional`；而 `enum` 类型的 `allow_alias` 默认设置为开放（OPEN）。proto3 的 `repeated` 字段默认使用 packed 编码，提高了序列化效率。作为早期版本，proto3 的语法和语义被 [[concepts/protobuf-editions|Protobuf Editions]] 体系所继承和扩展，通过 [[entities/prototiller|Prototiller]] 工具可以将其转换为 Edition 2024 文件且无行为变化。在 Editions 模式下，proto2 和 proto3 中原本存在的所有功能都将继续可用，而原本不可调和的那少数差异将作为 Features 统一表达。当前 proto3 仍被广泛使用，但 Protobuf 团队推荐新项目使用 Editions 体系以获得更灵活的字段特性控制，避免重复 proto2/proto3 分裂的历史教训。

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

> **Source: [[sources/proto3|proto3]]**
> - "It covers the proto3 revision of the protocol buffers language."
> - "The first line of the file specifies that you're using the proto3 revision of the protobuf language spec."
> - "syntax 'proto3'"
> - "In proto3, there are two types of singular fields: optional and implicit."
> - "In proto3, repeated fields of scalar numeric types use packed encoding by default."
> - "Covers how to use the proto3 revision of the Protocol Buffers language in your project."
> - "The first line of the file specifies that you're using the proto3 revision of the protobuf language spec."

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "The last radical change to Protobuf (syntax = "proto3";) split the ecosystem."
> - "proto3-style non-optional singular fields could allow non-zero defaults."
> - "In editions mode, everything that was possible in `proto2` and `proto3` will be possible, and the handful of irreconcilable differences will be expressed as features."