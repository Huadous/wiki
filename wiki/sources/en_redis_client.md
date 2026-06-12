---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "brpc/en_redis_client.md"
tags: [Redis协议, bthread, 一致性哈希, 单线程反应器, 连接池, 批量命令, QPS, 延迟, redis_verbose, ParallelChannel, O(N) 时间复杂度, 短字符串优化 (SSO), 位置对应 (positional correspondence)]
aliases: ["brpc Redis Client", "brpc Redis 文档"]
---

# Redis Client (brpc) - Summary

## 来源
- Original file: brpc/en_redis_client.md
- Ingested: 2026-06-12

## 核心内容
本文档介绍了 [[entities/brpc|brpc]] 框架对 [[concepts/redis协议|Redis协议]] 的原生支持，提供了一种高性能、线程安全的 [[entities/redis|Redis]] 客户端实现。与官方客户端 [[entities/hiredis|hiredis]] 相比，brpc Redis 客户端具有线程安全、支持同步/异步/半异步多种调用方式、可利用 [[concepts/parallelchannel|ParallelChannel]] 等组合 Channel 声明式定义访问模式、以及利用 [[concepts/bthread|bthread]] 实现高并发等优势。文档详细说明了如何通过 Channel 初始化 Redis 连接、使用 [[entities/redisrequest|RedisRequest]] 和 [[entities/redisresponse|RedisResponse]] 执行命令，以及如何通过一致性哈希访问 [[concepts/一致性哈希|Redis集群]]。性能测试显示，在单连接模式下使用 200 个 bthread 发送请求，QPS 可达 41 万，远超 hiredis 的池化连接模式，这是因为 [[concepts/单线程反应器|Redis服务器单线程]] 的特性使得单连接批处理模式更具优势。文档还提供了类似官方 redis-cli 的 [[entities/redis_cli|redis_cli]] 命令行调试工具。

## 关键实体
- [[entities/brpc|brpc]] — 百度开源的 RPC 框架，本文档核心主体
- [[entities/redis|Redis]] — 被访问的缓存服务
- [[entities/hiredis|hiredis]] — 官方 Redis C 客户端，与 brpc 进行对比
- [[entities/redisrequest|RedisRequest]] — 构造请求的类，支持多条命令
- [[entities/redisresponse|RedisResponse]] — 包含回复的类
- [[entities/redisreply|RedisReply]] — 单个回复对象
- [[entities/redisauthenticator|RedisAuthenticator]] — 认证器
- [[entities/redis_cli|redis_cli]] — 调试命令行工具
- [[entities/twemproxy|twemproxy]] — 另一种集群访问方案

## 关键概念
- [[concepts/redis协议|Redis协议]] — brpc 原生支持的序列化协议
- [[concepts/bthread|bthread]] — 高并发基础，用户态协程
- [[concepts/一致性哈希|一致性哈希]] — 集群访问负载均衡算法
- [[concepts/单线程反应器|单线程反应器]] — Redis 服务器架构模型
- [[concepts/连接池|连接池]] — hiredis 的劣质连接模式
- [[concepts/批量命令|批量命令]] — 多个命令打包发送
- [[concepts/qps|QPS]] — 吞吐量指标
- [[concepts/延迟|延迟]] — 响应时间指标
- [[concepts/redis_verbose|redis_verbose]] — 调试标志
- [[concepts/parallelchannel|ParallelChannel]] — 组合 Channel
- [[concepts/on-时间复杂度|O(N) 时间复杂度]] — 解析保证
- [[concepts/短字符串优化-sso|短字符串优化 (SSO)]] — 内存管理优化
- [[concepts/位置对应-positional-correspondence|位置对应 (positional correspondence)]] — 命令与回复顺序对应

## 要点
- brpc 原生支持 Redis 协议，无需 hiredis 依赖，提供线程安全、支持同步/异步的客户端
- 使用单连接共享模式，通过 bthread wait-free 合并请求，高并发下 QPS 远超 hiredis 池化模式
- RedisRequest 支持添加多条命令批量发送，但所有命令必须发往同一台服务器
- 访问集群时应使用一致性哈希负载均衡，每个请求应包含单命令或同 key 多命令
- 性能测试：单连接 200 bthread 时 QPS 达 41 万，池化连接仅 7.5 万，验证了对 Redis 单线程模型更优的适配
- 提供 redis_verbose 调试标志和 redis_cli 命令行工具
- 解析回复保证 O(N) 时间复杂度，实现短字符串优化和块内存分配