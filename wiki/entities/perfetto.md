---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "Perfetto Tracing Framework"
  - "Perfetto 追踪框架"
---


# Perfetto

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Perfetto 是一个由 Google 主导开发的开源系统追踪、性能分析和日志记录框架，官方网站为 [https://perfetto.dev](https://perfetto.dev)。它在 Protocol Buffers 全局扩展注册表中分配到的扩展编号为 **1156**。Perfetto 被广泛应用于 Android 系统以及跨平台的应用性能监控场景，其 protobuf 扩展机制被用于自定义追踪数据的元数据描述，使开发者能够在 `.proto` 文件中为追踪事件附加类型化的标签和配置信息。作为 [[entities/wire|Wire]] 等 protobuf 生态项目的同类工具，Perfetto 与 [[entities/protobuf-net|protobuf-net]]、[[entities/grpc-gateway|grpc-gateway]]、[[entities/scalapb|scalapb]]、[[entities/nanopb|nanopb]] 等项目共同构成了 Protocol Buffers 工具链的多样化生态。

## 相关实体
- [[entities/wire|Wire]]
- [[entities/protobuf-net|protobuf-net]]
- [[entities/grpc-gateway|grpc-gateway]]
- [[entities/scalapb|scalapb]]
- [[entities/nanopb|nanopb]]
- [[entities/protobuf-csharp-port|protobuf-csharp-port]]

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]

## 来源提及
- Perfetto — [[sources/options|options]]
- Website: https://perfetto.dev — [[sources/options|options]]
- Extension: 1156 — [[sources/options|options]]