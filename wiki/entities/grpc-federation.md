---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "grpc-federation"
  - "Mercari gRPC Federation"
  - "mercari/grpc-federation"
---


# gRPC Federation

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
gRPC Federation 是由 Mercari 开发的 gRPC 服务联邦框架,代码托管在 GitHub 的 mercari/grpc-federation 仓库中。该框架在 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 全局扩展注册表中注册了扩展编号 1187,用于在 Protocol Buffers 的自定义选项中声明式地定义 gRPC 服务之间的调用关系、数据转换与错误处理逻辑。

借助 gRPC Federation,开发者可以在单一 proto 文件中编排多个后端 gRPC 服务,实现类似 GraphQL 的 API 网关或 BFF(Backend for Frontend)模式。该框架强调以代码生成而非运行时反射的方式构建服务联邦,从而保证类型安全与运行时性能,并与 [[entities/protoc-gen-validate|protoc-gen-validate]] 等 protoc 插件生态紧密集成。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]

## 相关概念
- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/custom-options|Custom options]]
- [[concepts/descriptor.proto|descriptor.proto]]
- [[concepts/protoc-plugins|protoc plugins]]

## 来源提及
- "gRPC Federation — [[sources/options|options]]"
- "Website: https://github.com/mercari/grpc-federation — [[sources/options|options]]"
- "Extensions: 1187 — [[sources/options|options]]"