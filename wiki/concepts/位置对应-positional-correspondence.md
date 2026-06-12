---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_redis_client]]"]
tags: [term]
aliases:
  - "位置对应关系"
  - "命令与回复的对应"
  - "positional correspondence"
---


# 位置对应

## 定义
位置对应（positional correspondence）是 brpc Redis 客户端在处理多命令请求时遵循的一种协议约定。它假定在 Redis 服务器正常工作的前提下，响应中的第 `i` 个回复（reply(i)）与请求中通过 `AddCommand` 添加的第 `i` 个命令严格按顺序一一对应。这一约定简化了多命令批处理的回复解析，用户可以通过索引直接访问对应的回复内容。

## 关键特征
- **顺序一致性**：回复与命令在顺序上保持严格的一一对应关系，不存在乱序或交错。
- **依赖服务器正确性**：该对应关系成立的前提是 Redis 服务器正常工作；若服务器出现 bug，则对应关系可能被破坏。
- **简化处理模型**：用户无需创建复杂的映射表或等待所有回复就绪后再匹配，只需通过索引即可获取特定命令的回复。
- **批处理支持**：支持在单个 RPC 请求中包含多个命令（批量命令），并逐一处理各命令的回复。

## 应用
- **批处理命令解析**：在需要一次性发送多个 Redis 命令的场景中（如流水线操作），通过位置对应快速定位每个命令的回复结果。
- **RPC 响应验证**：检查 `response.reply_size()` 是否等于 `request.command_size()`，以快速发现潜在的服务器异常或 bug。
- **高性能 Redis 客户端实现**：brpc 等框架利用位置对应优化多请求并发处理，减少序列化和解析开销。

## 相关概念
- [[concepts/批量命令|批量命令]]
- [[concepts/redis协议|redis协议]]

## 相关实体
- [[entities/redisrequest|redisrequest]]
- [[entities/redisresponse|redisresponse]]

## 来源提及
- "The precondition that redis works correctly is that replies correspond to commands one by one in the same sequence (positional correspondence)." — [[sources/en_redis_client|en_redis_client]]
- "As long as RPC is successful, response.reply_size() should be equal to request.command_size(), unless the redis-server is buggy." — [[sources/en_redis_client|en_redis_client]]