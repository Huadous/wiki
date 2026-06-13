---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_service|http_service]]"]
tags: [term]
aliases:
  - "Accept-Encoding"
  - "Accept-Encoding header"
  - "HTTP Accept-Encoding 请求头"
---


# Accept-encoding header

## 定义
Accept-encoding 是 HTTP 协议中用于客户端通知服务端其能够接受的响应 body 内容编码方式的标准请求头。它是 HTTP 内容协商（content negotiation）机制的关键组成部分，允许客户端声明自己支持的压缩算法（如 gzip），服务端据此决定是否对响应进行压缩。

## 关键特征
- 作为标准 HTTP 请求头，属于 HTTP 内容协商机制的一部分
- 客户端通过该头部声明可接受的内容编码方式（如 gzip、deflate、br 等）
- brpc 服务端通过检查该头部决定是否对响应进行 gzip 压缩
- 如果请求中未设置该头部或不包含 gzip，服务端始终返回未压缩的结果
- header 名称大小写不敏感
- 典型未声明场景：curl 在不加 `--compressed` 参数时不支持压缩

## 应用
- **HTTP 内容协商**：客户端通过该头部告知服务端其支持的压缩方式，服务端据此选择合适的编码方式
- **brpc 服务端压缩**：brpc 服务端依据请求中的 Accept-encoding 字段决定是否启用 gzip 压缩以减少网络传输量
- **压缩阈值控制**：与 [[concepts/http_body_compress_threshold|http_body_compress_threshold]] 配合使用，仅对超过阈值的响应体进行压缩
- **API 调用方设置**：可通过 `cntl->http_response().SetHeader("Accept-encoding", "gzip")` 在响应中设置相关头部
- **HTTP 客户端行为**：类似 curl 的客户端在默认情况下不发送 Accept-encoding，需要显式添加 `--compressed` 等参数才会启用压缩协商

## 相关概念
- [[concepts/gzip压缩|gzip压缩]]
- [[concepts/Content-Encoding|Content-Encoding]]
- [[concepts/HTTP-headers|HTTP headers]]
- [[concepts/http_body_compress_threshold|http_body_compress_threshold]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- 请求中没有设置Accept-encoding或不包含gzip。比如curl不加--compressed时是不支持压缩的，这时server总是会返回不压缩的结果 — [[sources/http_service|http_service]]
- // 在header中增加"Accept-encoding: gzip"，大小写不敏感。 — [[sources/http_service|http_service]]