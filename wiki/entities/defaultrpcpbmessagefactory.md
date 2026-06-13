---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/server|server]]"]
tags: [other]
aliases:
  - "Default RpcPBMessageFactory"
  - "默认 RpcPBMessageFactory"
---


# DefaultRpcPBMessageFactory

## 基本信息
- Type: other
- Source: [[sources/server|server]]

## 描述
DefaultRpcPBMessageFactory 是 [[entities/brpc|brpc]] Server 端默认的 RpcPBMessageFactory 实现。它是一个简单的工厂类，通过 C++ 的 `new` 操作符创建请求和响应 message，通过 `delete` 操作符销毁请求和响应 message。该工厂适用于基础的 RPC 场景，使用 protobuf 默认的堆内存分配方式来管理 message 生命周期。

用户可以根据自身需求实现自定义的 RpcPBMessages 和 RpcPBMessageFactory，并通过 `ServerOptions.rpc_pb_message_factory` 字段进行替换，以适配特殊的内存管理策略。此外，若希望启用更高效的内存管理方式，用户可以调用 `brpc::GetArenaRpcPBMessageFactory()` 获取基于 protobuf arena 的工厂实例，从而使用 arena 来管理 message 内存，提升性能并减少内存碎片。

## 相关实体
- [[entities/brpc|brpc]]

## 相关概念
- [[concepts/protobuf-arena|protobuf arena]]
- [[concepts/rpc-protobuf-message-factory|RPC Protobuf message factory]]

## 来源提及
- Server默认使用`DefaultRpcPBMessageFactory`。它是一个简单的工厂类，通过`new`来创建请求/响应message和`delete`来销毁请求/响应message。 — [[sources/server|server]]