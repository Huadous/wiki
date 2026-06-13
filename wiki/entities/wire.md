---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "Square Wire"
  - "Wire Compiler"
---


# Wire

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Wire 是由 Square 公司开发的一款针对 Kotlin 和 Java 的协议缓冲区（Protocol Buffers）编译器。它在 [[sources/options|Protobuf 全局扩展注册表]]中注册了多个自定义扩展编号，用于增强 protobuf 在 JVM 平台上的能力。具体包括：扩展编号 1076 与 1077（用于支持 since 和 until 时间范围特性）、1087（wire_package 选项，用于自定义生成代码的包名）、1185（use_array 选项，控制集合类型的代码生成方式）以及 1190（enumMode 选项，控制枚举的生成模式）。Wire 的官方网站为 https://square.github.io/wire/，通过这些自定义选项以及 Kotlin 友好的代码生成器，为 JVM 开发者提供了更符合 Kotlin 语言习惯的 protobuf 使用体验。

## 相关实体
- [[entities/protoc-gen-validate|protoc-gen-validate]]
- [[entities/Buf|Buf]]

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]

## 来源提及
- "Wire since and until" — [[sources/options|options]]
- "Website: https://square.github.io/wire/" — [[sources/options|options]]
- "Extensions: 1076, 1077" — [[sources/options|options]]
- "Wire wire_package" — [[sources/options|options]]
- "Website: https://square.github.io/wire/" — [[sources/options|options]]
- "Extensions: 1087" — [[sources/options|options]]
- "Wire use_array" — [[sources/options|options]]
- "Extensions: 1185" — [[sources/options|options]]