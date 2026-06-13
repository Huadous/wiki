---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/java-lite]]"]
tags: [term]
aliases:
  - "ABI 稳定性"
  - "Application Binary Interface stability"
---


# ABI stability

## 定义
ABI（Application Binary Interface）稳定性是指库在升级过程中保持二进制层面兼容的能力，使得使用方无需重新编译即可在运行时直接替换为新版本。文档明确指出 Java Lite Runtime **不保证** API/ABI 稳定性，这是其为了追求最大性能与最小代码体积而做出的设计取舍。

## 关键特征
- 涉及库在升级时对外暴露的二进制接口（类布局、方法签名、字段偏移、虚函数表等）的兼容承诺。
- 一旦失去 ABI 稳定性，调用方在升级依赖后必须重新构建工程，否则可能因内部结构变化而出现运行期崩溃或行为异常。
- Java Lite Runtime 主动放弃 ABI 稳定性以换取更小的生成代码体积与更快的执行效率。
- 与完整 Java Runtime 的稳定性策略形成对比：完整 Runtime 倾向于保持 API/ABI 的向后兼容。

## 应用
- 在 Android 等资源受限平台上，通过 `LITE_RUNTIME` 优化选项生成精简版 Java 类，牺牲 ABI 稳定性以缩减 APK 体积并提升性能。
- 当 Android 应用升级 Protobuf Java Lite 依赖时，可能需要重新编译工程以适配运行时内部的二进制结构变更。
- 若调用方无法接受重新构建的成本，应改用完整 Java Runtime（full Java runtime）以获得稳定性保证。

## 相关概念
- [[concepts/lite_runtime-optimization-option|LITE_RUNTIME optimization option]]

## 相关实体
- [[entities/protobuf-java-lite-runtime|Protobuf Java Lite Runtime]]
- [[entities/android|Android platform]]
- [[entities/r8|R8 Shrinker]]
- [[entities/maven|Apache Maven]]

## 来源提及
- "In order to achieve maximum performance and code size, we do NOT guarantee API/ABI stability for Java Lite." — [[sources/java-lite]]
- "If this is not acceptable for your use-case, use the full Java runtime instead." — [[sources/java-lite]]