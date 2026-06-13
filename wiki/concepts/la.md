---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
tags: [method]
aliases:
  - "locality-aware"
  - "本地性感知负载均衡"
  - "la 负载均衡"
---


# la

## 定义
la（locality-aware，本地性感知负载均衡）是 [[sources/load_balancing|brpc 负载均衡]] 框架中的一种内置算法。它优先选择延时低的下游服务器，并在所选服务器延时高于其他机器时自动切换目标，整个过程无需额外配置，由框架根据历史延时数据动态选择最优目标。

## 关键特征
- **延时驱动选路**：持续记录各下游服务器的请求延时，优先将请求路由到延时最低的节点。
- **自动目标切换**：当当前目标服务器的延时被其他机器超过时，自动切换到新的最优目标。
- **零配置**：无需用户额外设置参数，框架会自动根据历史数据自适应。
- **算法并列**：与 rr、wrr、random、wr、c_murmurhash、c_md5 等算法并列，作为 brpc 提供的可选负载均衡算法之一。
- **不兼容集群宕机恢复限流**：目前集群宕机恢复限流机制仅对 rr 和 random 算法有效，la 不在支持范围内，因为该限流机制要求下游 server 能力类似。

## 应用
- 下游服务器分布在不同地理位置或多机房的部署场景，借助延时差异就近选择最优节点。
- 跨 IDC 部署中对网络抖动敏感的服务，通过历史延时数据规避高延时链路。
- 后端实例性能存在动态波动、希望自动追踪最优节点的场景。

## 相关概念
- [[concepts/负载均衡|负载均衡]]
- [[concepts/一致性哈希|一致性哈希]]
- [[concepts/rr|rr]]
- [[concepts/random|random]]
- [[concepts/wrr|wrr]]
- [[concepts/集群宕机恢复限流|集群宕机恢复限流]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/brpc-channel|brpc::Channel]]
- [[entities/brpc-client|brpc client]]

## 来源提及
- "locality-aware，优先选择延时低的下游，直到其延时高于其他机器，无需其他设置。" — [[sources/client]]
- "实现原理请查看[Locality-aware load balancing](lalb.md)。" — [[sources/client]]
- "此恢复机制要求下游server的能力是类似的，所以目前只针对rr和random有效" — [[sources/client]]