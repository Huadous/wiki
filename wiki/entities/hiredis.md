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
  - "hiredis 客户端"
  - "Redis C 客户端"
---

## Related Entities

- [[entities/brpc|brpc]]：提供了优于hiredis的Redis客户端实现，线程安全且支持多种连接方式
- [[entities/redis|Redis]]：hiredis所连接的Redis服务器，也是Redis协议的实现者
- [[entities/twemproxy|twemproxy]]：Redis中间件代理，与hiredis同属Redis生态系统
- [[entities/redisreply|redisreply]]：hiredis中用于封装Redis回复的对象
- [[entities/redis_cli|redis_cli]]：brpc提供的Redis CLI工具，与hiredis客户端对比测试

## Related Concepts

- [[concepts/单线程反应器|单线程反应器]]：hiredis连接池性能瓶颈的根本原因，也是hiredis架构局限性的核心
- [[concepts/连接池|连接池]]：hiredis池化连接模式在性能上低于brpc单连接，并反映了单线程反应器架构的局限性
- [[concepts/QPS|QPS]]：hiredis风格的连接池在测试中QPS远低于brpc
- [[concepts/延迟|延迟]]：hiredis多连接模式带来的额外IO开销增加了延迟
- [[concepts/Redis协议|Redis协议]]：hiredis与brpc Redis客户端共同遵循的通信协议，两者在基本格式上兼容