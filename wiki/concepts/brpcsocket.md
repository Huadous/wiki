---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/client|client]]"]
tags: [term]
aliases:
  - "Socket"
  - "brpc Socket"
---


# brpc::Socket

## 定义
brpc::Socket 是 brpc 中对底层 TCP/Unix socket 的封装抽象，作为统一短连接、连接池、单连接三种连接方式下的实际通信端点。它是 brpc 客户端发起请求时与对端进行数据收发的基本载体。

## 关键特征
- **连接方式统一抽象**：在客户端基本流程中，根据连接方式（单连接、连接池、短连接），从 [[concepts/SocketMap|SocketMap]] 或 [[concepts/LoadBalancer|LoadBalancer]] 选出的目的地选择一个 Socket 发送请求。
- **回调与错误处理**：Socket 上绑定 [[concepts/Channel-HandleSocketFailed|Channel::HandleSocketFailed]] 等回调以处理断连和写失败等错误。
- **引用计数管理生命周期**：通过引用计数管理生命周期，多个 [[entities/brpc-Channel|brpc::Channel]] 可能引用同一 Socket；最后一个引用释放时连接会被关闭（或被 [[concepts/defer-close-second|defer_close_second]] 延迟关闭）。
- **跨连接方式复用**：同一个 Socket 抽象同时服务于短连接、连接池和单连接三种模式，使得上层 [[entities/brpc-Channel|brpc::Channel]] 无需关心底层连接的具体形态。

## 应用
- **brpc 客户端通信**：作为 brpc 客户端中所有 RPC 请求的实际通信端点，统一短连接、连接池、单连接三种连接方式。
- **连接复用与共享**：在连接池和单连接模式下，多个 [[entities/brpc-Channel|brpc::Channel]] 可共享同一个 Socket，降低建连开销。
- **错误传播与资源回收**：通过回调机制把写失败、断连等错误事件传播到 [[entities/brpc-Channel|brpc::Channel]]，并依据引用计数在最后一个引用方析构时安全关闭或延迟关闭底层连接。

## 相关概念
- [[concepts/连接方式|连接方式]]
- [[concepts/SocketMap|SocketMap]]
- [[concepts/LoadBalancer|LoadBalancer]]
- [[concepts/延迟关闭连接|延迟关闭连接]]
- [[concepts/关闭连接池中的闲置连接|关闭连接池中的闲置连接]]
- [[concepts/Channel-HandleSocketFailed|Channel::HandleSocketFailed]]
- [[concepts/defer-close-second|defer_close_second]]

## 相关实体
- [[entities/brpc-Channel|brpc::Channel]]
- [[entities/brpc-LoadBalancer|brpc::LoadBalancer]]

## 来源提及
- "根据连接方式（单连接、连接池、短连接），选择一个[Socket](https://github.com/apache/brpc/blob/master/src/brpc/socket.h)。" — [[sources/client|client]]
- "多个channel可能通过引用计数引用同一个连接，当引用某个连接的最后一个channel析构时，该连接将被关闭。" — [[sources/client|client]]