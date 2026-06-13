---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "term"
aliases:
  - "Virtual IP"
  - "VIP (Virtual IP)"
  - "layer-4 load balancer VIP"
---

## Related Concepts
- [[concepts/wrr|wrr]]
- [[concepts/load-balancer|Load Balancer]]
- [[concepts/connection-type|Connection Type]]
- [[concepts/naming-service-filter|Naming Service Filter]]

## Related Entities
无相关实体。

## Mentions in Source
> **Source: [[sources/en_client]]**
> - "VIP is often the public IP of layer-4 load balancer, which proxies traffic to RS behide. When a client connects to the VIP, a connection is established to a chosen RS. When the client connection is broken, the connection to the RS is reset as well."
> - "If one client establishes only one connection to the VIP("single" connection type in brpc), all traffic from the client lands on one RS."

> **Source: [[sources/client]]**
> - "VIP一般是4层负载均衡器的公网ip，背后有多个RS。当客户端连接至VIP时，VIP会选择一个RS建立连接，当客户端连接断开时，VIP也会断开与对应RS的连接。"
> - "如果客户端只与VIP建立一个连接(brpc中的单连接)，那么来自这个客户端的所有流量都会落到一台RS上。"