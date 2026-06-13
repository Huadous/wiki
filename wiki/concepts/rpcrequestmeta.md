---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/baidu_std.md]]"]
tags: [term]
aliases:
  - "RpcRequestMeta 消息"
  - "请求包元数据消息"
---


# RpcRequestMeta

## 定义
RpcRequestMeta 是 baidu_std 协议中用于描述请求包元数据的 Protobuf 消息。该消息在请求包中唯一标识了需要调用的 RPC 方法，包含 `service_name`、`method_name` 和 `log_id` 三个字段。

## 关键特征
- 字段 `service_name`（必填）：标识要调用的 RPC 服务名。
- 字段 `method_name`（必填）：标识要调用的 RPC 方法名。
- 字段 `log_id`（可选，int64）：用于日志打印，可用于存放 BFE_LOGID。
- `service_name` 与 `method_name` 为必填字段，组合起来唯一确定一次 RPC 调用目标。
- `log_id` 为可选字段，便于请求链路追踪与日志关联。

## 应用
- 在 baidu_std 协议的请求包中描述并唯一标识需要调用的 RPC 方法。
- 配合 [[concepts/RpcMeta|RpcMeta]] 在请求包整体结构中提供方法路由信息。
- 通过 `log_id` 字段承载 BFE_LOGID 等日志标识，用于请求日志的关联与排查。
- 与 [[concepts/RpcResponseMeta|RpcResponseMeta]] 配合，分别描述请求侧与响应侧的元数据。

## 相关概念
- [[concepts/RpcMeta]]
- [[concepts/RpcResponseMeta]]
- [[concepts/元数据]]

## 相关实体
- [[entities/baidu_std]]

## 来源提及
- 请求包的元数据主要描述了需要调用的RPC方法信息，Protobuf如下 — [[brpc/baidu_std|baidu_std]]
- message RpcRequestMeta { required string service_name = 1; required string method_name = 2; optional int64 log_id = 3; }; — [[brpc/baidu_std|baidu_std]]
- | service_name | 服务名，约束见上文 | — [[brpc/baidu_std|baidu_std]]
- | method_name  | 方法名，约束见上文 | — [[brpc/baidu_std|baidu_std]]