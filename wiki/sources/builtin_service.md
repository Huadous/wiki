---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[brpc/builtin_service.md]]"
tags: [内置服务, 安全模式, /status, /vars, /connections, /flags, /rpcz, cpu profiler, heap profiler, contention profiler, /version, /health, /protobufs, /vlog]
aliases: ["BRPC内置服务概述", "BRPC Built-in Services Documentation"]
---

# 内置服务 - Summary

## 来源
- Original file: [[brpc/builtin_service.md]]
- Ingested: 2026-06-12

## 核心内容

本文档全面介绍了[[entities/brpc|brpc]]框架的[[concepts/内置服务|内置服务]]系统。这些服务通过HTTP协议以纯文本或HTML形式展示服务器内部状态，可通过浏览器或curl访问，并支持添加`?console=1`强制纯文本输出。当服务器端口受限时，可使用[[entities/rpc_view|rpc_view]]进行转发。文档详细列出了多种内置服务接口，包括七个主要服务：[[concepts/status|/status]]（服务状态）、[[concepts/vars|/vars]]（自定义计数器）、[[concepts/connections|/connections]]（连接统计）、[[concepts/flags|/flags]]（gflags管理，支持动态修改）、[[concepts/rpcz|/rpcz]]（RPC细节追踪）、[[concepts/cpu-profiler|cpu profiler]]（CPU热点分析）、[[concepts/heap-profiler|heap profiler]]（内存占用分析）和[[concepts/contention-profiler|contention profiler]]（锁竞争分析）。其他服务包括[[concepts/version|/version]]（版本信息）、[[concepts/health|/health]]（存活探测）、[[concepts/protobufs|/protobufs]]（Protobuf结构查看）、[[concepts/vlog|/vlog]]（VLOG日志控制）、[[entities/dir|/dir]]（文件浏览，默认关闭）和[[entities/threads|/threads]]（线程查看，默认关闭）。文档特别强调，出于安全考虑，直接对外服务时必须通过[[concepts/安全模式|安全模式]]隐藏内置服务接口。

## 关键实体

- [[entities/brpc|brpc]] — 高性能RPC框架，提供所有内置服务的底层支持
- [[entities/rpc_view|rpc_view]] — 端口受限环境下的HTTP转发工具
- [[entities/dir|/dir]] — 文件浏览服务，默认关闭，开启有安全风险
- [[entities/threads|/threads]] — 线程查看服务，默认关闭，调用时性能影响大

## 关键概念

- [[concepts/内置服务|内置服务]] — brpc框架提供的HTTP接口集合，用于展示服务器内部状态
- [[concepts/安全模式|安全模式]] — 控制内置服务对外可访问性的安全机制
- [[concepts/status|/status]] — 显示所有服务的主要状态
- [[concepts/vars|/vars]] — 用户可定制的计数器展示接口
- [[concepts/connections|/connections]] — 所有连接的统计信息
- [[concepts/flags|/flags]] — gflags状态查看与动态修改
- [[concepts/rpcz|/rpcz]] — 所有RPC调用细节查看
- [[concepts/cpu-profiler|cpu profiler]] — CPU热点分析工具
- [[concepts/heap-profiler|heap profiler]] — 内存占用分析工具
- [[concepts/contention-profiler|contention profiler]] — 锁竞争分析工具
- [[concepts/version|/version]] — 服务器版本查询
- [[concepts/health|/health]] — 服务存活探测
- [[concepts/protobufs|/protobufs]] — Protobuf结构查看
- [[concepts/vlog|/vlog]] — VLOG日志控制

## 要点

- 内置服务通过HTTP提供，支持浏览器和curl访问，自动适配纯文本或HTML格式
- 七个主要服务覆盖服务状态、自定义计数器、连接统计、gflags管理、RPC追踪和三种性能分析
- /flags支持在线修改gflags，无需重启服务，极大提升运维灵活性
- 性能分析器（cpu profiler、heap profiler、contention profiler）提供火焰图展示，分别覆盖CPU、内存、锁三个维度
- /dir和/threads默认关闭，前者有严重安全风险，后者调用时性能影响较大
- 直接对外服务时必须隐藏内置服务接口，防止信息泄露
- /rpcz可查看RPC完整链路，是调试分布式系统的强大工具