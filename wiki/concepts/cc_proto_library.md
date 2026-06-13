---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems|cpp_build_systems]]"]
tags: [method]
aliases:
  - "cc_proto_library rule"
  - "Bazel cc_proto_library"
---


# cc_proto_library

## 定义
`cc_proto_library` 是 Bazel 的标准构建规则之一，用于从 `proto_library` 目标编译生成 C++ 代码。它通过一个 aspect 遍历 `proto_library` 的依赖图，并动态地附加动作来调用 Protobuf 编译器生成 C++ 源文件，再调用 C++ 编译器完成编译。

## 关键特征
- 基于 Bazel 的 aspect 机制实现，沿 `proto_library` 依赖图传播并收集需要处理的源文件。
- 在 aspect 内部动态生成 Bazel 动作（action），分别调用 protoc 生成 C++ 源代码与 C++ 编译器进行编译。
- 与 `proto_file_list_aspect` 等自定义 aspect 共享同一套 Bazel 底层机制，因此常被作为 Protobuf 文档中 aspect 用法的典型示例。
- 属于 Bazel 原生规则集合，行为由 Bazel 与 Protobuf 的官方代码共同保证。

## 应用
- 在基于 Bazel 构建的项目中，把 `.proto` 文件及其依赖自动转换为可被 C++ 代码链接的目标。
- 作为 Protobuf 文档中讲解 "如何用 aspect 在依赖图上附加代码生成与编译动作" 的参考实现，用于说明 `cc_file_list_aspect`、`proto_file_list_aspect` 等同类自定义 aspect 的工作机制。
- 帮助构建系统在保持 Bazel 增量构建与依赖追踪能力的同时，透明地接入 Protobuf 编译流水线。

## 相关概念
- [[concepts/Bazel Aspect|Bazel Aspect]]
- [[concepts/proto_file_list_aspect|proto_file_list_aspect]]

## 相关实体
- [[entities/Bazel|Bazel]]
- [[entities/Protobuf|Protobuf]]

## 来源提及
- "the cc_proto_library rule uses an aspect to traverse the dependency graph of proto_library rules, and dynamically attaches actions to generate C++ code using the Protobuf compiler and compile using the C++ compiler." — [[sources/cpp_build_systems|cpp_build_systems]]