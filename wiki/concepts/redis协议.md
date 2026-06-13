---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_redis_client]]"
  - "[[sources/redis_client]]"
tags:
  - "standard"
aliases:
  - "RESP (REdis Serialization Protocol)"
  - "Redis wire protocol"
---

## Related Concepts

- [[concepts/bthread|bthread]]
- [[concepts/连接池|连接池]]

## Related Entities

- [[entities/brpc|brpc]]
- [[entities/redis|redis]]
- [[entities/hiredis|hiredis]]
- [[entities/redisrequest|redisrequest]]
- [[entities/redisreply|redisreply]]
- [[entities/redisresponse|redisresponse]]
- [[entities/redisauthenticator|redisauthenticator]]
- [[entities/redis_cli|redis_cli]]
- [[entities/twemproxy|twemproxy]]

## Mentions in Source

> **Source: [[sources/en_redis_client|en_redis_client]]**
> - "In order to access redis servers more conveniently and make full use of bthread's capability of concurrency, brpc directly supports the redis protocol."
> - "Similarly with http, brpc guarantees that the time complexity of parsing redis replies is O(N) in worst cases rather than O(N^2), where N is the number of bytes of reply."

> **Source: [[sources/redis_client|redis_client]]**
> - "为了使用户更快捷地访问redis并充分利用bthread的并发能力，brpc直接支持redis协议。"
> - "像http一样，brpc保证在最差情况下解析redis reply的时间复杂度也是O(N)，N是reply的字节数，而不是O(N^2)。"
> - "每个reply可能是：REDIS_REPLY_NIL、REDIS_REPLY_STATUS、REDIS_REPLY_STRING、REDIS_REPLY_ERROR、REDIS_REPLY_INTEGER、REDIS_REPLY_ARRAY。"