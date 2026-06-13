---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/builtin_service]]"]
tags: [term]
aliases:
  - "连接统计服务"
  - "connections接口"
  - "BRPC连接监控端点"
---


# /connections

## 定义
/connections是brpc内置服务中用于展示所有连接统计信息的HTTP接口。它提供当前服务器所有TCP连接的汇总数据，包括连接数、连接状态、流量统计等关键指标，是诊断网络问题和监控连接泄露的核心观测手段。

## 关键特征
- **实时连接快照**：提供服务器当前全部TCP连接的即时状态快照
- **流量统计**：包含每个连接的收发字节数、报文数等流量指标
- **连接状态追踪**：显示连接的健康状态、存活时长等信息
- **低开销访问**：通过浏览器或命令行工具即可快速获取数据，不显著影响服务性能
- **与其他内置服务互补**：与/status、/vars、/flags、/rpcz等共同构成完整的服务观测体系

## 应用
- **连接泄露诊断**：通过监控连接数变化趋势，快速发现未正常关闭的连接
- **网络问题排查**：分析单连接流量异常、连接状态异常等网络层问题
- **运维监控**：集成到自动化监控系统，实时告警连接异常
- **容量规划**：统计服务器承载的连接总数，辅助判断是否需要扩容
- **调试测试**：开发阶段快速验证连接的创建、复用和销毁逻辑

## 相关概念
- [[concepts/status|/status]]
- [[concepts/vars|/vars]]
- [[concepts/flags|/flags]]
- [[concepts/rpcz|/rpcz]]
- [[concepts/builtin-service|内置服务]]

## 相关实体
- [[entities/connections-监控页面|connections-监控页面]]
- [[entities/brpc|brpc]]

## 来源提及
- "/connections: 所有连接的统计信息。" — [[sources/builtin_service|builtin_service]]