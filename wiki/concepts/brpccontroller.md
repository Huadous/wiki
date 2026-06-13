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

## Related Concepts
- [[concepts/socket-management|Socket管理]]
- [[concepts/socketuniqueptr|SocketUniquePtr]]
- [[concepts/socketid|SocketId]]
- [[concepts/http-parameters|HTTP参数]]
- [[concepts/progressive-attachment|ProgressiveAttachment]]
- [[concepts/progressivereader|ProgressiveReader]]
- [[concepts/http-h2-service|HTTP/h2服务]]
- [[concepts/bthread|bthread]]
- [[concepts/race-condition|竞态条件]]
- [[concepts/aba-problem|ABA问题]]
- [[concepts/uri|URI]]
- [[concepts/query-string|Query String]]
- [[concepts/status-code|Status Code]]
- [[concepts/gzip-compression|gzip压缩]]
- [[concepts/streaming-rpc|Streaming RPC]]
- [[concepts/streamcreate|StreamCreate]]
- [[concepts/streamaccept|StreamAccept]]
- [[concepts/baidu-std|baidu_std协议]]
- [[concepts/authcontext|AuthContext]]
- [[concepts/最大消息限制|最大消息限制]]
- [[concepts/serveroptions|brpc::ServerOptions]]
- [[concepts/json-protobuf-conversion|JSON-protobuf转换规则]]
- [[concepts/repeated-field-json-encoding|repeated字段JSON编码]]
- [[concepts/pb2jsonoptions|Pb2JsonOptions]]
- [[concepts/channel|Channel]]
- [[concepts/butil-iobuf|butil::IOBuf]]
- [[concepts/http-method|HTTP Method]]
- [[concepts/http-header-query|HTTP Header 与 Query]]
- [[concepts/http-version-control|HTTP 版本控制]]
- [[concepts/http-request-compression|HTTP 请求压缩]]
- [[concepts/channel-options|ChannelOptions]] *(newly implied by en_client: ChannelOptions 决定 Channel 级默认值，Controller 在单次 RPC 中覆盖)*
- [[concepts/retry|Retry]] *(newly linked from en_client)*
- [[concepts/timeout|Timeout]] *(newly linked from en_client)*
- [[concepts/authentication|Authentication]] *(newly linked from en_client)*
- [[concepts/compression|Compression]] *(newly linked from en_client)*

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/brpc-server|brpc::Server]]
- [[entities/controller|brpc::Controller]]
- [[entities/iobuf|iobuf]]
- [[entities/datafactory|datafactory]]
- [[entities/certinfo|certinfo]]
- [[entities/nginx|nginx]]
- [[entities/closurguard|ClosureGuard]]
- [[entities/authcontext|AuthContext]]
- [[entities/socket|Socket]]
- [[entities/socketuniqueptr|SocketUniquePtr]]
- [[entities/bthread|bthread]]
- [[entities/progressiveattachment|ProgressiveAttachment]]
- [[entities/progressivereader|ProgressiveReader]]
- [[entities/google-protobuf|Google Protobuf]]
- [[entities/streamid|StreamId]]
- [[entities/streamoptions|StreamOptions]]
- [[entities/streaminputhandler|StreamInputHandler]]
- [[entities/server-options|brpc::ServerOptions]]
- [[entities/json2pb|json2pb]]
- [[entities/inputmessenger|InputMessenger]]
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/channel|brpc::Channel]]
- [[entities/done|done]] *(newly implied by en_client: Controller 在异步 done->Run() 中删除)*

## Mentions in Source
> **Source: [[sources/en_http_service|en_http_service]]**
> - "Header of the http/h2 request is in Controller.http_request() and the body is in Controller.request_attachment()."
> - "Header of the http/h2 response is in Controller.http_response() and the body is in Controller.response_attachment()."
> - "brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);"

> **Source: [[sources/en_http_service|en_http_service]]**
> - 该源文件未提供与Controller直接相关的新信息。

> **Source: [[sources/streaming_rpc|streaming_rpc]]**
> - "Create a Stream at client-side along with the |cntl|, which will be connected when receiving the response with a Stream from server-side."
> - "Accept the Stream. If client didn't create a Stream with the request (cntl.has_remote_stream() returns false), this method would fail."
> - "过程中的任何错误都把RPC标记为失败，同时也意味着Stream创建失败。"
> - "No directly relevant information"

> **Source: [[sources/server|server]]**
> - "在brpc中可以静态转为brpc::Controller（前提是代码运行brpc.Server中），包含了所有request和response之外的参数集合"
> - "调用Controller.SetFailed()可以把当前调用设置为失败"
> - "controller->remote_side()可获得发送该请求的client地址和端口，类型是butil::EndPoint。"
> - "controller->local_side()获得server端的地址，类型是butil::EndPoint。"
> - "No directly relevant information"

> **Source: [[sources/json2pb|json2pb]]**
> - "该特性默认为关闭状态，客户端在发送请求时，或服务端在发送回复时，可手动开启："
> - "brpc::Controller cntl;
cntl.set_pb_single_repeated_to_array(true);"
> - "No directly relevant information"

> **Source: [[sources/io|io]]**
> - "像Controller贯穿了RPC的整个流程，和Socket中的数据有大量交互，它存放的是SocketUniquePtr。"
> - "存储SocketUniquePtr还是SocketId取决于是否需要强引用。"
> - "No directly relevant information"

> **Source: [[sources/http_client|http_client]]**
> - "brpc::Controller cntl;
cntl.http_request().uri() = "www.baidu.com/index.html";  // 设置为待访问的URL
channel.CallMethod(NULL, &cntl, NULL, NULL, NULL/*done*/);"
> - "HTTP/h2和protobuf关系不大，所以除了Controller和done，CallMethod的其他参数均为NULL。如果要异步操作，最后一个参数传入done。"
> - "No directly relevant information"

> **Source: [[sources/en_client|en_client]]**
> - "brpc::Controller: defined in src/brpc/controller.h, for overriding fields in brpc::ChannelOptions for some RPC according to contexts."
> - "A Controller corresponds to a RPC. A Controller can be re-used by another RPC after Reset(), but a Controller can't be used by multiple RPC simultaneously"
> - "Related concepts: Channel, Retry, Timeout, Authentication, Compression"
> - "Summary: Controller 是 brpc 客户端每次 RPC 的控制对象，定义了请求级选项（如 timeout_ms、max_retry、backup_request_ms、request_compress_type、log_id 等），并承载响应结果与错误信息。Controller 与 ChannelOptions 的关系是：ChannelOptions 决定 Channel 级默认值，Controller 可在单次 RPC 中覆盖。一个 Controller 同时只能被一个 RPC 使用，不可在多线程间共享；异步调用时 Controller 必须放在堆上并在 done->Run() 中删除，同步调用则可放栈上。文档还提供了 remote_side()、local_side()、Reset()、Failed()、response()、request_attachment() 等关键 API 的使用说明。"
> - "No directly relevant information"