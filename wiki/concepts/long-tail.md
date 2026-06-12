---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_io]]"]
tags: [phenomenon]
aliases:
  - "long tail latency"
  - "尾部延迟"
  - "长尾效应"
  - "长尾时延"
---


# long tail

## 定义
Long tail（长尾）指在分布式系统中，一小部分请求经历显著高于平均水平的延迟，形成延迟分布曲线上的一条“长尾”。在 brpc 的 IO 设计中，长尾延迟是当线程 IO 无法高效地同时处理多个文件描述符（fd）时产生的后果。brpc 通过无锁事件分发与工作窃取（work stealing）设计来缓解这一问题，确保单个 fd 不会独占事件分发器。

## 关键特征
- **分布偏斜**：少量请求延迟远高于中位数，形成重尾分布。
- **系统性成因**：在高负载下，单个 fd 的长时间延迟会拖慢 IO 线程上的所有 fd，产生级联效应。
- **对性能敏感**：在微秒级延迟要求的系统中，长尾会显著影响整体服务质量（QoS）。
- **资源争用**：事件分发器被某个 fd 阻塞，其他 fd 得不到及时处理。
- **设计可优化**：通过无锁事件分发、工作窃取等机制可以有效抑制。

## 应用
- **IO 线程池设计**：通过无锁事件分发和工作窃取，避免单个 fd 阻塞事件循环，减少长尾延迟。
- **负载均衡策略**：在多路复用、高并发场景中识别并隔离慢速连接，防止其影响其他请求。
- **性能调优**：在 brpc 等高性能 RPC 框架中，通过监控延迟分布识别长尾问题并优化 IO 路径。
- **多租户环境**：隔离不同租户的 IO 资源，避免一个租户的慢操作导致其他租户的尾部延迟恶化。

## 相关概念
- [[concepts/multi-tenancy|multi-tenancy]] — 多租户环境下资源隔离可缓解长尾问题
- [[concepts/work-stealing|work stealing]] — 工作窃取机制用于平衡事件分发器的负载

## 相关实体
- [[entities/brpc|brpc]] — 实现了无锁事件分发与工作窃取以对抗长尾延迟
- [[entities/eventdispatcher|EventDispatcher]] — 负责事件分发，其设计直接影响长尾表现
- [[entities/bthread|bthread]] — brpc 的轻量级线程，其调度机制与长尾延迟相关

## 来源提及
- "Under high workloads, regular long delays on one fd may slow down all fds in the IO thread, causing more long tails." — [[sources/en_io|en_io]]