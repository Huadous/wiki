---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems]]"]
tags: [project]
aliases:
  - "rules_pkg"
  - "bazelbuild/rules_pkg"
  - "Bazel rules_pkg"
---


# rules_pkg

## 基本信息
- Type: project
- Source: [[sources/cpp_build_systems]]

## 描述
rules_pkg 是 [[entities/Bazel|Bazel]] 生态系统中由 bazelbuild 组织在 GitHub 上维护的项目，提供用于打包和分发软件产物的 Bazel 规则集合。在 [[entities/Protobuf|Protobuf]] 项目的 [[sources/cpp_build_systems|cpp_build_systems]] 文档中，rules_pkg 提供的 `pkg_files` 与 `pkg_filegroup` 规则承担了双重职责：一方面被 [[concepts/gen_cmake_file_lists|gen_cmake_file_lists]] 用于生成 CMake 构建系统所需的文件列表，另一方面被用于构建按语言切片的源码分发归档（即 [[concepts/Distribution archive|分发归档]]）。然而这两类目标在覆盖范围上存在差异：源码分发归档需要额外包含 `BUILD.bazel` 等元数据文件并覆盖 Protobuf 的所有语言实现，而 `gen_cmake_file_lists` 输出的构建系统文件列表仅涉及 C++ 代码且按构建用途进行分组。

## 相关实体
- [[entities/Bazel|Bazel]]
- [[entities/Protobuf|Protobuf]]

## 相关概念
- [[concepts/Distribution archive|Distribution archive]]
- [[concepts/gen_cmake_file_lists|gen_cmake_file_lists]]

## 来源提及
- "pkg_files or pkg_filegroup rules from https://github.com/bazelbuild/rules_pkg" — [[sources/cpp_build_systems]]
- "These archives are defined using rules from the rules_pkg project." — [[sources/cpp_build_systems]]
- "A very similar set of rules is defined in //pkg to build source distribution archives for releases." — [[sources/cpp_build_systems]]