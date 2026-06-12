---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_rdma]]"
  - "[[sources/rdma]]"
tags:
  - "product"
aliases:
  - "RDMA端点"
  - "RdmaEndpoint类"
---

## Related Entities
- [[entities/brpc|brpc]]：宿主RPC框架
- [[entities/dp系统|dp系统]]：使用brpc及RDMA的分布式系统平台
- [[entities/iobuf|iobuf]]：brpc中的缓冲区实现
- [[entities/block-pool|block-pool]]：RDMA内存池

## Related Concepts
- [[concepts/RDMA|RDMA]]：远程直接内存访问技术
- [[concepts/QP|QP]]：队列对，RdmaEndpoint的核心资源
- [[concepts/CQ|CQ]]：完成队列，用于通知RDMA操作完成
- [[concepts/零拷贝|零拷贝]]：RdmaEndpoint实现的关键传输优化
- [[concepts/滑动窗口流控|滑动窗口流控]]：控制数据发送速率的机制
- [[concepts/事件聚合|事件聚合]]：通过solicited标志控制事件通知频率的性能优化
- [[concepts/事件驱动架构|事件驱动架构]]：brpc中的事件分发器
- [[concepts/pollcq|PollCq]]：轮询CQ获取完成事件的函数
- [[concepts/Verbs API|Verbs API]]：RDMA编程接口
- [[concepts/握手|握手]]：建立RdmaEndpoint前用于交换参数的前置TCP握手过程
- [[concepts/RC|RC]]：可靠连接模式，RdmaEndpoint数据传输的基础

## Mentions in Source
> **Source: [[sources/en_rdma]]**
> - "the Socket class created has RdmaEndpoint (see src/brpc/rdma/rdma_endpoint.cpp)."
> - "When RDMA is enabled, the data which need to transmit will be posted to RDMA QP with verbs API, not written to TCP fd."

> **Source: [[sources/rdma]]**
> - "当用户选择ChannelOptions或ServerOptions中的use_rdma为true时，创建出的Socket类中则有对应的RdmaEndpoint（参见src/brpc/rdma/rdma_endpoint.cpp）。"
> - "当RDMA被使能时，写入Socket的数据会通过RdmaEndpoint提交给RDMA QP（通过verbs API），而非拷贝到fd。"
> - "RdmaEndpoint数据传输逻辑的第一个重要特性是零拷贝。"
> - "RdmaEndpoint数据传输逻辑的第二个重要特性是滑动窗口流控。"

## 相关页面
- RdmaEndpoint 通过轮询 CQ 获取 RDMA 完成事件，实现高效数据传输 [[concepts/cq|CQ]]