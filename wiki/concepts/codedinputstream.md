---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/techniques]]"]
tags: [term]
aliases:
  - "CodedInputStream 类"
  - "编码输入流"
---


# CodedInputStream

## 定义
CodedInputStream 是 Protocol Buffers 库中提供的一个高效输入流类，用于从字节序列中读取和解析编码后的 Protocol Buffers 消息。该类支持 C++ 和 Java 语言，允许开发者限制读取特定字节数，从而在不额外拷贝缓冲的情况下处理流式消息。

## 关键特征
- 支持限制读取到指定字节数，避免内存拷贝开销
- 提供高效的二进制数据解析方法
- 跨语言支持：C++ 和 Java 实现
- 适用于处理大型或流式数据流
- 与 Protocol Buffers 编码格式原生集成

## 应用
- **流式传输多个消息**：当通过同一连接或流传输多个连续的 Protocol Buffers 消息时，使用 CodedInputStream 可以避免将每个消息拷贝到独立缓冲区，提高性能
- **大数据集处理**：在处理分块的大型 Protocol Buffers 数据时，通过限制读取字节数实现高效的分段处理
- **网络通信优化**：在基于 Protocol Buffers 的 RPC 框架（如 gRPC）中减少内存拷贝次数
- **文件解析**：处理存储为连续消息序列的 Protocol Buffers 文件

## 相关概念
- [[concepts/streaming-multiple-messages|streaming-multiple-messages]]

## 相关实体
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/grpc|grpc]]

## 来源提及
- "(If you want to avoid copying bytes to a separate buffer, check out the CodedInputStream class (in both C++ and Java) which can be told to limit reads to a certain number of bytes.)" — [[protobuf/techniques.md]]