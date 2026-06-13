---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_redis_client]]"
  - "[[concepts/单线程反应器]]"
  - "[[sources/redis_client]]"
  - "[[sources/en_overview]]"
tags:
  - "product"
aliases:
  - "redis-server"
  - "Redis 数据库"
---

## Related Entities
- [[entities/memcached|Memcached]]
- [[entities/baidu|百度]]
- [[entities/braft|braft]]

## Related Concepts
- [[concepts/redis-protocol|Redis协议]]
- [[concepts/单线程反应器|单线程反应器]]
- [[concepts/QPS|QPS]]
- [[concepts/延迟|延迟]]
- [[concepts/bthread|bthread]]
- [[concepts/连接池|连接池]]
- [[concepts/一致性哈希负载均衡|一致性哈希负载均衡]]
- [[concepts/RPC|RPC]]
- [[concepts/序列化|序列化]]
- [[concepts/缓存|缓存]]

## Mentions in Source

> **Source: [[sources/en_redis_client|en_redis_client]]**
- "redis (http://redis.io/) is one of the most popular caching service in recent years."
- "redis-server is a single-threaded reactor, utilizing one core is the maximum that it can do."
- "redis version: 2.6.14"

> **Source: [[sources/单线程反应器|单线程反应器]]**
- "Redis 服务器即采用此架构，因此尽管支持多连接，其吞吐量仍受单线程处理能力的限制。"
- "Note that redis-server is a single-threaded reactor, utilizing one core is the maximum that it can do."
- "We can see a tremendous drop of QPS compared to the one using single connection above, and the redis-server has reached the CPU cap."

> **Source: [[sources/redis_client|redis_client]]**
- "redis是最近几年比较火的缓存服务，相比memcached在server端提供了更多的数据结构和操作方法，简化了用户的开发工作。"
- "redis_channel.Init(\"0.0.0.0:6379\", &options)  // 6379是redis-server的默认端口"
- "redis-server实际处理的qps要乘10。"
- "redis-server是单线程reactor，一个核心打满就意味server到极限了。"

> **Source: [[sources/en_overview|en_overview]]**
- "[redis](redis_client.md) and [memcached](memcache_client.md), thread-safe, more friendly and performant than the official clients"
- "You can use it to: Build a server that can talk in multiple protocols (on same port), or access all sorts of services"