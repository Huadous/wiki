---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems|cpp_build_systems]]"]
tags: [product]
aliases:
  - "Protocol Buffers Lite"
  - "Protobuf Lite"
  - "protobuf-lite"
---


# protobuf_lite

## 基本信息
- Type: product
- Source: [[sources/cpp_build_systems|cpp_build_systems]]

## 描述
protobuf_lite 是 [[entities/Protobuf|Protobuf]] 项目中的一个轻量级 C++ 运行时库，是完整 Protobuf 运行时的精简版本。该组件主要面向资源受限的环境（如移动设备和嵌入式系统），提供核心的 Protocol Buffer 序列化与反序列化功能，但省略了完整运行时中的部分高级特性（例如反射和描述符支持）。在 Protobuf 的多构建系统设计（见 [[sources/cpp_build_systems|cpp_build_systems]]）中，protobuf_lite 与完整运行时分别通过独立的 `cc_dist_library` 规则来生成其源文件列表，使得二者可以作为可独立分发与裁剪的组件纳入构建。文档明确指出，[[entities/Protobuf]] 的分发库（cc_dist_library）可以定义为不包含全部的 protobuf_lite 内容，从而允许下游用户按需选择是否启用该组件。

## 相关实体
- [[entities/Protobuf|Protobuf]]

## 相关概念
- [[concepts/distribution-library|Distribution library]]
- [[concepts/cc_library|cc_library]]
- [[concepts/cc_dist_library|cc_dist_library]]

## 来源提及
- "a distribution library for `//:protobuf` could be defined not to include all of `//:protobuf_lite`" — [[sources/cpp_build_systems|cpp_build_systems]]
- "The main C++ runtimes (lite and full) and the Protobuf compiler use their corresponding `cc_dist_library` rules to generate file lists." — [[sources/cpp_build_systems|cpp_build_systems]]