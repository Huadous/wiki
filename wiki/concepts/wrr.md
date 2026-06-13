---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "method"
aliases:
  - "Weighted Round Robin"
  - "weighted round robin load balancer"
  - "wrr 负载均衡算法"
---

## Related Concepts
- [[concepts/Load Balancer|Load Balancer]]
- [[concepts/负载均衡|负载均衡]]
- [[concepts/一致性哈希|一致性哈希]]
- [[concepts/集群恢复限流|集群恢复限流]]
- [[concepts/rr|rr]]
- [[concepts/random|random]]
- [[concepts/wr|wr]]
- [[concepts/VIP|VIP]]
- [[concepts/la|la]]
- [[concepts/c_murmurhash|c_murmurhash]]
- [[concepts/c_md5|c_md5]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/brpc::Channel|brpc::Channel]]

## Mentions in Source

**Source: [[sources/en_client|en_client]]**
- "which is weighted round robin. Choose the next server according to the configured weight. The chances a server is selected is consistent with its weight, and the algorithm can make each server selection scattered."
- "The instance tag must be an int32 number representing the weight, eg. `tag="50"`."

**Source: [[sources/client|client]]**
- "即weighted round robin, 根据服务器列表配置的权重值来选择服务器。服务器被选到的机会正比于其权重值，并且该算法能保证同一服务器被选到的结果较均衡的散开。"
- "实例的tag需要是表示权值的int32数字，如tag="50"。"
- "如果你需要"带权重的轮询"，你应当优先考虑使用[wrr算法](#wrr)，而不是用tag来模拟。"