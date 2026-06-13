---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/techniques]]"
  - "[[sources/editions]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/java-lite.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
  - "[[protobuf/editions.md]]"
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
  - "[[protobuf/editions-minimum-required-edition.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "product"
aliases:
  - "Protocol Buffers compiler"
  - "protoc compiler"
---

## Description
protoc 是 Protocol Buffers 的官方编译器，是 Protobuf Editions 机制的核心工具。在 Editions 体系中，protoc 扮演双重角色：其 frontend 与各语言后端（backend）共同理解一组 feature 的默认值集合——这就是一个 edition（"An edition is a set of default values for all features that protoc's frontend, and its backends, understand"）。其中，protoc 仅定义全局（global）feature 的 edition 默认值，而各 backend 则自行定义其语言作用域（language-scoped）feature 的默认值。

protoc 在 Edition 时代提供了多种面向大规模迁移的工具能力。`protoc --gc-features` 可以计算并回收（garbage-collect）一个 .proto 文件中冗余的 feature 设置，仅保留必要的最小集合；`protoc --upgrade-edition`（Editions adopter）以及 Editions upgrader 则帮助用户将旧语法（proto2/proto3）平稳升级到指定 edition。此外，protoc 还提供 `--latest-edition` 命令以输出当前支持的最新 edition，方便外部工具（如 ProtoChangeSpec）据此生成最新的 .proto 模板。

在历史演进方面，protoc 自 v3.15.0 起默认启用 proto3 字段存在性（presence）跟踪，在此之前（v3.12.0 及更早版本）需要显式传递 `--experimental_allow_proto3_optional` 标志才能使用该特性。对于 Editions，`protoc` 必须能够同时消费 proto3、proto2 与 editions 文件，并校验 .proto 定义文件的语法正确性。`protoc` 的 frontend 还承担跟踪各语法构造所需最低 edition（minimum required edition）的职责。

## Related Entities
- [[entities/google-inc|Google Inc.]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|Protocol Buffers v3.12.0]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/bazel|Bazel]]
- [[entities/protobuf-team|Protobuf team]]
- [[entities/prototiller|Prototiller]]
- [[entities/protobuf-minimum-required-edition|Protobuf Minimum Required Edition]]

## Related Concepts
- [[concepts/protocol-buffers|Protocol Buffers]]
- [[concepts/.proto-file|.proto file]]
- [[concepts/message-type|Message Type]]
- [[concepts/feature-proto3-optional|FEATURE_PROTO3_OPTIONAL]]
- [[concepts/code-generator|Code Generator]]
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/proto3|proto3]]
- [[concepts/proto2|proto2]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/optional-label|Optional label]]
- [[concepts/schema-producer|Schema Producer]]
- [[concepts/schema-consumer|Schema Consumer]]
- [[concepts/semantic-patch|Semantic Patch]]
- [[concepts/target-attributes|Target Attributes]]
- [[concepts/retention|Retention]]
- [[concepts/options-attributes|Options Attributes]]
- [[concepts/fieldoptions|FieldOptions]]
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/filedescriptorproto|FileDescriptorProto]]
- [[concepts/descriptor.proto|descriptor.proto]]
- [[concepts/edition|Edition]]
- [[concepts/protoc-frontend|protoc frontend]]
- [[concepts/feature|Feature]]
- [[concepts/features-gc|Features GC]]
- [[concepts/editions-adopter|Editions adopter]]
- [[concepts/editions-upgrader|Editions upgrader]]
- [[concepts/protochangespec|ProtoChangeSpec]]

## Mentions in Source

> **Source: [[sources/proto3|proto3]]**
> - "If no syntax is specified, the protocol buffer compiler will assume you are using proto2."
> - "When you run the protocol buffer compiler on a .proto, the compiler generates the code in your chosen language you'll need to work with the message types you've described in the file, including getting and setting field values, serializing your messages to an output stream, and parsing your messages from an input stream."
> - "The protoc compiler will generate error messages if any future developers try to use these reserved field numbers."

> **Source: [[sources/java-lite|java-lite]]**
> - "You can generate Java Lite code for your .proto files:"
> - "$ protoc --java_out=lite:${OUTPUT_DIR} path/to/your/proto/file"
> - "The \"optimize_for = LITE_RUNTIME\" option in the .proto file no longer has any effect on Java code."

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "If you try to run `protoc` on a file with proto3 optional fields, you will get an error because the feature is still experimental."
> - "Pass `--experimental_allow_proto3_optional` to protoc."
> - "Make your filename (or a directory name) contain the string `test_proto3_optional`."

> **Source: [[sources/field_presence|field_presence]]**
> - "Run protoc (at least v3.15, or v3.12 using --experimental_allow_proto3_optional flag)."
> - "Presence tracking for proto3 messages is enabled by default since v3.15.0 release, formerly up until v3.12.0 the --experimental_allow_proto3_optional flag was required when using presence tracking with protoc."

> **Source: [[sources/editions|editions]]**
> - "When you run the protocol buffer compiler on a .proto, the compiler generates the code in your chosen language you'll need to work with the message types you've described in the file"
> - "The protoc compiler will generate error messages if any future developers try to use these reserved field numbers."
> - "The protoc parser validates that a given proto definition file is parseable."

> **Source: [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]]**
> - "There will be a large period of time during which `protoc` is able to consume `proto3`, `proto2`, and editions files."
> - "we will provide primitives in `protoc` to compile a `.proto` file and a semantic patch as a set of inputs so that users never have to materialize the modified `.proto` file."

> **Source: [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]**
> - "If no target is provided, `protoc` will permit the target to apply to any entity."
> - "Otherwise, `protoc` will allow an option to be applied at either the file level or to its target entity (and will produce a compile error for any other placement)."
> - "**Code generators that emit generated descriptors will be required to omit/strip options with `SOURCE` retention from their generated descriptors.**"

> **Source: [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]**
> - "`protoc` should keep track of which constructions require which minimum edition."
> - "This logic should be implemented entirely in the protoc frontend."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "An edition is a set of default values for all features that protoc's frontend, and its backends, understand."
> - "Running protoc --gc-features foo.proto on a file in editions mode will compute the minimal (or a heuristically minimal, if this proves expensive) set of features to set on things, given the edition specified in the file."