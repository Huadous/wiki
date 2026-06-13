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
  - "Redis 响应类"
  - "响应类"
---

## 相关实体
- [[entities/redisrequest|RedisRequest]]
- [[entities/redisreply|RedisReply]]
- [[entities/hiredis|hiredis]]
- [[entities/brpc|brpc]]
- [[entities/redis|Redis]]
- [[entities/redisauthenticator|RedisAuthenticator]]

## 相关概念
- [[concepts/位置对应-positional-correspondence|位置对应-positional-correspondence]]

## 来源提及
> **Source: [[sources/en_redis_client|en_redis_client]]**
> - "A RedisResponse may contain one or multiple RedisReplys."
> - "Use reply_size() for total number of replies and reply(i) for reference to the i-th reply."
> - "As long as RPC is successful, response.reply_size() should be equal to request.command_size(), unless the redis-server is buggy."

> **Source: [[sources/redis_client|redis_client]]**
> - "RedisResponse已经包含了N个reply，通过reply(i)获取就行了。"
> - "只要RPC成功，response.reply_size()应与request.command_size()相等"
> - "response中的所有reply的ownership属于response。当response析构时，reply也析构了。"