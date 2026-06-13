---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client|en_client]]"]
tags: [standard]
aliases:
  - "PROTOCOL_HTTP"
  - "http"
  - "HTTP/1.0"
  - "HTTP/1.1"
---


# PROTOCOL_HTTP

## 定义
PROTOCOL_HTTP 是 brpc 在 [[concepts/channel-options|ChannelOptions]] 中 `protocol` 字段所设置的协议标识之一，对应 HTTP/1.0 与 HTTP/1.1 协议。它既可用于访问普通的 HTTP 服务，也可通过 `http:json` 或 `http:proto` 派生方式访问基于 protobuf 的服务（pb 服务）。当 `Init()` 检测到 `https://` 前缀时，会自动开启 [[concepts/ssl|SSL]]。

## 关键特征
- 默认使用 pooled connection（即 Keep-Alive 长连接）。
- 同时覆盖 HTTP/1.0 与 HTTP/1.1 两种协议版本。
- 既可作为普通 HTTP 客户端协议，也可作为派生协议前缀（`http:json`、`http:proto`）访问 pb 服务。
- HTTP 协议下的错误以 `EHTTP` 错误码标识。
- 在 HTTP 协议下，[[concepts/attachment|Attachment]] 对应于 HTTP 消息体（message body），即存储在 `request_attachment()` 中的数据就是要 POST 到服务端的内容。

## 应用
- 访问普通 HTTP 服务（参见 [[sources/http_client|http_client]]）。
- 通过 `http:json` 或 `http:proto` 派生方式，将 pb 服务以 HTTP 接口形式暴露或调用。
- 在需要 Keep-Alive 长连接复用的场景下作为首选协议，以减少连接建立开销。
- 通过 `https://` 前缀直接启用 [[concepts/ssl|SSL]]，访问 HTTPS 服务端点。
- 作为 [[entities/channel|Channel]] 的协议选项进行配置，与 [[concepts/compression|Compression]]、[[concepts/connection-type|Connection Type]] 等选项协同工作。

## 相关概念
- [[concepts/ssl|SSL]]
- [[concepts/attachment|Attachment]]
- [[concepts/channel-options|ChannelOptions]]
- [[concepts/connection-type|Connection Type]]
- [[concepts/compression|Compression]]

## 相关实体
- [[entities/channel|Channel]]
- [[entities/controller|Controller]]
- [[entities/apache-thrift|Apache Thrift]]

## 来源提及
- "PROTOCOL_HTTP or 'http', which is http/1.0 or http/1.1, using pooled connection by default (Keep-Alive)." — [[sources/en_client|en_client]]
- "Methods for accessing ordinary http services are listed in [Access http/h2](http_client.md)." — [[sources/en_client|en_client]]
- "In http/h2, attachment corresponds to message body, namely the data to post to server is stored in request_attachment()." — [[sources/en_client|en_client]]