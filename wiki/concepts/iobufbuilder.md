---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/iobuf|iobuf]]"
  - "[[brpc/http_client.md]]"
tags:
  - "method"
aliases:
  - "IOBufBuilder"
  - "butil IOBufBuilder"
  - "butil::IOBufBuilder"
  - "IOBufBuilder"
  - "butil IOBufBuilder"
---

## 定义
IOBufBuilder 是 [[entities/暂无条目|butil::IOBuf]] 提供的辅助构造类，其用法与 `std::ostringstream` 类似，允许开发者像使用标准 C++ 流一样通过 `operator<<` 流式地增量构造一个 IOBuf 实例。它将所有通过 `operator<<` 写入的数据累积到内部的 IOBuf 中，最终通过 `os.buf()` 取出构建完成的 IOBuf，或通过 `os.move_to(...)` 将其整体转移到目标容器（如 `cntl.request_attachment()`）。

## Description
IOBufBuilder 是 brpc 生态中用于以流式 API 增量构造 IOBuf 的辅助类，其行为高度类似 `std::ostringstream`：开发者通过 `operator<<` 连续写入各种可序列化或可打印数据，IOBufBuilder 在内部将这些数据聚合到底层 IOBuf 中，构造完成后即可通过 `os.buf()` 获取产物，或通过 `os.move_to(...)` 将所有权零成本地转移给目标（如 HTTP 请求附件）。在需要构造"包含大量打印过程的 body"（例如大型 HTTP POST body）的场景下，IOBufBuilder 能显著简化代码：与 c-style `printf` 相比，它不仅可读性更好，而且避免了多次 `append` 调用和大量临时 `std::string` 的开销，效率可能更高。需要注意，由 IOBufBuilder 输出的 IOBuf 只有在内容为可打印字符时，才能直接通过 `std::cout` 流式输出或使用 `iobuf.to_string()` 转换为 `std::string`，后者会引入额外的内存分配。

## Related Concepts
- [[concepts/零拷贝缓冲|零拷贝缓冲]]
- [[concepts/流式构造|流式构造]]

## Related Entities
- [[entities/暂无条目|butil::IOBuf]]
- [[entities/暂无条目|brpc]]
- [[entities/暂无条目|brpc::Controller]]
- [[entities/examplehttp_c++|examplehttp_c++]]

## Mentions in Source

> **Source: [[sources/iobuf|iobuf]]**
> - "IOBufBuilder可以把IOBuf当std::ostream用。"
> - "用可打印数据创建IOBuf: IOBufBuilder os; os << \"anything can be sent to std::ostream\"; os.buf();  // IOBuf"
> - "可直接打印至std::ostream. 注意这个例子中的iobuf必需只包含可打印字符。"

> **Source: [[sources/http_client|http_client]]**
> - "需要大量打印过程的body建议使用butil::IOBufBuilder，它的用法和std::ostringstream是一样的。对于有大量对象要打印的场景，IOBufBuilder简化了代码，效率也可能比c-style printf更高。"
> - "butil::IOBufBuilder os; os << \"A lot of printing\" << printable_objects << ...; os.move_to(cntl.request_attachment());"