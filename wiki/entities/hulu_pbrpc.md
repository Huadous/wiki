---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "product"
aliases:
  - "hulu-pbrpc"
  - "hulu RPC协议"
  - "hulu_pbrpc协议"
  - "hulu-pbrpc"
  - "hulu RPC协议"
---

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
- "Protocol of hulu-pbrpc, shown as 'hulu_pbrpc', enabled by default."
- "Protocol of sofa-pbrpc, shown as 'sofa_pbrpc', enabled by default."
- "Server detects supported protocols automatically, without assignment from users."
- "baidu_std and hulu_pbrpc supports attachments which are sent along with messages and set by users to bypass serialization of protobuf."
- "Server is able to accept connections with different protocols from one port, users don't need to assign different ports for different protocols."

## Additional Information

hulu_pbrpc（亦称hulu-pbrpc或Hulu PBRPC协议）是Hulu公司开发的一套基于Protocol Buffers的RPC通信协议，被brpc框架原生支持（默认启用）。在brpc服务器中，该协议与[[concepts/baidu_std-protocol|baidu_std]]、HTTP、gRPC等协议共存于同一端口，由框架通过[[concepts/协议自动检测|协议自动检测]]机制自动识别协议类型。启用该协议无需额外配置，只需在ServerOptions中不关闭即可。brpc通过适配层将hulu_pbrpc消息转换为内部pb请求/响应，使得服务代码无需关心底层协议细节。

hulu_pbrpc与[[concepts/baidu_std-protocol|baidu_std]]协议类似，两者都支持[[concepts/附件|附件]]（attachment）功能，允许用户绕过protobuf序列化直接传输数据。不过，两者在内部编码细节上存在差异。

作为brpc默认支持的协议之一，hulu_pbrpc与[[concepts/sofa_pbrpc|sofa_pbrpc]]、[[concepts/nova_pbrpc|nova_pbrpc]]、[[concepts/public_pbrpc|public_pbrpc]]、[[concepts/nshead_mcpack|nshead_mcpack]]等相关协议共同构成了brpc的[[concepts/多协议支持|多协议支持]]体系。