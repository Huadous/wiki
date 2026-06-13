---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/java-lite|java-lite]]"
  - "[[protobuf/editions-java-lite-for-editions.md]]"
tags:
  - "product"
aliases:
  - "Java Lite Runtime"
  - "protobuf-javalite"
  - "Protobuf Java Lite"
  - "Java Lite"
  - "Java Lite Runtime"
  - "protobuf-javalite"
  - "Protobuf Java Lite"
---

## Description
Protobuf Java Lite Runtime 是 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 主 Java 运行时的精简版本，专为 Android 等资源受限平台设计。与完整 Java 运行时相比，它体积更小、性能更高，更适合在 Android 等移动环境中使用。该产品通过 Maven artifact `com.google.protobuf:protobuf-javalite` 发布，文档示例版本为 3.25.3。为了在性能和代码体积上达到最优，Google 明确不保证 Java Lite 的 API/ABI 稳定性。

出于代码体积与性能的关键约束，Java Lite 并未直接嵌入完整的描述符（descriptor），而是采用了一种自定义的紧凑编码格式：代码生成器将描述符信息编码为一段描述符样式的信息字符串，存入 `RawMessageInfo`，运行时再将其解码为 `MessageSchema` 以供解析和序列化使用。Java Lite 的字段编码在 flags 中预留了多个位用于表达 proto2/proto3 区分及 packed 编码、UTF- 8 校验、has 位等多种扩展特性，这些位恰好覆盖了 Editions Zero 大多数特性的需求。Editions 迁移的核心挑战在于：当前实现以 `is_proto3` 位作为语法分支的主要依据，而 Editions 体系下应改用对应的特性位。该产品内部采用反射机制以避免生成 hashCode、equals 与序列化方法，这一设计虽然有利于控制代码体积，但容易与 R8 等代码混淆/优化工具产生冲突，因此通常需要配置相应的 ProGuard 规则。

## Related Entities
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- R8 (not yet in wiki)

## Related Concepts
- [[concepts/raw-message-info|RawMessageInfo]] (not yet in wiki)
- [[concepts/message-schema|MessageSchema]] (not yet in wiki)
- [[concepts/lite-runtime-custom-descriptor-format|Lite Runtime Custom Descriptor Format]] (not yet in wiki)
- [[concepts/editions-feature-flags|Editions Feature Flags]] (not yet in wiki)
- LITE_RUNTIME optimization option (not yet in wiki)
- ABI stability (not yet in wiki)
- Reflection-based serialization (not yet in wiki)
- ProGuard obfuscation rules (not yet in wiki)

## Mentions in Source

> **Source: [[sources/java-lite|java-lite]]**
> - "The Protobuf Java Lite runtime is separated from the main Java runtime because it's designed and implemented with different constraints."
> - "In particular, the Java Lite runtime is much smaller which makes it more suitable to be used on Android."
> - "In order to achieve maximum performance and code size, we do NOT guarantee API/ABI stability for Java Lite."

> **Source: [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]**
> - "The \"Lite\" implementation for Java utilizes a custom format for embedding descriptors motivated by critical code-size and performance requirements for Android."
> - "The code generator for Java Lite encodes an descriptor-like info string which is stored into `RawMessageInfo`."