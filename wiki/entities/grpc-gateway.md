---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "grpc-gateway"
  - "gRPC Gateway"
  - "grpc gateway"
---


# grpc-gateway

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
grpc-gateway 是一个将 gRPC 服务自动反向代理为 JSON HTTP API 的工具，最初由 gengo 开发，托管地址为 https://github.com/gengo/grpc-gateway（使用扩展编号 1022）。其后续版本 grpc-gateway protoc-gen-swagger 迁移至 grpc-ecosystem 组织下，托管地址为 https://github.com/grpc-ecosystem/grpc-gateway（使用扩展编号 1042），用于生成 Swagger/OpenAPI 文档。grpc-gateway 通过读取 Protocol Buffers 中的自定义选项（custom options）注解，将 gRPC 的 service/method 映射为 RESTful HTTP 路由，使得基于 gRPC 的微服务能够同时对外提供 JSON over HTTP 接口，是云原生架构中桥接 gRPC 与 HTTP/REST 的重要工具。它与 [[entities/butil|butil]] 等百度 brpc 生态项目在 API 网关领域形成互补，在微服务统一接入层具有广泛的应用价值。

## 相关实体
- [[entities/protoc-gen-openapi|protoc-gen-openapi]]
- [[entities/Connect|Connect]]
- [[entities/Buf|Buf]]
- [[entities/protoc-gen-jsonschema|protoc-gen-jsonschema]]

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]

## 来源提及
- grpc-gateway — [[sources/options|options]]
- Website: https://github.com/gengo/grpc-gateway — [[sources/options|options]]
- Extensions: 1022 — [[sources/options|options]]
- grpc-gateway protoc-gen-swagger — [[sources/options|options]]
- Website: https://github.com/grpc-ecosystem/grpc-gateway — [[sources/options|options]]
- Extensions: 1042 — [[sources/options|options]]