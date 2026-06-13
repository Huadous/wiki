---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/flatmap|flatmap]]"]
tags: [method]
aliases:
  - "Murmur Hash"
  - "MurmurHash3"
---


# Murmurhash

## 定义
Murmurhash 是一族非加密型哈希函数，适用于通用的哈希查找场景。它由 Austin Appleby 设计，核心目标是在不依赖加密安全性的前提下，提供极快的计算速度和良好的分布质量，是工业级系统中常用的通用哈希算法之一。

## 关键特征
- **非加密型哈希**：不提供抗碰撞、抗预映像等加密安全保证，专注于通用哈希场景的吞吐量与分布质量
- **雪崩效应良好**：输入的微小变化会导致输出哈希值产生大幅且均匀的变化，从而降低哈希冲突概率
- **计算速度快**：实现简洁且高度优化，能够在现代 CPU 上以极高速度处理大量数据
- **充分利用现代 CPU 特性**：算法设计中考虑了 CPU 流水线和整数运算特性，适合大规模并发的服务端场景
- **多版本演进**：包含 MurmurHash1、MurmurHash2、MurmurHash3 等多个版本，针对不同应用场景持续优化

## 应用
- 在 [[sources/flatmap|flatmap]] 等高性能哈希容器中作为通用哈希函数使用
- 大数据处理系统中的数据分片与负载均衡
- 数据库、缓存等需要快速键值映射的存储结构
- 分布式系统中的节点路由与一致性哈希
- 任何对哈希速度敏感、但无需加密安全性的内部数据结构

## 相关概念
- [[concepts/哈希函数|哈希函数]]
- [[concepts/雪崩效应|雪崩效应]]
- [[concepts/线性同余|线性同余]]

## 相关实体
- [[entities/flatmap|FlatMap]]
- [[entities/smalltable|smalltable]]
- [[entities/cowhashmap|CowHashMap]]
- [[entities/alignhashmap|AlignHashMap]]
- [[entities/stdmap|std::map]]

## 来源提及
- 通用算法可选择Murmurhash。 — [[sources/flatmap|flatmap]]
- 对于工程师来说，选用何种算法得看实践效果，一些最简单的方法也许就有很好的效果。 — [[sources/flatmap|flatmap]]