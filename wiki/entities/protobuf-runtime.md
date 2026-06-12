---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/editions-what-are-protobuf-editions]]"]
tags: [product]
aliases:
  - "Protocol Buffers runtime"
  - "protobuf libraries"
---


# Protobuf runtime

## 基本信息
- Type: product
- Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]

## 描述
Protobuf运行时是指在各编程语言中实现Protocol Buffers序列化与反序列化逻辑的库与组件集合。这些运行时需要具备向后兼容能力，能够处理来自未来的描述符（descriptor），当遇到不理解的版本或新特性时必须提供合理的回退行为。运行时与[[entities/protoc|protoc]]后端（代码生成器）协同工作，后者生成的代码依赖运行时提供的核心功能。不同语言拥有独立的运行时实现，例如C++、Java、Python等，且各实现必须支持语言作用域内的特性。Protobuf运行时是Google开发的[[entities/Google|Google]] Protobuf生态系统的重要组成部分。

## 相关实体
- [[entities/Google|Google]] — Protobuf的创始与维护组织
- [[entities/Protobuf|Protobuf]] — 基于Protobuf运行时的序列化框架
- [[entities/protoc|protoc]] — Protobuf编译器，与运行时协同工作

## 相关概念
- [[concepts/Feature inheritance|Feature inheritance]] — 运行时需要理解的特性继承机制
- [[concepts/Features|Features]] — Protobuf Editions中定义的功能特性
- [[concepts/Language-scoped features|Language-scoped features]] — 不同语言运行时需支持的特性范围

## 来源提及
- "Runtimes must be able to handle descriptors 'from the future'; this only means that upon encountering a descriptor with an edition or feature it does not understand, there must be a reasonable fallback for the runtime's behavior." — [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]