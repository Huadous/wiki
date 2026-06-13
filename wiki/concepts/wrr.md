---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [method]
aliases:
  - "Weighted Round Robin"
  - "weighted round robin load balancer"
  - "wrr 负载均衡算法"
---


# wrr

## 定义
wrr 是 brpc 中的一种加权轮询（weighted round-robin）负载均衡算法。它按照每个服务器配置的权重比例来选择服务器，同时尽量使各个服务器的选中在列表中均匀分布。服务器权重通过实例的 tag 字段传递，tag 必须是一个 int32 数字（例如 `tag="50"`）。

## 关键特征
- 按权重比例选择服务器：每个服务器被选中的概率与其配置的权重成正比。
- 选择分布均匀：算法在保证权重比例的前提下，使每次选择尽量分散在列表中，避免短时间内对同一后端造成热点。
- 通过 tag 配置权重：实例 tag 必须为 int32 数字形式（如 `tag="50"`），作为该实例的权重。
- 相对 rr 的扩展：相比不带权重的 [[concepts/rr|rr]]，wrr 适用于后端容量不一致或希望按资源比例分配流量的场景。
- 与 [[concepts/wr|wr]] 同属带权重的负载均衡策略家族，但 wrr 侧重轮询式均匀分布，[[concepts/wr|wr]] 则依据当前负载进行动态选取。

## 应用
- 在多台容量或处理能力不同的后端服务器之间按比例分配请求流量。
- 在多个 VIP（虚拟 IP）共存、需要为不同 VIP 指定不同权重比例的 VIP 相关部署场景中，是官方推荐方案之一。
- 与 [[concepts/Load Balancer|Load Balancer]] 配合使用，作为 brpc 服务发现与流量调度体系中的核心策略之一。

## 相关概念
- [[concepts/Load Balancer|Load Balancer]]
- [[concepts/rr|rr]]
- [[concepts/random|random]]
- [[concepts/wr|wr]]
- [[concepts/VIP|VIP]]

## 相关实体
无相关实体。

## 来源提及
- which is weighted round robin. Choose the next server according to the configured weight. The chances a server is selected is consistent with its weight, and the algorithm can make each server selection scattered. — [[sources/en_client]]
- The instance tag must be an int32 number representing the weight, eg. `tag="50"`. — [[sources/en_client]]