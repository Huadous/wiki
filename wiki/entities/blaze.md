---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems]]"]
tags: [product]
aliases:
  - "Blaze 构建系统"
  - "Google Blaze"
---


# Blaze

## 基本信息
- Type: product
- Source: [[sources/cpp_build_systems]]

## 描述
Blaze 是 Google 内部的构建系统，是开源构建工具 [[entities/bazel|Bazel]] 的商业前身。[[entities/protobuf|Protobuf]] 项目历史上一直使用 Blaze 在 Google 内部进行开发，绝大多数 Google 对 Protobuf 的贡献至今仍以这种方式完成。Blaze 的设计初衷之一就是支持像 Protobuf 这样需要构建多种语言且依赖 C++ 编译器的复杂多语言项目。后来 Google 将其核心思想以开源形式发布为 [[entities/bazel|Bazel]]，使其成为面向更广泛开发社区的构建工具。Blaze 与 [[entities/google|Google]] 的内部基础设施深度集成，长期支撑着 [[entities/protobuf|Protobuf]] 等大规模项目的多语言构建需求。

## 相关实体
- [[entities/google|Google]]
- [[entities/bazel|Bazel]]
- [[entities/protobuf|Protobuf]]

## 相关概念
- No related concepts

## 来源提及
- "the Protobuf project was developed using Google's internal build system, which was the predecessor to Bazel." — [[sources/cpp_build_systems]]
- "the vast majority of Google's contributions continue to be developed this way" — [[sources/cpp_build_systems]]
- "Bazel (and its predecessor, Blaze) was designed in large part to support exactly this type of rich, multi-language build." — [[sources/cpp_build_systems]]