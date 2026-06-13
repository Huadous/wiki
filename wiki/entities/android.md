---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/java-lite]]"]
tags: [other]
aliases:
  - "Android platform"
  - "Android 平台"
---


# Android

## 基本信息
- Type: other
- Source: [[sources/java-lite]]

## 描述
Android 是 Protobuf Java Lite 运行时主要面向的目标平台之一。Java Lite 运行时相比完整 Java 运行时体积更小，更适合在 [[entities/android|Android]] 这种对 APK 大小和内存占用敏感的环境中部署。在 Android 应用构建流程中，Java Lite 与 [[entities/r8|R8]] 混淆工具存在交互，需要通过 [[concepts/proguard-obfuscation-rules|ProGuard 混淆规则]]保留 GeneratedMessageLite 子类以避免反射失败。R8 与 Protobuf 项目方均存在与该问题相关的公开 issue。Android 由 [[entities/google-inc|Google Inc.]] 开发并维护，是当前全球市场占有率最高的移动操作系统。

## 相关实体
- [[entities/r8|R8]]
- [[entities/google-inc|Google Inc.]]
- [[entities/protobuf-java-lite-runtime|Protobuf Java Lite Runtime]]

## 相关概念
- [[concepts/code-size-optimization|Code size optimization]]
- [[concepts/reflection-based-serialization|Reflection-based serialization]]
- [[concepts/proguard-obfuscation-rules|ProGuard obfuscation rules]]

## 来源提及
- The Protobuf Java Lite runtime is separated from the main Java runtime because it's designed and implemented with different constraints. In particular, the Java Lite runtime is much smaller which makes it more suitable to be used on Android. — [[sources/java-lite|java-lite]]