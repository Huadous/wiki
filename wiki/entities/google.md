---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/java-lite.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/editions-cpp-apis-for-edition-zero.md]]"
  - "[[protobuf/cpp_build_systems.md]]"
tags:
  - "organization"
aliases:
  - "Google LLC"
  - "Google Inc."
---

## Description
Protocol Buffers（Protobuf）是 Google 最初开发的序列化与通信数据格式，也是 Google 最古老且最成功的工具链项目之一，现由 Google 作为主要维护者持续开发。Protobuf 最初作为 Google 内部项目诞生，2008 年以开源软件形式对外发布，使外部开发者也能享受与 Google 内部相同的工具链收益，至今仍是 Google 内部最常用的数据格式。在 Google 内部，Protobuf 项目长期使用其自有的内部构建系统 Blaze（Bazel 的前身）进行开发，并且 Google 绝大多数提交至今仍沿用这一方式完成。Protobuf 与 Bazel、gRPC、Protoscope 等工具共同构成了 Google 围绕结构化数据描述与序列化的完整生态。

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/grpc|gRPC]]
- [[entities/google-cloud|Google Cloud]]
- [[entities/github|GitHub]]
- [[entities/protoscope|Protoscope]]
- [[entities/thrift|Apache Thrift]]
- [[entities/tcmalloc|tcmalloc]]
- [[entities/bazel|Bazel]]
- [[entities/protobuf-java-lite-runtime|protobuf-java-lite-runtime]]
- [[entities/r8|r8]]
- [[entities/blaze|Blaze]]

## Related Concepts
- [[concepts/backward-compatibility|Backward compatibility]]
- [[concepts/proto3|Proto3]]
- [[concepts/proto2|Proto2]]
- [[concepts/editions|Editions]]
- [[concepts/features|Features]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/lsc|LSC]]
- [[concepts/breaking-changes-policy|Breaking Changes Policy]]
- [[concepts/abi-stability|ABI stability]]
- [[concepts/code-size-optimization|Code size optimization]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/code-generator|Code Generator]]
- [[concepts/internal-build-system|Internal Build System]]

## Mentions in Source
- "Protocol buffers are the most commonly-used data format at Google." — [[sources/overview|overview]]
- "The following languages are supported directly in the protocol buffers compiler, protoc:" — [[sources/overview|overview]]
- "Protocol buffers were open sourced in 2008 as a way to provide developers outside of Google with the same benefits that we derive from them internally." — [[sources/overview|overview]]

> **Source:** [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]
- "Protobuf is one of Google's oldest and most successful toolchain projects."
- "The migration to edition '2025' across google will move very fast as it is a no-op."
- "Internal users will be migrated centrally before a feature is deprecated."
- "We will partner with use-cases that are known risks for migration, such as storage providers, to minimize toil and disruption on all sides."

> **Source:** [[sources/java-lite|java-lite]]
- "Copyright 2008 Google Inc."
- "https://developers.google.com/protocol-buffers/"

> **Source:** [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- "First-party code generators developed by Google are being updated already."
- "Presence tracking was added to proto3 in response to user feedback, both from inside Google and from open-source users."

> **Source:** [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]
- "there are significant uses of `FileDescriptor::syntax()` in internal Google repositories that Edition Zero will break"
- "The volume of such changes in google3 is small enough that it's probably easiest to create a giant CL that fixes every instance of a particular misuse and then hand it to Rosie for splitting up."

> **Source:** [[sources/cpp_build_systems|cpp_build_systems]]
- "the Protobuf project was developed using Google's internal build system"
- "the vast majority of Google's contributions continue to be developed this way"
- "On a historical note, prior to its release as Open Source Software, the Protobuf project was developed using Google's internal build system"