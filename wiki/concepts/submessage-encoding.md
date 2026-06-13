---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/encoding]]"]
tags: [method]
aliases:
  - "Embedded message encoding"
  - "Nested message encoding"
  - "子消息编码"
---


# Submessage encoding

## 定义
子消息编码（Submessage encoding）是协议缓冲区（Protocol Buffers）中用于编码嵌套消息字段的机制。它使用LEN线类型（wire type），通过先输出字段标签（tag），然后是一个长度前缀（varint），最后是子消息的二进制数据来表示一个内嵌的消息结构。

## 关键特征
- **LEN线类型**：子消息字段采用LEN（长度定界）线类型进行编码，与字符串和字节字段类似。
- **三部分结构**：编码结果由字段标签（tag）、长度前缀（varint）和子消息二进制数据三部分顺序组成。
- **递归嵌套**：子消息内部可以继续包含其他子消息，支持任意深度的嵌套消息结构。
- **长度前缀灵活**：长度前缀使用varint编码，能够高效表示不同大小的子消息数据。
- **与Protoscope兼容**：在Protoscope工具中，可以使用大括号简化子消息的表示，例如 `3: {1: 150}`。

## 应用
- 在Protocol Buffers消息定义中，定义一个字段类型为其他消息类型时，该字段的编码即使用子消息编码。
- 在高效的数据序列化和通信协议中，用于构建复杂的嵌套数据结构，例如RPC请求和响应中的分层参数。
- 在分布式系统或微服务架构中，用于编码包含多个子结构的配置、状态或元数据消息。

## 相关概念
- [[concepts/length-delimited-records|Length-delimited records]]
- [[concepts/wire-format|Wire format]]
- [[concepts/tag-length-value-tlv|Tag-Length-Value (TLV)]]
- [[concepts/varint|Varint]]

## 相关实体
- [[entities/protoscope|Protoscope]]
- [[entities/protoscope|Protocol Buffers]]

## 来源提及
- "Submessage fields also use the LEN wire type. Here’s a message definition with an embedded message of our original example message, Test1." — [[sources/encoding|encoding]]
- "If we set the c field (i.e., Test3.c) to 150, we get `1a03089601`." — [[sources/encoding|encoding]]