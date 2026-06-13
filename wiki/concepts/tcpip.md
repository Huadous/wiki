---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[brpc/baidu_std.md]]"
tags:
  - "standard"
aliases:
  - "传输控制协议/网际协议"
  - "互联网协议栈"
  - "TCP"
  - "传输控制协议/网际协议"
  - "互联网协议栈"
---

## Description
TCP/IP 是互联网通信的基础协议族，绝大多数联网机器之间的数据传输都基于 TCP/IP 完成。然而，TCP/IP 的职责仅停留在保证可靠的字节流传输层面——它并不关心上层应用如何组织请求与响应，也不提供过程调用或服务调用的语义抽象，因此在构建分布式服务时，开发者通常需要在 TCP/IP 之上再叠加一层协议（如 RPC 框架）来实现请求-响应的配对、序列化与并发模型等高级特性。TCP 同样是 [[sources/baidu_std|baidu_std]] 协议的底层传输载体：baidu_std 是一种基于 TCP 协议的二进制 RPC 通信协议，其请求与响应必须在同一个 TCP 连接内完成配对，不考虑跨 TCP 连接的情况。baidu_std 包头中的整数统一采用网络字节序（大端序）表示，这也是 TCP/IP 协议族所规定的标准编码方式，确保了不同架构的通信双方能够正确解析二进制字段。

## Related Concepts
- [[concepts/rpc|远程过程调用（RPC）]]
- [[concepts/network-byte-order|网络字节序（大端序）]]

## Related Entities
- [[entities/baidu_std|baidu_std]]

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
- "Most machines on internet communicate with each other via TCP/IP. However, TCP/IP only guarantees reliable data transmissions. We need to abstract more to build services"
- "RPC can't do everything surely, otherwise we don't need the layer of TCP/IP. But in most network communications, RPC meets requirements and isolates the underlying details."
- "Most machines on internet communicate with each other via TCP/IP."
- "However, TCP/IP only guarantees reliable data transmissions."

> **Source: [[sources/baidu_std|baidu_std]]**
- "baidu_std是一种基于TCP协议的二进制RPC通信协议。"
- "baidu_std不考虑跨TCP连接的情况。"
- "整数均采用网络字节序表示。"