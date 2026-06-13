---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
tags:
  - "method"
aliases:
  - "Feature"
  - "特性"
---

## 描述
在 Protobuf Editions 中，Feature 是一种附加在任意语法实体（如文件、消息、字段、枚举）上的选项，用于细粒度控制代码生成和运行时行为。每个 Feature 都具有层级继承机制：下层实体（如字段）默认继承上层实体（如文件或消息）中定义的 Feature 值，除非在本地显式覆盖。这种设计使得大型项目可以在文件级别统一设定默认行为，然后在特定消息或字段级别进行微调。Features 不能引入会直接破坏现有二进制兼容性的更改，但可能支持语言后端定义自己的语言范围 feature。Features 的默认值由所使用的 edition 决定，从而确保版本迁移时的向后兼容性。常见的 Features 包括字段的 packed 编码控制、枚举的开放/封闭类型控制等。

## 相关概念
- [[concepts/editions|Editions]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/backward-compatibility|Backward Compatibility]]

## 相关实体
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protoc|protoc]]

## 来源提及
> **Source: [[sources/editions-what-are-protobuf-editions|Protobuf Editions 介绍文档]]**
> - "Features control the individual codegen and runtime behavior of fields, messages, enums, etc."
> - "Features cannot introduce changes that would directly break existing binaries."
> - "A feature, in the narrow context of Protobuf Editions, is an option on any syntax entity of a .proto file that has the following properties..."