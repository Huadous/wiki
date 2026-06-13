---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems|cpp_build_systems]]"]
tags: [method]
aliases:
  - "Starlark"
  - "Skylark"
---


# Starlark API

## 定义
Starlark API 是 Bazel 构建系统使用的配置语言 Starlark（前身为 Skylark）的编程接口。它允许用户在 `.bzl` 文件中定义自定义规则（rules）、aspect（构建图遍历机制）和 provider（用于在规则之间传递结构化信息的载体）。Bazel 通过该 API 暴露了构建图的遍历、检查与扩展能力。

## 关键特征
- **基于 Starlark 语言**：一种受 Python 启发的受限配置语言，专为构建系统设计，强调可读性与确定性。
- **Aspect 机制**：允许用户在不修改原始规则的前提下，遍历依赖图、检查规则属性并定义额外构建动作。
- **Provider 机制**：用于在不同规则与 aspect 之间以结构化方式传递信息（如文件列表、元数据等）。
- **自定义规则定义**：可在 `.bzl` 文件中编写完整的自定义规则，实现复杂的构建逻辑。
- **构建图扩展能力**：能够在已有构建图的基础上增加新的输出产物或派生信息。

## 应用
Protobuf 项目大量使用 Starlark API 来实现其多构建系统（特别是 CMake 与 Bazel）的协同支持，主要场景包括：
- **依赖图遍历**：通过自定义 aspect（如 `cc_file_list_aspect`、`proto_file_list_aspect`）遍历构建图，收集 Bazel 已知的源文件信息。
- **文件列表信息暴露**：通过 provider 在规则间传递 C++ 源文件、proto 文件列表等结构化数据。
- **生成 CMake 输入文件**：通过自定义规则（如 `cc_dist_library`、`gen_cmake_file_lists`）整合 aspect 与 provider 收集的信息，最终生成 CMake 可消费的文件列表，从而让 Bazel 管理的代码也能被 CMake 构建系统使用。
- **跨构建系统桥接**：作为 Bazel 与其他原生构建系统（CMake、Makefile 等）之间的桥梁，使同一份源码可在不同构建系统中构建。

## 相关概念
- [[concepts/bazel-aspect|Bazel Aspect]]
- [[concepts/cc-file-list-aspect|cc_file_list_aspect]]
- [[concepts/proto-file-list-aspect|proto_file_list_aspect]]

## 相关实体
- [[entities/bazel|Bazel]]

## 来源提及
- Bazel's Starlark API provides aspects to traverse the build graph, inspect build rules, define additional actions, and expose information through providers. — [[sources/cpp_build_systems|cpp_build_systems]]