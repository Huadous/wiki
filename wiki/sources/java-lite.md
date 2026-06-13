---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/java-lite.md]]"
tags: [LITE_RUNTIME optimization option, ABI stability, Reflection-based serialization, ProGuard obfuscation rules, Code size optimization]
aliases: ["Protobuf Java Lite 使用指南", "Java Lite Runtime Documentation"]
---

# Protocol Buffers - Google's data interchange format - Summary

## 来源
- Original file: [[protobuf/java-lite.md]]
- Ingested: 2026-06-13

## 核心内容
本文档是 [[entities/google-inc|Google]] 于 2008 年发布的 [[entities/protocol-buffers|Protocol Buffers]]（Protobuf）数据交换格式官方文档的一部分，主题为 **Java Lite 运行时的使用指南**。[[entities/protobuf-java-lite-runtime|Protobuf Java Lite Runtime]] 是完整 Java 运行时的精简版，专为 [[entities/android|Android]] 等资源受限平台设计，体积更小、性能更高，但官方明确不保证 API 与 [[concepts/abi-stability|ABI 稳定性]]。文档说明了如何通过 [[entities/protoc|protoc]] 编译器的 `--java_out=lite:` 选项生成 Java Lite 代码（指出 [[concepts/lite_runtime-optimization-option|`optimize_for = LITE_RUNTIME`]] 选项已不再对 Java 生效），并给出 [[entities/maven|Maven]] 依赖 `com.google.protobuf:protobuf-javalite` 的集成示例。文档重点讨论了 Lite Runtime 的 [[concepts/reflection-based-serialization|反射式序列化]]机制与 [[entities/r8|R8]] 代码混淆之间的冲突问题，并给出 [[concepts/proguard-obfuscation-rules|ProGuard 规则]]解决方案。

## 关键实体
- [[entities/protocol-buffers|Protocol Buffers]] —— Google 开发的数据序列化机制
- [[entities/protobuf-java-lite-runtime|Protobuf Java Lite Runtime]] —— 精简版 Java 运行时
- [[entities/r8|R8]] —— Android 默认代码混淆与缩减工具
- [[entities/google-inc|Google Inc.]] —— 项目版权所有者与开发主体
- [[entities/android|Android]] —— Java Lite Runtime 的主要目标平台
- [[entities/maven|Maven]] —— Java 依赖管理与分发工具
- [[entities/protoc|protoc]] —— Protocol Buffers 官方编译器

## 关键概念
- [[concepts/lite_runtime-optimization-option|LITE_RUNTIME optimization option]] —— `.proto` 文件中的 `optimize_for = LITE_RUNTIME` 选项（对 Java 已失效）
- [[concepts/abi-stability|ABI stability]] —— 应用二进制接口稳定性
- [[concepts/reflection-based-serialization|Reflection-based serialization]] —— Lite Runtime 的内部反射式序列化机制
- [[concepts/proguard-obfuscation-rules|ProGuard obfuscation rules]] —— 控制混淆器保留特定类的规则配置
- [[concepts/code-size-optimization|Code size optimization]] —— 缩减运行时二进制体积的设计目标

## 要点
- Java Lite Runtime 是 Protocol Buffers 主 Java 运行时的精简版，专为 Android 设计，体积更小但不保证 API/ABI 稳定性
- protoc 通过 `--java_out=lite:` 选项生成 Java Lite 代码；`.proto` 中的 `optimize_for = LITE_RUNTIME` 已不再对 Java 代码生效
- Java Lite Runtime 通过 Maven artifact `com.google.protobuf:protobuf-javalite` 引入（示例版本 3.25.3）
- Lite Runtime 内部使用反射实现 hashCode/equals/序列化，与 R8 的字段名混淆冲突，会抛出 `Field {NAME}_ for {CLASS} not found` 运行时异常
- 解决 R8 兼容问题需要在 `proguard-rules.pro` 中添加 `-keep class * extends com.google.protobuf.GeneratedMessageLite { *; }`
- 相关问题在 protobuf GitHub #6463 与 R8 issue tracker (144631039) 中跟踪
- 旧版本（v3.0.0）的 Java Lite 文档位于 GitHub javalite 分支的 `java/lite.md`