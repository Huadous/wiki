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
  - "Queue Pair"
  - "队列对"
---

## Related Concepts
- [[concepts/rdma|rdma]]
- [[concepts/握手|握手]]
- [[concepts/事件抑制|事件抑制]]
- [[concepts/滑动窗口流控|滑动窗口流控]]
- [[concepts/轮询模式|轮询模式]]
- [[concepts/可靠连接|可靠连接]]
- [[concepts/cq|cq]]
- [[concepts/verbs-api|verbs-api]]

## Related Entities
- [[entities/rdmaendpoint|rdmaendpoint]]
- [[entities/block-pool|block-pool]]
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: [[sources/en_rdma|en_rdma]]**
> - "Every RdmaEndpoint has its own QP."
> - "rdma_sq_size: the size of SQ，default is 128"
> - "rdma_rq_size: the size of RQ，default is 128"

> **Source: [[sources/rdma|rdma]]**
> - "brpc内部使用RDMA RC模式，每个RdmaEndpoint对应一个QP。"
> - "当RDMA被使能时，写入Socket的数据会通过RdmaEndpoint提交给RDMA QP（通过verbs API），而非拷贝到fd。"
> - "rdma_prepared_qp_size: 程序启动预生成的QP的大小，默认128"
> - "rdma_sq_size: SQ大小，默认128"
> - "rdma_prepared_qp_cnt: 程序启动预生成的QP的数量，默认1024"