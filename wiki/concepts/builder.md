---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions]]"]
tags: [term]
aliases:
  - "Builder class"
  - "message Builder"
  - "构建器类"
---


# Builder

## 定义
Builder（构建器类）是 Protocol Buffers 编译器在生成 Java 语言代码时，为每个消息类型额外生成的一种特殊辅助类，用于创建消息类实例。指南原文指出："a special Builder class for creating message class instances"，说明 Builder 在 Java 代码生成产物中扮演关键角色。Builder 模式允许开发者以流式 API 或分步方式构造消息实例，比直接使用构造函数更加灵活和可读。

## 关键特征
- 由 Protocol Buffers 编译器在 Java 代码生成过程中自动创建，与每个消息类型一一对应。
- 属于生成产物（generated artifact），开发者无需手动编写 Builder 代码。
- 支持链式调用（chaining）或分步调用的方式逐步设置消息字段。
- 与不可变或半不可变的消息实例配合，解耦构造过程与最终对象。
- 在 Kotlin 环境下，编译器在 Java 生成代码基础上还会生成改进的 Kotlin API，提供 DSL、可空字段访问器和 copy 函数等特性。

## 应用
- 在 Java 中以流式 API 方式构造复杂的 Protobuf 消息实例，提升代码可读性。
- 分步骤构建消息，允许对单个字段进行条件性赋值。
- 作为 Kotlin DSL 构建消息实例的底层支持，简化消息创建逻辑。
- 用于代码生成工具链中，作为 protoc 插件输出的标准组成部分。

## 相关概念
- [[concepts/.proto-file|.proto file]]
- [[concepts/message-type|Message Type]]

## 相关实体
（暂无相关实体）

## 来源提及
- "Java, the compiler generates a .java file with a class for each message type, as well as a special Builder class for creating message class instances." — [[sources/editions]]
- "Kotlin, in addition to the Java generated code, the compiler generates a file for each message type with an improved Kotlin API. This includes a DSL that simplifies creating message instances, a nullable field accessor, and a copy function." — [[sources/editions]]