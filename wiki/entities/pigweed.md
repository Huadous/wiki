---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "Pigweed"
  - "pw_protobuf"
  - "Google Pigweed"
---


# Pigweed

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Pigweed是Google面向嵌入式系统开发的模块化C++库集合,其中的pw_protobuf子模块注册了Protocol Buffers扩展编号1155,项目网站为pigweed.dev/pw_protobuf。Pigweed的目标是在资源受限的微控制器环境中提供高质量的开发库与工具链,其中pw_protobuf提供了一个针对嵌入式场景优化的轻量级Protocol Buffers运行时与编译器。Pigweed强调在嵌入式设备上对Protobuf消息的低开销编解码,并支持自定义选项以控制代码生成策略。该项目体现了Protobuf在嵌入式与物联网领域的进一步拓展,与[[entities/protocolbuffersprotobuf|Protocol Buffers]]主项目以及[[entities/nanopb|nanopb]]等同类嵌入式Protobuf实现形成互补。

## 相关实体
- [[entities/protocolbuffersprotobuf|protobuf]]
- Protobuf Global Extension Registry

## 相关概念
- Extension numbers
- Custom options
- descriptor.proto
- protoc plugins

## 来源提及
- Pigweed protobuf compiler — [[sources/options|options]]
- Website: https://pigweed.dev/pw_protobuf — [[sources/options|options]]
- Extension: 1155 — [[sources/options|options]]