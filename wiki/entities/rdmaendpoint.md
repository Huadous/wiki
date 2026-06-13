---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_rdma]]"
  - "[[sources/rdma]]"
  - "[[brpc/rdma.md]]"
tags:
  - "product"
aliases:
  - "RDMA端点"
  - "RdmaEndpoint类"
---

## Related Entities
- [[entities/brpc|brpc]]：宿主RPC框架
- [[entities/dp系统|dp系统]]：使用brpc及RDMA的分布式系统平台
- [[entities/iobuf|iobuf]]：brpc中的缓冲区实现，RdmaEndpoint 通过 `_sbuf` 和 `_rbuf` 管理 IOBuf Block
- [[entities/block-pool|block-pool]]：RDMA内存池

## Related Concepts
- [[concepts/RDMA|RDMA]]：远程直接内存访问技术
- [[concepts/QP|QP]]：队列对，每个 RdmaEndpoint 对应一个 QP
- [[concepts/CQ|CQ]]：完成队列，RdmaEndpoint 通过 PollCq 从 CQ 中获取完成事件
- [[concepts/零拷贝|零拷贝]]：RdmaEndpoint实现的关键传输优化
- [[concepts/滑动窗口流控|滑动窗口流控]]：RdmaEndpoint 数据传输的第二个重要特性
- [[concepts/事件聚合|事件聚合]]：通过 solicited 标志控制事件通知频率的性能优化
- [[concepts/事件驱动架构|事件驱动架构]]：brpc 中的事件分发器，RdmaEndpoint 复用 EventDispatcher
- [[concepts/pollcq|PollCq]]：`RdmaEndpoint::PollCq` 处理函数，用于轮询 CQ 获取完成事件
- [[concepts/Verbs API|Verbs API]]：RDMA 编程接口，RdmaEndpoint 通过其提交操作并获取完成信息
- [[concepts/握手|握手]]：建立 RdmaEndpoint 前基于 TCP 交换 GID、QPN 等参数的前置过程
- [[concepts/RC|RC]]：可靠连接模式，brpc 内部 RDMA 使用模式，每个 RdmaEndpoint 对应一个 RC QP

## Mentions in Source

> **Source: [[sources/en_rdma]]**
> - "the Socket class created has RdmaEndpoint (see src/brpc/rdma/rdma_endpoint.cpp)."
> - "When RDMA is enabled, the data which need to transmit will be posted to RDMA QP with verbs API, not written to TCP fd."

> **Source: [[sources/rdma]]**
> - "当用户选择ChannelOptions或ServerOptions中的use_rdma为true时，创建出的Socket类中则有对应的RdmaEndpoint（参见src/brpc/rdma/rdma_endpoint.cpp）。"
> - "当RDMA被使能时，写入Socket的数据会通过RdmaEndpoint提交给RDMA QP（通过verbs API），而非拷贝到fd。"
> - "RdmaEndpoint数据传输逻辑的第一个重要特性是零拷贝。"
> - "RdmaEndpoint数据传输逻辑的第二个重要特性是滑动窗口流控。"
> - "对于数据读取，RdmaEndpoint中则调用verbs API从RDMA CQ中获取对应完成信息（事件获取有独立的fd，复用EventDispatcher，处理函数采用RdmaEndpoint::PollCq）。"
> - "brpc内部使用RDMA RC模式，每个RdmaEndpoint对应一个QP。"

## 相关页面
- RdmaEndpoint 通过轮询 CQ 获取 RDMA 完成事件，实现高效数据传输 [[concepts/cq|CQ]]