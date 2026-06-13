---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/implementing_proto3_presence|implementing_proto3_presence]]"]
tags: [standard]
aliases:
  - "proto3_optional field option"
  - "proto3_optional=true"
---


# proto3_optional

## 定义
proto3_optional 是 `FieldDescriptorProto` 中定义的一个字段选项（field option），用于在描述符层面标记一个字段为 proto3 optional 字段。当用户在 proto3 源文件中编写 `optional` 字段时，该字段在内部会被重写为一个仅含单字段的合成 oneof（synthetic oneof），并同时设置 `proto3_optional=true` 以保留用户原始的语义意图。该选项本身不应作为公共 API 暴露给最终用户，而应通过 `FieldDescriptor::has_presence()` 或 `has_optional_keyword()` 等更高级别的抽象进行访问。

## 关键特征
- 属于 `FieldDescriptorProto` 的字段级选项（field option），仅在描述符层面生效
- 在 proto3 源文件中以 `optional` 关键字声明的字段，编译时会被改写为合成 oneof 形式
- 合成 oneof 与 `proto3_optional=true` 标记共同保留原始字段的存在语义（field presence）
- 不应作为公共 API 直接暴露给用户，避免业务代码中编写 proto2/proto3 特定分支逻辑
- 应通过 `FieldDescriptor::has_presence()`、`has_optional_keyword()` 等高级抽象屏蔽底层差异
- 设计目标是提供统一的、跨 proto2/proto3 一致的字段存在性访问语义

## 应用
- 在 Protocol Buffers 编译器（protoc）将 proto3 源文件转换为 `FileDescriptorProto` 时，用于标识由 `optional` 关键字生成的合成 oneof 字段
- 在运行时反射库中，作为区分「用户显式声明的 oneof」与「由 proto3 optional 派生的合成 oneof」的内部依据
- 在跨语言代码生成器中，用于正确生成字段存在性检查方法（如 C++ 的 `has_field()`、Java 的 `hasField()`）
- 在 Java Lite 等精简运行时中，用于在描述符反序列化阶段还原字段的 presence 行为

## 相关概念
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/synthetic-oneof|Synthetic Oneof]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/oneof|Oneof]]

## 相关实体
- [[entities/descriptor|Descriptor]]
- [[entities/descriptorpool|DescriptorPool]]
- [[entities/oneofdescriptor|OneofDescriptor]]
- [[entities/codegeneratorresponse|CodeGeneratorResponse]]
- [[entities/plugin-proto|plugin.proto]]

## 来源提及
- // oneof _foo {
//   int32 foo = 1 [proto3_optional=true];
// } — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- please do *not* expose an accessor for the FieldDescriptorProto.proto3_optional field. We want to avoid having users implement any proto2/proto3-specific logic. — [[sources/implementing_proto3_presence|implementing_proto3_presence]]