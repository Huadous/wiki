---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_rdma]]"
  - "[[sources/rdma]]"
tags:
  - "method"
aliases:
  - "应用层连接"
  - "brpc应用层连接方式"
---

## Related Concepts
- [[concepts/rdma|远程直接内存访问]]
- [[concepts/握手|握手]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/rdmaendpoint|RdmaEndpoint]]

## Mentions in Source
> **Source: [[sources/en_rdma|en_rdma]]**
> - "The handshake procedure is completed in the AppConnect way in brpc."
> - "The TCP connection will keep in EST state but not be used for data transmission after RDMA connection is established."

> **Source: [[sources/rdma|rdma]]**
> - "握手过程采用了brpc中已有的AppConnect逻辑。"