---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client|en_client]]"]
tags: [method]
aliases:
  - "Random load balancer"
  - "random load balancing"
---


# random

## 定义
random 是 brpc 中最简单的一种随机化负载均衡算法。它针对每一次请求，从服务器列表中以均匀分布的概率随机选取一台服务器来处理。与 [[concepts/rr|rr]] 类似，该算法假设被访问的服务器在机器规格、网络延迟和负载方面是相似的，因此除了权重（weight）之外不提供针对单台服务器的额外设置。random 是 brpc 中两种支持集群宕机恢复限流机制（cluster-downtime recovery throttling）的负载均衡算法之一（另一种为 [[concepts/rr|rr]]），可通过附加在 `load_balancer_name` 字符串后的 `min_working_instances` 与 `hold_seconds` 参数来启用该机制。

## 关键特征
- 实现最简单：从服务器列表中以等概率随机选择一台服务器，无任何额外状态或调度策略。
- 假设集群中各服务器在机器规格、网络延迟、负载等方面同质，仅依赖权重（weight）进行差异化。
- 支持集群宕机恢复限流机制：通过在 `load_balancer_name` 字符串后追加 `min_working_instances` 与 `hold_seconds` 参数来启用。
- 与 [[concepts/rr|rr]] 共同构成支持上述恢复限流机制的两种负载均衡算法，前提是下游服务器的能力彼此相似。
- 相比 [[concepts/wrr|wrr]] 等加权算法，random 不维护请求计数或加权游标，开销极低。

## 应用
- 适用于后端服务器规模较小、配置基本一致、对请求分布均匀性要求不高的中小规模集群。
- 在临时性、探索性或测试场景中，作为快速接入的默认随机负载均衡选择。
- 在具备一定容灾需求的下游集群中，配合 `min_working_instances` 与 `hold_seconds` 使用，实现集群宕机恢复期间的请求限流保护。
- 与 [[concepts/load-balancer|Load Balancer]]、[[concepts/rr|rr]]、[[concepts/wr|wr]]、[[concepts/la|la]] 等其他负载均衡算法并列选用，根据业务对均匀性、局部性、加权策略等需求做权衡。

## 相关概念
- [[concepts/load-balancer|Load Balancer]]
- [[concepts/rr|rr]]
- [[concepts/wrr|wrr]]
- [[concepts/wr|wr]]
- [[concepts/la|la]]

## 相关实体
无相关实体。

## 来源提及
- "Randomly choose one server from the list, no other settings. Similarly with round robin, the algorithm assumes that servers to access are similar." — [[sources/en_client|en_client]]
- "This recovery mechanism requires the capabilities of downstream servers to be similar, so it is currently only valid for rr and random." — [[sources/en_client|en_client]]