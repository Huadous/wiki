---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/load_balancing|load_balancing]]"]
tags: [other]
aliases:
  - "NamingServiceThread bthread container"
  - "brpc NamingServiceThread"
---


# NamingServiceThread

## 基本信息
- Type: other
- Source: [[sources/load_balancing|load_balancing]]

## 描述
NamingServiceThread 是 brpc 中用于运行命名服务（Naming Service）逻辑的独立 bthread 容器类。它为 [[entities/periodicnamingservice|PeriodicNamingService]] 的整套流程——包括周期性获取服务列表、对结果进行去重与比较、以及在列表发生变化时通知订阅者——提供独立的执行环境，避免阻塞调用方线程。一个 NamingServiceThread 可以被多个 [[entities/channel|Channel]] 共享，其生命周期与所有权通过 [[concepts/intrusive-ptr|intrusive_ptr]] 进行引用计数管理，从而在多个 Channel 之间复用同一个命名服务线程，避免对同一服务列表的重复拉取，并在多线程环境下保证访问安全。

## 相关实体
- [[entities/periodicnamingservice|PeriodicNamingService]]
- [[entities/bthread|bthread]]
- [[entities/channel|Channel]]

## 相关概念
- [[concepts/naming-service|命名服务]]
- [[concepts/intrusive-ptr|intrusive_ptr]]

## 来源提及
- "这套逻辑会运行在独立的bthread中，即NamingServiceThread。" — [[sources/load_balancing|load_balancing]]
- "一个NamingServiceThread可能被多个Channel共享，通过intrusive_ptr管理ownership。" — [[sources/load_balancing|load_balancing]]