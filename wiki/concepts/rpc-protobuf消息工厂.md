---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "method"
aliases:
  - "RPC Protobuf 消息工厂"
  - "RpcPBMessageFactory"
  - "自定义消息工厂"
  - "RPC PB Message Factory"
  - "RPC Protobuf 消息工厂"
  - "RpcPBMessageFactory"
  - "自定义消息工厂"
  - "RPC Protobuf message factory"
  - "RPC Protobuf 消息工厂"
  - "RpcPBMessageFactory"
  - "自定义消息工厂"
  - "RPC PB Message Factory"
  - "RPC Protobuf 消息工厂"
  - "RpcPBMessageFactory"
  - "自定义消息工厂"
---

## Description
RpcPBMessageFactory 是 brpc 框架中用于自定义 Protobuf 消息对象创建与销毁的核心工厂接口。服务器端默认使用 [[entities/defaultrpcpbmessagefactory|DefaultRpcPBMessageFactory]]，该实现是一个简单的工厂类，通过 `new` 操作符创建请求/响应消息，通过 `delete` 操作符销毁。开发者通过实现 `RpcPBMessages`（请求/响应消息的封装接口）和 `RpcPBMessageFactory`（工厂类）两个接口，可以完全接管消息生命周期管理，并将自定义工厂通过 `ServerOptions.rpc_pb_message_factory` 注入到服务器选项中。工厂的核心职责是管理 `RpcPBMessages` 实例，在 server 启动后 server 即拥有该工厂的所有权，在整个运行期间不可更改。最典型的自定义场景是启用 Protobuf Arena 分配器，通过 `brpc::GetArenaRpcPBMessageFactory()` 可一键式开启 Arena 内存池管理，从而在高并发 RPC 场景中减少内存碎片和拷贝开销。此特性目前存在协议限制，仅支持 `baidu_std` 和 HTTP 协议，其他协议如 hulu_pbrpc、sofa_pbrpc 等暂不适用。用户可通过该工厂集成 Protobuf Arena 或其他自定义内存池策略。

## Related Concepts
- [[concepts/protobuf-arena|Protobuf Arena]]
- [[concepts/事件驱动架构模式|事件驱动架构模式]]
- [[concepts/extension-declaration|扩展声明语法]]
- [[concepts/服务器生命周期管理|服务器生命周期管理]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/defaultrpcpbmessagefactory|DefaultRpcPBMessageFactory]]

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
> - "Implement `RpcPBMessages' (encapsulation of request/response message) and `RpcPBMessageFactory' (factory class) to customize the creation and destruction mechanism of protobuf message, and then set to `ServerOptions.rpc_pb_message_factory`."
> - "Users can set `ServerOptions.rpc_pb_message_factory = brpc::GetArenaRpcPBMessageFactory();` to manage Protobuf message memory."
> - "`DefaultRpcPBMessagesFactory' is used at server-side by default. It is a simple factory class that uses `new' to create request/response messages and `delete' to destroy request/response messages."
> - "Users can implement RpcPBMessages (encapsulation of request/response message) and RpcPBMessageFactory (factory class) to customize the creation and destruction mechanism of protobuf message, and then set to ServerOptions.rpc_pb_message_factory."
> - "Users can set ServerOptions.rpc_pb_message_factory = brpc::GetArenaRpcPBMessageFactory(); to manage Protobuf message memory."
> - "After the server is started, the server owns the RpcPBMessageFactory."

> **Source: [[sources/server|server]]**
> - "Server默认使用DefaultRpcPBMessageFactory。它是一个简单的工厂类，通过new来创建请求/响应message和delete来销毁请求/响应message。"
> - "如果用户希望自定义创建销毁机制，可以实现RpcPBMessages（请求/响应message的封装）和RpcPBMessageFactory（工厂类）"
> - "并设置ServerOptions.rpc_pb_message_factory为自定义的RpcPBMessageFactory。注意：server启动后，server拥有了RpcPBMessageFactory的所有权。"
> - "Factory to manage `RpcPBMessages'."