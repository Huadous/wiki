---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "Cloudstate.io"
  - "CloudState"
  - "Cloudstate 有状态无服务器平台"
---


# Cloudstate

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Cloudstate 是一个面向有状态无服务器 (stateful serverless) 场景的开源平台,其在 [[sources/options|descriptor.proto 扩展登记表]] 中注册了 Protocol Buffers 扩展编号 1080-1084,项目官方网站为 [https://cloudstate.io](https://cloudstate.io)。该项目基于 [[entities/protocolbuffersprotobuf|gRPC]] 与 Akka Cluster 构建,为开发者提供分布式状态管理、事件溯源 (Event Sourcing)、CQRS 以及最终一致性 (eventual consistency) 保证,使开发者能够以函数式编程模型构建有状态服务。

Cloudstate 使用 Protocol Buffers 作为其服务定义、状态序列化以及 CRDT 消息的统一格式,并通过 [[sources/options|descriptor.proto]] 扩展为其特有的状态选项保留较大范围的扩展编号段 (1080-1084)。在 [[sources/options|descriptor.proto 扩展登记表]] 中,Cloudstate 是为数不多占用连续五个扩展编号的项目之一,这反映了其服务定义中包含多个相互关联的自定义选项。

该项目最初由 Lightbend 发起,后被捐献并整合到其商业产品 Kalix (原 Lightbend 平台)中,成为 Kalix 分布式状态运行时的重要组成部分。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]] — Cloudstate 使用 Protocol Buffers 作为服务定义、状态序列化与 CRDT 消息的统一格式
- [[entities/protocolbuffersprotobuf|Protobuf Global Extension Registry]] — 维护 descriptor.proto 扩展编号注册信息的官方资源

## 相关概念
- [[concepts/extension-numbers|Extension numbers]] — Cloudstate 注册的 1080-1084 属于 Protocol Buffers 自定义扩展编号体系
- [[concepts/custom-options|Custom options]] — Cloudstate 通过自定义选项扩展 Protocol Buffers 的服务定义能力
- [[concepts/descriptor-proto|descriptor.proto]] — Cloudstate 的扩展注册于 descriptor.proto 文件中

## 来源提及
- Cloudstate — [[sources/options|options]]
- Website: https://cloudstate.io — [[sources/options|options]]
- Extensions: 1080-1084 — [[sources/options|options]]