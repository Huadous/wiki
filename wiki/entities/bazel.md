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

> **Source: en_getting_started**
> - "if building with Bazel, please add the `--define with_bthread_tracer=true` option."

> **Source: options**
> - "Bazel, Failure Details"

> **Source: editions-protobuf-editions-for-schema-producers**
> - "Language agnostic build systems, like Bazel, can run `protoc` as one of the build steps."
> - "In the long term, we want a Bazel rule (and possibly similar for other build systems) that seamlessly packages changes like:"

> **Source: cpp_build_systems**
> - "Protobuf primarily uses Bazel to build the Protobuf C++ runtime and Protobuf compiler."
> - "Bazel is a natural choice for a project-wide build system -- in fact, Bazel (and its predecessor, Blaze) was designed in large part to support exactly this type of rich, multi-language build."