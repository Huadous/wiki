---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/iobuf|iobuf]]"]
tags: [method]
aliases:
  - "IOBuf protobuf 解析与序列化"
  - "IOBuf Protobuf Interop"
---


# IOBuf 与 Protobuf 互操作

## 定义
IOBuf 与 Protobuf 的互操作是一组通过零拷贝流包装类在 [[entities/butil-iobuf|butil::IOBuf]] 与 protobuf 消息之间进行解析与序列化的方法。该方法使用两个适配器类——`IOBufAsZeroCopyInputStream`（解析方向）和 `IOBufAsZeroCopyOutputStream`（序列化方向）——将 IOBuf 包装为 protobuf 的 `ZeroCopy*Stream` 接口，从而在不将 IOBuf 数据先拷贝到连续 `std::string` 的前提下完成 protobuf 消息的编解码。

## 关键特征
- **零拷贝解析**：使用 `IOBufAsZeroCopyInputStream` 将 IOBuf 包装为输入流，直接传入 `ParseFromZeroCopyStream` 或 `CodedInputStream::ReadLittleEndian32` 等方法，无需构造中间 `std::string`。
- **零拷贝序列化**：使用 `IOBufAsZeroCopyOutputStream` 包装目标 IOBuf，通过 `SerializeToZeroCopyStream` 将 protobuf 消息直接写入 IOBuf。
- **基于 Protobuf 标准流接口**：复用 google protobuf 自带的 `ZeroCopyInputStream` / `ZeroCopyOutputStream` 抽象，无需修改 protobuf 库本身。
- **可扩展到自定义二进制结构**：开发者可以基于 `IOBufAsZeroCopyInputStream` 进一步构造 `CodedInputStream`，用于解析非 protobuf 格式的自定义二进制结构。
- **保留 IOBuf 链式缓冲特性**：在整个编解码过程中维持 IOBuf 的引用链与分片结构，避免大块内存的额外分配与拷贝。

## 应用
- 在 [[sources/server|brpc Server]] 端接收网络数据后，直接将包含协议负载的 IOBuf 解析为 protobuf 消息，省去数据重组开销。
- 在 brpc Client 端将待发送的 protobuf 消息序列化到 IOBuf，再交由 brpc 的零拷贝发送路径传出。
- 在 [[entities/brpc|brpc]] 内部各模块之间传递 protobuf 数据时维持零拷贝语义，减少内存带宽消耗。
- 解析非 protobuf 的自定义二进制协议（例如某些私有帧格式），借助 `CodedInputStream` 在 IOBuf 上按小端序等规则读取字段。

## 相关概念
- [[concepts/零拷贝缓冲]]

## 相关实体
- [[entities/butil-iobuf|butil::IOBuf]]
- [[entities/brpc|brpc]]

## 来源提及
- 可以解析或序列化为protobuf messages. — [[sources/iobuf|iobuf]]
- 解析IOBuf为protobuf message: IOBufAsZeroCopyInputStream wrapper(&iobuf); pb_message.ParseFromZeroCopyStream(&wrapper); — [[sources/iobuf|iobuf]]
- protobuf序列化为IOBuf: IOBufAsZeroCopyOutputStream wrapper(&iobuf); pb_message.SerializeToZeroCopyStream(&wrapper); — [[sources/iobuf|iobuf]]