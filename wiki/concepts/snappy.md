---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client]]"
  - "[[brpc/baidu_std.md]]"
tags:
  - "method"
aliases:
  - "Snappy 压缩算法"
  - "Snappy compression"
  - "brpc::CompressTypeSnappy"
---

## Related Concepts
- [[concepts/compression|Compression]]
- [[concepts/controller|Controller]]
- [[concepts/压缩算法|压缩算法]]
- [[concepts/rpcmeta|RpcMeta]]

## Related Entities
- [[entities/channel|Channel]]
- [[entities/baidu_std|baidu_std]]

## Mentions in Source

> **Source: [[sources/en_client|en_client]]**
> - "brpc::CompressTypeSnappy : snappy, compression and decompression are very fast, but compression ratio is low."
> - "| Snappy          | 128              | 0.753114          | 0.890815            | 162.0875                  | 137.0322                    | 37.50%         |"

> **Source: [[sources/baidu_std|baidu_std]]**
> - "可以使用指定的压缩算法来压缩消息包中的数据部分。"
> - "| 1    | 使用Snappy |"