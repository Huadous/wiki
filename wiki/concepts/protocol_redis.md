---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [standard]
aliases:
  - "PROTOCOL_REDIS"
  - "brpc Redis 协议"
  - "Redis Protocol"
---


# PROTOCOL_REDIS

## 定义
PROTOCOL_REDIS 是 brpc 框架对 Redis 1.2+ 协议（与 hiredis 所支持的协议一致）的支持选项。通过将 [[entities/Channel|ChannelOptions.protocol]] 设置为 `PROTOCOL_REDIS` 或字符串 `"redis"` 即可启用，默认采用 single connection 模式。它使 brpc 客户端能够作为 Redis 客户端访问 Redis 服务。

## 关键特征
- 支持 Redis 1.2+ 协议规范，与 hiredis 库所遵循的协议完全一致
- 通过 `ChannelOptions.protocol` 配置项启用，可接受枚举值 `PROTOCOL_REDIS` 或字符串 `"redis"`
- 默认采用 single connection（单连接）模式
- 属于 brpc 客户端侧支持的多种协议之一，与 [[concepts/PROTOCOL_MEMCACHE|PROTOCOL_MEMCACHE]] 并列
- 详细使用方法参见 [[sources/redis_client|Access Redis]] 指南

## 应用
- 使用 brpc 客户端作为 Redis 客户端访问 Redis 服务，执行键值读写、发布订阅、Lua 脚本等操作
- 在需要将 brpc 与现有 Redis 基础设施集成的场景中，复用 Redis 协议而无需引入额外的 Redis 客户端库
- 作为 brpc 多协议支持能力的一部分，与其他 [[concepts/Connection Type|Connection Type]] 组合使用以适应不同部署拓扑

## 相关概念
- [[concepts/PROTOCOL_MEMCACHE]]
- [[concepts/Connection Type]]
- [[concepts/ChannelOptions]]

## 相关实体
- [[entities/Channel]]
- [[entities/Controller]]

## 来源提及
- PROTOCOL_REDIS or "redis", which is protocol of redis 1.2+ (the one supported by hiredis), using **single connection** by default. — [[sources/en_client]]
- Check out [Access Redis](redis_client.md) for details. — [[sources/en_client]]