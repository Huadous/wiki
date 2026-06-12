---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "term"
aliases:
  - "网络端点"
  - "EndPoint"
  - "Butil.EndPoint"
  - "网络端点"
  - "EndPoint"
---

## 描述
butil::EndPoint 封装了网络通信所需的 IP 地址和端口号，是 brpc 框架中处理网络端点的基础数据类型。通过在 `brpc::Controller` 对象上调用 `remote_side()` 和 `local_side()` 方法，开发者可以分别获取发起请求的客户端地址和 RPC 连接的服务器端地址。该类型支持通过 `butil::endpoint2str()` 函数转换为人类可读的字符串，同时兼容 `LOG(INFO)` 等日志流的直接输出，便于调试和地址管理。在不同网络协议（如 TCP、RDMA）之间，butil::EndPoint 提供了统一的端点表示方式。

## 相关概念
- [[concepts/远程地址|远程地址]]
- [[concepts/本地地址|本地地址]]
- [[concepts/solicited标志|solicited标志]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/rdmaendpoint|rdmaendpoint]]

## 来源提及
**Source: [[sources/en_server|en_server]]**
- "controller->remote_side() gets address of the client which sent the request. The return type is butil::EndPoint."
- "controller->local_side() gets server-side address of the RPC connection, return type is butil::EndPoint."
- "LOG(INFO) << "remote_side=" << cntl->remote_side(); printf("remote_side=%s\n", butil::endpoint2str(cntl->remote_side()).c_str());"