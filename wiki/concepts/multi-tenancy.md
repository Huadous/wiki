---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_io]]"]
tags: [phenomenon]
aliases:
  - "multi-tenant"
  - "多租户"
---


# multi-tenancy

## 定义
Multi-tenancy（多租户）是指多个用户、应用程序或服务共享同一套底层计算资源（如CPU、内存、网络、文件描述符）的系统架构模式。在这种共享环境下，一个租户的行为（如高负载、资源争用）可能对其他租户的性能和可用性产生负面影响，导致资源隔离失效和性能干扰。

## 关键特征
- **资源共享**：不同租户共享物理或虚拟化资源池，而非独占资源。
- **性能干扰**：一个租户的资源密集型操作（如占用繁忙的fd）可能延迟其他租户的请求处理。
- **长尾延迟加剧**：在多租户场景下，共享资源的争用会导致请求响应时间的分布变宽，尾部延迟显著增加。
- **复杂性放大**：多租户与环境中的其他因素（如复杂负载均衡、流式RPC）结合时，会进一步恶化系统稳定性问题。
- **隔离机制需求**：需要设计专门的调度、限流或资源配额机制来缓解租户间的相互干扰。

## 应用
- **云计算平台**：多个云租户共享同一台物理服务器或虚拟机的网络、IO和计算资源。
- **微服务架构**：多个服务实例共享同一进程内的网络连接池、线程池或事件循环。
- **数据库服务**：多租户数据库（如SaaS应用）共享数据库连接、缓存和存储I/O。
- **brpc框架**：在brpc的IO模型中，多租户导致多个fd共享同一个EventDispatcher线程，繁忙的fd会阻塞其他fd的读写事件，最终增加整体请求的尾延迟。brpc通过引入bthread轻量级线程和事件分发器设计来对抗此问题。

## 相关概念
- [[concepts/long-tail|long tail]]
- [[concepts/load-balancing|load balancing]]
- [[concepts/io-model|IO模型]]
- [[concepts/resource-isolation|资源隔离]]

## 相关实体
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/bthread|bthread]]
- [[entities/brpc|brpc]]
- [[entities/socket|Socket]]

## 来源提及
- "Multi-tenancy, complicated load balancing and Streaming RPC worsen the problem." — [[brpc/en_io]]