---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client|en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "term"
aliases:
  - "幂等性"
  - "idempotency"
  - "Idempotence"
---

## Related Concepts
- [[concepts/retry|Retry]]
- [[concepts/backup-request|Backup Request]]
- [[concepts/controller|Controller]]
- [[concepts/重试退避|重试退避]]

## Related Entities
（暂无相关实体）

## Mentions in Source
- Generally RPC services with side effects must consider idempotence of the service, otherwise retries may make side effects be done more than once and result in unexpected behavior. — [[sources/en_client|en_client]]

> **Source: [[sources/client|client]]**
> - Q: 怎么确保请求只被处理一次 — [[brpc/client|client]]
> - 这不是RPC层面的事情。当response返回且成功时，我们确认这个过程一定成功了。 — [[brpc/client|client]]
> - 带副作用的RPC服务都应当考虑[幂等]问题，否则重试可能会导致多次叠加副作用而产生意向不到的结果。 — [[brpc/client|client]]
> - No directly relevant information — [[sources/client|client]]