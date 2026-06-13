---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [method]
aliases:
  - "Weighted Random"
  - "weighted random load balancer"
---


# wr

## 定义
wr（weighted random，加权随机）是 brpc 所提供的一种负载均衡算法。该算法按照每个服务端配置的权重，以与权重成比例的概率随机选择一个服务端作为下一个请求的目标。wr 在权重配置上与 wrr 完全一致，但二者的区别在于：wrr 以确定的轮询顺序依次选择服务端，而 wrr 对应的 wr 则以随机顺序进行选择。这种随机化的选择顺序在某些场景下非常有用——例如，当请求顺序之间的微小关联性会对后端处理造成问题时，使用 wr 可以打破这种关联性。

## 关键特征
- 基于权重进行随机选择：服务端被选中的概率与其配置的权重成正比
- 实例标签（instance tag）要求与 wrr 相同：必须为一个 int32 数值，表示该服务端的权重
- 选择顺序是随机的，而不是像 wrr 那样按确定性的轮询顺序
- 适用于需要打散请求顺序关联性的后端服务场景

## 应用
- 后端服务对请求到达顺序敏感、希望避免连续到达请求之间存在相关性时的负载均衡场景
- 适用于需要按权重分配流量，但又不希望出现确定性轮询模式的分布式系统
- 与 wrr 的确定性轮询相比，wr 提供的随机顺序选择可以在统计意义上提供更平滑的流量分布，避免某些后端节点因请求顺序相关性而出现热点

## 相关概念
- [[concepts/load-balancer|Load Balancer]]
- [[concepts/rr|rr]]
- [[concepts/wrr|wrr]]
- [[concepts/random|random]]

## 相关实体
No related entities

## 来源提及
- "which is weighted random. Choose the next server according to the configured weight. The chances a server is selected is consistent with its weight." — [[sources/en_client]]
- "Requirements of instance tag is the same as wrr." — [[sources/en_client]]