---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_client|http_client]]"]
tags: [term]
aliases:
  - "HTTP 请求体"
  - "HTTP 响应体"
  - "request body"
  - "response body"
---


# HTTP Body

## 定义
HTTP Body 是 HTTP 请求和响应消息中用于承载实际业务数据的部分，位于 HTTP 头部（headers）之后。在 brpc 框架中，HTTP body 一律以 [[concepts/butil-iobuf|butil::IOBuf]] 形式进行存储与处理，并通过 [[concepts/brpc-controller|brpc::Controller]] 提供的接口进行读写。

## 关键特征
- **统一 IOBuf 表示**：在 brpc 中，HTTP body 始终以 [[concepts/butil-iobuf|butil::IOBuf]] 形式呈现，避免了反复的内存拷贝。
- **Client 端写入**：通过 `cntl.request_attachment()` 写入请求 body，支持 append `std::string` / `char*`，也可使用 [[concepts/butil-iobufbuilder|butil::IOBufBuilder]] 构造后 `move_to` 转入。
- **Client 端读取**：响应 body 通过 `cntl.response_attachment()` 读取。
- **压缩控制**：调用 `cntl.set_request_compress_type(brpc::COMPRESS_TYPE_GZIP)` 将尝试用 gzip 压缩 HTTP body，压缩阈值受 `-http_body_compress_threshold` 参数控制。
- **解压责任**：gzip 解压由用户自行调用 `brpc::policy::GzipDecompress` 完成，框架不自动解压响应 body。
- **渐进式读取**：对超长 body，brpc 提供 [[concepts/progressivereader|ProgressiveReader]] 策略以避免一次性分配大块内存。
- **Server 端错误响应**：Server 端可通过 `cntl.response_attachment()` 把代表错误的 HTML 或 JSON 作为 HTTP body 返回给客户端。
- **流式编码兼容**：body 可结合 [[concepts/chunked-transfer-encoding|chunked transfer encoding]] 进行分块传输。

## 应用
- 客户端构造 JSON / protobuf / 任意二进制负载并作为请求 body 发送。
- 客户端解析响应 body 以提取服务器返回的数据或错误信息。
- 对大请求体启用 gzip 压缩以节省网络带宽（受阈值开关控制）。
- 处理超长 body（上传文件、流式响应）时使用 [[concepts/progressivereader|ProgressiveReader]] 渐进式读取。
- Server 端在业务失败时返回错误页 HTML 或结构化错误 JSON 作为 body。

## 相关概念
- [[concepts/butil-iobuf|butil::IOBuf]]
- [[concepts/butil-iobufbuilder|butil::IOBufBuilder]]
- [[concepts/brpc-controller|brpc::Controller]]
- [[concepts/http-请求压缩|HTTP 请求压缩]]
- [[concepts/http-响应解压|HTTP 响应解压]]
- [[concepts/progressivereader|ProgressiveReader]]
- [[concepts/chunked-transfer-encoding|chunked transfer encoding]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "调用Controller::set_request_compress_type(brpc::COMPRESS_TYPE_GZIP)将尝试用gzip压缩http body。" — [[sources/http_client|http_client]]
- "访问body
butil::IOBuf& buf = cntl->request_attachment();
std::string str = cntl->request_attachment().to_string(); // 有拷贝" — [[sources/http_client|http_client]]
- "同时server端可以把代表错误的html或json置入`cntl->response_attachment()`作为http body传递回来。" — [[sources/http_client|http_client]]