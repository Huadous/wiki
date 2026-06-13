---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/builtin_service]]"]
tags: [term]
aliases:
  - "RPC详情服务"
  - "rpcz接口"
---


# /rpcz

## 定义
/rpcz是[[entities/brpc|brpc]]内置服务中用于查看所有RPC调用细节的HTTP接口。它提供每个RPC请求的完整链路信息，包括调用来源、目标、耗时、状态码等，是调试分布式系统、排查性能瓶颈和异常调用的核心工具之一。

## 关键特征
- **全局视角**：展示服务进程中所有RPC调用的完整明细，而非抽样数据
- **结构化输出**：返回格式化的RPC日志，可通过浏览器或curl访问
- **可筛选排序**：支持按条件筛选和排序RPC记录，便于定位特定问题
- **实时性强**：提供近期的RPC调用快照，反映服务当前状态
- **与性能工具互补**：与[[concepts/cpu-profiler|cpu profiler]]、[[concepts/heap-profiler|heap profiler]]等工具配合，从不同维度分析服务行为

## 应用
- **异常调用排查**：当服务出现高延迟或错误响应时，通过/rpcz定位具体的异常RPC请求
- **性能瓶颈分析**：查看每个RPC的耗时分布，识别慢调用或热点路径
- **分布式链路追踪**：在缺乏全链路追踪系统时，作为轻量级替代方案分析上下游调用关系
- **日常调试**：开发阶段验证RPC调用是否符合预期，检查参数传递和状态码
- **容量规划**：统计RPC调用频率和耗时趋势，辅助服务容量评估

## 相关概念
- [[concepts/status|/status]]
- [[concepts/vars|/vars]]
- [[concepts/connections|/connections]]
- [[concepts/flags|/flags]]
- [[concepts/cpu-profiler|cpu profiler]]
- [[concepts/heap-profiler|heap profiler]]
- [[concepts/contention-profiler|contention profiler]]
- [[concepts/builtin-service|内置服务]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "/rpcz: 查看所有的RPC的细节。" — [[sources/builtin_service|builtin_service]]