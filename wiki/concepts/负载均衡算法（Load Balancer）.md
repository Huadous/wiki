---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/combo_channel]]"
  - "[[sources/en_overview]]"
  - "[[brpc/load_balancing.md]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/client.md]]"
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
  - "brpc::LoadBalancer"
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
- [[concepts/Locality-aware load balancing|Locality-aware load balancing]]
- [[concepts/集群宕机恢复限流|集群宕机恢复限流]]

## Related Entities
- [[entities/SelectiveChannel|SelectiveChannel]]
- [[entities/ParallelChannel|ParallelChannel]]
- [[entities/brpc|brpc]]
- [[entities/bns|bns]]
- [[entities/etcd|etcd]]
- [[entities/zookeeper|zookeeper]]
- [[entities/brpc::Channel|brpc::Channel]]
- [[entities/brpc::Controller|brpc::Controller]]
- [[entities/brpc::SocketMap|brpc::SocketMap]]
- [[entities/brpc::Socket|brpc::Socket]]

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

> **Source: [[sources/en_client|en_client]]**
> - "When there're more than one server to access, we need to divide the traffic. The process is called load balancing"
> - "Algorithms provided by brpc (specified by `load_balancer_name`): rr, wrr, random, wr, la, c_murmurhash or c_md5"
> - "la: which is locality-aware. Perfer servers with lower latencies"

> **Source: [[sources/client|client]]**
> - "当下游机器超过一台时，我们需要分割流量，此过程一般称为负载均衡，在client端的位置如下图所示"
> - "rr 即round robin，总是选择列表中的下一台服务器，结尾的下一台是开头，无需其他设置。"
> - "c_murmurhash or c_md5 一致性哈希，与简单hash的不同之处在于增加或删除机器时不会使分桶结果剧烈变化，特别适合cache类服务。"
> - "从进程级的[SocketMap](https://github.com/apache/brpc/blob/master/src/brpc/socket_map.h)中或从[LoadBalancer](https://github.com/apache/brpc/blob/master/src/brpc/load_balancer.h)中选择一台下游server作为本次RPC发送的目的地。"
> - "这类Channel需要定期从naming_service_url指定的命名服务中获得服务器列表，并通过load_balancer_name指定的负载均衡算法选择出一台机器发送请求。"