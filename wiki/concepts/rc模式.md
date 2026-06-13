---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_rdma]]"
  - "[[sources/rdma]]"
  - "[[brpc/rdma.md]]"
tags:
  - "standard"
aliases:
  - "RC mode"
  - "Reliable Connection"
  - "RC"
  - "RC mode"
  - "Reliable Connection"
---

## Related Concepts
- [[concepts/rdma|rdma]]
- [[concepts/握手|握手]]
- [[concepts/qp|qp]]
- [[concepts/事件抑制|事件抑制]]
- [[concepts/滑动窗口流控|滑动窗口流控]]
- [[concepts/零拷贝|零拷贝]]

## Related Entities
- [[entities/rdmaendpoint|rdmaendpoint]]
- [[entities/brpc|brpc]]
- [[entities/block-pool|block-pool]]

## Mentions in Source
> **Source: [[sources/en_rdma|en_rdma]]**
> - "brpc uses RDMA RC mode."
> - "Every RdmaEndpoint has its own QP."

> **Source: [[sources/rdma|rdma]]**
> - "brpc内部使用RDMA RC模式，每个RdmaEndpoint对应一个QP。"
> - "RDMA连接建立依赖于前置TCP建连，TCP建连后双方交换必要参数，如GID、QPN等，再发起RDMA连接并实现数据传输。这个过程我们称为握手（参见RdmaEndpoint）。"