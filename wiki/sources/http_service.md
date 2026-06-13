---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/http_service.md]]"
tags: [HTTP/H2服务, Restful URL映射, default_method, HTTP headers, Content-Type, Status Code, Query String, gzip压缩, HTTPS, ProgressiveAttachment, Server-Sent Events, protobuf服务定义, 持续接收, request body解压, chunked传输, h2c, http_verbose, http_body_compress_threshold, Accept-encoding header, Base64编码, percent encoding, 302重定向]
aliases: ["brpc HTTP/H2 服务文档", "brpc HTTP service"]
---

# brpc HTTP/H2 服务文档 - Summary

## 来源
- Original file: [[brpc/http_service.md]]
- Ingested: 2026-06-13

## 核心内容
本文档详细介绍了 [[entities/brpc|brpc]] 框架中 HTTP/H2 服务的使用方法与实现机制。brpc 的 HTTP/H2 服务接口需要在 proto 文件中定义，request 和 response 使用空结构体，数据通过 Controller 传递。文章阐述了三种 URL 路由模式：以 /ServiceName/MethodName 为前缀的标准模式、以 /ServiceName 为前缀的资源服务模式（使用 [[concepts/default_method|default_method]]）、以及通过 AddService 的 restful_mappings 参数配置的 [[concepts/restful-url映射|Restful URL 映射]]。文档涵盖了 HTTP 参数处理，包括 [[concepts/http-headers|HTTP headers]]、[[concepts/content-type|Content-Type]]、[[concepts/status-code|Status Code]] 和 [[concepts/query-string|Query String]] 的读写接口；介绍了 response body 的 [[concepts/gzip压缩|gzip 压缩]]机制与 [[concepts/request-body解压|request body 解压]]方法；说明了 [[concepts/https|HTTPS/SSL]] 的开启方式。性能方面，brpc 使用 [[entities/node-js-http-parser|node.js http parser]] 和 [[entities/rapidjson|rapidjson]] 解析 HTTP 消息，支持 O(N) 解析复杂度，并通过 [[concepts/progressiveattachment|ProgressiveAttachment]] 支持超大或无限长 body 的持续发送，可实现 [[concepts/server-sent-events|Server-Sent Events (SSE)]] 服务。FAQ 部分解答了 [[entities/nginx|nginx]] final fail、chunked 传输、Base64 query string 解析等问题。

## 关键实体
- [[entities/brpc|brpc]]
- [[entities/nginx|nginx]]
- [[entities/rapidjson|rapidjson]]
- [[entities/node-js-http-parser|node.js http parser]]

## 关键概念
- [[concepts/httph2服务|HTTP/H2服务]]
- [[concepts/restful-url映射|Restful URL映射]]
- [[concepts/default_method|default_method]]
- [[concepts/http-headers|HTTP headers]]
- [[concepts/content-type|Content-Type]]
- [[concepts/status-code|Status Code]]
- [[concepts/query-string|Query String]]
- [[concepts/gzip压缩|gzip压缩]]
- [[concepts/https|HTTPS]]
- [[concepts/progressiveattachment|ProgressiveAttachment]]
- [[concepts/server-sent-events|Server-Sent Events]]
- [[concepts/protobuf服务定义|protobuf服务定义]]
- [[concepts/持续接收|持续接收]]
- [[concepts/request-body解压|request body解压]]
- [[concepts/chunked传输|chunked传输]]
- [[concepts/h2c|h2c]]
- [[concepts/http_verbose|http_verbose]]
- [[concepts/http_body_compress_threshold|http_body_compress_threshold]]
- [[concepts/accept-encoding-header|Accept-encoding header]]
- [[concepts/base64编码|Base64编码]]
- [[concepts/percent-encoding|percent encoding]]
- [[concepts/302重定向|302重定向]]

## 要点
- brpc 的 HTTP/H2 服务接口必须在 proto 文件中定义，request 和 response 使用空结构体，数据通过 Controller 对象传递
- brpc 支持三种 URL 路由模式：`/ServiceName/MethodName` 前缀模式、`/ServiceName` 资源模式（使用 [[concepts/default_method|default_method]]）、以及 AddService 的 restful_mappings 参数配置的 [[concepts/restful-url映射|Restful URL 映射]]
- Restful URL 映射的星号 (`*`) 通配符匹配部分对应 `cntl.http_request().unresolved_path()`，保证 normalized：开头结尾不含斜杠、中间斜杠不重复
- [[concepts/content-type|Content-Type]] 是 brpc 特殊处理的 header，必须通过 `content_type()` 读取，不能用 `GetHeader("Content-Type")`
- brpc 使用 [[entities/node-js-http-parser|node.js http parser]] 和 [[entities/rapidjson|rapidjson]] 保证 HTTP 解析的 O(N) 线性时间复杂度和高并发性能
- Response body 的 [[concepts/gzip压缩|gzip 压缩]]受客户端 [[concepts/accept-encoding-header|Accept-encoding header]] 和 [[concepts/http_body_compress_threshold|http_body_compress_threshold]]（默认 512 字节）两个条件约束
- [[concepts/progressiveattachment|ProgressiveAttachment]] 机制支持发送超大或无限长 body，可实现 [[concepts/server-sent-events|Server-Sent Events (SSE)]] 服务，适合 chatGPT 类实时应用
- [[entities/nginx|nginx]] 前置 brpc 时报 'final fail' 的原因是 brpc 对无法识别的 HTTP 请求直接关闭连接，可通过 `$HTTP_method` 限制放行方法或设置 `proxy_method` 解决