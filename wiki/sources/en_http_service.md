---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[brpc/en_http_service.md]]"
tags: [HTTP/2, gzip compression, content-type, status-code, query-string, SSL, RESTful API, Server-Sent Events, chunked transfer encoding]
aliases: ["HTTP/2 Service 文档", "brpc HTTP 服务指南"]
---

# HTTP/h2 Service - Summary

## 来源
- Original file: [[brpc/en_http_service.md]]
- Ingested: 2026-06-12

## 核心内容

本文档详细介绍了 [[entities/brpc|brpc]] 框架中的 HTTP 和 HTTP/2 服务实现。核心内容包括：通过 protobuf 文件中定义空请求和响应消息来声明服务接口，所有数据通过 Controller 对象访问。文档阐释了三种 URL 模式：[[concepts/servicenamemethodname-url-pattern|ServiceName/MethodName 模式]]、[[concepts/servicename-url-pattern|ServiceName 资源管理模式]]和 [[concepts/restful-url-mapping|RESTful URL 映射]]，以及如何处理 [[concepts/http-headers-in-brpc|HTTP 头部]]、[[concepts/content-type-in-brpc|Content-Type]]、[[concepts/status-code-in-brpc|状态码]]和[[concepts/query-string-in-brpc|查询字符串]]。此外，还涵盖 [[concepts/gzip-compression-in-brpc|Gzip 压缩]]、[[concepts/progressiveattachment-brpc|渐进发送]]及其实现的[[concepts/server-sent-events-sse-in-brpc|SSE]]、[[concepts/ssltls-in-brpc|SSL/TLS 支持]]，以及[[concepts/chunked-transfer-encoding-in-brpc|分块传输编码]]。文档也提供了常见问题的解答，包括 nginx 故障排查和[[concepts/percent-encoding-in-brpc|百分比编码]]查询字符串的处理。

## 关键实体

- [[entities/brpc|brpc]] — 高性能 RPC 框架，提供 HTTP/h2 完整支持

## 关键概念

- [[concepts/httph2-service|HTTP/h2 service]] — 使用空请求/响应 protobuf 消息的服务定义方法
- [[concepts/servicenamemethodname-url-pattern|ServiceName/MethodName URL pattern]] — 默认 URL 访问模式
- [[concepts/servicename-url-pattern|ServiceName URL pattern]] — 资源管理类服务的 URL 前缀模式
- [[concepts/restful-url-mapping|RESTful URL mapping]] — 自定义 URL 路径支持通配符和后缀匹配
- [[concepts/http-headers-in-brpc|HTTP headers (in brpc)]] — 通过 Controller 操作的键值对
- [[concepts/content-type-in-brpc|Content-Type (in brpc)]] — 正文类型标识的专用处理方法
- [[concepts/status-code-in-brpc|Status Code (in brpc)]] — 响应处理状态的特殊字段
- [[concepts/query-string-in-brpc|Query String (in brpc)]] — URL 中 ? 后的参数解析
- [[concepts/gzip-compression-in-brpc|Gzip compression (in brpc)]] — 响应体自动压缩机制
- [[concepts/progressiveattachment-brpc|ProgressiveAttachment (brpc)]] — 渐进式发送大响应体的机制
- [[concepts/server-sent-events-sse-in-brpc|Server-Sent Events (SSE) (in brpc)]] — 服务器推送事件流技术
- [[concepts/ssltls-in-brpc|SSL/TLS (in brpc)]] — 加密传输支持
- [[concepts/chunked-transfer-encoding-in-brpc|Chunked transfer encoding (in brpc)]] — 分块传输编码支持
- [[concepts/percent-encoding-in-brpc|Percent-encoding (in brpc)]] — URI 保留字符编码标准
- [[concepts/default_method|default_method]] — 资源管理 URL 模式的特殊方法名
- [[concepts/unresolved_path|unresolved_path]] — 未匹配路径的获取方法
- [[concepts/h2c|h2c]] — 未加密 HTTP/2 连接标识
- [[concepts/http_verbose|http_verbose]] — 调试用的请求/响应打印开关
- [[concepts/http_body_compress_threshold|http_body_compress_threshold]] — Gzip 压缩阈值配置项

## 要点

- brpc 通过 protobuf 空请求/响应消息定义 HTTP/h2 服务，数据全部通过 Controller 访问
- 支持三种 URL 路由模式，其中 RESTful 映射支持通配符和多路径映射
- HTTP 参数（头部、Content-Type、状态码、查询字符串）均有专用 Controller 接口
- Gzip 压缩默认只在响应体超过 512 字节且客户端支持时启用
- ProgressiveAttachment 机制支持大文件/无限长度数据的渐进式发送，可基于此实现 SSE
- HTTP/2 连接在管理界面区分加密（h2）和未加密（h2c）
- 常见问题涵盖 nginx 代理错误、BASE64 编码查询字符串的百分比编码处理等