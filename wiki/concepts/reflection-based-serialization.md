---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/java-lite]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
tags:
  - "method"
aliases:
  - "反射式序列化"
  - "Reflection-based Serialization"
  - "Reflection-based algorithms"
  - "反射式序列化"
  - "Reflection-based Serialization"
---

## Description
反射式序列化涵盖两类典型场景。第一类体现在 Protobuf Java Lite Runtime 的内部实现中：运行时通过 Java 反射按字段名动态读取生成的 `MessageLite` 子类字段，从而避免在编译期生成 hashCode、equals、（反）序列化等方法，显著减小库体积和生成代码总量；这种实现强依赖运行时能够通过字段名解析到目标字段，因此一旦 R8 等代码混淆工具重命名了字段，运行时反射查找就会失败并抛出类似 `Field {NAME}_ for {CLASS} not found` 的异常。

第二类则是更广义的基于描述符驱动的反射算法，常见于 JSON、TextFormat 等通用序列化器、动态 RPC 框架以及 descriptor 驱动的工具，这类算法通过读取 descriptor 并调用 Protobuf 反射接口来处理消息，而不依赖生成的强类型代码。基于反射的算法在面对 proto3 optional 字段时表现尤为关键：因为 proto3 optional 在反射层会被呈现为一个普通的单字段 oneof，而现有的 proto3 反射代码早已知道如何为 oneof 字段判定存在性，因此反射式实现在 proto3 引入 optional 时通常无需修改代码即可正确保留 presence 信息，这也是采用"合成 oneof"方案的核心动机之一。

## Related Concepts
- [[concepts/proguard-obfuscation-rules|ProGuard obfuscation rules]]
- [[concepts/synthetic-oneof|Synthetic Oneof]]
- [[concepts/oneof|Oneof]]
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/reflection|Reflection]]

## Related Entities
- [[entities/protobuf-java-lite-runtime|Protobuf Java Lite Runtime]]
- [[entities/r8|R8]]
- [[entities/descriptor|Protocol Buffers Descriptor]]
- [[entities/oneofdescriptor|OneofDescriptor]]
- [[entities/codegeneratorresponse|CodeGeneratorResponse]]

## Mentions in Source

> **Source: [[sources/java-lite|java-lite]]**
> - "The Lite runtime internally uses reflection to avoid generating hashCode/equals/(de)serialization methods."
> - "R8 by default obfuscates the field names, which makes the reflection fail causing exceptions of the form `java.lang.RuntimeException: Field {NAME}_ for {CLASS} not found. Known fields are [ {FIELDS} ]` in MessageSchema.java."

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "Since oneof fields in proto3 already track presence, existing proto3 reflection-based algorithms should correctly preserve presence for proto3 optional fields with no code changes."
> - "For example, the JSON and TextFormat parsers/serializers in C++ and Java did not require any changes to support proto3 presence. This is the major benefit of synthetic oneofs."