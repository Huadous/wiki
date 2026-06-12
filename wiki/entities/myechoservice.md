---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_server]]"]
tags: [other]
aliases:
  - "MyEchoService 类"
  - "Echo 服务实现"
---


# MyEchoService

## 基本信息
- Type: other
- Source: [[sources/en_server|en_server]]

## 描述
MyEchoService 是 brpc 示例中用户实现的服务类，继承自 `EchoService`（由 Protocol Buffers 生成）。在它的 `Echo` 方法中，它将请求中的消息原样设置到响应中，并使用 `ClosureGuard` 自动调用 done 回调。该类展示了如何在 brpc 中实现同步服务：通过 `brpc::ClosureGuard done_guard(done);` 确保回调被正确调用，并填充响应消息。MyEchoService 是 brpc 服务端编程的基础示例，演示了 [[entities/brpc|brpc]] 服务端请求处理的基本流程。该类的实现方式体现了 brpc 框架中 [[concepts/baidu_std-protocol|baidu_std-protocol]] 的标准服务定义模式。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/echoservice|EchoService]]

## 相关概念
- [[concepts/baidu_std-protocol|baidu_std-protocol]]
- [[concepts/stream|Stream]]

## 来源提及
- "class MyEchoService : public EchoService {" — [[sources/en_server|en_server]]
- "MyEchoService my_echo_service;" — [[sources/en_server|en_server]]
- "void Echo(::google::protobuf::RpcController* cntl_base, const ::example::EchoRequest* request, ::example::EchoResponse* response, ::google::protobuf::Closure* done) {" — [[sources/en_server|en_server]]