---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client|en_client]]"]
tags: [standard]
aliases:
  - "PROTOCOL_MEMCACHE"
  - "memcache"
  - "memcached binary protocol"
---


# PROTOCOL_MEMCACHE

## 定义
PROTOCOL_MEMCACHE 是 brpc 客户端协议矩阵中的一种标准协议，用于访问 memcached 缓存服务。它对应 memcached 的二进制协议，在使用时可将 `ChannelOptions.protocol` 设置为 `PROTOCOL_MEMCACHE` 或字符串 `"memcache"` 来启用。

## 关键特征
- 属于 brpc 客户端协议之一，标识符为 `PROTOCOL_MEMCACHE` 或字符串 `"memcache"`。
- 对应 memcached 的二进制协议（binary protocol of memcached）。
- 默认采用 single connection（单连接）模式。
- 通过 `ChannelOptions.protocol` 字段进行协议选择与启用。
- 与 [[concepts/PROTOCOL_REDIS|PROTOCOL_REDIS]] 同属 brpc 对 NoSQL 缓存后端的协议支持。

## 应用
- 通过 brpc 客户端访问 memcached 服务，执行缓存读写操作。
- 在需要统一 RPC 框架与缓存访问层的场景下，使用 brpc Channel 即可访问 memcached 后端。
- 详细使用方式参见 [Access memcached](memcache_client.md) 文档（来源：[[sources/en_client|en_client]]）。

## 相关概念
- [[concepts/PROTOCOL_REDIS|PROTOCOL_REDIS]]
- [[concepts/Connection Type|Connection Type]]
- [[concepts/ChannelOptions|ChannelOptions]]

## 相关实体
- [[entities/Channel|Channel]]
- [[entities/Controller|Controller]]

## 来源提及
- PROTOCOL_MEMCACHE or "memcache", which is binary protocol of memcached, using **single connection** by default. — [[sources/en_client|en_client]]
- Check out [Access memcached](memcache_client.md) for details. — [[sources/en_client|en_client]]