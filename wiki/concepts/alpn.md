---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/server|server]]"]
tags: [standard]
aliases:
  - "Application-Layer Protocol Negotiation"
  - "应用层协议协商"
  - "ALPN 协议"
---


# ALPN

## 定义
ALPN（Application-Layer Protocol Negotiation，应用层协议协商）是 TLS 的一个扩展协议，允许客户端和服务器在建立安全连接时协商使用哪种应用层协议。在 brpc 中，通过 `ServerSSLOptions.alpns` 字段可以设置 Server 端支持的协议字符串，Server 在启动时会校验协议字符串的有效性，多个协议之间使用逗号分隔。

## 关键特征
- TLS 扩展协议：在 TLS 握手阶段完成应用层协议的协商，无需额外的协议握手过程
- 协议字符串列表：服务端通过 `alpns` 字段声明支持的协议集合，例如 `"http, h2, baidu_std"`
- 启动时校验：Server 在启动阶段对配置的协议字符串进行合法性校验，确保格式有效
- 与 SSL 集成：与 [[concepts/SSL|SSL]] 结合使用，使同一 TLS 连接可根据需要选择不同的 RPC 协议
- 多协议共存：避免了为不同的安全协议使用不同端口或连接的开销

## 应用
- 在 brpc 中启用安全 RPC 服务时，通过 `ServerSSLOptions.alpns` 配置支持的应用层协议，使客户端能在同一 TLS 连接中根据需要选择合适的协议（如 HTTP/2 或 baidu_std）
- 适用于需要同时支持多种 RPC 协议（HTTP、H2、自研协议等）的安全通信场景
- 在安全连接中实现协议层与应用层的解耦，提升部署灵活性

## 相关概念
- [[concepts/SSL|SSL]]
- [[concepts/ServerSSLOptions|ServerSSLOptions]]

## 相关实体
*No related entities*

## 来源提及
- 如果想支持应用层协议协商，可通过`alpns`选项设置Server端支持的协议字符串，在Server启动时会校验协议的有效性，多个协议间使用逗号分割。 — [[sources/server|server]]
- ```cpp
ServerSSLOptions ssl_options;
ssl_options.alpns = "http, h2, baidu_std";
— [[sources/server|server]]