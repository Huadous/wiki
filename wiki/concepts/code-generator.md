---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/implementing_proto3_presence|implementing_proto3_presence]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
tags:
  - "method"
aliases:
  - "代码生成器"
  - "Code Generator"
  - "protoc 代码生成器"
  - "CodeGenerator framework"
  - "代码生成器"
  - "Code Generator"
  - "protoc 代码生成器"
---

## Description
Code Generator 是 protoc 生态中负责将 protobuf 接口描述（通常为 `FileDescriptorProto`）转换为目标编程语言可调用类、结构体或服务桩的核心组件。它既可以泛指任何遵循 protoc 插件协议、响应 [[entities/codegeneratorresponse|CodeGeneratorRequest]] 并输出 [[entities/codegeneratorresponse|CodeGeneratorResponse]] 的工具，也可以特指 Google 提供的 C++ 抽象基类 `google::protobuf::compiler::CodeGenerator`，后者为插件开发者提供了一套标准化框架。

在 [[sources/implementing_proto3_presence|implementing_proto3_presence]] 文档中，Code Generator 的核心关注点之一是正确支持 proto3 optional 字段。基于 C++ `CodeGenerator` 框架实现的代码生成器需要重写 `GetSupportedFeatures()` 方法，并在返回值中包含 [[concepts/FEATURE_PROTO3_OPTIONAL|FEATURE_PROTO3_OPTIONAL]] 标志，以告知 protoc 其已具备处理可选字段的能力。这一检查机制的设计动机在于：防止老版本代码生成器在不知情的情况下处理 proto3 optional 文件，从而生成依赖于合成 oneof 访问器的过时 API，避免给未来的迁移工作造成负担。

文档同时强调，仅声明能力并不足够——即使代码生成器在 `GetSupportedFeatures()` 中声明支持 `FEATURE_PROTO3_OPTIONAL`，也必须真正实现对 proto3 optional 字段的生成逻辑，否则不应正式发布。整体而言，Code Generator 体系是 [[entities/protocol-buffers|Protocol Buffers]] 多语言支持与 [[entities/protoc|protoc]] 构建流程的关键衔接环节。

## Related Concepts
- [[concepts/FEATURE_PROTO3_OPTIONAL|FEATURE_PROTO3_OPTIONAL]]
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/reflection|Reflection]]

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/codegeneratorresponse|CodeGeneratorResponse]]
- [[entities/plugin-proto|plugin-proto]]

## Mentions in Source
> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "This document is targeted at developers who own or maintain protobuf code generators."
> - "All code generators will need to be updated to support proto3 optional fields."
> - "If you are using the CodeGenerator framework:"
>
> ```c++
> class MyCodeGenerator : public google::protobuf::compiler::CodeGenerator {"
> - "you need to tell `protoc` what features you support. The method for doing this depends on whether you are using the C++ `google::protobuf::compiler::CodeGenerator` framework or not."