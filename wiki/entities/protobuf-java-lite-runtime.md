---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/java-lite|java-lite]]"]
tags: [product]
aliases:
  - "Java Lite Runtime"
  - "protobuf-javalite"
  - "Protobuf Java Lite"
---


# Protobuf Java Lite Runtime

## 基本信息
- Type: product
- Source: [[sources/java-lite|java-lite]]

## 描述
Protobuf Java Lite Runtime 是 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 主 Java 运行时的精简版本，专为 Android 等资源受限平台设计。与完整 Java 运行时相比，它体积更小、性能更高，更适合在 Android 等移动环境中使用。该产品通过 Maven artifact `com.google.protobuf:protobuf-javalite` 发布。文档示例版本为 3.25.3。为了在性能和代码体积上达到最优，Google 明确不保证 Java Lite 的 API/ABI 稳定性。运行时内部采用反射机制以避免生成 hashCode、equals 与序列化方法，这一设计虽然在代码体积上具备优势，但容易与 R8 等代码混淆/优化工具产生冲突，因此通常需要配置相应的 ProGuard 规则。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- R8 (not yet in wiki)

## 相关概念
- LITE_RUNTIME optimization option (not yet in wiki)
- ABI stability (not yet in wiki)
- Reflection-based serialization (not yet in wiki)
- ProGuard obfuscation rules (not yet in wiki)

## 来源提及
- "The Protobuf Java Lite runtime is separated from the main Java runtime because it's designed and implemented with different constraints." — [[sources/java-lite|java-lite]]
- "In particular, the Java Lite runtime is much smaller which makes it more suitable to be used on Android." — [[sources/java-lite|java-lite]]
- "In order to achieve maximum performance and code size, we do NOT guarantee API/ABI stability for Java Lite." — [[sources/java-lite|java-lite]]