---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_client|http_client]]"]
tags: [method]
aliases:
  - "HTTP Version"
  - "HTTP 协议版本设置"
  - "brpc HTTP 版本控制"
---


# HTTP 版本控制

## 定义
HTTP 版本控制是指在 brpc 框架中根据通信需求选择和协商 HTTP 协议版本（如 HTTP/1.1、HTTP/1.0、HTTP/2）的机制与方法。brpc 的 HTTP 客户端默认采用 HTTP/1.1 协议；当与不支持长连接的旧版 HTTP 服务器通信时，可通过 `cntl.http_request().set_version(1, 0)` 降级至 HTTP/1.0；brpc server 端则会自动识别客户端请求的 HTTP 版本并相应回复。

## 关键特征
- **默认协议版本**：brpc HTTP 客户端默认使用 HTTP/1.1 协议。
- **降级支持**：与古老 HTTP server（不支持长连接）通信时，可通过 `cntl.http_request().set_version(1, 0)` 显式降级到 HTTP/1.0。
- **H2 协议的特殊行为**：显式设置 HTTP 版本对 H2 协议无效；但客户端收到的 H2 response 以及服务器收到的 H2 request 中的 `version` 字段会被自动设置为 `(2, 0)`。
- **服务端自动适配**：brpc server 端会自动识别客户端请求所使用的 HTTP 版本，并据此返回相应版本的响应，无需用户显式设置版本。
- **长连接差异**：HTTP/1.0 相比 HTTP/1.1 缺少长连接（keep-alive）能力。

## 应用
- 与仅支持 HTTP/1.0 的旧版服务器进行兼容通信。
- 在 H2 通信场景下隐式感知协议版本，便于协议协商与版本日志记录。
- 排查因 HTTP 版本不匹配导致的长连接复用异常或服务器响应异常问题。

## 相关概念
- [[concepts/http-h2-client|HTTP/h2 客户端]]

## 相关实体
*无相关实体*

## 来源提及
- "brpc的http行为默认是http/1.1。" — [[sources/http_client|http_client]]
- "http/1.0相比http/1.1缺少长连接功能，brpc client与一些古老的http server通信时可能需要按如下方法设置为1.0。" — [[sources/http_client|http_client]]
- "设置http版本对h2无效，但是client收到的h2 response和server收到的h2 request中的version会被设置为(2, 0)。" — [[sources/http_client|http_client]]