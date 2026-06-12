---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/lalb]]"]
tags: [method]
aliases:
  - "轮询"
  - "RR"
  - "Round Robin"
---


# round-robin

## 定义
Round-robin是一种基础的负载均衡方法，按顺序将请求依次分配给后端的每个服务器节点。它与随机算法并列为最基本的分流方法，实现简单但前提条件是下游机器的处理能力和网络环境高度同质化。

## 关键特征
- **轮询调度**：请求按固定顺序循环分配给每个可用节点，无优先级或权重区分。
- **同质化假设**：假定所有后端服务器性能相同、网络延迟相似，否则会导致性能差的节点拖累整体吞吐。
- **无状态感知**：不感知节点当前负载、延迟或健康状态，仅依赖静态轮转顺序。
- **实现极简**：核心逻辑只需一个计数器取模，几乎无运行时开销。

## 应用
- 最适合服务器规格一致、网络拓扑对称的经典数据中心场景。
- 在混部（colocation）环境下难以适用，因为不同节点资源争抢程度差异大，round-robin会严重拉低全局QPS。
- 常作为负载均衡算法的性能基线或反例，用于对比展示动态感知算法（如LALB）的优势。

## 相关概念
- [[concepts/locality-aware-load-balancing|Locality-aware load balancing]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/nginx|nginx]]
- [[entities/envoy-proxy|envoy-proxy]]

## 来源提及
- "最常见的分流算法是round robin和随机。" — [[sources/lalb|lalb]]
- "'rr' or 'random': ... 'la': ... 真实的场景中不会有这么显著的差异，但你应该能看到差别了。" — [[sources/lalb|lalb]]