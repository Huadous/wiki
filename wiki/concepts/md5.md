---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/consistent_hashing|consistent_hashing]]"]
tags: [method]
aliases:
  - "MD5"
  - "md5"
---


# md5

## 定义
md5 是 brpc 一致性哈希负载均衡器内置支持的哈希算法之一。在 brpc 中，可通过将 `load_balancer_name` 设置为 `c_md5` 来启用该算法。其本质是对输入 key 计算 md5 摘要，并取摘要的 32 位无符号整数部分用于一致性哈希环上的节点定位与请求路由。

## 关键特征
- 哈希算法实现：基于标准 md5 摘要算法，与 murmurhash3 并列为 brpc 一致性哈希负载均衡器内置的两种哈希实现。
- 启用方式：在 brpc 客户端通过 `load_balancer_name = "c_md5"` 指定。
- 输出要求：与 `c_murmurhash` 相同，最终输出必须是 32 位无符号整数（`uint32_t`），以便在同一哈希环空间内参与一致性哈希计算。
- 端到端无关性：request 端使用的哈希算法不需要与 lb 端使用的哈希算法保持一致，只要输出为 32 位无符号整数即可，c_md5 与 c_murmurhash 在 lb 端可互换使用。
- 生态兼容性优先：c_md5 主要是为了兼容既有生态系统（如 memcached），而非性能或分布均匀性上的优化选择。

## 应用
- 访问 memcached 集群：memcache 协议默认使用 md5 对 key 做哈希，因此 brpc 在访问 memcached 集群时必须选择 `c_md5`，以保证客户端哈希结果与 memcached 协议层期望一致，避免路由到错误的节点。
- 已有基于 md5 的客户端哈希体系接入：在已有生态（例如其他语言的 memcached 客户端、自定义代理层）统一使用 md5 哈希 key 时，使用 `c_md5` 可保证多端哈希结果一致，减少缓存命中率损失。
- 一般一致性哈希场景：除 memcached 外，其他场景官方推荐使用 `c_murmurhash` 以获得更高的哈希计算性能和更均匀的分布，因此 md5 在 brpc 中通常仅作为兼容性选项出现。

## 相关概念
- [[concepts/consistent-hashing|一致性哈希]]
- [[concepts/murmurhash3|murmurhash3]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "由于memcache默认使用md5，访问memcached集群时请选择c_md5保证兼容性，其他场景可以选择c_murmurhash以获得更高的性能和更均匀的分布。" — [[sources/consistent_hashing|consistent_hashing]]
- "我们内置了分别基于murmurhash3和md5两种hash算法的实现" — [[sources/consistent_hashing|consistent_hashing]]