---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_redis_client]]"
  - "[[sources/redis_client]]"
tags:
  - "term"
aliases:
  - "-redis_verbose"
  - "verbose 调试标志"
  - "redis_verbose_crlf2space"
  - "-redis_verbose"
  - "verbose 调试标志"
---

## Related Concepts
- [[concepts/Redis协议|Redis协议]]
- [[concepts/调试标志|调试标志]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/redis|redis]]
- [[entities/redisrequest|redisrequest]]
- [[entities/redisresponse|redisresponse]]
- [[entities/hiredis|hiredis]]

## Mentions in Source

> **Source: [[sources/en_redis_client|en_redis_client]]**
> - "Turn on -redis_verbose to print contents of all redis requests and responses."
> - "Note that this should only be used for debugging rather than online services."
> - "Turn on -redis_verbose_crlf2space to replace the CRLF (\r\n) with spaces in debugging logs for better readability."

> **Source: [[sources/redis_client|redis_client]]**
> - "打开-redis_verbose即看到所有的redis request和response，注意这应该只用于线下调试，而不是线上程序。"
> - "打开-redis_verbose_crlf2space可让打印内容中的CRLF (\r\n)变为空格，方便阅读。"
> - "| redis_verbose_crlf2space | false | [DEBUG] Show \r\n as a space | src/brpc/redis.cpp |"