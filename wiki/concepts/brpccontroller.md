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
- [[entities/progressiveattachment|progressiveattachment]]
- [[entities/google-protobuf|Google Protobuf]]
- [[entities/streamid|StreamId]]
- [[entities/streamoptions|StreamOptions]]
- [[entities/streaminputhandler|StreamInputHandler]]
- [[entities/server-options|brpc::ServerOptions]]
- [[entities/json2pb|json2pb]]
- [[entities/inputmessenger|InputMessenger]]
- [[entities/eventdispatcher|EventDispatcher]]

## Mentions in Source
> **Source: en_http_service**
> - "Header of the http/h2 request is in Controller.http_request() and the body is in Controller.request_attachment()."
> - "Header of the http/h2 response is in Controller.http_response() and the body is in Controller.response_attachment()."
> - "brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);"

> **Source: en_http_service**
> - 该源文件未提供与Controller直接相关的新信息。

> **Source: streaming_rpc**
> - "Create a Stream at client-side along with the |cntl|, which will be connected when receiving the response with a Stream from server-side."
> - "Accept the Stream. If client didn't create a Stream with the request (cntl.has_remote_stream() returns false), this method would fail."
> - "过程中的任何错误都把RPC标记为失败，同时也意味着Stream创建失败。"
> - "No directly relevant information"

> **Source: server**
> - "在brpc中可以静态转为brpc::Controller（前提是代码运行brpc.Server中），包含了所有request和response之外的参数集合"
> - "调用Controller.SetFailed()可以把当前调用设置为失败"
> - "controller->remote_side()可获得发送该请求的client地址和端口，类型是butil::EndPoint。"
> - "controller->local_side()获得server端的地址，类型是butil::EndPoint。"
> - "No directly relevant information"

> **Source: json2pb**
> - "该特性默认为关闭状态，客户端在发送请求时，或服务端在发送回复时，可手动开启："
> - "brpc::Controller cntl;
cntl.set_pb_single_repeated_to_array(true);"
> - "No directly relevant information"

> **Source: io**
> - "像Controller贯穿了RPC的整个流程，和Socket中的数据有大量交互，它存放的是SocketUniquePtr。"
> - "存储SocketUniquePtr还是SocketId取决于是否需要强引用。"
> - "No directly relevant information"