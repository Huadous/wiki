---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_redis_client]]"
  - "[[sources/redis_client]]"
tags:
  - "product"
aliases:
  - "Redis 回复对象"
  - "Redis 回复"
---

## Related Entities
- [[entities/redisresponse|redisresponse]] — 包含一个或多个 RedisReply 对象的回复容器
- [[entities/redisrequest|redisrequest]] — 构建 Redis 请求的类，与 RedisReply 对应形成请求-回复模式
- [[entities/brpc|brpc]] — 提供 RedisReply 的 RPC 框架
- [[entities/hiredis|hiredis]] — 底层 Redis C 客户端库，brpc Redis 实现的基础
- [[entities/redis|redis]] — Redis 数据库系统

## Related Concepts
- [[concepts/redis协议|Redis协议]] — RedisReply 实现的基础通信协议
- [[concepts/redisresponse|RedisResponse]] — 包含 RedisReply 的响应容器
- [[concepts/redisrequest|RedisRequest]] — 与 RedisReply 对应的请求构建类