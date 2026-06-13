---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_getting_started]]"
  - "[[protobuf/options.md]]"
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
tags:
  - "product"
aliases:
  - "Bazel构建系统"
  - "Google Bazel"
---

## Related Entities
- [[entities/brpc|brpc]] — 使用 Bazel 作为替代构建系统的 RPC 框架
- [[entities/libunwind|libunwind]] — 与 bthread tracer 功能相关的依赖库
- [[entities/cmake|CMake]] — brpc 的主要构建系统，Bazel 作为替代方案
- [[entities/gcc|GCC]] — Bazel 构建时可能使用的编译器之一
- [[entities/clang|Clang]] — Bazel 构建时可能使用的编译器之一
- [[entities/protoc|protoc]] — Bazel 可作为构建步骤运行的 Protocol Buffers 编译器
- [[entities/protobuf-team|Protobuf team]] — 计划为 Bazel 添加 Editions 语义补丁支持的团队

## Related Concepts
- [[concepts/静态链接|静态链接]] — Bazel 构建方式中涉及的链接方式
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]] — Bazel 注册 Failure Details 扩展的注册表
- [[concepts/schema-consumer|Schema Consumer]] — Bazel 语义补丁支持所面向的 proto 文件使用者
- [[concepts/semantic-patch|Semantic Patch]] — Protobuf 团队期望为 Bazel 添加的、不修改原始 .proto 即可应用 features 的能力

## Mentions in Source

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "if building with Bazel, please add the `--define with_bthread_tracer=true` option."

> **Source: [[sources/options|options]]**
> - "Bazel, Failure Details"

> **Source: [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]]**
> - "Language agnostic build systems, like Bazel, can run `protoc` as one of the build steps."
> - "In the long term, we want a Bazel rule (and possibly similar for other build systems) that seamlessly packages changes like:"