---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_rdma]]"
  - "[[sources/rdma]]"
  - "[[brpc/rdma.md]]"
tags:
  - "term"
aliases:
  - "Completion Queue"
  - "完成队列"
---

## Related Concepts
- [[concepts/rdma|RDMA]]
- [[concepts/qp|QP]]
- [[concepts/事件抑制|事件抑制]]
- [[concepts/轮询模式|轮询模式]]
- [[concepts/事件聚合|事件聚合]]
- [[concepts/verbs-api|verbs API]]

## Related Entities
- [[entities/rdmaendpoint|RdmaEndpoint]]

## Mentions in Source

> **Source: [[sources/en_rdma|en_rdma]]**
> - "RdmaEndpoint will get completions from RDMA CQ with verbs API"
> - "the event will be generated from a dedicated fd and be added into EventDispatcher, the handling function is RdmaEndpoint::PollCq"
> - "rdma_cqe_poll_once: the number of CQE pooled from CQ once，default is 32"

> **Source: [[sources/rdma|rdma]]**
> - "对于数据读取，RdmaEndpoint中则调用verbs API从RDMA CQ中获取对应完成信息（事件获取有独立的fd，复用EventDispatcher，处理函数采用RdmaEndpoint::PollCq）。"
> - "rdma_cqe_poll_once: 从CQ中一次性poll出的CQE数量，默认32"