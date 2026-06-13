---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [method]
aliases:
  - "Snappy 压缩算法"
  - "Snappy compression"
  - "brpc::CompressTypeSnappy"
---


# Snappy

## 定义
Snappy 是 brpc 通过 `brpc::CompressTypeSnappy` 支持的一种压缩算法。它以极快的压缩和解压速度著称，但压缩率相对较低，属于速度优先型的压缩方法。

## 关键特征
- **压缩与解压速度极快**：在 128B 至 32768B 的数据规模下，Snappy 的压缩吞吐可达 162–1933 MB/s，解压吞吐可达 137–2520 MB/s，性能远高于 Gzip 与 Zlib。
- **压缩率较低**：在基准测试中，Snappy 的压缩率约为 37.50%，相比 Gzip/Zlib 在压缩比上不具优势。
- **速度–压缩率权衡**：在 brpc 客户端场景中，当延迟敏感程度高于带宽节省需求时，Snappy 是更合适的选择。
- **作为 brpc 客户端的默认推荐压缩算法**：在对延迟敏感的业务场景中，brpc 文档将其列为默认推荐。

## 应用
- **延迟敏感的 brpc 客户端通信**：在需要快速响应、低处理开销的 RPC 调用中，通过 `brpc::CompressTypeSnappy` 启用 Snappy 压缩，以最小化端到端延迟。
- **中小规模数据（128B–32KB）传输**：在该数据规模区间内，Snappy 压缩/解压吞吐达到 GB/s 级别，适合作为高频小包传输的压缩方案。
- **CPU 资源紧张的压缩场景**：当服务端或客户端不希望因压缩消耗过多 CPU 时，可选用 Snappy 替代 Gzip/Zlib。

## 相关概念
- [[concepts/compression|Compression]]
- [[concepts/controller|Controller]]

## 相关实体
- [[entities/channel|Channel]]

## 来源提及
- "brpc::CompressTypeSnappy : snappy, compression and decompression are very fast, but compression ratio is low." — [[sources/en_client|en_client]]
- "| Snappy          | 128              | 0.753114          | 0.890815            | 162.0875                  | 137.0322                    | 37.50%         |" — [[sources/en_client|en_client]]