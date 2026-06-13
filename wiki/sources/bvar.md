---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/bvar.md]]"
tags:
  - "Cacheline"
  - "mbvar"
  - "cache bouncing"
  - "thread local存储"
  - "原子操作"
  - "dump功能"
  - "/vars"
  - "/brpc_metrics"
aliases:
  - "bvar介绍"
  - "What is bvar"
---

## 核心内容
本文档介绍 [[entities/brpc|brpc]] 项目内置的多线程计数器类库 [[entities/bvar|bvar]]。[[entities/bvar|bvar]] 位于 brpc 源代码树的 `src/bvar` 目录下，专门为多线程环境下的计数和监控场景设计。它利用 [[concepts/thread-local存储|thread local存储]] 技术让每个线程只累加私有变量、读取时再合并所有线程数据，从而避免 [[concepts/cache-bouncing|cache bouncing]] 问题，将写竞争转移至读端，写入开销极低（约 20 纳秒）且几乎不随线程数增长。[[entities/bvar|bvar]] 性能显著优于百度内部旧版计数器库 [[entities/ubmonitor|UbMonitor]]（300 次 bvar 累加的开销才抵得上一次动态 UbMonitor），同时也快于竞争频繁的 [[concepts/原子操作|原子操作]]。文档涵盖其设计原理、单维度与多维度形式（[[concepts/mbvar|mbvar]]）、HTTP 接口 `/vars` 的查看方式、文件导出（[[concepts/dump功能|dump功能]]）以及与 [[entities/prometheus|prometheus]]、百度 [[entities/noah|noah]] 等监控系统的集成方法。

[[entities/bvar|bvar]] 是 brpc 可观测性体系的核心组件，被 brpc 大量用于提供各类运行时统计数值。它是 [[entities/brpc|brpc]] 的内置模块，因此也被称为 [[entities/bvar|bvar计数器库]]，方便用户记录和查看程序中的各类数值。

## 关键实体
- [[entities/bvar|bvar]] — Apache brpc 内置的多线程计数器类库（别名：[[entities/bvar|bvar计数器库]]）
- [[entities/brpc|brpc]] — 集成并大量使用 bvar 的 RPC 框架
- [[entities/ubmonitor|UbMonitor]] — 百度内部旧版计数器库，bvar 的性能对比基线
- [[entities/prometheus|prometheus]] — 通过 `/brpc_metrics` 端点采集 bvar 指标的开源监控系统
- [[entities/apache|apache]] — 管理 brpc 项目的开源组织
- [[entities/noah|noah]] — 百度内部基于 bvar dump 文件的监控系统
- [[entities/bthread|bthread]] — brpc 框架的用户态线程库，提供多个 bvar 统计指标
- [[entities/iobuf|iobuf]] — brpc 框架的 I/O 缓冲区，提供多个 bvar 统计指标

## 关键概念
- [[concepts/cacheline|cacheline]] — 理解 bvar 性能原理所需的基础缓存概念
- [[concepts/cache-bouncing|cache-bouncing]] — 多线程竞争同一缓存行导致的性能问题
- [[concepts/thread-local存储|thread-local存储]] — bvar 避免 cache bouncing 的核心技术
- [[concepts/原子操作|原子操作]] — 性能对比中的一种基线方案
- [[concepts/mbvar|mbvar]] — 多维度版本的 bvar
- [[concepts/dump功能|dump功能]] — 将 bvar 导出到文件供监控系统采集的机制
- [[concepts/vars|vars]] — brpc 提供 bvar 列表的 HTTP 端点，可通过 `/vars` 查看所有曝光的 bvar，或通过 `/vars/VARNAME` 查阅某个具体的 bvar
- [[concepts/brpc_metrics|brpc_metrics]] — brpc 为 Prometheus 提供的指标抓取端点

## 要点
- bvar 是 [[entities/brpc|brpc]] 内置的多线程计数器类库，分为单维度 [[entities/bvar|bvar]] 和多维度 [[concepts/mbvar|mbvar]] 两种形式，是 brpc 可观测性体系的核心组件
- bvar 采用 thread local 存储将写竞争转移至读端，写入开销极低（约 20 纳秒），适合写入频繁但读取低频的监控场景
- 性能优势显著：相比 [[entities/ubmonitor|UbMonitor]] 几乎不增加程序开销，相比 [[concepts/原子操作|原子操作]] 在高竞争下更快
- [[entities/brpc|brpc]] 集成了 bvar，可通过 HTTP 接口 [[concepts/vars|vars]]（`/vars` 列出所有 bvar，`/vars/VARNAME` 查询单个 bvar）查看曝光的计数器
- 支持三种数据消费方式：HTTP 接口 [[concepts/vars|vars]] 网页查看、文件 [[concepts/dump功能|dump功能]] 导出、与 [[entities/prometheus|prometheus]] 通过 [[concepts/brpc_metrics|brpc_metrics]] 端点集成
- bvar 不能完全替代所有计数器，因为读操作需合并所有线程数据，比写更慢