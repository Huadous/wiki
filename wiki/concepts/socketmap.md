---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [term]
aliases:
  - "brpc::SocketMap"
  - "global SocketMap"
  - "SocketMap"
---


# SocketMap

## 定义
SocketMap 是 brpc 内部的全局数据结构（定义于 `src/brpc/socket_map.h`），用于维护 brpc 客户端到各服务器的连接映射。在客户端工作流程中，Channel 在初始化后会从全局 SocketMap 或 LoadBalancer 中选择一个服务器作为请求目的地；SocketMap 中保存的连接同时被用于健康检查（Health Checking）以及跨多个 Channel 的连接共享，并配合 `-idle_timeout_second` 等 gflag 实现空闲连接的自动关闭。

## 关键特征
- 全局数据结构，定义于 `src/brpc/socket_map.h`，对所有客户端 Channel 可见
- 作为 Channel 初始化时选取目标服务器的来源之一（与 LoadBalancer 并列）
- 维护到各服务器的连接，并支持跨 Channel 的连接共享，避免重复建连
- 连接被用于健康检查（Health Checking），用于判断服务器可用性
- 连接失效的服务器会被临时隔离（isolate），防止被 LoadBalancer 再次选中
- 通过 `-idle_timeout_second` 等 gflag 控制空闲连接的自动回收
- 是 [[concepts/Connection Type]] 在 brpc 客户端中的具体承载形式之一

## 应用
- 客户端 Channel 初始化时从 SocketMap 中选择请求目的地
- 跨多个 Channel 共享到同一服务器的连接，降低建连开销
- 配合健康检查机制（[[concepts/Health Checking]]）持续跟踪服务器连接状态
- 与 [[concepts/Load Balancer]] 协作：连接丢失的服务器被临时隔离，避免被再次选中
- 通过 `-idle_timeout_second` 等 gflag 实现空闲连接的自动关闭，释放资源

## 相关概念
- [[concepts/Health Checking]]
- [[concepts/Load Balancer]]
- [[concepts/Connection Type]]

## 相关实体
- [[entities/Channel]]
- [[entities/Controller]]

## 来源提及
- "According to how the Channel is initialized, choose a server from global SocketMap or LoadBalancer as destination of the request." — [[sources/en_client]]
- "Servers whose connections are lost are isolated temporarily to prevent them from being selected by LoadBalancer." — [[sources/en_client]]