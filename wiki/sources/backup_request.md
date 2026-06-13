---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[brpc/backup_request.md]]"
tags: [backup request, SelectiveChannel, latency_cdf, LatencyRecorder]
aliases: ["brpc备用请求机制", "Backup Request in brpc"]
---

# brpc Backup Request机制 - Summary

## 来源
- Original file: [[brpc/backup_request.md]]
- Ingested: 2026-06-12

## 核心内容
本文档介绍了[[entities/brpc|brpc]]框架中用于提升服务可用性的**Backup Request（备用请求）机制**。核心思路是：客户端同时向多个服务端发送相同的请求，取最先返回的结果，从而避免因单个节点异常导致的请求超时。当后端服务器可挂载在同一命名服务内时，只需在Channel中开启backup request功能，并设置合理的`backup_request_ms`超时时间；当服务器分属不同集群时，推荐使用开启backup request的SelectiveChannel实现互备。文档强调，合理选择超时时间（参考latency_cdf图）可在大部分场景下仅发送一个请求，对后端压力仅为一倍。此外，文档还介绍了如何使用[[concepts/latencyrecorder|LatencyRecorder]]自定义函数延迟监控，辅助调优超时参数。

## 关键实体
- [[entities/brpc|brpc]] — 提供backup request机制的RPC框架

## 关键概念
- [[concepts/backup-request|backup request]] — 备用请求核心机制，通过配置`backup_request_ms`实现多路并发
- [[concepts/selectivechannel|SelectiveChannel]] — 用于跨集群备份请求的推荐方案
- [[concepts/latency_cdf|latency_cdf]] — 延迟累积分布函数图，用于辅助选择最优超时值
- [[concepts/latencyrecorder|LatencyRecorder]] — bvar库中的延迟记录器，支持自定义函数性能监控

## 要点
- Backup request是brpc内置的高可用机制，客户端同时请求多个服务端，取最先返回的结果
- 当后端可挂载同一命名服务时，直接启用Channel的backup request功能
- 不能挂载同一命名服务时，推荐使用开启backup request的SelectiveChannel，避免不必要的双倍请求压力
- 选择`backup_request_ms`可依据latency_cdf图，通常选择覆盖99%以上请求的超时值
- 可通过bvar::LatencyRecorder自定义函数延迟监控，生成自定义latency_cdf图辅助调优
- 不推荐使用两个异步RPC加取消逻辑的方式，因为总会发送两倍请求，不够经济