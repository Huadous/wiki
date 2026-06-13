---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/proto3]]"
tags:
  - "method"
aliases:
  - "代码生成"
  - "generated code"
  - "Protobuf code generation"
  - "代码生成"
  - "generated code"
---

## 描述
代码生成是 Protocol Buffers 编译器的核心功能之一，通过运行 `protoc` 编译器处理 `.proto` 文件，根据指定的目标语言生成相应的数据访问类。不同语言生成的代码形态各异，例如 C++ 生成 `.pb.h` 和 `.pb.cc` 文件，Java 生成 `.java` 文件并包含 Builder 类，Kotlin 额外生成 DSL 和可空字段访问器，Python 生成模块配合元类，Go 生成 `.pb.go` 文件。每个消息类型在生成的代码中对应一个独立的类、struct 或模块，提供字段访问、序列化与反序列化、消息解析等完整功能。代码生成使得开发者能够以类型安全的方式操作结构化数据，无需手动处理二进制序列化细节，实现了从 `.proto` 定义到具体语言实现的自动化映射。

## 相关概念
- [[concepts/protoc|protoc]]
- [[concepts/message|message]]
- [[concepts/field|field]]
- [[concepts/proto3|proto3]]
- [[concepts/wire-format|wire format]]
- [[concepts/enumeration|enumeration]]
- [[concepts/scalar-types|scalar types]]
- [[concepts/field-cardinality|field cardinality]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]

## 来源提及
> **Source: [[sources/proto3|proto3]]**
> - "When you run the protocol buffer compiler on a .proto, the compiler generates the code in your chosen language you’ll need to work with the message types you’ve described in the file, including getting and setting field values, serializing your messages to an output stream, and parsing your messages from an input stream."
> - "For C++, the compiler generates a .pb.h and .pb.cc file from each .proto, with a class for each message type described in your file."