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
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
  - "[[protobuf/editions-edition-zero-json-handling.md]]"
tags:
  - "product"
aliases:
  - "Protocol Buffers compiler"
  - "protoc compiler"
---

## Description
protoc 是 Protobuf 项目的官方编译器工具，负责将 .proto 文件解析为 [[concepts/descriptor-pool|Descriptor Pool]]，并将其分发至各语言后端代码生成器以及特性解析模块。在字段存在性方面，protoc 自 v3.15.0 起默认启用 proto3 的 [[concepts/explicit-presence-discipline|显式存在性]]语义（之前需使用 `--experimental_allow_proto3_optional` 标志）。在 Editions 体系中，protoc 前端承担 [[concepts/feature-resolution|特性解析]]、[[concepts/edition-defaults|版本默认值]]应用以及 [[concepts/features-gc|Features GC]]（通过 `protoc --gc-features`）等关键职责，并将 [[concepts/filedescriptorproto|FileDescriptorProto]] 等描述符传递给代码生成器与后端运行时。protoc 同时是 [[concepts/minimum-required-edition|Minimum Required Edition]] 的判定执行点，相关逻辑完整实现于 protoc 前端。

在 JSON 互操作方面，protoc 是 [[concepts/json_format feature|json_format]] 特性所规定的字段名冲突检测与报告机制的执行点：在 proto3 模式下默认对 JSON 映射进行唯一性校验并发出错误，在 proto2 或启用 `deprecated_legacy_json_field_conflicts` 时则降级为警告；建议的 `json_format` 特性依赖 protoc 在编译期分别触发错误（ALLOW）或警告（LEGACY_BEST_EFFORT），并在 DISALLOW 模式下允许 message 包含非法 JSON 映射的子类型字段。protoc 还能检测嵌套类型违规（例如 ALLOW message 嵌套 DISALLOW 类型）。

此外，protoc 还支持 `--java_out=lite` 生成 [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]] 兼容的 Java Lite 代码，并通过对保留字段编号的检查在编译期阻止未来开发者误用。

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
- [[entities/mkruskal-google|mkruskal-google]]
- [[entities/descriptor.proto|descriptor.proto]]
- [[entities/edition-zero|Edition Zero]]
- [[entities/protocolbuffers/protobuf|protocolbuffers/protobuf]]

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
- [[concepts/featureset|FeatureSet]]
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/descriptor-pool|Descriptor Pool]]
- [[concepts/codegenerator|CodeGenerator]]
- [[concepts/edition-defaults|Edition Defaults]]
- [[concepts/json-format-feature|json_format feature]]
- [[concepts/allow|ALLOW]]
- [[concepts/disallow|DISALLOW]]
- [[concepts/legacy-best-effort|LEGACY_BEST_EFFORT]]
- [[concepts/deprecated-legacy-json-field-conflicts|deprecated_legacy_json_field_conflicts]]

## Mentions in Source

> **Source: [[sources/proto3|proto3]]**
> - "If no syntax is specified, the protocol buffer compiler will assume you are using proto2."
> - "When you run the protocol buffer compiler on a .proto, the compiler generates the code in your chosen language you'll need to work with the message types you've described in the file, including getting and setting field values, serializing your messages to an output stream, and parsing your messages from an output stream."
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
> - "The intent is for tooling that wants to generate .proto templates externally can choose to use the latest edition for new messages."

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "Protoc works by first parsing the input protofiles and building them into a descriptor pool."
> - "The flaw that all of these design documents suffer from is that protoc can't be the universal source-of-truth for feature resolution under the original design."
> - "For built-in languages, the resulting descriptors are passed directly to the generator for codegen."

> **Source: [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]**
> - "The Protobuf compiler will fail to parse any proto3 files if any JSON conflicts are detected by default"
> - "Any conflicting JSON mappings will trigger protoc errors, guaranteeing uniqueness."