---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems|cpp_build_systems]]"]
tags: [term]
aliases:
  - "Bazel cc_test"
  - "cc_test rule"
---


# cc_test

## 定义
cc_test 是 Bazel 构建系统中原生的 C++ 测试规则，用于定义和构建 C++ 项目的测试目标。在 Protobuf 项目的多构建系统支持机制中，cc_test 扮演着关键角色，但与 [[concepts/cc_dist_library|cc_dist_library]] 之间存在一个微妙的配置差异问题。

## 关键特征
- **原生 Bazel 规则**：cc_test 是 Bazel 内置的 C++ 测试构建规则，并非 Protobuf 自定义规则
- **配置差异**：Bazel 在评估 cc_test 规则时使用的配置与评估 cc_dist_library 时略有不同
- **测试配置特性**：测试配置包含额外的选项，用于告知 Bazel 如何执行测试
- **冲突风险**：当 cc_test 目标被包含在 cc_dist_library 规则中时，若两者同时被 Bazel 评估，可能导致针对同一输出产生两个冲突动作（conflicting actions），从而引发构建错误
- **构建配置差异**：cc_file_list_aspect 的构建配置不包含测试配置中的额外选项

## 应用
- 在 Protobuf 项目的 [[sources/cpp_build_systems|cpp_build_systems]] 中定义 C++ 测试目标
- 当 cc_test 需要与 cc_dist_library 协同工作时，最简单的解决方法是：
  - 通过 filegroup 或类似机制提供源文件
  - 从而避免 cc_test 与 cc_dist_library 两条规则对同一输出产生冲突动作
- 用于在 Bazel 生态系统中执行 C++ 单元测试和集成测试

## 相关概念
- [[concepts/cc_library|cc_library]]
- [[concepts/distribution-library|Distribution library]]
- [[concepts/file-list-generation|File list generation]]

## 相关实体
- [[entities/bazel|Bazel]]
- [[entities/cc_dist_library|cc_dist_library]]

## 来源提及
- Internally, a slightly different configuration is used when evaluating `cc_test` rules as compared to `cc_dist_library`. — [[sources/cpp_build_systems|cpp_build_systems]]