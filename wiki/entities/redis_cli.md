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
  - "brpc-redis-cli"
  - "brpc Redis CLI 工具"
  - "redis-cli"
  - "brpc-redis-cli"
  - "brpc Redis CLI 工具"
---

## Description
redis_cli 是 [[entities/brpc|brpc]] 框架提供的一个命令行工具，位于 `example/redis_c++/redis_cli.cpp`。该工具类似于官方的 redis-cli，用于演示 brpc 与 [[entities/redis|Redis]] 服务器的交互能力。redis_cli 支持两种运行模式：直接运行进入交互式 shell（交互式模式），或通过 `redis_cli <command>` 执行单条命令（单命令模式）。用户可以通过 `-server` 参数指定目标 Redis 服务器地址。在交互模式下，该工具支持执行各类 Redis 命令（如 mset、mget、incrby、client setname 等）并格式化输出结果，输出风格类似官方 CLI。该工具特别适用于调试场景：当使用 brpc 客户端从 Redis 获得意外结果时，可以使用此工具进行交互式验证，以排查问题。

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/redis|redis]]
- [[entities/hiredis|hiredis]]

## Related Concepts
- [[concepts/redis协议|redis协议]]
- Redis请求/响应

## Mentions in Source
> **Source: [[sources/en_redis_client|en_redis_client]]**
- "example/redis_c++/redis_cli.cpp is a command line tool similar to the official CLI, demostrating brpc's capability to talk with redis servers."
- "When unexpected results are got from a redis-server using a brpc client, you can debug with this tool interactively as well."

> **Source: [[sources/redis_client|redis_client]]**
- "example/redis_c++/redis_cli是一个类似于官方CLI的命令行工具，以展示brpc对redis协议的处理能力。"
- "当使用brpc访问redis-server出现不符合预期的行为时，也可以使用这个CLI进行交互式的调试。"
- "redis 127.0.0.1:6379> mset key1 foo key2 bar key3 17
OK
redis 127.0.0.1:6379> mget key1 key2 key3
["foo", "bar", "17"]"