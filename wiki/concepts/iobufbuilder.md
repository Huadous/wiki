---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/iobuf|iobuf]]"
  - "[[brpc/http_client.md]]"
  - "[[brpc/en_iobuf.md]]"
tags:
  - "method"
aliases:
  - "IOBufBuilder"
  - "butil IOBufBuilder"
  - "butil::IOBufBuilder"
  - "IOBufBuilder"
  - "butil IOBufBuilder"
---

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

> **Source: [[sources/en_iobuf|en_iobuf]]**
> - "constructible like a std::ostream using IOBufBuilder."
> - "IOBufBuilder os;
os << \"anything can be sent to std::ostream\";
os.buf();  // IOBuf"