---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client|en_client]]"]
tags: [standard]
aliases:
  - "HTTP/2"
  - "h2"
  - "brpc H2 协议"
---


# PROTOCOL_H2

## 定义
PROTOCOL_H2 是 brpc 对 HTTP/2 协议的支持选项，通过 `ChannelOptions.protocol` 设置为 `PROTOCOL_H2` 或字符串 `"h2"` 启用。该协议默认采用 single connection（单连接）模式，既可以访问标准 h2 服务，也可以通过派生方式（h2:json 或 h2:proto）访问 pb 服务，或以 h2:grpc 形式访问 gRPC 服务。

## 关键特征
- 协议标识：可通过枚举值 `PROTOCOL_H2` 或字符串 `"h2"` 进行设置。
- 默认连接模式：single connection（单连接）。
- 派生协议：
  - `h2:json`：基于 h2 的 JSON 序列化变体，用于访问 pb 服务。
  - `h2:proto`：基于 h2 的 Protobuf 序列化变体，用于访问 pb 服务。
  - `h2:grpc`：基于 h2 的 gRPC 协议变体，同样默认使用 single connection。
- Attachment 语义：与 HTTP 相同，H2 中的 attachment 也对应于消息体（message body）。
- SSL 支持：可与 SSL 结合以实现加密传输。
- Channel 集成：通过 [[entities/brpcdonothing|brpc::DoNothing]] 等机制集成在 [[entities/Channel|Channel]] 中，由 [[concepts/Controller|Controller]] 控制请求行为。

## 应用
- 调用标准 HTTP/2 服务：作为通用 h2 客户端访问遵循 HTTP/2 协议的 Web 服务。
- 调用 Protobuf 服务：通过 `h2:proto` 或 `h2:json` 派生方式访问 pb 服务，兼容不同序列化需求。
- gRPC 互通：使用 `h2:grpc` 派生协议与 gRPC 服务端进行通信。
- 加密通信场景：与 [[concepts/SSL|SSL]] 结合使用，建立安全的 h2 通道。
- 不同连接策略：通过 [[concepts/Connection Type|Connection Type]] 控制 single connection 或 pooled connection 等模式。

## 相关概念
- [[concepts/PROTOCOL_HTTP|PROTOCOL_HTTP]]
- [[concepts/SSL|SSL]]
- [[concepts/Attachment|Attachment]]
- [[concepts/ChannelOptions|ChannelOptions]]
- [[concepts/Connection Type|Connection Type]]

## 相关实体
- [[entities/gRPC|gRPC]]
- [[entities/Channel|Channel]]
- [[entities/Controller|Controller]]

## 来源提及
- "PROTOCOL_H2 or "h2", which is http/2, using single connection by default." — [[sources/en_client|en_client]]
- ""h2:grpc", which is the protocol of gRPC and based on h2, using single connection by default, check out [h2:grpc](http_derivatives.md#h2grpc) for details." — [[sources/en_client|en_client]]