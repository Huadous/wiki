---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/iobuf|iobuf]]"]
tags: [term]
aliases:
  - "IOBuf 输入流适配器"
  - "ZeroCopyInputStream wrapper"
---


# IOBufAsZeroCopyInputStream

## 定义
IOBufAsZeroCopyInputStream 是 butil 库中提供的一个适配器类，用于将 butil::IOBuf 适配为 Google Protobuf 的 ZeroCopyInputStream 接口。通过包装一个 IOBuf 实例，它使得用户可以直接将 IOBuf 作为输入流传给 Protobuf 的 ParseFromZeroCopyStream 方法，从而实现零拷贝的 Protobuf 消息解析。

## 关键特征
- 作为 butil::IOBuf 与 Protobuf ZeroCopyInputStream 接口之间的桥接适配器
- 支持零拷贝解析，无需先将 IOBuf 物化为连续字节数组
- 可与 Google 的 CodedInputStream 组合使用，实现对 IOBuf 中二进制数据的按需读取
- 支持自定义结构的解析，例如以小端格式读取 32 位整数等
- 是 brpc 在高性能反序列化场景下的关键工具

## 应用
- **解析 IOBuf 为 Protobuf 消息**：通过 `ParseFromZeroCopyStream` 方法直接将 IOBuf 中的数据解析为 Protobuf 消息对象，避免中间拷贝
- **解析 IOBuf 为自定义结构**：结合 CodedInputStream 实现灵活的二进制数据读取与解析，适用于非 Protobuf 格式的自定义协议
- **高性能网络通信场景**：在 brpc 的 RPC 框架中，接收到的网络数据通常以 IOBuf 形式存在，使用该适配器可避免额外的内存拷贝开销

## 相关概念
- [[concepts/butil-iobuf|butil::IOBuf]]
- [[concepts/iobufbuilder|IOBufBuilder]]
- [[concepts/iobuf-protobuf-interop|IOBuf 与 Protobuf 互操作]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- 解析IOBuf为protobuf message — [[sources/iobuf|iobuf]]
- 解析IOBuf为自定义结构 — [[sources/iobuf|iobuf]]
- IOBufAsZeroCopyInputStream wrapper(&iobuf);
pb_message.ParseFromZeroCopyStream(&wrapper); — [[sources/iobuf|iobuf]]
- IOBufAsZeroCopyInputStream wrapper(&iobuf);
CodedInputStream coded_stream(&wrapper);
coded_stream.ReadLittleEndian32(&value); — [[sources/iobuf|iobuf]]