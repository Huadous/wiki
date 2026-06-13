---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/consistent_hashing.md]]"
tags: [一致性哈希, Hash Ring, 虚拟节点, murmurhash3, md5, 平衡性, 单调性, 分散性, 负载, 雪崩, Double Buffered Data]
aliases: ["brpc 一致性哈希", "Consistent Hashing in brpc"]
---

# 一致性哈希（Consistent Hashing）- Summary

## 来源
- Original file: [[brpc/consistent_hashing.md]]
- Ingested: 2026-06-13

## 核心内容
本文档来源于 [[entities/brpc|brpc]] 官方文档站点，介绍了一致性哈希负载均衡策略的原理与实现。在分布式缓存等场景中，简单的 `hash(x) % n` 在节点数量变化时会导致几乎全部请求重新映射，从而引发[[concepts/雪崩|雪崩]]。[[concepts/一致性哈希|一致性哈希]]通过将所有 server 的 32 位 hash 值构成一个[[concepts/hash-ring|Hash Ring]]，使得增减节点时只影响相邻区间的部分请求，实现平滑迁移。该算法满足[[concepts/平衡性|平衡性]]、[[concepts/单调性|单调性]]、[[concepts/分散性|分散性]]和[[concepts/负载|负载]]四个关键性质。文档重点阐述了 brpc 如何引入[[concepts/虚拟节点|虚拟节点]]解决节点较少时区间不均衡的问题，以及如何选择有序数组存储 Hash Ring 以获得更高的二分查找效率，并内置 [[concepts/murmurhash3|murmurhash3]] 与 [[concepts/md5|md5]] 两种哈希算法实现。

## 关键实体
- [[entities/brpc|brpc]]：Apache 开源 RPC 框架，本文一致性哈希策略的所属框架
- [[entities/memcached|memcached]]：分布式内存缓存系统，brpc 通过 c_md5 实现与其协议兼容

## 关键概念
- [[concepts/一致性哈希|一致性哈希]]：一种在节点动态变化时实现请求平滑迁移的哈希算法
- [[concepts/hash-ring|Hash Ring]]：将 server 的 32 位 hash 值映射到环形值域所形成的数据结构
- [[concepts/虚拟节点|虚拟节点]]：为每个 server 计算多个 hash 值以均匀化区间划分的技术
- [[concepts/murmurhash3|murmurhash3]]：brpc 内置的高性能哈希算法，对应 `c_murmurhash`
- [[concepts/md5|md5]]：brpc 内置的哈希算法，对应 `c_md5`，用于兼容 memcached
- [[concepts/平衡性|平衡性]]：每个节点被选中的概率为 O(1/n)
- [[concepts/单调性|单调性]]：新增节点时请求只从老节点迁移到新节点
- [[concepts/分散性|分散性]]：不同下游列表视角下同一请求尽量映射到少量节点
- [[concepts/负载|负载]]：不同视角下各下游服务器分到的请求数量尽量一致
- [[concepts/雪崩|雪崩]]：因缓存大面积同时失效引发的级联崩溃现象
- [[concepts/double-buffered-data|double-buffered-data]]：brpc 用于保证 Hash Ring 线程安全性的双缓冲并发模式

## 要点
- **平滑迁移机制**：一致性哈希通过 Hash Ring 实现节点增减时仅部分请求路由发生改变，避免传统模运算哈希引发的缓存雪崩
- **四项核心性质**：算法需同时满足平衡性、单调性、分散性和负载
- **虚拟节点策略**：每个 server 默认生成 100 个虚拟节点（可通过 `-chash_num_replicas` 或 `replicas=<num>` 参数调整），均匀化区间并分散故障转移压力
- **数据结构选型**：brpc 选择有序数组而非平衡二叉树，修改复杂度 O(n)，但利用连续存储获得更高的二分查找效率
- **两种哈希算法**：访问 memcached 集群时必须使用 `c_md5` 以保证兼容性，其他场景推荐 `c_murmurhash` 以获得更高性能与更均匀分布
- **线程安全保障**：Hash Ring 的线程安全性通过 [[concepts/double-buffered-data|double-buffered-data]] 双缓冲机制实现，避免读写锁开销