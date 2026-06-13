---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[brpc/consistent_hashing.md]]"
tags:
  - "product"
aliases:
  - "Memcached"
  - "memcached缓存系统"
---

## Related Entities
- [[entities/brpc|brpc]] — 提供Memcached协议原生支持以及 `c_md5` 负载均衡器以兼容 memcached 集群的RPC框架

## Related Concepts
- [[concepts/rpc|RPC]] — 远程过程调用框架，brpc通过RPC方式支持Memcached协议
- [[concepts/serialization|Serialization]] — 序列化概念，与缓存系统中数据的存储和传输相关
- [[concepts/cache|缓存]] — 内存缓存技术，Memcached是该领域的关键实现之一
- [[concepts/md5|md5]] — memcached 默认使用的哈希算法，brpc 提供 `c_md5` 负载均衡器以保证兼容性
- [[concepts/consistent-hashing|一致性哈希]] — brpc 在访问 memcached 集群时所采用的负载均衡方式
- [[concepts/hash-ring|Hash Ring]] — 一致性哈希用于定位后端节点的环形结构

## Mentions in Source

> **Source: [[sources/consistent_hashing|consistent_hashing]]**
> - "由于memcache默认使用md5，访问memcached集群时请选择c_md5保证兼容性，其他场景可以选择c_murmurhash以获得更高的性能和更均匀的分布。"