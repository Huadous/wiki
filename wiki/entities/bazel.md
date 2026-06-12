---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "Bazel构建系统"
  - "Google Bazel"
---


# Bazel

## 基本信息
- **类型**: 产品
- **来源文件**: [[sources/en_getting_started|en_getting_started]]

## 描述
Bazel 是 Google 开发的开源构建和测试工具，支持多种语言和平台。在 brpc 项目中，Bazel 被提及作为与 CMake 并行的替代构建系统。brpc 文档明确指出，如果使用 Bazel 构建并需要启用 bthread tracer 功能，开发者必须添加特定的构建选项。这体现了 brpc 对 Bazel 构建方式的原生支持，尽管文档中的提及相对简短。Bazel 的设计理念与 [[entities/cmake|CMake]] 不同，它更强调构建的可重复性和增量构建效率。brpc 项目通过支持 Bazel，降低了使用 Google 生态系统的开发者的接入门槛。

## 相关实体
- [[entities/brpc|brpc]] — 使用 Bazel 作为替代构建系统的 RPC 框架
- [[entities/libunwind|libunwind]] — 与 bthread tracer 功能相关的依赖库
- [[entities/cmake|CMake]] — brpc 的主要构建系统，Bazel 作为替代方案
- [[entities/gcc|GCC]] — Bazel 构建时可能使用的编译器之一
- [[entities/clang|Clang]] — Bazel 构建时可能使用的编译器之一

## 相关概念
- [[concepts/静态链接|静态链接]] — Bazel 构建方式中涉及的链接方式

## 来源提及
- "if building with Bazel, please add the `--define with_bthread_tracer=true` option." — [[sources/en_getting_started|en_getting_started]]