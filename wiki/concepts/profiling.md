---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_overview]]"]
tags: [method]
aliases:
  - "性能分析"
  - "profilers"
  - "Profiling工具"
---


# Profiling

## 定义
Profiling是brpc框架内置的一组性能分析工具，包括CPU分析器（CPU profiler）、堆分析器（heap profiler）和锁竞争分析器（contention profiler），允许用户通过HTTP接口或[[entities/curl|curl]]命令行工具实时分析线上服务的性能瓶颈。

## 关键特征
- **实时在线分析**：无需重启服务，通过HTTP接口即可触发性能数据采集
- **三种分析维度**：覆盖CPU热点、内存分配和锁竞争三大常见性能问题
- **与bvar集成**：与[[concepts/bvar|bvar]]统计量配合，提供多维度的性能可观测性
- **低侵入性**：基于brpc内置机制，对服务代码影响最小
- **HTTP接口访问**：支持浏览器直接访问或通过curl命令获取分析结果

## 应用
- **CPU热点定位**：识别线上服务中消耗CPU最多的函数调用路径
- **内存分配分析**：检测堆内存分配频率和分布，定位内存泄漏或过度分配问题
- **锁竞争诊断**：分析锁竞争热点，优化并发性能
- **性能回归检测**：在版本更新后对比Profiling数据，发现性能退化
- **容量规划**：通过Profiling数据了解服务资源消耗特性，指导扩缩容决策

## 相关概念
- [[concepts/bvar|bvar]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/curl|curl]]

## 来源提及
- "Debug services via http, and run cpu, heap and contention profilers." — [[sources/en_overview|en_overview]]
- "analyze cpu hotspots, heap allocations and lock contentions of online services" — [[sources/en_overview|en_overview]]