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
  - "[[brpc/client.md]]"
  - "[[brpc/baidu_std.md]]"
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
- [[concepts/rpc|RPC]]
- [[concepts/protobuf|Protobuf]]
- [[concepts/包头|包头]]
- [[concepts/元数据|元数据]]
- [[concepts/数据|数据]]
- [[concepts/附件|附件]]
- [[concepts/rpcmeta|RpcMeta]]
- [[concepts/压缩算法|压缩算法]]
- [[concepts/http接口|HTTP接口]]

## Related Entities
- [[entities/hulu|Hulu]]
- [[entities/sofa|Sofa]]

## Mentions in Source

> **Source: [[sources/baidu_std|baidu_std]]**
> - "baidu_std是一种基于TCP协议的二进制RPC通信协议。它以Protobuf作为基本的数据交换格式，并基于Protobuf内置的RPC Service形式，规定了通信双方之间的数据交换协议，以实现完整的RPC调用。"
> - "baidu_std不考虑跨TCP连接的情况。"
> - "包是baidu_std的基本数据交换单位。每个包由包头和包体组成，其中包体又分为元数据、数据、附件三部分。"