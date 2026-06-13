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

## Description
负载均衡算法是分布式系统中在多个服务实例之间分配请求的关键策略。brpc 支持多种负载均衡算法，包括轮询（round-robin）、随机（randomized）、一致性哈希（consistent-hashing，基于 murmurhash3 或 md5）以及局部感知（locality-aware）。用户通过命名服务发现后端机器列表，并在初始化 Channel 时指定负载均衡算法，框架会根据所选算法对每个请求选择一台机器。

在实现层面，brpc 在 `src/brpc/load_balancer.h` 中定义了 LoadBalancer 接口，负责从多个服务节点中选择一个节点处理请求。LoadBalancer 的核心挑战是如何让不同线程的负载均衡操作不产生互斥，brpc 通过 [[concepts/DoublyBufferedData|DoublyBufferedData]] 技术解决该问题。LoadBalancer 同样采用字符串工厂模式，在 `global.cpp` 中注册，用户可在新建 Channel 时通过字符串选择具体策略。LoadBalancer 选择的节点必须来自 NamingService 当前有效的列表，且 Socket 处于可用状态（未被 SetFailed 或已被 Revive）。

这种机制使得 brpc 能够实现高可用性和可扩展性，同时支持灵活的层级化组合策略——例如 [[entities/SelectiveChannel|SelectiveChannel]] 可用一致性哈希，而其包含的 sub channel 可使用轮询，形成强大的组合模式。当某个 sub channel 请求失败时，系统可根据负载均衡算法按策略重试其他 sub channel，进一步提升容错性。

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