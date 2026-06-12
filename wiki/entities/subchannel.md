---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_io]]"
tags:
  - "other"
aliases:
  - "子通道"
  - "SubChannel"
---

## Related Concepts
- [[concepts/health-checking|Health Checking]] — SubChannel 通过伪造的 Socket 实现健康检查功能
- [[concepts/load-balancing|负载均衡]] — SubChannel 作为后端端点封装单位，为 SelectiveChannel 的负载均衡策略提供支撑
- [[concepts/fault-tolerance|容错]] — SubChannel 通过 SocketId 管理机制实现故障隔离和资源释放