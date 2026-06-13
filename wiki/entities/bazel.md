---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_getting_started]]"
  - "[[protobuf/options.md]]"
tags:
  - "product"
aliases:
  - "Bazel构建系统"
  - "Google Bazel"
---

## 相关实体
- [[entities/brpc|brpc]] — 使用 Bazel 作为替代构建系统的 RPC 框架
- [[entities/libunwind|libunwind]] — 与 bthread tracer 功能相关的依赖库
- [[entities/cmake|CMake]] — brpc 的主要构建系统，Bazel 作为替代方案
- [[entities/gcc|GCC]] — Bazel 构建时可能使用的编译器之一
- [[entities/clang|Clang]] — Bazel 构建时可能使用的编译器之一

## 相关概念
- [[concepts/静态链接|静态链接]] — Bazel 构建方式中涉及的链接方式
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]] — Bazel 注册 Failure Details 扩展的注册表

## 来源提及
> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "if building with Bazel, please add the `--define with_bthread_tracer=true` option."

> **Source: [[sources/options|options]]**
> - "Bazel, Failure Details"