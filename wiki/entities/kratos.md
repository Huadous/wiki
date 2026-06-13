---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "Kratos API Errors"
  - "go-kratos"
  - "bilibili/kratos"
---


# Kratos

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述

Kratos 是由 bilibili 开源的 Go 微服务框架,项目网站为 [go-kratos.dev](https://go-kratos.dev)。该框架提供了一整套用于构建生产级微服务所需的组件,涵盖传输协议(gRPC 与 HTTP)、服务治理(服务发现、负载均衡、熔断与限流)、配置管理、可观测性(指标、日志、链路追踪)以及 API 错误处理等关键能力。

Kratos 以 Protocol Buffers 作为其 IDL(接口定义语言),并通过自定义选项(注册到 [[entities/protobuf-global-extension-registry|Protobuf Global Extension Registry]] 的扩展编号 **1108**)来定义其标准化的 API 错误响应模型,采用与 `google.rpc.Status` 兼容的结构。该实践体现了 Protobuf 扩展在 Go 微服务生态中规范 API 错误格式的常见用法,使得不同服务间能够以统一的 wire-format 传递错误信息。

作为 Protobuf 生态中的重要项目,Kratos 隶属于 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 生态,并与 [[entities/protoc-gen-validate|protoc-gen-validate]]、[[entities/grpc-gateway|grpc-gateway]]、[[entities/connect|Connect RPC]] 等工具在 Go 微服务场景中相互配合,共同构成了基于 Protobuf 的现代服务开发体系。

## 相关实体

- [[entities/protocolbuffersprotobuf|protocolbuffers/protobuf]]
- [[entities/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[entities/grpc-gateway|grpc-gateway]]
- [[entities/connect|connect]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]

## 相关概念

- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/custom-options|Custom options]]
- [[concepts/descriptor.proto|descriptor.proto]]
- [[concepts/protoc-plugins|protoc plugins]]

## 来源提及

- "Kratos API Errors" — [[sources/options|options]]
- "Website: https://go-kratos.dev" — [[sources/options|options]]
- "Extension: 1108" — [[sources/options|options]]