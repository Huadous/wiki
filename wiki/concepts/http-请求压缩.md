---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_client]]"]
tags: [method]
aliases:
  - "request body 压缩"
  - "gzip 压缩"
  - "HTTP request body compression"
---


# HTTP 请求压缩

## 定义
HTTP 请求压缩是 brpc 客户端提供的一种 HTTP request body 压缩机制。用户可调用 `Controller::set_request_compress_type(brpc::COMPRESS_TYPE_GZIP)` 尝试使用 gzip 算法压缩 HTTP 请求体。该机制会根据请求体大小自动决定是否真正执行压缩，以在传输节省与压缩开销之间取得平衡。

## 关键特征
- 通过 `Controller::set_request_compress_type(brpc::COMPRESS_TYPE_GZIP)` 显式声明希望使用 gzip 压缩
- 压缩"尝试"语义：压缩不一定实际发生，受阈值条件约束
- 阈值由 `-http_body_compress_threshold` 参数控制，默认 512 字节
- 当 body 尺寸小于阈值时，框架跳过压缩以避免小 body 场景下压缩延时超过网络传输节省
- 该设计源于 gzip 本身并非高性能压缩算法，对小数据压缩开销可能反而成为负担

## 应用
- brpc HTTP/H2 客户端中发送较大 JSON、protobuf 序列化结果等请求体时，启用 gzip 压缩以减少网络带宽占用
- 跨机房、跨地域等高延迟网络环境下，对大体积请求体进行压缩以缩短传输时间
- 与 [[concepts/http-响应解压|HTTP 响应解压]] 配合，构建完整的请求/响应压缩通道
- 用于 [[concepts/http-h2-客户端|HTTP/h2 客户端]] 场景下的传输性能调优

## 相关概念
- [[concepts/http-响应解压]]
- [[concepts/http-h2-客户端]]

## 相关实体
- 无

## 来源提及
- "调用Controller::set_request_compress_type(brpc::COMPRESS_TYPE_GZIP)将尝试用gzip压缩http body。" — [[sources/http_client|http_client]]
- ""尝试"指的是压缩有可能不发生，条件有：" — [[sources/http_client|http_client]]
- "body尺寸小于-http_body_compress_threshold指定的字节数，默认是512。这是因为gzip并不是一个很快的压缩算法，当body较小时，压缩增加的延时可能比网络传输省下的还多。" — [[sources/http_client|http_client]]