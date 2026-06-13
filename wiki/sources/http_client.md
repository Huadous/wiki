---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/http_client.md]]"
tags: [HTTP/h2 客户端, Channel, HTTP Method, HTTP 版本控制, URL 与 Host 字段, HTTP Header 与 Query, HTTP 错误处理, HTTP 请求压缩, HTTP 响应解压, ProgressiveReader, HTTPS/SSL 客户端, butil::IOBuf, butil::IOBufBuilder, brpc::Controller, NamingService, chunked transfer encoding, HTTP Body]
aliases: ["brpc HTTP/H2 客户端指南", "brpc HTTP Client Guide"]
---

# brpc HTTP/H2 客户端使用指南 - Summary

## 来源
- Original file: [[brpc/http_client.md]]
- Ingested: 2026-06-13

## 核心内容
本文档是 [[entities/brpc|brpc]] 框架关于 [[concepts/httph2-客户端|HTTP/H2 客户端]] 使用的官方中文指南，配套示例代码位于 [[entities/examplehttp_c++|example/http_c++]]。文档说明了 brpc 中 HTTP 与 HTTP/2（统称 h2，含 h2/h2c）编程接口的统一性，详细介绍了通过 [[concepts/channel|brpc::Channel]] 创建协议通道（`ChannelOptions.protocol` 须指定为 PROTOCOL_HTTP 或 PROTOCOL_H2）、[[concepts/http-method|HTTP Method]]（默认 GET，可设置 POST 等）、[[concepts/http-版本控制|HTTP 版本控制]]（默认 1.1，可降级 1.0）、[[concepts/url-与-host-字段|URL 与 Host 字段]]的自动填充规则、[[concepts/http-header-与-query|HTTP Header 与 Query]] 的设置方法，以及 [[concepts/http-错误处理|HTTP 错误处理]]（非 2xx 时 ErrorCode 为 EHTTP）。文档还涵盖 [[concepts/http-请求压缩|request body 的 gzip 压缩]]（受阈值控制）、[[concepts/http-响应解压|response body 的手动解压]]、[[concepts/progressivereader|ProgressiveReader]] 持续下载能力（与 chunked mode 正交）、[[concepts/httpsssl-客户端|HTTPS/SSL 自动开启]]（https 前缀触发）以及 [[concepts/http-body|HTTP Body]] 的 [[concepts/butiliobuf|butil::IOBuf]] 与 [[concepts/butiliobufbuilder|butil::IOBufBuilder]] 处理方式，整体通过 [[concepts/brpccontroller|brpc::Controller]] 统一管理请求上下文，并通过 [[concepts/namingservice|NamingService]] 支持 BNS 等命名服务寻址。

## 关键实体
- [[entities/brpc|brpc]]
- [[entities/examplehttp_c++|example/http_c++]]

## 关键概念
- [[concepts/httph2-客户端|HTTP/h2 客户端]]
- [[concepts/channel|Channel]]
- [[concepts/http-method|HTTP Method]]
- [[concepts/http-版本控制|HTTP 版本控制]]
- [[concepts/url-与-host-字段|URL 与 Host 字段]]
- [[concepts/http-header-与-query|HTTP Header 与 Query]]
- [[concepts/http-错误处理|HTTP 错误处理]]
- [[concepts/http-请求压缩|HTTP 请求压缩]]
- [[concepts/http-响应解压|HTTP 响应解压]]
- [[concepts/progressivereader|ProgressiveReader]]
- [[concepts/httpsssl-客户端|HTTPS/SSL 客户端]]
- [[concepts/butiliobuf|butil::IOBuf]]
- [[concepts/butiliobufbuilder|butil::IOBufBuilder]]
- [[concepts/brpccontroller|brpc::Controller]]
- [[concepts/namingservice|NamingService]]
- [[concepts/chunked-transfer-encoding|chunked transfer encoding]]
- [[concepts/http-body|HTTP Body]]

## 要点
- brpc 将 HTTP 与 HTTP/2 统称为 h2 协议族（含加密 h2 与明文 h2c），编程接口基本一致，`ChannelOptions.protocol` 须指定 `PROTOCOL_HTTP` 或 `PROTOCOL_H2`
- `Channel::Init` 第一个参数可为任意合法 URL，但框架仅使用其中的 host 和 port；HTTP 代理或 BNS 多节点等场景下需通过 `cntl.http_request().uri()` 区分目标 URI
- GET 请求设置 uri() 后调用 `CallMethod`，POST 请求还需 `set_method(HTTP_METHOD_POST)` 并将数据写入 `request_attachment()`（类型为 butil::IOBuf）
- 默认 HTTP/1.1，可通过 `cntl.http_request().set_version(1, 0)` 降级到 HTTP/1.0；HTTP 版本设置对 H2 无效，H2 协议下的 version 字段会被自动设置为 (2, 0)
- Host 字段按规则自动填充：用户填写优先 > URL 含 host > Channel 域名为兜底 > 使用 server IP:port；H2 中对应 `:authority` 字段
- HTTP header field_name 不区分大小写（遵循 RFC 2616），相同 field_name 用逗号合并；query 用 `&` 分隔，value 可省略
- 非 2xx 响应视为失败，`ErrorCode` 为 `EHTTP`，可通过 `cntl->http_response().status_code()` 获取具体状态码；启用 `-use_http_error_code=true` 可在 brpc server 场景下获取真实错误码
- request body 通过 `set_request_compress_type(COMPRESS_TYPE_GZIP)` 压缩，小于 `-http_body_compress_threshold`（默认 512 字节）时不压缩
- response body 不自动解压，用户手动调用 `brpc::policy::GzipDecompress` 处理 `Content-Encoding: gzip`
- 超长或无限长 body 通过 ProgressiveReader 接口实现：`response_will_be_read_progressively()` + 实现 `OnReadOnePart`/`OnEndOfMessage` + `ReadProgressiveAttachmentBy()`，该能力与 HTTP chunked mode 正交
- HTTPS 通过 https 前缀 URI 自动开启 SSL，认证信息通过 HTTP `Authorization` header 传递 `auth_data`
- HTTP/H2 客户端支持 [[concepts/namingservice|NamingService]]（如 BNS）寻址，Channel.Init 传入命名服务名称，uri() 填入完整目标 URL
- `-http_verbose` 调试开关可输出所有 HTTP/H2 请求与响应细节，仅供线下调试使用