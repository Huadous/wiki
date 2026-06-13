---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/lalb]]"]
tags: [phenomenon]
aliases:
  - "CPU空闲悖论"
  - "CPU闲置悖论"
  - "CPU Idle悖论"
---


# CPU Idle Paradox

## 定义
CPU Idle Paradox（CPU空闲悖论）是指在基于CPU占用率进行负载均衡时，权值转换过程中出现的数学悖论。假设两台机器权值之比等于CPU idle之比，当按此比例分流后，预期CPU idle会更接近，但这一变化又会导致分流比例随之调整，使得CPU idle再次出现差距。这种自指性的循环矛盾揭示了单一CPU指标难以稳定指导权值分配的根本缺陷。

## 关键特征
- **自指循环性**：权值分配依赖于CPU idle，而权值分配又会改变CPU idle，形成反馈循环
- **数学悖论**：理想状态的均衡点（CPU idle相等）在动态调整中无法稳定收敛
- **指标局限性**：暴露了单一CPU idle指标的固有不稳定性，无法作为唯一负载度量
- **静态算法失效根源**：是[[concepts/weightedstrategy|WeightedStrategy]]等静态自适应算法失败的主要原因之一
- **动态算法促进因素**：其发现间接推动了基于延时和吞吐的动态算法（如[[concepts/lalb|LALB]]）的提出

## 应用
- **负载均衡算法评估**：用于分析为何纯CPU指标方案在实际生产中不可行
- **权值分配策略设计**：指导设计更鲁棒的权值计算公式，避免自指问题
- **系统稳定性分析**：帮助理解分布式系统中反馈控制回路的稳定性条件
- **性能调优**：在[[entities/brpc|brpc]]等RPC框架中选择负载均衡策略时的理论依据

## 相关概念
- [[concepts/lalb|LALB]] — 解决CPU Idle Paradox的动态负载均衡算法，基于延时而非CPU idle
- [[concepts/weightedstrategy|WeightedStrategy]] — 受此悖论影响的静态权值策略
- [[concepts/base_weight|base_weight]] — LALB算法中的基础权值计算方法
- [[concepts/inflight-delay|inflight-delay]] — LALB使用的替代度量指标

## 相关实体
- [[entities/brpc|brpc]] — 提出该悖论的RPC框架
- [[entities/ub|ub]] — 使用WeightedStrategy的中间件平台

## 来源提及
- "假设下游差异仅仅由同机运行的其他程序导致，机器配置和网络完全相同，两台机器权值之比是cpu idle之比吗？假如是的，当我们以这个比例给两台机器分流之后，它们的cpu idle应该会更接近对吧？而这会导致我们的分流比例也变得接近，从而使两台机器的cpu idle又出现差距。你注意到这个悖论了吗？" — [[brpc/lalb|lalb]]