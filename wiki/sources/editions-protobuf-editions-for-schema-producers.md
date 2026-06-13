---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
tags: [Schema Producer, Schema Consumer, Edition Zero, Feature, Semantic Patch, Wire Format Compatibility, proto2, proto3, Support Matrix]
aliases: ["Protobuf Editions for Schema Producers", "Editions Schema Producer Guide"]
---

# Protobuf Editions for Schema Producers - Summary

## 来源
- Original file: [[protobuf/editions-protobuf-editions-for-schema-producers.md]]
- Ingested: 2026-06-13

## 核心内容
本文档由 [[entities/protobuf-team|Protobuf team]] 的成员 @fowles 撰写，系统阐述了 [[entities/protobuf-editions|Protobuf Editions]] 项目中 Schema Producer（发布 `.proto` 文件供他人消费的团队）的使用场景与最佳实践。文档以 [[concepts/edition-zero|Edition Zero]] 为切入点，说明 Editions 通过 [[concepts/feature|features]] 机制来安全演进 Protobuf，且 features 通常不会改变消息的 wire format，从而保证线缆兼容性。文档详细描述了初始发布期的升级策略、稳态工作流（采用"针对支持矩阵中最旧版本定位最新 edition"的经验法则）、发布 `.proto` 文件而非生成代码的原则，以及 [[concepts/schema-consumer|Schema Consumer]] 的多种使用模式（包括运行 [[entities/protoc|protoc]]、使用 [[concepts/semantic-patch|语义补丁]]、发布生成库的注意事项）。同时探讨了 [[entities/bazel|Bazel]] 等构建系统的集成方案。

## 关键实体
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protoc|protoc]]
- [[entities/bazel|Bazel]]
- [[entities/protobuf-team|Protobuf team]]

## 关键概念
- [[concepts/schema-producer|Schema Producer]]
- [[concepts/schema-consumer|Schema Consumer]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/feature|Feature]]
- [[concepts/semantic-patch|Semantic Patch]]
- [[concepts/wire-format-compatibility|Wire Format Compatibility]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]
- [[concepts/support-matrix|Support Matrix]]

## 要点
- **发布 `.proto` 文件而非生成代码**：Schema producer 应发布源文件而非生成代码，发布生成代码容易在编译器与运行时之间产生不匹配，安全补丁通常需要同时更新二者。
- **Wire format 兼容性是关键保证**：[[concepts/feature|features]] 一般不会改变消息的 wire format，因此更改 `.proto` 文件的 edition 不会影响线缆兼容性，这是整个 Editions 设计的核心安全保证。
- **统一升级策略**：[[concepts/edition-zero|Edition Zero]] 通过选取"好的"默认值并要求对"不好的"语义进行显式请求来统一 [[concepts/proto2|proto2]] 与 [[concepts/proto3|proto3]]；[[entities/protobuf-team|Protobuf team]] 将提供完全兼容的升级工具。
- **Support Matrix 经验法则**：升级 edition 时应以支持矩阵中最旧 protobuf 版本所支持的最新 edition 为目标，保持所有 `.proto` 文件使用一致的 edition 以简化用户使用。
- **生成器特定 features 的边界**：代码生成器特定的 features（如 `features.(pb.cpp).string_field_type`）应仅在单个代码库内部使用，producer 不应将其强加给消费者。
- **语义补丁工具链**：[[entities/protobuf-team|Protobuf team]] 将提供两类工具——将语义补丁自动应用到 `.proto` 文件并提交源码控制，以及让 [[entities/protoc|protoc]] 直接将 `.proto` 文件与语义补丁作为输入编译而无需物化修改文件。
- **构建系统约束**：[[concepts/schema-consumer|Schema Consumer]] 的使用模式高度依赖其构建系统——语言无关构建系统（如 [[entities/bazel|Bazel]]）便于运行 protoc，而语言特定构建系统（如 Maven、Go）或缺乏构建系统的语言（如 Python）则面临更大挑战。