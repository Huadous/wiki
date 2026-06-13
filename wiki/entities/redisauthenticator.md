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
  - "认证器"
  - "Redis 认证器"
  - "Redis 认证类"
---

## Related Entities
- [[entities/brpc|brpc]] — 所属框架
- [[entities/redisrequest|redisrequest]] — Redis 请求类
- [[entities/redis_cli|redis_cli]] — Redis 命令行工具
- [[entities/redis|redis]] — Redis 数据库
- [[entities/redisreply|redisreply]] — Redis 回复对象
- [[entities/redisresponse|redisresponse]] — Redis 响应类
- [[entities/hiredis|hiredis]] — Redis C 客户端
- [[entities/twemproxy|twemproxy]] — Redis 代理

## Related Concepts
- [[concepts/authentication|认证]] — 身份验证机制

## Mentions in Source
> **Source: [[sources/en_redis_client|en_redis_client]]**
> - "Create a RedisAuthenticator, and set to ChannelOptions."
> - "brpc::policy::RedisAuthenticator* auth = new brpc::policy::RedisAuthenticator("my_password");"
> - "options.auth = auth;"

> **Source: [[sources/redis_client|redis_client]]**
> - "创建一个RedisAuthenticator，并设置到ChannelOptions里即可。"
> - "brpc::policy::RedisAuthenticator* auth = new brpc::policy::RedisAuthenticator("my_password"); options.auth = auth;"