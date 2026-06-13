---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
tags:
  - "term"
aliases:
  - "Reflection API"
  - "Protobuf Reflektion"
---

## 描述
Reflection 提供了一种在运行时遍历消息字段、检查 oneof 结构、读取描述符信息（如 `FileDescriptor`、`Descriptor`、`FieldDescriptor`、`OneofDescriptor`）的能力，使存储服务、自定义代码生成器、序列化/验证框架等高级场景得以脱离静态生成的代码运作。实现反射时必须新增 `has_presence()`、`is_synthetic()`、`real_containing_oneof()`、`real_oneof_decl_count()` 等方法，并保证 `HasField()`、`HasOneof()` 等 API 在合成 oneof（synthetic oneof）上行为正确，以使存在性对反射透明。在 proto3 中，由于 oneof 字段本就跟踪存在性，基于反射的现有算法（如 C++ 与 Java 中的 JSON 与 TextFormat 解析器/序列化器）无需任何代码修改即可正确保留 proto3 optional 字段的存在性。此外，Reflection 在 Protobuf Editions 体系下还需与 [[concepts/feature-inheritance|Feature Inheritance]] 兼容，做到特征继承对用户完全透明——反射行为应如同特征已被显式设置在所有位置一样。

## 相关概念
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/protobuf-editions|Edition]]
- [[concepts/feature|Feature]]
- [[concepts/language-scoped-feature|Language-scoped Feature]]
- [[concepts/synthetic-oneof|Synthetic Oneof]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/proto3-optional-fields|proto3 optional fields]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/oneofdescriptor|oneofdescriptor]]
- [[entities/descriptor|descriptor]]
- [[entities/descriptorpool|descriptorpool]]
- [[entities/codegeneratorresponse|codegeneratorresponse]]

## 来源提及
> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "We plan to upgrade reflection to be feature-aware in a way that minimizes code we need to change."
> - "We do not expect anyone to implement feature-inheritance logic themselves; feature inheritance should be fully transparent to users, behaving as if features had been placed explicitly everywhere."

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "Since oneof fields in proto3 already track presence, existing proto3 reflection-based algorithms should correctly preserve presence for proto3 optional fields with no code changes."
> - "For example, the JSON and TextFormat parsers/serializers in C++ and Java did not require any changes to support proto3 presence."