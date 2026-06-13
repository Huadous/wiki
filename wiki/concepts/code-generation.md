---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/proto3]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
tags:
  - "method"
aliases:
  - "代码生成"
  - "generated code"
  - "Protobuf code generation"
  - "代码生成"
  - "generated code"
  - "Codegen"
  - "代码生成"
  - "generated code"
  - "Protobuf code generation"
  - "代码生成"
  - "generated code"
---

## Description
代码生成是 Protocol Buffers 编译器的核心功能之一，通过运行 `protoc` 编译器处理 `.proto` 文件，根据指定的目标语言生成相应的数据访问类。不同语言生成的代码形态各异，例如 C++ 生成 `.pb.h` 和 `.pb.cc` 文件，Java 生成 `.java` 文件并包含 Builder 类，Kotlin 额外生成 DSL 和可空字段访问器，Python 生成模块配合元类，Go 生成 `.pb.go` 文件。每个消息类型在生成的代码中对应一个独立的类、struct 或模块，提供字段访问、序列化与反序列化、消息解析等完整功能。

然而，各语言代码生成器在 API 命名约定上并不完全一致。以 proto2 的 group（分组）字段为例，针对同一 `.proto` 定义，不同语言生成的访问器方法可能采用不同来源的命名：C++、Python、Go、upb 倾向使用字段名（如 `MyGroup mygroup()`），而 Java、Objective-C、Swift 则使用消息名（如 `MyGroup getMyGroup()`），Dart V1 和 C# 则表现出混合行为。当同一类型被用于同一消息中的两个 delimited 字段时，部分语言甚至会生成同名（签名冲突）的两组 API。这种由语言间实现差异导致的"随机混合"（fairly random-seeming mix）在向 [[concepts/edition-2023|edition 2023]] 迁移时可能产生令人惊讶的拼写结果，因此成为 editions 升级需要重点关注的兼容性问题之一。

## Related Concepts
- [[concepts/protoc|protoc]]
- [[concepts/message|message]]
- [[concepts/field|field]]
- [[concepts/proto3|proto3]]
- [[concepts/wire-format|wire format]]
- [[concepts/enumeration|enumeration]]
- [[concepts/scalar-types|scalar types]]
- [[concepts/field-cardinality|field cardinality]]
- [[concepts/delimited-encoding|delimited encoding]]
- [[concepts/group-fields|group fields]]
- [[concepts/group-like-fields|group-like fields]]
- [[concepts/text-format|text format]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/edition-2023|Edition 2023]]

## Mentions in Source

> **Source: [[sources/proto3|proto3]]**
> - "When you run the protocol buffer compiler on a .proto, the compiler generates the code in your chosen language you'll need to work with the message types you've described in the file, including getting and setting field values, serializing your messages to an output stream, and parsing your messages from an input stream."
> - "For C++, the compiler generates a .pb.h and .pb.cc file from each .proto, with a class for each message type described in your file."

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "While using the field name for generated APIs required less special-casing in the generators, the field name ends up producing slightly-less-readable APIs for multi-word camelcased groups."
> - "the result is that we see a fairly random-seeming mix in different generators."