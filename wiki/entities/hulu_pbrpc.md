---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/baidu_std.md]]"
tags:
  - "product"
aliases:
  - "hulu-pbrpc"
  - "hulu RPC协议"
  - "hulu_pbrpc协议"
  - "hulu-pbrpc"
  - "hulu RPC协议"
  - "Hulu"
  - "hulu-pbrpc"
  - "hulu RPC协议"
  - "hulu_pbrpc协议"
  - "hulu-pbrpc"
  - "hulu RPC协议"
---

## Description

hulu_pbrpc（亦称 hulu-pbrpc 或 Hulu PBRPC 协议）是 Hulu 公司开发的一套基于 Protocol Buffers 的 RPC 通信协议，被 brpc 框架原生支持并默认启用。在 brpc 服务器中，该协议与 [[concepts/baidu_std-protocol|baidu_std]]、HTTP、gRPC 等协议共存于同一端口，由框架通过 [[concepts/协议自动检测|协议自动检测]]机制自动识别协议类型，用户无需为不同协议分配不同端口。启用该协议无需额外配置，只需在 ServerOptions 中不关闭即可；brpc 通过适配层将 hulu_pbrpc 消息转换为内部 pb 请求/响应，使得服务代码无需关心底层协议细节。

hulu_pbrpc 与 [[concepts/baidu_std-protocol|baidu_std]] 协议类似，两者都支持[[concepts/附件|附件]]（attachment）功能，允许用户绕过 protobuf 序列化直接传输数据。不过，两者在内部编码细节上存在差异。除作为独立协议被支持外，Hulu 还是 [[concepts/baidu_std-protocol|baidu_std]] 协议的扩展方之一：baidu_std 协议接口规范委员会为 Hulu 分配了序号 100，用于其在元数据中的专有扩展字段（例如在 RpcMeta、RpcRequestMeta 和 RpcResponseMeta 中分别添加 hulu_meta、hulu_request_meta 和 hulu_response_meta 等字段）。

作为 brpc 默认支持的协议之一，hulu_pbrpc 与 [[concepts/sofa_pbrpc|sofa_pbrpc]]、[[concepts/nova_pbrpc|nova_pbrpc]]、[[concepts/public_pbrpc|public_pbrpc]]、[[concepts/nshead_mcpack|nshead_mcpack]] 等相关协议共同构成了 brpc 的[[concepts/多协议支持|多协议支持]]体系。Hulu 在序号 100 上的扩展字段是 baidu_std 向后兼容机制的具体示例——其他不识别这些字段的 proto 实现会将其作为 Unknown 字段忽略，从而保证不同实现之间的互操作性。

## Related Entities
- [[sources/baidu_std|baidu_std]]（Hulu 作为扩展方参与其中的协议规范）
- [[sources/en_server|en_server]]（介绍 brpc Server 多协议支持的源文档）

## Related Concepts
- [[concepts/baidu_std-protocol|baidu_std]]（关联协议，Hulu 同时是其扩展方）
- [[concepts/sofa_pbrpc|sofa_pbrpc]]（同属 brpc 支持的协议）
- [[concepts/nova_pbrpc|nova_pbrpc]]（同属 brpc 支持的协议）
- [[concepts/public_pbrpc|public_pbrpc]]（同属 brpc 支持的协议）
- [[concepts/nshead_mcpack|nshead_mcpack]]（同属 brpc 支持的协议）
- [[concepts/多协议支持|多协议支持]]（hulu_pbrpc 所属的 brpc 协议体系）
- [[concepts/协议自动检测|协议自动检测]]（brpc Server 识别 hulu_pbrpc 的机制）
- [[concepts/附件|附件]]（hulu_pbrpc 支持的附件功能，attachment）
- [[concepts/rpc-meta|RpcMeta]]（Hulu 在 baidu_std 中扩展字段所在的元数据结构）

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
- "Protocol of hulu-pbrpc, shown as 'hulu_pbrpc', enabled by default."
- "Protocol of sofa-pbrpc, shown as 'sofa_pbrpc', enabled by default."
- "Server detects supported protocols automatically, without assignment from users."
- "baidu_std and hulu_pbrpc supports attachments which are sent along with messages and set by users to bypass serialization of protobuf."
- "Server is able to accept connections with different protocols from one port, users don't need to assign different ports for different protocols."

> **Source: [[sources/baidu_std|baidu_std]]**
- "以Hulu为例，被分配的序号为100。因此Hulu可以使用这样的proto定义："
- "因为只是将100这个序号保留给Hulu使用，因此Hulu可以自由决定是否添加这些字段，以及使用什么样的名字。其余实现使用的proto中不存在这些定义，会直接作为Unknown字段忽略。"
- "| 100  | Hulu |"