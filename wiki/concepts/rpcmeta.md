---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/baidu_std|baidu_std]]"]
tags: [term]
aliases:
  - "RpcMeta 消息"
  - "RpcMeta message"
  - "RpcMeta"
---


# RpcMeta

## 定义
RpcMeta 是 baidu_std 协议中用于表示包元数据的 Protobuf 消息，定义了请求包和响应包的通用元数据结构。它通过域的存在性来区分请求与响应，并预留扩展字段以支持各实现的自定义扩展。

## 关键特征
- 包含 `request`、`response`、`compress_type`、`correlation_id`、`attachment_size`、`chunk_info`、`authentication_data` 等可选字段
- 请求包仅包含 `request` 域，响应包仅包含 `response` 域；实现可根据域的存在性区分请求包与响应包
- 通过分配的扩展字段序号支持各实现的自定义扩展，例如 100 分配给 Hulu、101 分配给 Sofa
- 作为 baidu_std 协议层的通用元数据容器，承载压缩类型、关联 ID、附件大小、分块信息以及认证数据等控制信息

## 应用
- 作为 baidu_std 协议下请求包与响应包的统一元数据载体
- 在 brpc 内部用于编码请求/响应控制信息（如 correlation_id 关联、compress_type 压缩协商、authentication_data 认证等）
- 为不同实现（如 Hulu、Sofa）通过预留的扩展字段序号挂载自定义元数据提供机制

## 相关概念
- [[concepts/RpcRequestMeta|RpcRequestMeta]]
- [[concepts/RpcResponseMeta|RpcResponseMeta]]
- [[concepts/元数据|元数据]]
- [[concepts/correlation_id|correlation_id]]

## 相关实体
- [[entities/baidu_std|baidu_std]]
- [[entities/Hulu|Hulu]]
- [[entities/Sofa|Sofa]]

## 来源提及
- ```
  message RpcMeta {
    optional RpcRequestMeta request = 1;
    optional RpcResponseMeta response = 2;
    optional int32 compress_type = 3;
    optional int64 correlation_id = 4;
    optional int32 attachment_size = 5;
    optional ChunkInfo chuck_info = 6;
    optional bytes authentication_data = 7;
  };
  ``` — [[brpc/baidu_std|baidu_std]]
- 请求包中只有request，响应包中只有response。实现可以根据域的存在性来区分请求包和响应包。 — [[brpc/baidu_std|baidu_std]]