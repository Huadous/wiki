---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/cpp_build_systems]]"
  - "[[protobuf/cpp_build_systems.md]]"
tags:
  - "method"
aliases:
  - "cc_dist_library 规则"
  - "Protobuf Bazel 分发库规则"
  - "Distribution library"
  - "cc_dist_library 规则"
  - "Protobuf Bazel 分发库规则"
---

## Description
`cc_dist_library` 是 Protobuf 项目为解决 Bazel 与 CMake 等其他构建系统之间粒度差异问题而提出的核心抽象。Bazel 原生的 `cc_library` 规则是细粒度的，而 CMake 等传统构建系统倾向于粗粒度的库定义——由于整个"Protobuf 库"由许多细粒度的 `cc_library` 规则组成，`cc_dist_library` 规则将它们合并为一个整体的（monolithic）库。在 Protobuf 项目中，这些"分发库"被设计为与基于 CMake 的构建粒度保持一致。该规则通过调用 `cc_file_list_aspect` 收集所有输入库中的源文件（srcs、hdrs、textual_hdrs），因此一个 `cc_dist_library` 不仅产生复合库制品，还收集并提供在另一个构建系统中重现该库所需的输入源文件列表。`cc_file_list_aspect` 是非传递性的，不会沿依赖图向下传播，从而仅暴露直接依赖的源文件，确保对最终库构成进行精确控制。

## Related Concepts
- [[concepts/cc_file_list_aspect]]
- [[concepts/CcFileList]]
- [[concepts/Distribution archive]]
- [[concepts/cc_library]]
- [[concepts/File list generation]]

## Related Entities
- [[entities/Protobuf]]
- [[entities/Bazel]]
- [[entities/CMake]]
- [[entities/cc_dist_library]]

## Mentions in Source

> **Source: [[sources/cpp_build_systems|cpp_build_systems]]**
> - "Since the entire 'Protobuf library' includes many constituent `cc_library` rules, a special rule, `cc_dist_library`, combines several fine-grained libraries into a single, monolithic library."
> - "For the Protobuf project, these 'distribution libraries' are intended to match the granularity of the CMake-based builds."
> - "the cc_dist_library rule invokes the cc_file_list_aspect on its input libraries. The result is that a cc_dist_library rule not only produces composite library artifacts, but also collect and provide the list of sources that were inputs."