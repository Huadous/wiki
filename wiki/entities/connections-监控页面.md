---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/circuit_breaker]]"]
tags: [other]
aliases:
  - "connections页面"
  - "连接监控页面"
---


# /connections 监控页面

## 基本信息
- Type: other
- Source: [[sources/circuit_breaker|circuit_breaker]]

## 描述

`/connections` 是 [[entities/brpc|brpc]] 框架内建的一个监控端点（endpoint），用于展示当前进程中所有下游节点的连接状态和熔断相关统计信息。该页面以表格形式列出每个节点的关键指标，包括节点地址、当前连接状态、熔断总次数（`nBreak`）以及自最近一次从熔断恢复后累积的错误请求数（`RecentErr`）。即便用户没有显式开启可选的熔断策略，[[entities/brpc|brpc]] 也会自动对这些数据进行统计，确保运维人员可以在任何情况下获得基础的节点健康视图。通过该页面，用户可以直观地观察下游节点的健康情况、熔断历史以及连接异常，辅助进行故障排查和容量规划。`nBreak` 的值不仅由熔断器产生，也可能因 TCP 连接建立失败等其他原因而增加。

## 相关实体
- [[entities/brpc|brpc]] — 所属框架
- [[entities/socket|socket]] — 底层连接表示
- [[entities/bvar|bvar]] — 统计数据的采集与展示基础

## 相关概念
- [[concepts/熔断|熔断]] — 核心监控指标之一
- [[concepts/健康检查|健康检查]] — 节点健康状态监测
- [[concepts/隔离时间|隔离时间]] — 熔断后的恢复策略

## 来源提及
- "节点的熔断次数、最近一次从熔断中恢复之后的累积错误数都可以在监控页面的/connections里找到，即便我们没有开启可选的熔断策略，brpc也会对这些数据进行统计。" — [[sources/circuit_breaker|circuit_breaker]]
- "nBreak表示进程启动之后该节点的总熔断次数，RecentErr则表示该节点最近一次从熔断中恢复之后，累计的出错请求数。" — [[sources/circuit_breaker|circuit_breaker]]
- "由于brpc默认熔断策略是一直开启的，即便我们没有开启可选的熔断策略，nBreak还是可能会大于0，这时nBreak通常是因为tcp连接建立失败而产生的。" — [[sources/circuit_breaker|circuit_breaker]]