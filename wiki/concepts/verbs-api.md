---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/rdma]]"
  - "[[brpc/rdma.md]]"
tags:
  - "standard"
aliases:
  - "RDMA verbs API"
  - "InfiniBand verbs"
  - "verbs API"
---

## Related Concepts

- [[concepts/QP|QP]]（队列对）
- [[concepts/CQ|CQ]]（完成队列）
- [[concepts/内存注册|内存注册]]（Memory Registration, MR）
- [[concepts/零拷贝|零拷贝]]
- [[concepts/RDMA|RDMA]]
- [[concepts/EventDispatcher|EventDispatcher]]

## Related Entities

- [[entities/brpc|brpc]]
- [[entities/rdmaendpoint|RdmaEndpoint]]

## Mentions in Source

> **Source: [[sources/rdma|rdma]]**
> - "当RDMA被使能时，写入Socket的数据会通过RdmaEndpoint提交给RDMA QP（通过verbs API），而非拷贝到fd。"
> - "对于数据读取，RdmaEndpoint中则调用verbs API从RDMA CQ中获取对应完成信息（事件获取有独立的fd，复用EventDispatcher，处理函数采用RdmaEndpoint::PollCq）。"

## Additional Notes

新来源文件 [[sources/rdma|rdma]] 未提供与 verbs API 直接相关的新增信息。