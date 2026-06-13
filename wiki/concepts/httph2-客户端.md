---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_client]]"]
tags: [method]
aliases:
  - "HTTP client"
  - "h2 客户端"
  - "HTTP/h2 Client"
---


# HTTP/h2 客户端

## 定义
HTTP/h2 客户端是 brpc 框架中提供的能力，允许用户通过统一的 [[concepts/Channel|brpc::Channel]] 与 [[concepts/Controller|brpc::Controller]] 接口访问 HTTP/1.1、HTTP/2 以及 HTTPS 服务。客户端通过 `ChannelOptions.protocol` 字段指定 `PROTOCOL_HTTP` 或 `PROTOCOL_H2` 来选择协议，其中 HTTP/2 包含 h2（加密）与 h2c（明文）两种形式。

## 关键特征
- **协议统一**：HTTP 与 H2 的编程接口基本一致，除特殊说明外所有 HTTP 特性对 H2 同样有效。
- **协议选择**：通过 `ChannelOptions.protocol` 字段指定 `PROTOCOL_HTTP` 或 `PROTOCOL_H2` 来选择协议。
- **多 Method 支持**：支持 GET、POST 等多种 HTTP Method。
- **请求构造**：可通过 `cntl.http_request()` 接口构造请求头、URI、Body 等内容。
- **HTTPS 兼容**：通过 h2（加密）形式支持 HTTPS 服务访问。
- **统一控制器**：所有 HTTP/H2 请求通过 [[concepts/Controller|brpc::Controller]] 接口统一管理。

## 应用
- 访问外部 HTTP/1.1 RESTful API 服务。
- 通过 HTTP/2（h2/h2c）协议访问支持 HTTP/2 的服务。
- 通过 HTTPS 访问需要加密传输的 Web 服务。
- 在 brpc 客户端中以 HTTP 协议调用上游服务，灵活适配多种协议栈。
- 通过 `cntl.http_request()` 接口自定义请求头、URI、Body 等内容，构造复杂 HTTP 请求。

## 相关概念
- [[concepts/Channel|Channel]]
- [[concepts/HTTP Method|HTTP Method]]
- [[concepts/HTTP Header 与 Query|HTTP Header 与 Query]]
- [[concepts/HTTPS/SSL 客户端|HTTPS/SSL 客户端]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "brpc中http和h2的编程接口基本没有区别。除非特殊说明，所有提到的http特性都同时对h2有效。" — [[sources/http_client]]
- "brpc::Channel可访问http/h2服务，ChannelOptions.protocol须指定为PROTOCOL_HTTP或PROTOCOL_H2。" — [[sources/http_client]]