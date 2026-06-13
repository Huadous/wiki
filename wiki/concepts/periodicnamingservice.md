---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/load_balancing]]"]
tags: [term]
aliases:
  - "PeriodicNamingService"
  - "周期性命名服务基类"
---


# PeriodicNamingService

## 定义
PeriodicNamingService 是 brpc 在 `src/brpc/periodic_naming_service.h` 中提供的辅助基类，专门用于没有事件通知能力的命名服务（如 bns）。用户只需继承该类并实现 `GetServers` 方法即可完成周期性拉取逻辑，默认拉取间隔为 5 秒（可通过 `ns_access_interval` 标志调整）。PeriodicNamingService 内部封装了定时调用、子线程管理以及调用 `NamingServiceActions::ResetServers` 的样板代码。其执行流运行在独立的 bthread 中，即 [[entities/namingservicethread|NamingServiceThread]]，多个 Channel 可通过 `intrusive_ptr` 共享同一个 NamingServiceThread。

## 关键特征
- 抽象基类，定义在 `src/brpc/periodic_naming_service.h` 中，简化无事件通知能力的命名服务接入流程
- 用户仅需实现 `GetServers` 方法即可完成单次拉取逻辑
- 默认拉取间隔为 5 秒，可通过 `ns_access_interval` 标志调整
- 内部封装了定时调度、子线程生命周期管理以及调用 `NamingServiceActions::ResetServers` 的样板代码
- 执行流运行在独立的 bthread（即 [[entities/namingservicethread|NamingServiceThread]]）中
- 多个 Channel 可通过 `intrusive_ptr` 共享同一个 NamingServiceThread，避免重复拉取
- 典型应用场景：bns 等没有 watch/notify 机制的命名服务

## 应用
- 实现基于 bns（百度名字服务）等不支持事件通知的命名服务的后端拉取逻辑
- 为任何没有内置变更通知机制的命名服务添加周期性的服务发现能力
- 减少用户自行管理定时器、线程及 NamingServiceActions 调用的样板代码

## 相关概念
- [[concepts/命名服务|命名服务]]
- [[concepts/NamingService|NamingService]]
- [[concepts/NamingServiceActions|NamingServiceActions]]
- [[concepts/bthread|bthread]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/namingservicethread|NamingServiceThread]]

## 来源提及
- "为了简化这类定期获取的逻辑，brpc提供了PeriodicNamingService供用户继承，用户只需要实现单次如何获取（GetServers）。" — [[sources/load_balancing]]
- "这套逻辑会运行在独立的bthread中，即NamingServiceThread。" — [[sources/load_balancing]]
- "一个NamingServiceThread可能被多个Channel共享，通过intrusive_ptr管理ownership。" — [[sources/load_balancing]]