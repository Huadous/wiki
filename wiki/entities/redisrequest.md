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
  - "Redis 请求类"
  - "RedisRequest 类"
  - "BRPC Redis 请求"
---

## Related Entities
- [[entities/RedisResponse|RedisResponse]]
- [[entities/RedisReply|RedisReply]]
- [[entities/RedisAuthenticator|RedisAuthenticator]]
- [[entities/brpc|brpc]]
- [[entities/redis|redis]]
- [[entities/hiredis|hiredis]]

## Related Concepts
- [[concepts/位置对应|位置对应]]

## Mentions in Source
> **Source: [[sources/en_redis_client|en_redis_client]]**
> - "A RedisRequest may contain multiple commands by calling AddCommand*, which returns true on success and false otherwise."
> - "Use command_size() to get number of commands added successfully."
> - "Call Clear() before re-using the RedisRequest object."
> - "AddCommandByComponents is similar to redisCommandArgv in hiredis."

> **Source: [[sources/redis_client|redis_client]]**
> - "RedisRequest可包含多个Command，调用AddCommand*增加命令。"
> - "注意，AddCommand和AddCommandV的fmt参数如果设置错误，有可能导致程序crash或者数据泄露，请谨慎设置。"
> - "Clear()后可重用RedisRequest"