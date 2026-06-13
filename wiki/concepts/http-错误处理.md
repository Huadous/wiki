---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_client]]"]
tags: [method]
aliases:
  - "HTTP Error Handling"
  - "brpc HTTP 错误处理"
  - "HTTP/H2 错误处理"
---


# HTTP 错误处理

## 定义
HTTP 错误处理是 brpc 框架中针对 HTTP/H2 协议访问失败的一组约定与机制：当 Server 返回的 HTTP status code 不是 2xx 时，brpc 客户端将此次访问视为失败，把 `cntl->ErrorCode()` 统一设置为 `EHTTP`，并允许用户通过 `cntl->http_response().status_code()` 获取具体的 HTTP 错误码。Server 端可将代表错误的 HTML 或 JSON 内容置入 `cntl->response_attachment()` 作为 body 返回，从而向客户端透出更丰富的错误信息。

## 关键特征
- **统一错误码**：当 HTTP/H2 响应状态码非 2xx 时，brpc 客户端默认将 `cntl->ErrorCode()` 设为 `EHTTP`，作为对所有 HTTP 类失败的统一标记。
- **原始状态码可读**：用户可通过 `cntl->http_response().status_code()` 取得具体的 HTTP 状态码（如 4xx/5xx），便于上层做更细粒度的错误分支处理。
- **Server 端可附带错误体**：Server 端可向 `cntl->response_attachment()` 写入 HTML、JSON 等结构作为错误响应体，便于客户端解析错误详情。
- **跨框架真实 ErrorCode 透出**：当 Server 同样是 brpc 框架实现的服务时，可通过设置 GFlag `-use_http_error_code=true`，让 client 在 HTTP/H2 失败时获取 Server 端返回的真实 `ErrorCode`，而非统一 `EHTTP`。
- **调试开关**：文档建议使用 `-http_verbose` 调试开关查看完整的 HTTP/H2 请求与响应，但仅用于线下调试，不建议在线上开启。

## 应用
- 在 brpc HTTP/H2 客户端中，通过判断 `cntl->Failed()` 与 `cntl->ErrorCode() == EHTTP` 来识别 HTTP 类访问失败。
- 当需要区分具体失败原因（如 404、500、502 等）时，结合 `cntl->http_response().status_code()` 做业务级错误处理。
- Server 端为 HTTP/H2 访问生成错误页面或错误 JSON 时，将内容写入 `cntl->response_attachment()`，配合非 2xx 状态码返回。
- 当 Server 与 Client 同为 brpc 时，开启 `-use_http_error_code=true`，将 Server 侧的真实错误码透出给 Client，便于在 RPC 语义下统一处理错误。
- 线下排查 HTTP/H2 请求问题时，临时打开 `-http_verbose` 以观察完整请求/响应内容。

## 相关概念
- [[concepts/http-h2-客户端|HTTP/h2 客户端]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "当Server返回的http status code不是2xx时，该次http/h2访问被视为失败，client端会把`cntl->ErrorCode()`设置为EHTTP，用户可通过`cntl->http_response().status_code()`获得具体的http错误。" — [[sources/http_client|http_client]]
- "如果Server也是brpc框架实现的服务，client端希望在http/h2失败时获取brpc Server返回的真实`ErrorCode`，而不是统一设置的`EHTTP`，则需要设置GFlag`-use_http_error_code=true`。" — [[sources/http_client|http_client]]