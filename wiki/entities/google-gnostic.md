---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "Gnostic"
  - "google/gnostic"
  - "Google Gnostic 工具链"
---


# Google Gnostic

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Google Gnostic 是 Google 维护的 OpenAPI/gRPC 工具链,代码托管在 GitHub 的 google/gnostic 仓库中。Gnostic 在 [[sources/options|Protocol Buffers 扩展注册表]]中注册了扩展编号 1143,用于在 OpenAPI 与 Protobuf 互转过程中保留工具链特定的选项。Gnostic 能够读取 OpenAPI 规范(原 Swagger),生成对应的 Protocol Buffers 文件、客户端 SDK 与文档,并支持从 .proto 文件反向生成 OpenAPI 描述。该项目是 Google 内部支撑 Cloud Endpoints、gRPC Gateway 等服务的关键基础设施之一,促进了 REST API 描述语言与 Protobuf 生态之间的桥梁构建。Gnostic 的工作原理基于 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 的 [[concepts/descriptor.proto|descriptor.proto]] 扩展机制,通过为自定义选项保留 [[concepts/extension-numbers|扩展编号]]实现双向转换时的语义保真。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/protoc-gen-openapi|protoc-gen-openapi]]
- Protobuf Global Extension Registry

## 相关概念
- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/custom-options|Custom options]]
- [[concepts/descriptor.proto|descriptor.proto]]
- [[concepts/protoc-plugins|protoc plugins]]

## 来源提及
- "Google Gnostic — [[sources/options|options]]"
- "Website: https://github.com/google/gnostic — [[sources/options|options]]"
- "Extension: 1143 — [[sources/options|options]]"