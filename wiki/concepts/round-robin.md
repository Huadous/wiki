---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/lalb]]"
  - "[[brpc/en_client.md]]"
tags:
  - "method"
aliases:
  - "轮询"
  - "RR"
  - "Round Robin"
  - "rr"
  - "轮询"
  - "RR"
  - "Round Robin"
---

## Related Concepts
- [[concepts/locality-aware-load-balancing|Locality-aware load balancing]]
- [[concepts/random|Random load balancing]]
- [[concepts/wrr|Weighted round robin (wrr)]]
- [[concepts/wr|Weighted random (wr)]]
- [[concepts/load-balancer|Load balancer]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/nginx|nginx]]
- [[entities/envoy-proxy|envoy-proxy]]

## Mentions in Source

> **Source: [[sources/lalb|lalb]]**
> - "最常见的分流算法是round robin和随机。"
> - "'rr' or 'random': ... 'la': ... 真实的场景中不会有这么显著的差异，但你应该能看到差别了。"

> **Source: [[sources/en_client|en_client]]**
> - "which is round robin. Always choose next server inside the list, next of the last server is the first one. No other settings. For example there're 3 servers: a,b,c, brpc will send requests to a, b, c, a, b, c, … and so on."
> - "This recovery mechanism requires the capabilities of downstream servers to be similar, so it is currently only valid for rr and random."