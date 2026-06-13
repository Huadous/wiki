---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[sources/en_io]]"
  - "[[sources/en_http_service]]"
  - "[[brpc/streaming_rpc.md]]"
  - "[[brpc/server.md]]"
  - "[[brpc/json2pb.md]]"
  - "[[brpc/io.md]]"
  - "[[brpc/http_client.md]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/client.md]]"
tags:
  - "term"
aliases:
  - "Controller"
  - "RPC Controller"
  - "brpc控制器"
  - "brpc::Controller"
  - "Controller"
  - "RPC Controller"
  - "brpc控制器"
  - "remote_side"
  - "Controller"
  - "RPC Controller"
  - "brpc控制器"
  - "brpc::Controller"
  - "Controller"
  - "RPC Controller"
  - "brpc控制器"
---

## Description
brpc::Controller 是 brpc 客户端每次 RPC 的控制对象，与 [[concepts/channel-options|brpc::ChannelOptions]]（影响整个 Channel 上的所有 RPC）和全局 gflags（控制底层行为）共同构成 Client 端的三层配置体系。其核心职责是在单次 RPC 中根据上下文覆盖 Channel 级的默认选项，因此 timeout_ms、max_retry、backup_request_ms、request_compress_type、log_id 等频繁变化的参数都放在 Controller 上。Controller 同时承载响应数据、错误码、远端/本地地址等运行时信息，可通过 `response()`、`Failed()`、`remote_side()`、`local_side()`、`ErrorCode()` 等方法获取。

Controller 的生命周期约束严格：它不能被多个 RPC 同时使用，即使发起自同一线程也不行；通过 `Reset()` 可以将其复用于另一次 RPC。在 [[concepts/asynchronous-access|异步访问]] 场景下，Controller 通常在堆上分配，并在 `done->Run()` 回调中被删除；同步调用则可放栈上。r31384 之后，`local_side()` 可在 RPC 结束后获得发起 RPC 的地址和端口（类型为 butil::EndPoint），`remote_side()` 类似地获得对端地址。Controller 内部存放 [[entities/socketuniqueptr|SocketUniquePtr]]（或 [[concepts/socketid|SocketId]]，取决于是否需要强引用），与 [[concepts/socket-management|Socket]] 中的数据有大量交互，贯穿了 RPC 的整个流程。

在 HTTP/h2 场景下，Controller 还承担 HTTP 语义：请求头位于 `Controller.http_request()`，请求体位于 `Controller.request_attachment()`；响应头位于 `Controller.http_response()`，响应体位于 `Controller.response_attachment()`。[[concepts/streaming-rpc|Streaming RPC]] 中，Controller 是创建和接受 Stream 的载体，过程中的任何错误都会把 RPC 标记为失败并导致 Stream 创建失败。