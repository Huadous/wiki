---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/overview]]"]
tags: [product]
aliases:
  - "Envoy"
  - "Envoy proxy"
---


# Envoy Proxy

## 基本信息
- Type: product
- Source: [[protobuf/overview|overview]]

## 描述
Envoy Proxy 是一个高性能的、开源的边缘和服务代理，由 Lyft 公司创建并捐赠给云原生计算基金会（CNCF）。它被广泛用作服务网格架构中的数据平面组件，负责处理服务间的所有网络通信。Envoy Proxy 原生支持 [[entities/protocol-buffers|Protocol Buffers]]，用于其配置 API 和内部数据结构，这体现了 Protocol Buffers 在云原生基础设施中的广泛应用。作为 gRPC 的底层通信代理，Envoy 与 [[entities/grpc|gRPC]] 和 [[entities/google|Google Cloud]] 等生态成员紧密集成。它通过先进的负载均衡、可观测性和安全功能，成为微服务架构中的关键基础设施组件。

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]] — Envoy 使用 Protocol Buffers 作为其数据序列化格式
- [[entities/grpc|gRPC]] — Envoy 常作为 gRPC 服务的代理层
- [[entities/google|Google Cloud]] — Envoy 在 Google Cloud 服务网格中被广泛采用

## 相关概念
（无相关概念）

## 来源提及
- "Many projects use protocol buffers, including the following: gRPC, Google Cloud, Envoy Proxy." — [[protobuf/overview|overview]]