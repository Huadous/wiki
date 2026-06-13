---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "term"
aliases:
  - "SO_REUSEPORT"
  - "端口复用"
---

## Related Concepts

- [[concepts/多进程|多进程]]
- [[concepts/端口共享|端口共享]]
- [[concepts/协议自动检测|协议自动检测]]
- [[concepts/负载均衡|负载均衡]]
- [[concepts/服务器生命周期管理|服务器生命周期管理]]
- [[concepts/监听端口|监听端口]]
- [[concepts/并发限制|并发限制]]
- [[concepts/多端口监听|多端口监听]]
- [[concepts/socket选项|socket选项]]
- [[concepts/internal_port|internal_port]]

## Related Entities

- [[entities/brpc|brpc]]
- [[entities/nginx|nginx]]
- [[entities/envoy-proxy|envoy-proxy]]
- [[entities/ServerOptions|ServerOptions]]

## Mentions in Source

> **Source: [[sources/server|server]]**
> - "启动时开启reuse_port这个flag，就可以多进程共同监听一个端口（底层是SO_REUSEPORT）。"
> - "一个server只能监听一个端口（不考虑ServerOptions.internal_port），需要监听N个端口就起N个Server。"