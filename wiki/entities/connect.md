---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "Connect RPC"
  - "Connect Build"
  - "connect.build"
---


# Connect

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Connect 是由 [[entities/buf|Buf]] 团队开发的一款 gRPC 兼容的 RPC 框架，官方网站为 http://connect.build/。在 [[sources/options|Protobuf Global Extension Registry]] 中，Connect 注册的扩展编号范围为 1167–1176，是注册扩展数量较多的项目之一。Connect 的设计目标是成为 gRPC 和 gRPC-Web 的更简单替代方案，它支持 HTTP/1.1、HTTP/2 和 HTTP/3，并且通过同一套接口同时处理客户端和服务端的代码生成。Connect 与 [[entities/grpc-gateway|grpc-gateway]] 同样关注 gRPC 的易用性，但采用了不同的协议路由与代码生成策略。

## 相关实体
- [[entities/buf|Buf]]
- [[entities/grpc-gateway|grpc-gateway]]

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]

## 来源提及
- "Connect" — [[sources/options|options]]
- "Website: http://connect.build/" — [[sources/options|options]]
- "Extension: 1167-1176" — [[sources/options|options]]