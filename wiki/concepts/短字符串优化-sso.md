---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_redis_client]]"
  - "[[sources/redis_client]]"
tags:
  - "method"
aliases:
  - "SSO"
  - "Short String Optimization"
  - "短串优化(SSO)"
  - "SSO"
  - "Short String Optimization"
---

## 描述

短字符串优化是 brpc Redis 客户端性能优化体系中的关键一环。其核心思想是通过预先分配局部缓冲区来存储长度较短的字符串，从而避免频繁的堆内存分配与释放操作。当 Redis 回复字符串长度低于阈值（通常为 15-32 字节）时，数据直接存储在对象内部的栈空间内，实现零分配操作。该技术与 brpc 的块分配（block allocation）策略紧密结合——无论 Redis 回复的结构多复杂，整体内存都以连续块为单位分配，SSO 在此基础上进一步优化小字符串的处理。对使用者而言，SSO 完全透明，brpc 自动识别字符串长度并选择最优存储方式，有效减少了内存碎片和分配器争用，尤其在处理大量小型 Redis 回复（如 `GET`、`SET`、`PING` 命令的返回结果）时，能够显著提升系统吞吐量。

## 相关概念

- [[concepts/redis协议|redis协议]]
- [[concepts/延迟|延迟]]
- [[concepts/qps|qps]]
- [[concepts/批量命令|批量命令]]

## 相关实体

- [[entities/redisreply|redisreply]]
- [[entities/redisresponse|redisresponse]]
- [[entities/redisrequest|redisrequest]]
- [[entities/brpc|brpc]]

## 来源提及

> **Source: [[sources/en_redis_client|en_redis_client]]**
> - “Memory is allocated in blocks regardless of complexity of the reply, and short string optimization (SSO) is implemented to further improve performance.”

> **Source: [[sources/redis_client|redis_client]]**
> - “无论reply的组成多复杂，内存都会连续成块地分配，并支持短串优化(SSO)进一步提高性能。”