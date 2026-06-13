---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_streaming_rpc]]"
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
  - "[[brpc/streaming_rpc.md]]"
  - "[[brpc/server.md]]"
  - "[[brpc/en_client.md]]"
tags:
  - "standard"
aliases:
  - "baidu_std"
  - "百度标准协议"
  - "baidu_std协议"
  - "baidu_std"
  - "百度标准协议"
  - "Baidu Standard Protocol"
  - "baidu_std"
  - "百度标准协议"
  - "baidu_std协议"
  - "baidu_std"
  - "百度标准协议"
---

## Related Concepts
- [[concepts/protocol-buffers|Protocol Buffers]]
- [[concepts/http2|HTTP/2]]
- [[concepts/rpc|RPC]]
- [[concepts/serialization|Serialization]]
- [[concepts/streaming_rpc|Streaming RPC]]
- [[concepts/stream|Stream]]
- [[concepts/attachment|Attachment（附件）]]
- [[concepts/authentication|身份验证（Authentication）]]
- [[concepts/channel|Channel]]
- [[concepts/connection_type|Connection Type（单连接/短连接）]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/hulu_pbrpc|hulu-pbrpc]]
- [[entities/nshead_mcpack|nshead+mcpack]]
- [[entities/nova_pbrpc|nova-pbrpc]]
- [[entities/sofa_pbrpc|sofa-pbrpc]]
- [[entities/public_pbrpc|public-pbrpc]]
- [[entities/authcontext|AuthContext]]
- [[entities/grpc|gRPC]]
- [[entities/baidu|百度]]
- [[entities/streaming_rpc|streaming_rpc]]
- [[entities/ubrpc|ubrpc]]
- [[entities/brpc_server|brpc::Server]]
- [[entities/brpc_channel|brpc::Channel]]

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
> - Protocol of baidu_std, shown as 'baidu_std', enabled by default.
> - baidu_std and hulu_pbrpc supports attachments which are sent along with messages
> - Server detects supported protocols automatically, without assignment from users.

> **Source: [[sources/en_overview|en_overview]]**
> - all sorts of protocols used in Baidu: baidu_std, streaming_rpc, hulu_pbrpc, sofa_pbrpc, nova_pbrpc, public_pbrpc, ubrpc, and nshead-based ones.

> **Source: [[sources/streaming_rpc|streaming_rpc]]**
> - Client先在本地创建一个或者多个Stream，再通过一次RPC（必须使用baidu_std协议）与指定的Service建立一个Stream
> - 如果Client尝试向不支持Streaming RPC的老Server建立Stream，将总是失败。

> **Source: [[sources/server|server]]**
> - 百度标准协议，显示为"baidu_std"，默认启用。
> - baidu_std和hulu_pbrpc协议支持传递附件，这段数据由用户自定义，不经过protobuf的序列化。

> **Source: [[sources/en_client|en_client]]**
> - The default protocol used by Channel is baidu_std, which is changeable by setting ChannelOptions.protocol. The field accepts both enum and string.
> - PROTOCOL_BAIDU_STD or "baidu_std", which is the standard binary protocol inside Baidu, using single connection by default.