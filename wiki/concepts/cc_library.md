---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems]]"]
tags: [term]
aliases:
  - "Bazel cc_library"
  - "cc_library rule"
---


# cc_library

## 定义
cc_library 是 Bazel 中用于定义 C++ 库的核心原生构建规则。它通过指定源文件（`srcs`）、头文件（`hdrs`、`textual_hdrs`）以及依赖项来描述一个 C++ 库目标，是 Protobuf 等 C++ 项目在 Bazel 下的基本构建单元。

## 关键特征
- 细粒度构建：cc_library 通常在"细粒度"层面上使用，每个规则只封装少量源文件，使得可以编写范围较小的轻量级单元测试。
- 源文件与头文件分离：通过 `srcs`、`hdrs`、`textual_hdrs` 三个属性明确区分实现文件与头文件。
- 显式依赖管理：所有依赖库通过 `deps` 等属性显式声明。
- 适配 Bazel Aspect：`cc_file_list_aspect` 可以从 cc_library 中提取 `srcs`、`hdrs` 和 `textual_hdrs`，并通过 `CcFileList` provider 暴露给其他规则。
- 多构建系统桥接：在 Protobuf 中，其细粒度特性通过 [[concepts/distribution_library|cc_dist_library]] 规则聚合为匹配 CMake 构建粒度的分发库。

## 应用
- Protobuf 整个 C++ 库由大量 cc_library 规则组成，每个规则对应一组源文件、头文件和依赖项。
- 通过 cc_file_list_aspect 将 Bazel 内部构建粒度的源文件列表暴露给 CMake 等外部构建系统，实现 Protobuf 的多构建系统支持。
- 为窄范围的轻量级单元测试提供基础，使测试目标能够仅链接所需的最小子集。
- 与 [[concepts/proto_library|proto_library]]、[[concepts/cc_test|cc_test]] 等规则配合，构成完整的 Bazel C++ 构建与测试链路。

## 相关概念
- [[concepts/proto_library|proto_library]]
- [[concepts/cc_test|cc_test]]
- [[concepts/distribution_library|Distribution library]]

## 相关实体
- [[entities/bazel|Bazel]]
- [[entities/cc_dist_library|cc_dist_library]]
- [[entities/rules_cc|rules_cc]]

## 来源提及
- Bazel's native `cc_library` rule is typically used on a 'fine-grained' level, so that, for example, lightweight unit tests can be written with narrow scope. — [[sources/cpp_build_systems]]
- `cc_file_list_aspect` extracts `srcs`, `hdrs`, and `textual_hdrs` from build rules like `cc_library`. The sources are exposed through a provider named `CcFileList`. — [[sources/cpp_build_systems]]