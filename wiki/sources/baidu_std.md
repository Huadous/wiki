---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/baidu_std.md]]"
tags: [RPC, Protobuf, 包头, 元数据, RpcMeta, RpcRequestMeta, RpcResponseMeta, 附件, 压缩算法, HTTP接口, PRPC, Snappy, RESTful, Chunk模式, TCP, 服务, 包, JSON]
aliases: ["baidu_std协议规范", "baidu_std Protocol Specification"]
---

# baidu_std协议规范 - Summary

## 来源
- Original file: [[brpc/baidu_std.md]]
- Ingested: 2026-06-13

## 核心内容
本文档详细描述了 [[entities/baidu_std|baidu_std]] 协议的技术规范。baidu_std 是一种基于 [[concepts/tcp|TCP]] 协议的二进制 [[concepts/rpc|RPC]] 通信协议，使用 [[concepts/protobuf|Protobuf]] 作为基本数据交换格式，不考虑跨 TCP 连接的情况。其包结构由固定 12 字节的 [[concepts/包头|包头]]（包含 PRPC 标识、包体长度和元数据长度）和由 [[concepts/元数据|元数据]]、[[concepts/包|数据]]以及[[concepts/附件|附件]]三部分组成的包体构成。文档详细说明了 [[concepts/rpcmeta|RpcMeta]]、[[concepts/rpcrequestmeta|RpcRequestMeta]] 和 [[concepts/rpcresponsemeta|RpcResponseMeta]] 三个核心 Protobuf 消息的定义，并提供了服务命名（UpperCamelCase）和方法命名的约束规则。协议支持 [[concepts/snappy|Snappy]] 和 [[entities/gzip|gzip]] 两种[[concepts/压缩算法|压缩算法]]，并允许通过附件机制高效传输二进制数据。同时规定了基于标准 [[concepts/http接口|HTTP接口]] 的接口规范，默认使用 [[concepts/json|JSON]] 格式和 UTF-8 编码，建议采用 [[concepts/restful|RESTful]] 形式。元数据扩展通过分配专用序号实现，目前 [[entities/hulu|Hulu]] 使用序号 100，[[entities/sofa|Sofa]] 使用序号 101。

## 关键实体
- [[entities/baidu_std|baidu_std]]：本文档的核心主题，基于 TCP 的二进制 RPC 通信协议
- [[entities/hulu|Hulu]]：已分配元数据扩展字段序号 100
- [[entities/sofa|Sofa]]：已分配元数据扩展字段序号 101
- [[entities/chunkinfo|ChunkInfo]]：用于描述分块传输相关信息的 Protobuf 消息
- [[entities/gzip|gzip]]：baidu_std 协议支持的压缩算法之一

## 关键概念
- [[concepts/rpc|RPC]]：baidu_std 协议的核心通信范式
- [[concepts/protobuf|Protobuf]]：baidu_std 协议使用的基本数据交换格式
- [[concepts/包|包]]：baidu_std 的基本数据交换单位
- [[concepts/包头|包头]]：包结构中固定 12 字节的部分
- [[concepts/元数据|元数据]]：包体中用于描述请求/响应的部分
- [[concepts/rpcmeta|RpcMeta]]：表示包元数据的 Protobuf 消息
- [[concepts/rpcrequestmeta|RpcRequestMeta]]：描述请求包元数据的 Protobuf 消息
- [[concepts/rpcresponsemeta|RpcResponseMeta]]：描述响应包元数据的 Protobuf 消息
- [[concepts/附件|附件]]：用于高效传输二进制数据的机制
- [[concepts/压缩算法|压缩算法]]：用于压缩消息包数据部分的机制
- [[concepts/snappy|Snappy]]：baidu_std 协议支持的压缩算法之一
- [[concepts/http接口|HTTP接口]]：baidu_std 协议规定的对外服务发布方式之一
- [[concepts/json|JSON]]：HTTP 接口的默认数据交换格式
- [[concepts/restful|RESTful]]：HTTP 接口规范中推荐使用的 Web Service 形式
- [[concepts/prpc|PRPC]]：baidu_std 协议的协议标识符
- [[concepts/tcp|TCP]]：baidu_std 协议使用的底层传输协议
- [[concepts/服务|服务]]：通过 IP 地址端口发布的 RPC 服务单元
- [[concepts/chunk模式|Chunk模式]]：用于处理大块数据传输的方法

## 要点
- baidu_std 是基于 TCP 协议的二进制 RPC 通信协议，以 Protobuf 作为基本数据交换格式，不考虑跨 TCP 连接的情况
- 协议包由 12 字节固定包头（含 PRPC 标识、包体长度、元数据长度）和包体（包含元数据、数据、附件三部分）组成
- RPC 方法由 IP 地址、端口、服务名、方法名构成的四元组唯一标识，服务名采用 UpperCamelCase 命名
- 核心元数据结构包括 RpcMeta、RpcRequestMeta（含 service_name 和 method_name 等字段）和 RpcResponseMeta（含 error_code 和 error_text）
- 协议支持三种压缩模式：值为 0 不压缩、值为 1 使用 Snappy、值为 2 使用 gzip
- 提供附件机制以高效传输二进制数据，附件放在包体末尾，其大小记录在 RpcMeta 的 attachment_size 字段中
- 元数据扩展通过分配专用序号实现，当前 Hulu 使用序号 100、Sofa 使用序号 101，其他实现会忽略未知的扩展字段
- 协议同时定义了 TCP 和 HTTP 两种接口形式，HTTP 接口默认使用 JSON 格式和 UTF-8 编码，并建议采用 RESTful 风格