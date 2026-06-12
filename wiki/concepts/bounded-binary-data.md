---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [term]
aliases:
  - "有界二进制数据"
  - "bounded binary data"
---


# bounded binary data

## 定义
Bounded binary data（有界二进制数据）是 brpc 中对消息（message）的核心定义：从连接中读取或写入的、相邻的、具有已知大小的二进制数据段。该抽象将网络通信中的所有数据视为具有明确边界的离散消息，从而简化了解析与处理管线。

## 关键特征
- **有界性**：每个数据片段都有明确的尺寸边界，不是无限流
- **相邻性**：数据在内存中是连续存储的二进制块
- **来源中立**：既可以是来自上游客户端的请求，也可以是来自下游服务器的响应
- **读写对称**：读取和写入操作对 bounded binary data 的定义是对称的

## 应用
- 作为 brpc `InputMessenger` 输入切割的基本单位
- 作为 `Socket` 写操作的输出基本单位
- 支撑多种协议（如 protobuf、HTTP、Redis 等）的统一消息抽象
- 简化网络消息的解析流水线设计，无需处理流式边界

## 相关概念
- [[concepts/parse-callback|Parse callback]]
- [[concepts/protocols|protocols]]

## 相关实体
- [[entities/inputmessenger|InputMessenger]]
- [[entities/socket|Socket]]

## 来源提及
- "A message is a bounded binary data read from a connection, which may be a request from upstream clients or a response from downstream servers." — [[brpc/en_io]]
- "A message is a bounded binary data written to a connection, which may be a response to upstream clients or a request to downstream servers." — [[brpc/en_io]]