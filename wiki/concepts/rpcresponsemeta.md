---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/baidu_std|baidu_std]]"]
tags: [term]
aliases:
  - "RpcResponseMeta"
  - "响应包元数据"
  - "RpcResponseMeta 消息"
---


# RpcResponseMeta

## 定义
RpcResponseMeta 是 baidu_std 协议中用于描述响应包元数据的 Protobuf 消息类型，包含 `error_code` 和 `error_text` 两个字段。当调用过程中出现任何异常时，错误信息会通过该消息返回给调用方。

## 关键特征
- Protobuf 消息定义：
  ```
  message RpcResponseMeta {
      optional int32 error_code = 1;
      optional string error_text = 2;
  };
  ```
- `error_code` 为 0 时表示正常返回；非 0 时表示发生错误，错误号的具体含义由应用方自行定义。
- `error_text` 提供错误的文本描述，便于调用方进行调试和问题定位。
- 响应包的元数据是对返回结果的描述；如果调用出现任何异常，错误信息也会放在该元数据中返回。
- 属于 baidu_std 协议规范中 RpcMeta 的组成成员之一，与 RpcRequestMeta 相对应。

## 应用
- 在 baidu_std 协议中作为响应包的元数据载体，传递调用结果的状态信息。
- 用于在 RPC 调用出错时，将服务端的错误码和错误文本回传给客户端。
- 供应用程序根据自定义的错误码进行业务逻辑处理和错误恢复。
- 在分布式服务通信中，作为统一的错误信息传递通道。

## 相关概念
- [[concepts/rpc-meta|RpcMeta]]
- [[concepts/rpc-request-meta|RpcRequestMeta]]
- [[concepts/元数据|元数据]]

## 相关实体
- [[sources/baidu_std|baidu_std]]

## 来源提及
- "响应包的元数据是对返回结果的描述。如果出现任何异常，错误也会放在元数据中。其Protobuf描述如下" — [[sources/baidu_std|baidu_std]]
- "message RpcResponseMeta { optional int32 error_code = 1; optional string error_text = 2; };" — [[sources/baidu_std|baidu_std]]
- "| error_code | 发生错误时的错误号，0表示正常，非0表示错误。具体含义由应用方自行定义。 |" — [[sources/baidu_std|baidu_std]]