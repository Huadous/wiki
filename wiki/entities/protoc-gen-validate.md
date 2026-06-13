---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "PGV"
  - "protoc-gen-validate"
  - "protoc gen validate"
---


# protoc-gen-validate

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
protoc-gen-validate（PGV）是一个为 Protocol Buffers 生成代码时进行数据验证的 protoc 插件。它允许开发者通过在 `.proto` 文件中使用扩展选项（custom options）声明字段验证规则，包括数值范围、字符串长度、正则表达式、枚举取值等约束条件，并在运行时自动检查消息的合法性。PGV 在 Protocol Buffers 的全局扩展注册表中分配的扩展编号为 1071。该项目目前由 [[entities/buf|buf]]（Buf）维护，代码仓库托管于 https://github.com/bufbuild/protoc-gen-validate。它与同类验证工具 [[entities/scalapb|ScalaPB]] 内部提供的校验机制、以及 [[entities/grpc-gateway|grpc-gateway]] 等生态项目共同构成了 Protobuf 工具链中数据校验的一环。

## 相关实体
- [[entities/buf|buf]]
- [[entities/scalapb|ScalaPB]]
- [[entities/grpc-gateway|grpc-gateway]]
- [[entities/wire|Square Wire]]
- [[entities/protobuf-net|protobuf-net]]
- [[entities/nanopb|nanopb]]
- [[entities/perfetto|Perfetto]]
- [[entities/confluent-schema-registry|Confluent Schema Registry]]

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/protocol-buffers|Protocol Buffers]]
- [[concepts/protoc-plugin|protoc plugin]]
- [[concepts/message-validation|Message validation]]

## 来源提及
- Protoc-gen-validate — [[sources/options|options]]
- Website: https://github.com/bufbuild/protoc-gen-validate — [[sources/options|options]]
- Extensions: 1071 — [[sources/options|options]]