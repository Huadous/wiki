---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/circuit_breaker]]"]
tags: [method]
aliases:
  - "连接组"
---


# ConnectionGroup

## 定义
ConnectionGroup 是 brpc 中用于隔离连接的管理机制。它允许将不同 Channel 分配到独立的连接组中，使不同组的 Channel 拥有独立的 TCP 连接池，从而实现连接级别的故障隔离。

## 关键特征
- **连接隔离**：不同 ConnectionGroup 中的 Channel 不会共享下游节点的 TCP 连接，默认情况下所有 Channel 共享同一个连接池。
- **熔断粒度控制**：通过将 Channel 分配到不同组，可以精确控制熔断的影响范围，避免单个连接故障导致所有 Channel 瘫痪。
- **配置简单**：仅需设置 `ChannelOptions.connection_group` 字段即可启用，无需修改其他业务逻辑。
- **资源独立**：每个 ConnectionGroup 拥有独立的连接池和健康状态追踪，互不干扰。

## 应用
- **多租户隔离**：为不同租户或不同业务线的 RPC 调用分配不同的 ConnectionGroup，确保某个租户的熔断行为不影响其他租户。
- **高可用架构**：对关键服务部署双通道架构，将主备 Channel 放入不同 ConnectionGroup，避免单一连接故障导致全链路不可用。
- **灰度发布与迁移**：在服务升级或流量迁移场景中，将新旧版本的调用链路放在不同 ConnectionGroup，实现熔断范围的精准控制。

## 相关概念
- [[concepts/熔断|熔断]]
- [[concepts/可选熔断策略|可选熔断策略]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "假如想要避免2中所述的情况，可以通过设置ChannelOptions.connection_group将channel放进不同的ConnectionGroup，不同ConnectionGroup的channel并不会共享连接。" — [[sources/circuit_breaker|circuit_breaker]]