---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/techniques]]"]
tags: [method]
aliases:
  - "流式传输多个消息"
  - "Streaming Multiple Protocol Buffers Messages"
---


# 流式传输多个消息

## 定义
流式传输多个消息（Streaming Multiple Messages）是指在单个文件或流中连续写入多个Protocol Buffers消息时，由于Wire Format本身不自带消息边界标记，因此需要在每个消息前写入其大小以确定消息边界。这是处理Protocol Buffers消息序列流的推荐方法，通过将消息大小与消息内容交替存储，实现可靠的读写操作。

## 关键特征
- **手动边界管理**：Protocol Buffers的Wire Format不自主界定消息边界，必须由用户自行跟踪消息的开始和结束位置。
- **大小前缀**：写入每个消息前先写入其大小（通常为Varint编码），读取时先读取大小，再读取相应字节。
- **避免额外拷贝**：推荐使用`CodedInputStream`类（C++和Java）的`ReadLittleEndian32()`等方法限制读取字节数，从而避免将整个流数据拷贝到独立缓冲区中。
- **兼容性广泛**：此方法适用于任何Protocol Buffers支持的语言和环境。

## 应用
- **日志记录**：将多个Protocol Buffers消息连续写入日志文件，每个日志条目前附加其大小，便于后续解析和处理。
- **网络传输**：在流式TCP连接或持久化连接中发送多个Protocol Buffers消息，使用大小前缀分隔各个独立消息。
- **数据存储**：将序列化的消息存储在单个磁盘文件或数据库中，实现高效且易于遍历的批量存储格式。

## 相关概念
- [[concepts/serialization|serialization]]
- [[concepts/cross-language-compatibility|cross-language-compatibility]]

## 相关实体
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/protoc|protoc]]
- [[entities/grpc|grpc]]

## 来源提及
- "If you want to write multiple messages to a single file or stream, it is up to you to keep track of where one message ends and the next begins." — [[sources/techniques|techniques]]
- "The easiest way to solve this problem is to write the size of each message before you write the message itself." — [[sources/techniques|techniques]]
- "When you read the messages back in, you read the size, then read the bytes into a separate buffer, then parse from that buffer." — [[sources/techniques|techniques]]