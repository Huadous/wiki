---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/combo_channel]]"
  - "[[sources/en_overview]]"
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
---

## 描述

负载均衡算法是分布式系统中在多个服务实例之间分配请求的关键策略。brpc 支持多种负载均衡算法，包括轮询（round-robin）、随机（randomized）、一致性哈希（consistent-hashing，基于 murmurhash3 或 md5）以及局部感知（locality-aware）。用户通过命名服务发现后端机器列表，并在初始化 Channel 时指定负载均衡算法，框架会根据所选算法对每个请求选择一台机器。这种机制使得 brpc 能够实现高可用性和可扩展性，同时支持灵活的层级化组合策略——例如 `SelectiveChannel` 可用一致性哈希，而其包含的 sub channel 可使用轮询，形成强大的组合模式。当某个 sub channel 请求失败时，系统可根据负载均衡算法按策略重试其他 sub channel，进一步提升容错性。

## 相关概念
- [[concepts/命名服务|命名服务]]
- [[concepts/一致性哈希|一致性哈希]]
- [[concepts/容量计算规则|容量计算规则]]
- [[concepts/RPC|RPC]]

## 相关实体
- [[entities/SelectiveChannel|SelectiveChannel]]
- [[entities/ParallelChannel|ParallelChannel]]
- [[entities/brpc|brpc]]
- [[entities/bns|bns]]
- [[entities/etcd|etcd]]
- [[entities/zookeeper|zookeeper]]

## 来源提及

> **Source: [[sources/combo_channel|combo_channel]]**
> - "if (channel.Init('c_murmurhash', &schan_options) != 0) { "
> - "sub_channel->Init(ns_node_name[i], 'rr', NULL) != 0) { "
> - "SelectiveChannel按负载均衡算法访问其包含的Channel，相比普通Channel它更加高层：把流量分给sub channel，而不是具体的Server。"

> **Source: [[sources/en_overview|en_overview]]**
> - "Users specify load balancing algorithms to choose one machine for each request from all machines, including: round-robin, randomized, consistent-hashing(murmurhash3 or md5) and locality-aware."
> - "load balancers (rr, random, consistent hashing)"