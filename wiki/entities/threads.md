---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/builtin_service]]"]
tags: [product]
aliases:
  - "线程查看服务"
  - "线程状态服务"
  - "brpc线程诊断端点"
---


# /threads

## 基本信息
- Type: product
- Source: [[sources/builtin_service|builtin_service]]

## 描述
/threads 是 [[entities/brpc|brpc]] 内置的一个 HTTP 服务端点，用于查看进程内所有线程的运行状况。该服务在调用时会对程序性能产生较大影响，因此默认处于关闭状态。/threads 主要用于帮助开发人员诊断线程死锁、长时间阻塞等并发问题，但由于其性能开销，应仅在需要时临时启用。brpc 官方建议在调试或性能分析场景下谨慎使用 /threads，并在使用后立即关闭，避免影响线上服务的稳定性。该端点属于 brpc 内置服务体系的一部分，与其他内置服务（如 [[entities/status|/status]]、[[entities/dir|dir]]）一同提供运行时诊断能力。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/status|/status]]
- [[entities/cpu-profiler|cpu profiler]]
- [[entities/heap-profiler|heap profiler]]
- [[entities/dir|dir]]

## 相关概念
- [[concepts/内置服务|内置服务]]
- [[concepts/安全模式|安全模式]]

## 来源提及
- "/threads: 查看进程内所有线程的运行状况，调用时对程序性能影响较大，默认关闭。" — [[sources/builtin_service|builtin_service]]