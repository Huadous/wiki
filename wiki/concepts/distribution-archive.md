---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems]]"]
tags: [term]
aliases:
  - "Distribution archive"
  - "source distribution archive"
  - "分发归档包"
---


# Distribution archive

## 定义
分发归档（Distribution archive）是 Protobuf 发布流程中创建的源码归档文件，用于将源代码按语言切片分发（distribution）。Protobuf 在发布时不仅提供完整的源码归档，还提供每种编程语言单独的语言切片归档（例如 Ruby 切片中仍包含构建 Protobuf 编译器所需的 C++ 运行时）。分发归档通过 [[concepts/rules_pkg|rules_pkg]] 项目的规则构建。

## 关键特征
- 由 Protobuf 的 //pkg 目录下定义的规则构建，与构建系统文件列表共享类似但不完全相同的规则集合
- 目标用途是源码发布分发，而非编译构建
- 需要包含额外的元数据文件（如 `BUILD.bazel` 等），这些文件在构建系统文件列表中通常不需要
- 涵盖范围更广：必须包含所有语言的发布相关文件，而 [[concepts/CcFileList|CcFileList]] 等构建系统文件列表仅涉及 C++，并按是否包含测试等构建用途分组
- 某些语言切片在分发时仍需保留对 C++ 运行时的依赖（如 Ruby 切片包含构建 Protobuf 编译器所需的 C++ 运行时）

## 应用
- Protobuf 官方版本发布：为不同语言用户分发对应语言的源码切片
- 跨语言发布：使每种语言的发布包自带完整可用的运行时与构建依赖
- 与 [[concepts/cc_dist_library|cc_dist_library]] 配合，为 C++ 等核心语言生成分发友好的归档结构
- 配合 [[concepts/ProtoFileList|ProtoFileList]] 等构建文件列表，明确区分"构建输入"与"分发内容"两类不同范围

## 相关概念
- [[concepts/CcFileList]]
- [[concepts/ProtoFileList]]
- [[concepts/cc_dist_library]]

## 相关实体
- [[entities/Protobuf]]
- [[entities/rules_pkg]]

## 来源提及
- A very similar set of rules is defined in //pkg to build source distribution archives for releases. — [[sources/cpp_build_systems]]