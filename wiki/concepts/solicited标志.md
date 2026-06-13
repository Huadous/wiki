---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[]]"
  - "[[brpc/rdma.md]]"
tags:
  - "term"
  - "method"
aliases:
  - "solicited event flag"
  - "solicited completion flag"
  - "请求完成标志"
---

## Related Concepts
- [[concepts/event-aggregation|事件聚合]]
- [[concepts/CQ|CQ]]
- [[concepts/sliding-window-flow-control|滑动窗口流控]]

## Related Entities
- [[entities/rdmaendpoint|RdmaEndpoint]]

## Mentions in Source

> **Source: [[sources/rdma|rdma]]**
> - "每个消息的大小被限定在一个recv_block_size，默认为8KB。"
> - "如果每个消息都触发事件进行处理，会导致性能退化严重，甚至不如TCP传输（TCP拥有GSO、GRO等诸多优化）。"
> - "因此，RdmaEndpoint综合考虑数据大小、窗口与ACK的情况，对每个发送消息选择性设置solicited标志，来控制是否在发送端触发事件通知。"