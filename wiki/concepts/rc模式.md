---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_rdma]]"
  - "[[sources/rdma]]"
tags:
  - "standard"
aliases:
  - "RC mode"
  - "Reliable Connection"
  - "RC"
  - "RC mode"
  - "Reliable Connection"
---

## Description
RC模式是RDMA技术中的一种可靠连接传输服务，通过确认和重传机制确保数据完整、按序地送达接收端。在该模式下，每个通信对之间建立独占的QP连接，形成一对一的通信通道，需要显式地进行连接建立、维护和销毁管理。brpc框架选用RC模式作为其RDMA通信的基础，每个[[entities/rdmaendpoint|RdmaEndpoint]]实例对应一个独立的QP，通过RC模式实现低延迟、高吞吐的远程过程调用。这种设计保证了数据传输的可靠性，同时支持双向通信和零拷贝传输，适合对数据完整性和顺序性有严格要求的高性能计算和分布式系统场景。

## Related Concepts
- [[concepts/rdma|rdma]]
- [[concepts/握手|握手]]
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