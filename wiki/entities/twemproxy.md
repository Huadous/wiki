---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_redis_client]]"
  - "[[concepts/单线程反应器]]"
  - "[[sources/redis_client]]"
tags:
  - "product"
aliases:
  - "Twemproxy"
  - "nutcracker"
---

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/redis|Redis]]
- [[entities/envoy-proxy|Envoy proxy]] — 另一类代理方案，用于服务网格场景
- [[entities/hiredis|hiredis]] — Redis C客户端库
- [[entities/redis_cli|redis_cli]] — brpc Redis CLI工具

## Related Concepts
- [[concepts/backward-compatibility|一致性哈希]] — 用于替代 twemproxy 代理的客户端路由策略
- [[concepts/serialization|Redis协议]] — twemproxy 代理的底层通信协议
- [[concepts/单线程反应器|单线程反应器]] — 与 Redis 连接管理和代理影响相关
- [[concepts/连接池|连接池]] — 代理连接管理涉及的池化技术
- [[concepts/一致性哈希负载均衡|一致性哈希负载均衡]] — brpc通过此机制直接访问Redis集群，替代代理方案

## Mentions in Source

> **Source: [[sources/en_redis_client|en_redis_client]]**
> - "Another choice is to use the common twemproxy solution, which makes clients access the cluster just like accessing a single server, although the solution needs to deploy proxies and adds more latency."

> **Source: [[sources/单线程反应器|单线程反应器]]**
> - 相关实体: twemproxy — 该代理在文档中被列为相关实体，与 Redis 单线程反应器模型有关联，但未在正文中详细讨论。

> **Source: [[sources/redis_client|redis_client]]**
> - "或者你可以沿用常见的twemproxy方案。"
> - "这个方案虽然需要额外部署proxy，还增加了延时，但client端仍可以像访问单点一样的访问它。"