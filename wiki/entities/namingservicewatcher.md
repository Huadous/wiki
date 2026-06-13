---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/load_balancing|load_balancing]]"]
tags: [other]
aliases:
  - "NamingServiceWatcher 接口"
  - "brpc NamingServiceWatcher"
  - "观察者"
---


# NamingServiceWatcher

## 基本信息
- Type: other
- Source: [[sources/load_balancing|load_balancing]]

## 描述
NamingServiceWatcher 是 brpc 中用于感知命名服务列表变化的观察者接口。当 [[entities/NamingService|NamingService]] 获得新的服务器列表并完成去重、与旧列表比较之后，框架会通知所有对该列表感兴趣的 NamingServiceWatcher。它是 brpc 实现命名服务变更被动通知机制的关键组件，依赖于用户通过 [[entities/NamingServiceActions|NamingServiceActions]] 的 `ResetServers` 主动上报新列表这一反转控制权的设计。多个 NamingServiceWatcher 可同时关注同一命名服务，从而实现服务发现与其他关注方（如 [[entities/PeriodicNamingService|PeriodicNamingService]] 流程的下游处理模块）的解耦。

## 相关实体
- [[entities/NamingServiceActions|NamingServiceActions]]
- [[entities/PeriodicNamingService|PeriodicNamingService]]
- [[entities/NamingServiceThread|NamingServiceThread]]

## 相关概念
- [[concepts/naming-service|命名服务]]

## 来源提及
- 框架会对列表去重，和之前的列表比较，通知对列表有兴趣的观察者(NamingServiceWatcher)。 — [[sources/load_balancing|load_balancing]]
- NamingServiceWatcher"在 PeriodicNamingService 流程中作为列表变更的下游通知对象被提及。 — [[sources/load_balancing|load_balancing]]