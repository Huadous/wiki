---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/implementing_proto3_presence|implementing_proto3_presence]]"]
tags: [term]
aliases:
  - "合成 oneof"
  - "Synthetic Oneof"
  - "synthetic oneof"
---


# Synthetic Oneof

## 定义
Synthetic Oneof（合成 oneof）是 [[sources/implementing_proto3_presence|implementing_proto3_presence]] 中提出的关键设计概念，指每个 proto3 optional 字段在 descriptor 内部被表示为一个仅含单个字段的 oneof。该 oneof 不会出现在用户的 `.proto` 源文件中，而是在 proto 编译器内部合成生成。其设计目的是在不破坏现有 proto3 descriptor 语义的前提下，复用 oneof 字段已具备的存在性（presence）追踪能力。

## 关键特征
- **内部合成性**：synthetic oneof 由编译器在生成 descriptor 时合成，对用户不可见，不会出现在 `.proto` 源文件里。
- **单字段 oneof 结构**：每个 proto3 optional 字段独占一个 oneof，该 oneof 内部恰好只包含该 optional 字段。
- **复用 oneof 存在性机制**：proto3 中 oneof 字段天然具备 presence 追踪能力，synthetic oneof 借由该机制实现 optional 字段的存在性判断。
- **避免破坏性改动**：proto3 descriptor 已使用 `LABEL_OPTIONAL` 表示无存在性的 singular 字段，若直接复用 `LABEL_OPTIONAL` 表示 optional 字段，旧软件会因无法识别新语义而丢失存在性信息并造成数据丢失。Synthetic oneof 通过新增合成结构规避了此风险。
- **序列化器透明兼容**：基于反射的 JSON、TextFormat 等解析序列化器已能正确处理 oneof 的存在性语义，因此无需修改即可正确处理 optional 字段。
- **不可丢弃性**：synthetic oneof 绝不能从 proto schema 中安全移除，移除将破坏存在性信息的传递。

## 应用
- **proto3 optional 字段的底层实现**：在 [[sources/proto3|proto3 语言指南]] 中为 `optional` 关键字提供 descriptor 与运行时层面的支撑机制。
- **反射序列化器兼容**：使 [[entities/descriptor|google::protobuf::Descriptor]]、[[entities/oneofdescriptor|OneofDescriptor]] 等反射相关组件能够在不修改 JSON、TextFormat 等序列化器的前提下处理 optional 字段。
- **代码生成与插件协议**：在 [[entities/plugin-proto|plugin.proto]] 与 [[entities/codegeneratorresponse|CodeGeneratorResponse]] 涉及的代码生成流程中，作为 optional 字段呈现给下游生成器（如 `FEATURE_PROTO3_OPTIONAL`）的标准化表达方式。
- **跨语言运行时一致性**：保证 [[entities/protobuf-java-lite-runtime|Protobuf Java Lite]] 等不同语言运行时在 descriptor 层面对 optional 字段的处理语义统一。

## 相关概念
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/reflection|Reflection]]
- [[concepts/label-optional|LABEL_OPTIONAL]]

## 相关实体
- [[entities/descriptor|google::protobuf::Descriptor]]
- [[entities/oneofdescriptor|google::protobuf::OneofDescriptor]]

## 来源提及
- "Every proto3 optional field is placed into a one-field `oneof`. We call this a "synthetic" oneof, as it was not present in the source `.proto` file." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- "It is never safe to drop synthetic oneofs from a proto schema." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]