---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems|cpp_build_systems]]"]
tags: [project]
aliases:
  - "rules_cc project"
  - "bazelbuild/rules_cc"
---


# rules_cc

## 基本信息
- Type: project
- Source: [[sources/cpp_build_systems|cpp_build_systems]]

## 描述
rules_cc 是由 [[entities/bazelbuild|bazelbuild]] 组织维护的一个独立项目，专门为 [[entities/bazel|Bazel]] 构建系统提供标准化的 C++ 规则定义。该项目通过模块化规则包的形式，将 Bazel 中 C++ 相关构建逻辑从核心系统中解耦，使开发者可以独立版本化与升级这些规则。在 Protobuf 项目的 BUILD.bazel 文件中，rules_cc 通过 `load('@rules_cc//cc:defs.bzl', 'cc_library')` 方式加载，为项目提供原生的 [[concepts/cc_library|cc_library]] 规则源，使得 Protobuf 能够无缝接入 Bazel 生态系统并复用标准化的 C++ 构建定义。

## 相关实体
- [[entities/bazel|Bazel]]
- [[entities/bazelbuild|bazelbuild]]
- [[entities/rules_pkg|rules_pkg]]

## 相关概念
- [[concepts/cc_library|cc_library]]
- [[concepts/bazel-aspect|Bazel Aspect]]

## 来源提及
- `load('@rules_cc//cc:defs.bzl', 'cc_library')` — [[sources/cpp_build_systems|cpp_build_systems]]
- "Bazel's native `cc_library` rule is typically used on a 'fine-grained' level, so that, for example, lightweight unit tests can be written with narrow scope." — [[sources/cpp_build_systems|cpp_build_systems]]