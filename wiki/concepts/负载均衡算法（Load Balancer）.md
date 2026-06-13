---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/combo_channel]]"
  - "[[sources/en_overview]]"
  - "[[brpc/load_balancing.md]]"
tags:
  - "method"
aliases:
  - "负载均衡策略"
  - "Load Balancer"
  - "LB"
  - "负载均衡"
  - "负载均衡策略"
  - "Load Balancer"
  - "LB"
  - "LoadBalancer"
  - "负载均衡策略"
  - "Load Balancer"
  - "LB"
  - "负载均衡"
  - "负载均衡策略"
  - "Load Balancer"
  - "LB"
---

## Related Concepts
- [[concepts/命名服务|命名服务]]
- [[concepts/一致性哈希|一致性哈希]]
- [[concepts/容量计算规则|容量计算规则]]
- [[concepts/RPC|RPC]]
- [[concepts/DoublyBufferedData|DoublyBufferedData]]
- [[concepts/健康检查|健康检查]]

## Related Entities
- [[entities/SelectiveChannel|SelectiveChannel]]
- [[entities/ParallelChannel|ParallelChannel]]
- [[entities/brpc|brpc]]
- [[entities/bns|bns]]
- [[entities/etcd|etcd]]
- [[entities/zookeeper|zookeeper]]

## Mentions in Source

> **Source: [[sources/combo_channel|combo_channel]]**
> - "if (channel.Init('c_murmurhash', &schan_options) != 0) { "
> - "sub_channel->Init(ns_node_name[i], 'rr', NULL) != 0) { "
> - "SelectiveChannel按负载均衡算法访问其包含的Channel，相比普通Channel它更加高层：把流量分给sub channel，而不是具体的Server。"

> **Source: [[sources/en_overview|en_overview]]**
> - "Users specify load balancing algorithms to choose one machine for each request from all machines, including: round-robin, randomized, consistent-hashing(murmurhash3 or md5) and locality-aware."
> - "load balancers (rr, random, consistent hashing)"

> **Source: [[sources/load_balancing|load_balancing]]**
> - "brpc中LoadBalancer从多个服务节点中选择一个节点，目前的实现见负载均衡。"
> - "Load balancer最重要的是如何让不同线程中的负载均衡不互斥，解决这个问题的技术是DoublyBufferedData。"
> - "和NamingService类似，我们使用字符串来指代一个load balancer，在global.cpp中注册。"

> **Source: load_balancing (new)**
> - "No directly relevant information"