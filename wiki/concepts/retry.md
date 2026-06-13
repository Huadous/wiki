---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/avalanche.md]]"
tags:
  - "term"
aliases:
  - "RPC重试"
  - "Retry机制"
  - "重试"
  - "RPC重试"
  - "Retry机制"
---

## Description
重试是 RPC 客户端在请求失败后再次发起相同请求的机制，常用于在网络抖动或瞬时故障时提升请求成功率。当连接断开时，brpc 默认会自动发起重试；当服务端未在指定时间内响应时，客户端会返回超时错误，此时也可以选择进行重试。`ChannelOptions.max_retry` 控制了通过 channel 发起的所有 RPC 的最大重试次数，默认为 3，设为 0 则表示不重试；同时用户可以通过继承 `brpc::RetryPolicy` 来自定义重试条件。

然而，激进的重试策略存在显著风险：在雪崩场景中，基于超时的频繁重试不仅会让客户端的最大 QPS 降到"线程数 / 超时"，还会使下游 QPS 翻"重试次数"倍，可能陷入"线程数 / 超时 × 重试次数 > 下游最大 QPS"的恶性循环。brpc 的默认重试策略仅在连接出错时触发，避免了流量放大，是一种较为有效率的方式。如果确实需要基于超时进行重试，建议使用 backup request，其放大程度最多为 1 次。在自定义 `RetryPolicy` 时，用户需要仔细评估最差情况下的请求放大倍数，避免对下游造成过大压力。

## Related Concepts
- [[concepts/Timeout|Timeout]]
- [[concepts/RPC|RPC]]
- [[concepts/Backup Request|Backup Request]]
- [[concepts/Circuit Breaker|Circuit Breaker]]
- [[concepts/Controller|Controller]]
- [[concepts/雪崩|雪崩]] (如果存在，否则忽略)
- [[concepts/QPS|QPS]]
- [[concepts/RetryPolicy|RetryPolicy]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source
- "RPC retries when the connection is broken." — [[sources/en_overview|en_overview]]
- "When server does not respond within the given time, client fails with a timeout error." — [[sources/en_overview|en_overview]]
- "RPC retries when the connection is broken." — [[sources/en_overview|en_overview]]

> **Source: [[sources/en_client|en_client]]**
> - "ChannelOptions.max_retry is maximum retrying count for all RPC via the channel, Default value is 3, 0 means no retries."
> - "aggressive retries may easily make pressures from all clients double or even tripple against servers, and make the whole cluster down"
> - "Users can inherit brpc::RetryPolicy to customize conditions of retrying."
> - "No directly relevant information"

> **Source: [[sources/avalanche|avalanche]]**
> - "A可能对B发起了过于频繁的基于超时的重试。这不仅会让A的最大qps降到线程数 / 超时，还会让B处的qps翻重试次数倍。"
> - "brpc中重试默认只在连接出错时发起，避免了流量放大，这是比较有效率的重试方式。"
> - "注意考察重试发生时的行为，特别是在定制RetryPolicy时。"