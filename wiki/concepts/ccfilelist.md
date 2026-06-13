---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems]]"]
tags: [term]
aliases:
  - "CcFileList provider"
  - "Protobuf CcFileList Bazel Provider"
---


# CcFileList

## 定义
`CcFileList` 是 Protobuf 项目自定义的 Bazel provider，由 `cc_file_list_aspect` 在遍历 `cc_library` 规则时产生。它是 `cc_dist_library` 规则用于暴露其聚合 C++ 源文件列表的核心数据结构，也是从 Bazel 构建定义向其他构建系统（如 CMake）传递 C++ 源文件信息的关键桥梁。

## 关键特征
- 由 `cc_file_list_aspect` 在分析 `cc_library` 规则时作为 Starlark provider 产出
- 包含四个字段：`hdrs`、`internal_hdrs`、`srcs` 和 `textual_hdrs`
- 所有四个字段均为 `depset` 类型，用于高效聚合与遍历构建 C++ 库所需的文件
- 作为 Bazel 构建系统与外部构建系统（如 CMake）之间传递 C++ 源文件信息的中间数据结构
- 与 `ProtoFileList` 在 protobuf 构建系统中扮演对称角色，分别处理 C++ 与 Protobuf 两类源文件

## 应用
- 在 Bazel 构建图中聚合每个 `cc_library` 目标所引用的头文件、内部头文件、源文件和文本头文件
- 由 `cc_dist_library` 规则聚合各 `cc_library` 的 `CcFileList`，生成统一的 C++ 源文件列表
- 为 CMake 等外部构建系统提供生成 C++ 编译命令所需的文件信息
- 与 [[concepts/ProtoFileList|ProtoFileList]] 配合使用，分别管理 C++ 源码与 Protobuf 源文件的跨构建系统传递

## 相关概念
- [[concepts/cc-file-list-aspect|cc_file_list_aspect]]
- [[concepts/cc-dist-library|cc_dist_library]]
- [[concepts/ProtoFileList|ProtoFileList]]

## 相关实体
- [[entities/Protobuf|Protobuf]]
- [[entities/Bazel|Bazel]]

## 来源提及
- The sources are exposed through a provider named CcFileList. — [[sources/cpp_build_systems|cpp_build_systems]]
- struct( hdrs = depset([]), internal_hdrs = depset([]), srcs = depset([ <source file cc_dist_library_example/a.cc>, <source file cc_dist_library_example/b.cc>, ]), textual_hdrs = depset([]), ) — [[sources/cpp_build_systems|cpp_build_systems]]