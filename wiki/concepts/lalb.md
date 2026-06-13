---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/lalb]]"
  - "[[sources/en_overview]]"
  - "[[brpc/en_client.md]]"
tags:
  - "method"
aliases:
  - "Locality-aware load balancing"
  - "LALB算法"
  - "Load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "Load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "Load Balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "Load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "Load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "locality-aware load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "Load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "Load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "Load Balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "Load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
  - "Load balancing"
  - "Locality-aware load balancing"
  - "LALB算法"
---

## Description
LALB 全称 Locality-aware load balancing，是一种自适应负载均衡算法，其核心思想以下游节点的吞吐量除以延迟作为分流权值。算法持续统计 QPS 和延迟数据，动态调整权值，最终使各节点的延迟趋同，从而自动将流量引导到性能最佳的节点。该算法并不是按照延迟的比例来分流，例如一个下游30ms、另一个60ms时，流量比例并不是60/30，而是30ms的节点会一直获得流量直到其延迟高于60ms，或没有更多流量可用。引入的飞行中延迟（inflight delay）机制能够迅速对故障节点进行惩罚，减少对异常节点的流量分配。在实现上，LALB 通过 [[concepts/weight-tree|权值树]] 和 [[concepts/DoublyBufferedData|DoublyBufferedData]] 数据结构实现高效查找，并优先访问本机或同机架的服务以减少网络开销。该算法产生自 [[entities/dp系统|DP 2.0]] 系统，随后被收录到 [[entities/brpc|brpc]] 框架中，成为默认负载均衡算法之一。在 brpc 中，用户可以通过指定负载均衡策略（包括轮询、随机、一致性哈希和局部感知）来为每个请求选择最合适的机器，从而适应不同场景下的服务特性。在 brpc 客户端中，LALB 通过将 `load_balancer_name` 设为 `la` 来启用，配置简洁，无需其他额外设置：算法持续探测各服务器的访问延迟，优先选择延迟较低的服务器，直到该服务器的延迟明显高于其他服务器时才切换目标。负载均衡通常与[[concepts/naming-service|命名服务]]配合使用。算法在稳定状态下能够使各节点延时趋同，实现全局延时优化，特别适合混合部署、机器配置不一、网络延迟差异大的环境，被广泛应用于微服务架构、数据库代理层和 API 网关等场景。brpc 对 locality-aware 负载均衡的实现使其能够感知请求来源的本地性，在多数据中心或跨地域部署场景下有效降低跨网络请求的延迟。

## Related Concepts
- [[concepts/qps|qps]]
- [[concepts/延迟|延迟]]
- [[concepts/DoublyBufferedData|DoublyBufferedData]]
- [[concepts/weight-tree|权值树]]
- [[concepts/base_weight|基础权值]]
- [[concepts/inflight-delay|飞行中延迟]]
- [[concepts/一致性哈希|一致性哈希]]
- [[concepts/parallelchannel|parallelchannel]]
- [[concepts/lalb|lalb]]
- [[concepts/RPC|RPC]]
- [[concepts/naming-service|命名服务]]
- [[concepts/负载均衡|负载均衡]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/twemproxy|twemproxy]]
- [[entities/envoy-proxy|envoy-proxy]]
- [[entities/redis|redis]]
- [[entities/dp系统|dp系统]]
- [[entities/ub|ub]]
- [[entities/bns|bns]]
- [[entities/baidu|baidu]]

## Mentions in Source

> **Source: [[sources/lalb|lalb]]**
> - "LALB全称Locality-aware load balancing，是一个能把请求及时、自动地送到延时最低的下游的负载均衡算法，特别适合混合部署环境。"
> - "基本原理非常简单：以下游节点的吞吐除以延时作为分流权值。"
> - "算法并不是按照延时的比例来分流……而是30ms的节点会一直获得流量直到它的延时高于60ms，或者没有更多流量了。"
> - "LALB会优先访问这些最近的节点。"
> - "在DP 2.0中我们使用了一种新的算法: Locality-aware load balancing，能根据下游节点的负载分配流量，还能快速规避失效的节点，在很大程度上，这种算法的延时也是全局最优的。"

> **Source: [[sources/en_overview|en_overview]]**
> - "Users specify load balancing algorithms to choose one machine for each request from all machines, including: round-robin, randomized, consistent-hashing(murmurhash3 or md5) and locality-aware."
> - "round-robin, randomized, [consistent-hashing](../cn/consistent_hashing.md)(murmurhash3 or md5) and [locality-aware](../cn/lalb.md)."

> **Source: [[sources/en_client|en_client]]**
> - "la: which is locality-aware. Perfer servers with lower latencies, until the latency is higher than others, no other settings."
> - "Check out [Locality-aware load balancing](lalb.md) for more details."