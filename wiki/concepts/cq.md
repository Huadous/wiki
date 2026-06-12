---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_rdma]]"
  - "[[sources/rdma]]"
tags:
  - "term"
aliases:
  - "Completion Queue"
  - "完成队列"
---

## 关键特征
- **事件驱动**：CQ通过存放CQE来异步通知应用程序RDMA操作的完成状态。
- **轮询机制**：应用程序（如RdmaEndpoint）通过轮询（Polling）操作从CQ中获取CQE，这是一种低延迟的完成通知方式。
- **配置灵活性**：轮询行为是可配置的，例如通过`rdma_cqe_poll_once`参数可以设置每次轮询获取的CQE数量（默认值为32）。
- **事件注入**：CQ事件可以通过专用的文件描述符（fd）注入到事件分发器（如EventDispatcher）中，以便进行高效的事件处理。

## 应用
- **高性能RPC通信**：在brpc等RPC框架中，CQ是RDMA数据路径的关键组成部分。RdmaEndpoint轮询CQ以获取完成事件，然后解析RPC消息，实现高效的远程过程调用。
- **低延迟数据传输**：在需要极低延迟的场景（如高频交易、分布式存储）中，CQ的轮询模式相比中断模式能显著减少延迟。
- **大规模并行通信**：多个QP（Queue Pair）可以共享一个CQ，便于在复杂的通信模式中统一管理和处理完成事件。

## 相关概念
- [[concepts/rdma|RDMA]]
- [[concepts/qp|QP]]
- [[concepts/事件抑制|事件抑制]]
- [[concepts/轮询模式|轮询模式]]

## 相关实体
- [[entities/rdmaendpoint|RdmaEndpoint]]

## 来源提及
- "RdmaEndpoint will get completions from RDMA CQ with verbs API" — [[sources/en_rdma|en_rdma]]
- "the event will be generated from a dedicated fd and be added into EventDispatcher, the handling function is RdmaEndpoint::PollCq" — [[sources/en_rdma|en_rdma]]
- "rdma_cqe_poll_once: the number of CQE pooled from CQ once，default is 32" — [[sources/en_rdma|en_rdma]]

> **来源: [[sources/rdma|rdma]]**
> - "对于数据读取，RdmaEndpoint中则调用verbs API从RDMA CQ中获取对应完成信息（事件获取有独立的fd，复用EventDispatcher，处理函数采用RdmaEndpoint::PollCq）。" — [[sources/rdma|rdma]]
> - "rdma_cqe_poll_once: 从CQ中一次性poll出的CQE数量，默认32" — [[sources/rdma|rdma]]