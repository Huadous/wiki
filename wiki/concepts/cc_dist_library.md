---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems]]"]
tags: [method]
aliases:
  - "cc_dist_library 规则"
  - "Protobuf Bazel 分发库规则"
---


# cc_dist_library

## 定义
`cc_dist_library` 是 Protobuf 项目自定义的 Bazel 规则，用于将多个细粒度的 `cc_library` 合并为单一粗粒度的"分发库"（distribution library）。该规则的粒度设计旨在匹配基于 CMake 的构建方式，使 Bazel 与 CMake 构建产物在结构上保持对齐。它通过调用 `cc_file_list_aspect` 收集所有输入库中的源文件（包括 srcs、hdrs、textual_hdrs），并通过 `CcFileList` provider 暴露这些信息。

## 关键特征
- **粗粒度合并**：将多个细粒度 `cc_library` 合并为单一"分发库"，粒度与 CMake 构建产物对齐
- **源文件聚合**：调用 `cc_file_list_aspect` 收集所有输入库中的源文件（srcs、hdrs、textual_hdrs）
- **CcFileList provider 输出**：不仅产生合并后的库制品，还通过 `CcFileList` provider 收集并暴露输入源文件列表
- **非传递性 aspect**：aspect 不在依赖图中传递传播，仅暴露直接依赖的源文件，从而允许对最终库的构成进行精确控制

## 应用
- 在 Protobuf 项目中构建与 CMake 等价的 Bazel 制品结构
- 生成单一粗粒度的分发库以匹配发布/分发包的结构
- 为 Protobuf C++ 构建系统提供跨构建工具（CMake / Bazel）的一致性
- 在 Protobuf 项目的多构建系统支持机制中作为 Bazel 端的核心聚合规则

## 相关概念
- [[concepts/cc_file_list_aspect]]
- [[concepts/CcFileList]]
- [[concepts/Distribution archive]]

## 相关实体
- [[entities/Protobuf]]
- [[entities/Bazel]]

## 来源提及
- "a special rule, cc_dist_library, combines several fine-grained libraries into a single, monolithic library." — [[sources/cpp_build_systems]]
- "the cc_dist_library rule invokes the cc_file_list_aspect on its input libraries. The result is that a cc_dist_library rule not only produces composite library artifacts, but also collect and provide the list of sources that were inputs." — [[sources/cpp_build_systems]]