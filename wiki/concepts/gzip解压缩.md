---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_http_service]]"
  - "[[brpc/http_service.md]]"
tags:
  - "method"
aliases:
  - "Gzip decompress"
  - "解压缩请求体"
  - "brpc Gzip解压缩"
  - "GzipDecompress"
  - "Gzip decompress"
  - "解压缩请求体"
  - "brpc Gzip解压缩"
  - "request body解压"
  - "Gzip decompress"
  - "解压缩请求体"
  - "brpc Gzip解压缩"
  - "GzipDecompress"
  - "Gzip decompress"
  - "解压缩请求体"
  - "brpc Gzip解压缩"
---

## Description
Gzip解压缩是 brpc 框架中处理 HTTP 请求体 gzip 压缩数据的关键方法，位于 `brpc/policy/gzip_compress.h` 头文件中。与 brpc 自动处理的 gzip 响应压缩不同，请求解压缩需要开发者主动调用相关函数，因为 brpc 为了保持框架的通用性并且解压代码并不复杂，而选择不自动解压 request body。开发人员首先需要检查 HTTP 请求头中的 `Content-Encoding` 字段值是否为 `'gzip'`（通过 `cntl->http_request().GetHeader("Content-Encoding")`），如果匹配则调用 `brpc::policy::GzipDecompress` 函数，将请求体（`cntl->request_attachment()`）传入并接收解压后的 `butil::IOBuf`。解压缩后的数据通过 `std::swap` 操作替换原始请求体，从而避免不必要的数据拷贝，此时 `cntl->request_attachment()` 中已经是解压后的明文数据。该函数常用于处理来自外部客户端的 gzip 压缩请求数据，与 brpc 的 Gzip 压缩机制配合使用。

## Related Concepts
- [[concepts/gzip响应体压缩|gzip响应体压缩]] — 与请求体解压对应的响应压缩机制，由系统根据阈值和客户端 Accept-encoding 自动处理
- [[concepts/Content-Encoding|Content-Encoding]] — HTTP 协议中用于标识实体内容编码的头字段
- [[concepts/HTTP头部|HTTP头部]] — HTTP 协议中用于传递元数据的字段，Content-Encoding 是其中之一
- [[concepts/IOBuf|IOBuf]] — brpc 中使用的缓冲数据结构，用于高效地处理 I/O 操作中的数据
- [[concepts/Content-Type|Content-Type]] — HTTP 协议中标识实体内容类型的头字段

## Related Entities
- [[entities/brpc|brpc]] — 百度开源的 RPC 框架，提供了 `GzipDecompress` 方法用于手动解压 gzip 压缩的请求体

## Mentions in Source

> **Source: [[sources/en_http_service|en_http_service]]**
> - "Due to generality, brpc does not decompress request bodies automatically, but users can do the job by themselves as follows:" —（由于通用性考虑，brpc 不会自动解压缩请求体，但用户可以自行完成这一工作）
> - `#include <brpc/policy/gzip_compress.h>` — 包含 gzip 压缩/解压缩功能的头文件
> - `if (!brpc::policy::GzipDecompress(cntl->request_attachment(), &uncompressed)) {` — 调用 GzipDecompress 函数解压请求体
> - `const std::string* encoding = cntl->http_request().GetHeader("Content-Encoding"); if (encoding != NULL && *encoding == "gzip") {` — 检测请求头中的 Content-Encoding 字段是否为 'gzip'

> **Source: [[sources/http_service|http_service]]**
> - "出于通用性考虑且解压代码不复杂，brpc不会自动解压request body，用户可以自己做，方法如下" — 说明 brpc 出于通用性和代码复杂度考虑不自动解压请求体
> - `#include <brpc/policy/gzip_compress.h>` — 包含 gzip 压缩/解压缩功能的头文件
> - `const std::string* encoding = cntl->http_request().GetHeader("Content-Encoding");` — 获取 HTTP 请求头中的 Content-Encoding 字段
> - `// cntl->request_attachment()中已经是解压后的数据了` — 注释说明 swap 替换后 request_attachment 中已是明文数据