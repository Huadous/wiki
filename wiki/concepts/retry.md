---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[brpc/en_client.md]]"
tags:
  - "term"
aliases:
  - "RPC重试"
  - "Retry机制"
---

## Related Concepts
- [[concepts/Timeout|Timeout]]
- [[concepts/RPC|RPC]]
- [[concepts/Backup Request|Backup Request]]
- [[concepts/Circuit Breaker|Circuit Breaker]]
- [[concepts/Controller|Controller]]

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