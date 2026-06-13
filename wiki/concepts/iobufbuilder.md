---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/iobuf|iobuf]]"]
tags: [method]
aliases:
  - "IOBufBuilder"
  - "butil IOBufBuilder"
---


# IOBufBuilder

## 定义
IOBufBuilder 是 [[entities/暂无条目|butil::IOBuf]] 提供的辅助构造类，允许开发者像使用 `std::ostream` 一样通过流式操作构建一个 IOBuf 实例。它作为 `std::ostream` 的特化实现，将所有通过 `operator<<` 写入的数据累积到内部的 IOBuf 中，最终通过 `os.buf()` 获取构建完成的 IOBuf。

## 关键特征
- **流式构造接口**：继承自 `std::ostream`，可直接复用所有标准的流式输出操作符。
- **一次性产出**：构造完成后通过 `os.buf()` 取出已构建的 IOBuf 实例。
- **可序列化数据兼容**：支持写入可打印或可序列化数据，适合协议字段拼接二进制负载的场景。
- **关联打印能力**：构建出的 IOBuf 可直接通过 `std::cout` 输出（需确保内容为可打印字符），也可通过 `iobuf.to_string()` 转换为 `std::string`（后者会分配额外内存）。

## 应用
- **二进制负载拼接**：在序列化场景中，使用者可以创建 `IOBufBuilder` 对象，通过 `operator<<` 将协议字段或可序列化数据逐段写入，最后通过 `os.buf()` 获取完整的 IOBuf 用于发送。
- **调试与日志输出**：当 IOBuf 内容仅包含可打印字符时，可直接将其流式输出到 `std::ostream` 便于调试。
- **字符串转换**：通过 `iobuf.to_string()` 将 IOBuf 内容转为 `std::string`（注意会带来额外的内存分配开销）。

## 相关概念
- [[concepts/零拷贝缓冲|零拷贝缓冲]]

## 相关实体
- [[entities/暂无条目|butil::IOBuf]]
- [[entities/暂无条目|brpc]]

## 来源提及
- "IOBufBuilder可以把IOBuf当std::ostream用。" — [[sources/iobuf|iobuf]]
- "用可打印数据创建IOBuf: IOBufBuilder os; os << \"anything can be sent to std::ostream\"; os.buf();  // IOBuf" — [[sources/iobuf|iobuf]]
- "可直接打印至std::ostream. 注意这个例子中的iobuf必需只包含可打印字符。" — [[sources/iobuf|iobuf]]