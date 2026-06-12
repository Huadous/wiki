---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [phenomenon]
aliases:
  - "Nginx最终失败"
  - "Nginx upstream fail"
  - "nginx final fail"
---


# nginx final fail

## 定义

nginx final fail 是一个Nginx日志中出现的错误，表示当brpc服务器在处理HTTP请求失败时，直接关闭连接而不发送任何HTTP响应，导致Nginx认为上游服务器（brpc）出现了"最终失败"。

## 关键特征

- 错误发生在Nginx代理环境，且brpc作为上游服务器
- brpc服务器不发送400等错误响应，而是直接关闭TCP连接
- 根本原因是brpc的**多协议同端口**设计：服务器无法确定"解析失败"的请求是否确实是HTTP协议请求
- 错误通常出现在HTTP方法或序列化解析阶段
- Nginx将此行为归类为upstream错误，日志标记为'final fail'

## 应用

- **brpc服务部署**：当使用Nginx作为反向代理转发请求到brpc服务时，若brpc启用多协议同端口（如HTTP+Protobuf+Redis），请求格式不匹配可能导致此问题
- **协议兼容调试**：排查"请求正常但Nginx报502"或"Nginx日志出现final fail"的问题时，应考虑brpc的多协议处理策略

## 相关概念

- [[concepts/HTTP解析|HTTP解析]]
- [[concepts/多协议支持|多协议支持]]

## 相关实体

- [[entities/socket|Socket]]
- [[entities/inputmessenger|InputMessenger]]

## 来源提及

- "The error is caused by that brpc server closes the http connection directly without sending a response." — [[sources/en_http_service|brpc HTTP/h2服务]]
- "brpc server supports a variety of protocols on the same port. When a request is failed to be parsed in HTTP, it's hard to tell that the request is definitely in HTTP." — [[sources/en_http_service|brpc HTTP/h2服务]]