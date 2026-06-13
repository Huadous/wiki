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
  - "[[protobuf/features.md]]"
  - "[[protobuf/editions.md]]"
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-edition-zero-json-handling.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "standard"
aliases:
  - "Protocol Buffers version 3"
  - "protobuf 3"
  - "proto3 语法"
  - "proto3 syntax"
  - "Protocol Buffers version 3"
  - "protobuf 3"
  - "proto3 语法"
---

## Description
Proto3 于2016年发布，是 Protocol Buffers 语言发展中的重要里程碑。它大幅简化了 proto2 的语法，移除了 `required` 字段和自定义默认值等容易引发兼容性问题的特性，强制要求所有字段使用更安全的默认行为。然而，这次激进的语言变更（`syntax = "proto3"`）也导致了 Protobuf 生态系统的分裂，不同项目被迫维护两套不兼容的语法版本。文件首行必须通过 `syntax = "proto3"` 显式声明 proto3，否则编译器默认假定使用 proto2。

根据 [[sources/editions-edition-zero-features|editions-edition-zero-features]] 的总结，proto3 具有以下关键特性：枚举值是开放的（open）且第一个枚举值必须为零；具有 `defaulted` 字段但没有 `required` 字段；`repeated_field_encoding` 默认为 `PACKED`。在 proto3 中，标量字段默认采用隐式存在（implicit presence）语义，除非显式标记为 `optional`；而消息类型字段自动具有字段存在性（field presence），这一行为与 Edition 2023+ 的 IMPLICIT 默认设置不同。

根据 [[sources/features|features]] 文档对 proto3 各 feature 默认行为的总结，proto3 在多个核心 feature 上采用了相对开放和宽松的默认值：`enum` 类型的 `allow_alias` 默认设置为开放（OPEN）；字段存在性（field_presence）默认为 IMPLICIT，除非字段被显式标记为 `optional` 标签时表现为 EXPLICIT；符号可见性（default_symbol_visibility）默认为 EXPORT_ALL；命名风格（enforce_naming_style）默认为 STYLE_LEGACY。需要特别注意的是，`features.enum_type` 这一 feature 对 proto3 文件不产生影响，因此该章节没有提供 proto3 的前后对比示例。

关于 `optional` 字段的存在性跟踪功能，proto3 的支持经历了一个逐步启用的过程：在 v3.12.0 之前，需要使用 `--experimental_allow_proto3_optional` 编译标志才能为 proto3 的 optional 字段启用显式存在性跟踪；自 v3.15.0 版本起，该功能默认启用。基本类型（数值、字符串、字节、枚举）的 singular proto3 字段若被标记为 `optional`，则具有与 proto2 一致的显式存在性（explicit presence）。此外，proto3 还要求所有枚举类型必须包含一个映射到 0 的枚举值（通常命名为 `UNKNOWN` 或 `_UNKNOWN`），作为未知枚举值的默认表示。proto3 的 `repeated` 字段默认使用 packed 编码，提高了序列化效率；同时 `repeated` 标量数值类型也默认采用 packed 编码。

在内部实现层面，proto3 之所以选择默认不追踪字段存在性，是因为它已经在 descriptor 层面对 singular 字段使用了 `LABEL_OPTIONAL` 标签 —— 大量现有的反射代码已经假设 proto3 中 `LABEL_OPTIONAL` 不携带存在性信息，因此不能简单地复用 proto2 的 `LABEL_OPTIONAL` 描述符语义来表示存在性。作为早期版本，proto3 的语法和语义被 [[concepts/protobuf-editions|Protobuf Editions]] 体系所继承和扩展，通过 [[entities/prototiller|Prototiller]] 工具可以将其转换为 Edition 2024 文件且无行为变化。

根据 [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]] 的描述，proto3 在 [[concepts/edition-zero|Edition Zero]] 推出之前与 [[concepts/proto2|Proto2]] 并存；[[concepts/edition-zero|Edition Zero]] 将通过 features 机制把 proto2 与 proto3 的差异统一到一组良定义的默认值上。在过渡期内，`protoc` 必须能够同时解析 proto3、proto2 和 editions 文件，这一兼容窗口预计会持续相当长的时间。schema producers 在升级到 [[concepts/edition-zero|Edition Zero]] 时可以借助官方升级工具自动完成转换，新发布的 `.proto` 文件则应直接使用 [[concepts/edition-zero|Edition Zero]] 的默认值。在 Editions 模式下，proto2 和 proto3 中原本存在的所有功能都将继续可用，而原本不可调和的那少数差异将作为 Features 统一表达。在从 proto3 迁移到 editions 时，原有的 implicit 字段会使用 field_presence feature 并设置为 IMPLICIT 值。proto3 的语言指南是一个独立的文档，但 [[sources/editions|editions]] 指南对其迁移行为做了相应说明。

特别值得注意的是，根据 [[sources/editions-edition-zero-features|editions-edition-zero-features]] 的描述，proto3 的行为对应于大多数特性的默认值（如 `features.field_presence = EXPLICIT`、`features.enum_type = OPEN`、`features.repeated_field_encoding = PACKED`），因此大多数 proto3 文件迁移到 editions 时不需要额外标注。这一映射关系使得 proto3 成为 Editions 体系中最重要的"基线"语义集合。当前 proto3 仍被广泛使用，但 Protobuf 团队推荐新项目使用 Editions 体系以获得更灵活的字段特性控制，避免重复 proto2/proto3 分裂的历史教训。

根据 [[sources/editions-life-of-an-edition|editions-life-of-an-edition]] 的说明，与 [[concepts/proto2|Proto2]] 类似，从 proto3 到 Editions 的迁移也是通过 `protoc --upgrade-edition` 工具完成的。该工具会为文件添加适当的 edition 声明（如 `edition = "2023";`）和 `option features.* = ...;` 设置，使其保留原始行为。Editions 机制旨在统一替换 proto2 和 proto3，提供更灵活、可演进的 features 系统；[[concepts/edition-zero|Edition Zero]] 的迁移涉及同时处理这两种旧语法，升级工具能够自动判断源文件是 proto2 还是 proto3，并相应地添加 features 以维持原有语义。

根据 [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]] 的提案，proto3 在 editions 系统中同样被视为"遗留语法"。该提案建议将 proto3 作为 `EDITION_PROTO3 = 999` 的特殊 edition 来处理，使其与 proto2 一样被纳入统一的 editions 框架。proto3 的语法元素（如 `optional` 关键字设置 EXPLICIT presence）与 editions 的 feature 之间存在映射关系，需要通过专门的 feature inference 逻辑来处理。这意味着在从 proto3 向 editions 迁移时，系统需要自动识别 proto3 特有的语法形式（如 `optional` 标记的字段对应 `field_presence = EXPLICIT`），并将其转换为等价的 features 表达。

根据 [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]] 的讨论，由于 [[concepts/edition-zero|Edition Zero]] 保留了所有 proto2/proto3 行为，因此即使在 features 层面进行重新建模（例如 UTF8 校验应该如何作为 feature 表达），相关的提案都不会产生任何功能性变化 —— 这些讨论本质上只是为了确定应该使用哪些 features 来控制已有的行为。这一事实进一步说明了 proto3 的语义在 Editions 系统中被视为必须完全保留的基线（baseline），任何 features 的调整都不得突破该基线所承载的现有行为契约，从而保障现有 proto3 用户向 Editions 迁移的无缝性。

在 JSON 处理方面，根据 [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]] 的提案，proto3 默认会完全验证 JSON 映射的唯一性：protoc 会在解析时检测到任何 JSON 冲突并直接报错。可通过 `deprecated_legacy_json_field_conflicts` 选项禁用此严格检查，使其退化为尽力而为模式。该提案建议将 proto3 的这一默认行为迁移到 [[concepts/allow|ALLOW]] 状态，与 [[concepts/proto2|Proto2]] 的 JSON 处理行为保持一致。

## Related Concepts
- [[concepts/proto2|Proto2]]
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/edition-2024|Edition 2024]]
- [[concepts/editions|Protobuf Editions]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/editions-upgrader|Editions upgrader]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/features-field_presence|features.field_presence]]
- [[concepts/features-enum_type|features.enum_type]]
- [[concepts/features-enforce_naming_style|features.enforce_naming_style]]
- [[concepts/features-default_symbol_visibility|features.default_symbol_visibility]]
- [[concepts/features-repeated_field_encoding|features.repeated_field_encoding]]
- [[concepts/feature-setting-scope|Feature setting scope]]
- [[concepts/proto-file|.proto file]]
- [[concepts/field-number|Field number]]
- [[concepts/serialization|Serialization]]
- [[concepts/backward-compatibility|Backward compatibility]]
- [[concepts/forward-compatibility|Forward compatibility]]
- [[concepts/field|Field]]
- [[concepts/cardinality|Field cardinality]]
- [[concepts/message|Message]]
- [[concepts/field-presence|Field presence]]
- [[concepts/no-presence-discipline|No presence discipline]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/packed-encoding|Packed encoding]]
- [[concepts/reserved|Reserved]]
- [[concepts/features|Features]]
- [[concepts/naming-style|Naming style]]
- [[concepts/symbol-visibility|Symbol visibility]]
- [[concepts/enum-type|Enum type]]
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]
- [[concepts/feature-inference|Feature Inference]]
- [[concepts/editions-feature-visibility|Editions Feature Visibility]]
- [[concepts/allow|ALLOW]]
- [[concepts/legacy_best_effort|LEGACY_BEST_EFFORT]]
- [[concepts/deprecated_legacy_json_field_conflicts|deprecated_legacy_json_field_conflicts]]
- [[concepts/json-field-name-conflicts|JSON Field Name Conflicts]]

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
- [[entities/protobuf-team|Protobuf team]]
- [[entities/mkruskal-google|mkruskal-google]]

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
> - "proto3 IMPLICIT"
> - "proto3 is IMPLICIT unless the field has the optional label, in which case it behaves like EXPLICIT. See Presence in Proto3 APIs for more information."

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

> **Source: [[sources/editions|editions]]**
> - "Proto3 implicit fields that have been migrated to editions will use the field_presence feature set to the IMPLICIT value."

> **Source: [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]]**
> - "The first edition (colloquially known as "Edition Zero") will use features to unify proto2 and proto3 (Edition Zero Features)."
> - "There will be a large period of time during which `protoc` is able to consume `proto3`, `proto2`, and editions files."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "Tooling that can take a `proto2` or `proto3` file and add `edition = "2023";` and `option features.* = ...;` as appropriate, so that each file retains its original behavior."
> - "Running `protoc --upgrade-edition -I... file.proto` figure out how to update `file.proto` from `proto2` or `proto3` to the latest edition, adding features as necessary."

> **Source: [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]**
> - "Since early in the design process, we've discussed the possibility of making proto2 and proto3 "special" editions"
> - "we've discussed the possibility of making proto2 and proto3 "special" editions, but never laid out what exactly it would look like or determined if it was necessary."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "We've bounced back and forth on how UTF8 validation should be modeled as a feature. None of the proposals resulted in any functional changes, since edition zero preserves all proto2/proto3 behavior, the question was just about what features should be used to control them."

> **Source: [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]**
> - "The Protobuf compiler will fail to parse any proto3 files if any JSON conflicts are detected by default"
> - "Disabled by `deprecated_legacy_json_field_conflicts` option"

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "In proto3, `enum` values are open and the first `enum` value must be zero."
> - "Proto3 has `defaulted` but not `required`."
> - "In proto3, the `repeated_field_encoding` attribute defaults to `PACKED`."