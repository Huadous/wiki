---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_client]]"]
tags: [term]
aliases:
  - "HTTP 请求方法"
  - "HTTP Request Method"
  - "GET/POST"
---


# HTTP Method

## 定义
HTTP Method 指 HTTP 协议定义的请求动作类型，用于表明客户端希望服务器对资源执行何种操作。在 brpc 客户端中，HTTP Method 是 [[sources/http_client|http_client]] 构造请求时必须明确指定的核心属性之一。

## 关键特征
- **默认方法为 GET**：brpc 客户端在不显式设置时，默认使用 GET 方法发起请求。
- **可显式设置**：通过 `cntl.http_request().set_method()` 可将请求方法改为 POST，或其他在 [http_method.h](https://github.com/apache/brpc/blob/master/src/brpc/http_method.h) 中定义的更多方法。
- **GET 请求无需 body**：由于 GET 语义上不应携带请求体，调用方无需填充请求内容。
- **POST 请求需填充 body**：待 POST 的数据应置入 `request_attachment()`，其类型为 [butil::IOBuf](https://github.com/apache/brpc/blob/master/src/butil/iobuf.h)，可直接 `append` `std::string` 或 `char*`。
- **大输出推荐 IOBufBuilder**：对于大量打印输出的场景，推荐使用 `butil::IOBufBuilder` 构造 body，其用法类似 `std::ostringstream`。

## 应用
- 在 brpc HTTP/H2 客户端中切换 GET / POST 等不同语义请求。
- 通过 POST 携带序列化后的请求体（如 JSON、表单数据、二进制负载），配合服务端处理。
- 在批量调试或压测场景中，利用 `IOBufBuilder` 高效拼接大体积请求体。

## 相关概念
- [[concepts/http-h2-client|HTTP/h2 客户端]]
- [[concepts/http-header-query|HTTP Header 与 Query]]

## 相关实体
- [[entities/examplehttp_c++]]

## 来源提及
- 默认的HTTP Method为GET，可设置为POST或[更多http method](https://github.com/apache/brpc/blob/master/src/brpc/http_method.h)。 — [[sources/http_client|http_client]]
- 待POST的数据应置入request_attachment()，它([butil::IOBuf](https://github.com/apache/brpc/blob/master/src/butil/iobuf.h))可以直接append std::string或char*。 — [[sources/http_client|http_client]]