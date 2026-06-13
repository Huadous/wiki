---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems|cpp_build_systems]]"]
tags: [term]
aliases:
  - "Bazel proto_library"
  - "proto_library rule"
---


# proto_library

## 定义
proto_library 是 Bazel 构建系统中用于定义 Protocol Buffer 库（即 `.proto` 文件集合）的核心原生构建规则。它作为 Protobuf 项目构建系统的关键组成部分，将 `.proto` 源文件及其相关产物组织为可被其他规则（如 `cc_proto_library`）消费的库目标。

## 关键特征
- **原生 Bazel 规则**：作为 Bazel 内置的构建规则，用于声明和管理 Protobuf 源文件集合。
- **依赖图根节点**：`cc_proto_library` 规则使用一个 aspect 遍历 `proto_library` 规则的依赖图，并动态附加动作以生成 C++ 代码（通过 Protobuf 编译器）并完成编译（通过 C++ 编译器）。
- **srcs 来源**：`proto_file_list_aspect` 从 `proto_library` 提取 `srcs`，并生成 Protobuf 编译器预期生成的输出文件名（如 `.pb.cc`、`.pb.h`、`-descriptor-set.proto.bin`）。
- **Provider 暴露**：上述文件列表信息通过 `ProtoFileList` provider 暴露给下游规则使用。
- **双源文件组成**：其源文件既包含 `.proto` 文件本身，也包含由编译器生成的相关产物。

## 应用
- 在 Bazel 构建系统中声明和打包 Protobuf 模式定义（`.proto` 文件）。
- 作为 `cc_proto_library` 等语言特定规则的输入，桥接到 C++ 代码生成与编译流程。
- 支撑多语言 Protobuf 代码生成（C++、Java、Python 等）的统一依赖管理。
- 配合 `proto_file_list_aspect` 动态计算 Protobuf 编译器预期产出，供增量构建与动作调度使用。

## 相关概念
- [[concepts/cc_library|cc_library]]
- [[concepts/cc_proto_library|cc_proto_library]]
- [[concepts/file-list-generation|File list generation]]

## 相关实体
- [[entities/protobuf|Protobuf]]
- [[entities/cc_dist_library|cc_dist_library]]

## 来源提及
- the `cc_proto_library` rule uses an aspect to traverse the dependency graph of `proto_library` rules, and dynamically attaches actions to generate C++ code using the Protobuf compiler and compile using the C++ compiler. — [[sources/cpp_build_systems|cpp_build_systems]]