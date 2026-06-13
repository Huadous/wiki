---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
tags: [Enum Field Closedness, Open Enum, proto3 enum, UnknownFieldSet, legacy_treat_enum_as_closed, Edition Zero Features, FieldDescriptor, proto2, proto3, EnumDescriptor, FileDescriptor, implicit presence, conformance test, Reflection]
aliases: ["Enum Field Closedness 特性设计文档", "protobuf Edition Zero 枚举封闭性"]
---

# Edition Zero Feature: Enum Field Closedness - Summary

## 来源
- Original file: [[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]
- Ingested: 2026-06-13

## 核心内容

本文档由 [[entities/@mcy|@mcy]] 撰写并于 2023-02-13 获批，讨论 [[entities/protocol-buffers|Protocol Buffers]] Edition Zero 中关于**枚举字段封闭性（[[concepts/enum-field-closedness|Enum Field Closedness]]）**的特性设计。核心问题是：不同语言实现中，枚举字段的开放/封闭性判断方式不一致——部分语言（C++、Java 等）通过字段使用方的文件 syntax 来判断，部分语言（UPB、Swift 等）通过枚举定义文件的 syntax 判断，还有一些语言（C#、Go、JSPB 等）将所有枚举视为开放。作者在 2023-02-10 提交 CL 删除 `google::protobuf::Reflection::SupportsUnknownEnumValue()` 时发现关键边界情况：当 [[concepts/proto2|proto2]] 消息引用 [[concepts/proto3-enum|proto3 enum]] 时，该枚举会被错误地视为封闭类型。约 2.99% 的枚举字段跨 syntax 导入枚举。文档建议新增 [[concepts/legacy_treat_enum_as_closed|legacy_treat_enum_as_closed]] 特性，Edition 2023 默认设为 false，proto2 隐式视为 true。推荐方案是将官方行为定义为「枚举开放性由枚举定义文件决定」，并通过按语言特性逐步迁移。

## 关键实体

- [[entities/@mcy|@mcy]]：文档作者，发现枚举封闭性边界情况的工程师
- [[entities/protocol-buffers|Protocol Buffers]]：讨论的技术背景，即 protobuf 各语言实现
- [[entities/protoscope|Protoscope]]：用于验证枚举封闭性问题表现的数据解析工具
- [[entities/prototiller|Prototiller]]：迁移工具，在从 proto2 迁移到 editions 时需要特殊处理

## 关键概念

- [[concepts/enum-field-closedness|Enum Field Closedness]]：枚举字段处理未知值的方式（封闭拒绝 vs 开放接受）
- [[concepts/open-enum|Open Enum]]：接受任意整数值的开放枚举
- [[concepts/proto3-enum|proto3 enum]]：在 proto3 文件中定义的枚举类型
- [[concepts/unknownfieldset|UnknownFieldSet]]：存储解析时不存在的字段值的容器
- [[concepts/legacy_treat_enum_as_closed|legacy_treat_enum_as_closed]]：本文档提议新增的 Edition Zero 特性
- [[concepts/edition-zero-features|Edition Zero Features]]：protobuf 语法系统演进的重要里程碑
- [[concepts/fielddescriptor|FieldDescriptor]]：建议新增 `legacy_enum_field_treated_as_closed()` 方法的 protobuf C++ 类
- [[concepts/proto2|proto2]]：protobuf 遗留语法版本，枚举为封闭行为
- [[concepts/proto3|proto3]]：protobuf 当前主要语法版本，枚举默认为开放
- [[concepts/enumdescriptor|EnumDescriptor]]：暴露 `is_closed()` 属性的 protobuf 类
- [[concepts/filedescriptor|FileDescriptor]]：提供文件语法版本信息的 protobuf 类
- [[concepts/implicit-presence|implicit presence]]：proto3 字段的隐式存在性特性
- [[concepts/conformance-test|conformance test]]：确保各语言实现行为一致的方法论
- [[concepts/reflection|Reflection]]：`google::protobuf::Reflection` 类，触发本次发现的 bug 来源

## 要点

- 不同 protobuf 语言实现对枚举开放/封闭性的判断方式不一致：C++/Java 由使用方字段的 syntax 决定，UPB/Swift 由枚举定义文件的 syntax 决定，C#/Go/JSPB/ImmutableJs/JsProto 将所有枚举视为开放。
- 存在关键边界情况：proto2 消息引用 proto3 枚举时，某些语言实现会将该枚举错误地视为封闭类型，导致未知值进入 UnknownFieldSet 而不是被接受。
- 约 2.99% 的枚举字段存在跨 syntax 引用枚举的情况，影响约 0.18% 的总字段数。
- 建议新增 `legacy_treat_enum_as_closed` 特性，Edition 2023 默认设为 false，proto2 隐式视为 true，以支持渐进式迁移。
- 推荐方案：将官方行为定义为「枚举开放性由枚举定义文件决定」，并通过按语言特性逐步迁移；不建议在 FieldDescriptor 上强制进行迁移以避免锁定非 C++/Java 语言。
- 在 C++ 中计划新增 `FieldDescriptor::legacy_enum_field_treated_as_closed()` 方法，并建议在 Java 中废弃 `FileDescriptor.supportsUnknownEnumValue()`。