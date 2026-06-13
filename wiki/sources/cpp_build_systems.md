---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/cpp_build_systems.md]]"
tags: [cc_dist_library, cc_file_list_aspect, proto_file_list_aspect, CcFileList, ProtoFileList, Bazel Aspect, Starlark API, gen_cmake_file_lists, Distribution archive, cc_proto_library, cc_library, proto_library, cc_test, Distribution library, File list generation]
aliases: ["How Protobuf supports multiple C++ build systems", "Protobuf C++ 构建系统支持机制"]
---

# Protobuf 如何支持多种 C++ 构建系统 - Summary

## 来源
- Original file: [[protobuf/cpp_build_systems.md]]
- Ingested: 2026-06-13

## 核心内容
本文档详细介绍了 [[entities/protobuf|Protobuf]] 项目如何同时支持多种 C++ 构建系统（目前为 [[entities/bazel|Bazel]] 和 [[entities/cmake|CMake]]）。历史上 [[entities/protobuf|Protobuf]] 先在 [[entities/google|Google]] 内部使用专有构建系统 [[entities/blaze|Blaze]] 开发，2008 年开源后改用 [[entities/autoconf|Autoconf]]，随后在社区推动下引入 [[entities/bazel|Bazel]]。为避免在每个构建系统中重复定义配置，Protobuf 采用以 [[entities/bazel|Bazel]] 为权威源的设计：利用 [[concepts/starlark-api|Starlark API]] 的 aspect 机制，通过 [[concepts/cc_file_list_aspect|cc_file_list_aspect]] 和 [[concepts/proto_file_list_aspect|proto_file_list_aspect]] 分别提取 C++ 库和 proto 库的源文件列表，并通过 [[concepts/ccfilelist|CcFileList]] 和 [[concepts/protofilelist|ProtoFileList]] provider 暴露这些信息。自定义规则 [[concepts/cc_dist_library|cc_dist_library]] 将多个细粒度的 [[concepts/cc_library|cc_library]] 合并为单一粗粒度分发库，[[concepts/gen_cmake_file_lists|gen_cmake_file_lists]] 规则则将信息生成为 [[entities/cmake|CMake]] 可包含的文件格式。

## 关键实体
- [[entities/protobuf|Protobuf]]（Protocol Buffers）：Google 开发的开源数据序列化格式和工具集
- [[entities/bazel|Bazel]]：Google 开发的开源构建和测试工具
- [[entities/cmake|CMake]]：广泛使用的开源跨平台构建系统生成器
- [[entities/blaze|Blaze]]：Google 内部构建系统，[[entities/bazel|Bazel]] 的前身
- [[entities/google|Google]]：[[entities/protobuf|Protobuf]] 和 [[entities/bazel|Bazel]] 的最初开发者
- [[entities/autoconf|Autoconf]]：[[entities/protobuf|Protobuf]] 开源后早期使用的构建工具
- [[entities/rules_pkg|rules_pkg]]：[[entities/bazel|Bazel]] 生态中用于打包和分发的规则集
- [[entities/rules_cc|rules_cc]]：为 [[entities/bazel|Bazel]] 提供 C++ 规则定义的项目
- [[entities/protobuf_lite|protobuf_lite]]：[[entities/protobuf|Protobuf]] 的轻量级运行时库

## 关键概念
- [[concepts/cc_dist_library|cc_dist_library]]：自定义 [[entities/bazel|Bazel]] 规则，合并多个细粒度 [[concepts/cc_library|cc_library]] 为单一粗粒度分发库
- [[concepts/cc_file_list_aspect|cc_file_list_aspect]]：从 [[concepts/cc_library|cc_library]] 中提取 `srcs`、`hdrs`、`textual_hdrs` 的 aspect
- [[concepts/proto_file_list_aspect|proto_file_list_aspect]]：从 [[concepts/proto_library|proto_library]] 提取 srcs 并预测编译器生成文件名的 aspect
- [[concepts/ccfilelist|CcFileList]]：由 [[concepts/cc_file_list_aspect|cc_file_list_aspect]] 产生的 provider
- [[concepts/protofilelist|ProtoFileList]]：由 [[concepts/proto_file_list_aspect|proto_file_list_aspect]] 产生的 provider
- [[concepts/bazel-aspect|Bazel Aspect]]：[[entities/bazel|Bazel]] 提供的横切依赖图机制
- [[concepts/starlark-api|Starlark API]]：[[entities/bazel|Bazel]] 配置语言 API
- [[concepts/gen_cmake_file_lists|gen_cmake_file_lists]]：从 [[entities/bazel|Bazel]] 目标生成 [[entities/cmake|CMake]] 格式文件列表的规则
- [[concepts/distribution-library|Distribution library]]：匹配 [[entities/cmake|CMake]] 构建粒度的粗粒度库抽象
- [[concepts/file-list-generation|File list generation]]：核心方法论，由 [[entities/bazel|Bazel]] 生成可导入其他构建系统的文件列表
- [[concepts/distribution-archive|Distribution archive]]：[[entities/protobuf|Protobuf]] 发布时按语言切片的源码归档，与构建系统文件列表不同
- [[concepts/cc_proto_library|cc_proto_library]]：[[entities/bazel|Bazel]] 从 [[concepts/proto_library|proto_library]] 生成 C++ 代码的标准规则
- [[concepts/cc_library|cc_library]]：[[entities/bazel|Bazel]] 原生 C++ 库构建规则
- [[concepts/proto_library|proto_library]]：[[entities/bazel|Bazel]] 原生 [[entities/protobuf|Protobuf]] 库构建规则
- [[concepts/cc_test|cc_test]]：[[entities/bazel|Bazel]] 原生 C++ 测试规则，与 [[concepts/cc_dist_library|cc_dist_library]] 存在配置冲突问题

## 要点
- [[entities/protobuf|Protobuf]] 以 [[entities/bazel|Bazel]] 构建定义为权威源，通过 aspect 机制避免在每个构建系统中重复维护文件清单
- [[concepts/cc_file_list_aspect|cc_file_list_aspect]] 与 [[concepts/proto_file_list_aspect|proto_file_list_aspect]] 不在依赖图中传递传播，仅处理直接依赖，这既简化实现又允许通过 `select()` 进行细粒度条件控制
- [[concepts/cc_dist_library|cc_dist_library]] 将多个细粒度 [[concepts/cc_library|cc_library]] 合并为匹配 [[entities/cmake|CMake]] 构建粒度的粗粒度分发库
- [[concepts/gen_cmake_file_lists|gen_cmake_file_lists]] 生成的 `.cmake` 文件可由 [[entities/cmake|CMake]] 直接 `include`，支持从 `cc_dist_library`、`proto_library`、`filegroup`、`pkg_files` 等多种 [[entities/bazel|Bazel]] 目标派生
- [[concepts/distribution-archive|分发归档]]（distribution archive）与构建系统文件列表目标不同：归档涵盖所有语言并包含 `BUILD.bazel` 等额外文件，而构建系统文件列表仅涉及 C++ 并按构建用途分组
- [[concepts/cc_test|cc_test]] 与 [[concepts/cc_dist_library|cc_dist_library]] 存在配置冲突，最简解决方案是通过 `filegroup`（通常命名为 `test_srcs` 并使用 `glob()`）提供测试源文件
- 维护流程：当 `cc_library` 加入或删除时需修改对应的 `cc_dist_library`；新增 [[concepts/proto_library|proto_library]] 需在 `gen_cmake_file_lists` 的 `src_libs` 中显式列出