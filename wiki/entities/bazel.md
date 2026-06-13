---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_getting_started]]"
  - "[[protobuf/options.md]]"
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
  - "[[protobuf/cpp_build_systems.md]]"
tags:
  - "product"
aliases:
  - "Bazel构建系统"
  - "Google Bazel"
---

## Description
Bazel 是由 Google 开发的开源构建和测试工具，是其内部构建系统 Blaze 的开源版本。它使用 Starlark 语言定义构建规则，支持多语言项目，特别适合 Protobuf 这种涉及多语言且依赖 C++ 编译器的复杂项目。Protobuf 项目以 Bazel 的构建定义为权威源（source of truth），并利用 Bazel 的 aspects 和 providers 机制将源文件列表暴露给其他构建系统（如 CMake）使用，从而实现多构建系统协同。对于使用 Bazel 构建的 C++ 项目（如 brpc），可以通过 `--define` 选项启用特定功能，例如开启 bthread tracer。此外，Bazel 可作为语言无关的构建系统，将 `protoc` 作为构建步骤之一运行，Protobuf 团队期望其为 Bazel 添加语义补丁支持，以便在不修改原始 .proto 文件的情况下应用 features。

## Related Entities
- [[entities/brpc|brpc]] — 使用 Bazel 作为替代构建系统的 RPC 框架
- [[entities/libunwind|libunwind]] — 与 bthread tracer 功能相关的依赖库
- [[entities/cmake|CMake]] — brpc 的主要构建系统，Bazel 作为替代方案；通过 Bazel aspects 和 providers 机制消费 Bazel 构建定义的次级构建系统
- [[entities/gcc|GCC]] — Bazel 构建时可能使用的编译器之一
- [[entities/clang|Clang]] — Bazel 构建时可能使用的编译器之一
- [[entities/protoc|protoc]] — Bazel 可作为构建步骤运行的 Protocol Buffers 编译器
- [[entities/protobuf-team|Protobuf team]] — 计划为 Bazel 添加 Editions 语义补丁支持的团队
- [[entities/blaze|Blaze]] — Bazel 的前身，Google 内部构建系统，Bazel 在很大程度上为其精神延续
- [[entities/google|Google]] — Bazel 的开发方
- [[entities/protobuf|Protobuf]] — 主要使用 Bazel 构建 C++ 运行时和编译器

## Related Concepts
- [[concepts/静态链接|静态链接]] — Bazel 构建方式中涉及的链接方式
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]] — Bazel 注册 Failure Details 扩展的注册表
- [[concepts/schema-consumer|Schema Consumer]] — Bazel 语义补丁支持所面向的 proto 文件使用者
- [[concepts/semantic-patch|Semantic Patch]] — Protobuf 团队期望为 Bazel 添加的、不修改原始 .proto 即可应用 features 的能力
- [[concepts/starlark-api|Starlark API]] — Bazel 用于定义构建规则的领域特定语言
- [[concepts/bazel-aspect|Bazel Aspect]] — Bazel 提供的将源文件列表等数据暴露给其他构建系统（如 CMake）的机制
- [[concepts/cc-dist-library|cc_dist_library]] — Bazel 中用于分发 C++ 库目标的库类型

## Mentions in Source

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "if building with Bazel, please add the `--define with_bthread_tracer=true` option."

> **Source: [[sources/options|options]]**
> - "Bazel, Failure Details"

> **Source: [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]]**
> - "Language agnostic build systems, like Bazel, can run `protoc` as one of the build steps."
> - "In the long term, we want a Bazel rule (and possibly similar for other build systems) that seamlessly packages changes like:"

> **Source: [[sources/cpp_build_systems|cpp_build_systems]]**
> - "Protobuf primarily uses Bazel to build the Protobuf C++ runtime and Protobuf compiler."
> - "Bazel is a natural choice for a project-wide build system -- in fact, Bazel (and its predecessor, Blaze) was designed in large part to support exactly this type of rich, multi-language build."