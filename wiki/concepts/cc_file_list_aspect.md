---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems|cpp_build_systems]]"]
tags: [method]
aliases:
  - "cc_file_list_aspect"
  - "CcFileList Aspect"
  - "Protobuf C++ 文件列表 Aspect"
---


# cc_file_list_aspect

## 定义
`cc_file_list_aspect` 是 Protobuf 项目定义的一个 Bazel aspect，用于从 `cc_library` 等构建规则中提取源文件信息。它捕获规则的 `srcs`、`hdrs` 和 `textual_hdrs` 属性，并通过名为 `CcFileList` 的 provider 将这些信息暴露给其他规则。该 aspect 仅在直接依赖上运行，不在依赖图中传递传播，这一设计既简化了实现，又允许通过 `select()` 等机制对哪些文件应包含在最终库中进行细粒度条件控制。

## 关键特征
- **捕获三类源文件属性**：从构建规则中提取 `srcs`（源文件）、`hdrs`（头文件）和 `textual_hdrs`（文本头文件）。
- **使用专用 Provider 暴露信息**：通过名为 `CcFileList` 的 Bazel provider 将提取到的源文件列表传递给依赖该 aspect 的规则。
- **非传递性传播（Non-propagating）**：与大多数 Bazel 规则类型不同，文件列表 aspect 不沿依赖图传递，仅暴露直接依赖的源文件，而非传递依赖的源文件。
- **简化实现**：由于不传播，aspect 的实现复杂度显著降低，无需处理深层依赖的合并逻辑。
- **支持细粒度条件控制**：结合 Bazel 的 `select()` 机制，可在不同平台/配置下条件性地决定哪些文件被包含进最终的 C++ 库中。
- **与对应 proto aspect 对称**：存在类似 `proto_file_list_aspect` 的 aspect 用于处理 `.proto` 源文件，二者在设计上形成对称。

## 应用
- **Protobuf C++ 库的构建聚合**：在多语言、多平台构建系统中，用于将分散在各个 `cc_library` 目标中的源文件聚合到统一的文件列表中，供下游规则（如打包、发布、代码生成）使用。
- **替代 `filegroup` 的细粒度版本控制**：相比 Bazel 原生的 `filegroup`，通过 aspect 暴露文件列表允许在目标规则的 `srcs`、`hdrs` 上使用 `select()`，实现基于条件（如平台、特性开关）的源文件裁剪。
- **`cc_dist_library` 等规则的输入源**：为依赖 Bazel aspect 的 Protobuf 自定义规则（如 `cc_dist_library`）提供 C++ 源文件清单数据。
- **跨规则文件清单导出**：在 Protobuf 的多 C++ 构建系统（如 Makefile、CMake、Bazel）支持机制中，作为将源文件从 Bazel 规则同步到其他构建系统的桥梁。

## 相关概念
- [[concepts/cc-file-list|CcFileList]]
- [[concepts/cc-dist-library|cc_dist_library]]
- [[concepts/bazel-aspect|Bazel Aspect]]
- [[concepts/proto-file-list-aspect,proto_file_list_aspect]]

## 相关实体
- [[entities/protobuf|Protobuf]]
- [[entities/bazel|Bazel]]

## 来源提及
- "cc_file_list_aspect extracts srcs, hdrs, and textual_hdrs from build rules like cc_library. The sources are exposed through a provider named CcFileList." — [[sources/cpp_build_systems|cpp_build_systems]]
- "One major difference from most Bazel rule types is that the file list aspects do not propagate. In other words, they only expose the immediate dependency's sources, not transitive sources." — [[sources/cpp_build_systems|cpp_build_systems]]