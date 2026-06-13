---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "term"
aliases:
  - "brpc::SocketMap"
  - "global SocketMap"
  - "SocketMap"
---

## Related Concepts
- [[concepts/Health Checking]]
- [[concepts/Load Balancer]]
- [[concepts/Connection Type]]
- 连接方式
- 健康检查
- 负载均衡

## Related Entities
- [[entities/Channel]]
- [[entities/Controller]]
- [[entities/brpc::Channel]]
- [[entities/brpc::LoadBalancer]]

## Mentions in Source
> **Source: [[sources/en_client]]**
> - "According to how the Channel is initialized, choose a server from global SocketMap or LoadBalancer as destination of the request."
> - "Servers whose connections are lost are isolated temporarily to prevent them from being selected by LoadBalancer."

> **Source: [[sources/client]]**
> - "根据Channel的创建方式，从进程级的SocketMap中或从LoadBalancer中选择一台下游server作为本次RPC发送的目的地。"
> - "在默认的配置下，一旦server被连接上，它会恢复为可用状态,可通过-health_check_timeout_ms设置超时（默认500ms）"