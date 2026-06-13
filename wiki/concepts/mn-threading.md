---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bthread|bthread]]"]
tags: [term]
aliases:
  - "M:N线程模型"
  - "M:N threading model"
---


# M:N threading

## 定义
M:N threading 是指将 M 个用户级线程（user-level thread）映射到 N 个系统级线程（kernel-level thread）上的线程模型，是 [[sources/bthread|bthread]] 所采用的核心架构。在 Linux 平台下，由于 pthread 实现（NPTL）采用 1:1 模型，M 个 bthread 实际上被映射到 N 个 LWP（Light-weight process，轻量级进程）上。一般情况下 M 远大于 N。

## 关键特征
- **用户态调度为主**：M 个用户级线程在用户空间内被调度，由运行时库管理创建、销毁和切换，开销远低于内核级线程。
- **M 远大于 N**：通常用户级线程数量远多于系统级线程，N 一般等于 CPU 核心数。
- **基于 pthread worker**：N 个系统级线程由 [[sources/bthread|bthread]] 创建并管理，作为 worker 线程运行用户级 bthread。
- **充分利用多核**：相比 N:1 协程模型无法利用多核的缺陷，M:N 模型可以在多个 CPU 核上并行执行。
- **更好的 cache locality**：相比 1:1 pthread 模型，M:N 模型可以让相关任务集中在少数系统线程上运行，提升 CPU 缓存命中率。
- **集中的线程资源使用**：线程资源（栈、局部存储等）由运行时统一管理，避免 1:1 模型下大量线程带来的资源浪费。
- **阻塞隔离**：当一个 bthread 被阻塞（如执行同步系统调用）时，运行时会自动调度其他 bthread 到 worker 线程上，不会影响整体并发能力。

## 应用
- 作为 [[sources/bthread|bthread]] 的核心架构模型，用于 brpc 框架内的高并发 RPC 处理。
- 在需要支撑数十万级别并发连接、同时充分利用多核 CPU 的服务端程序中作为基础并发模型。
- 与 work stealing 调度策略结合，实现 bthread 在 N 个 worker 线程之间的负载均衡。
- 作为协程（coroutine）与系统线程之间的一种折中方案，被多种现代并发库采用。

## 相关概念
- [[concepts/coroutine|coroutine]]
- [[concepts/fiber|fiber]]
- [[concepts/work-stealing|work stealing]]
- [[concepts/pthread-worker|pthread worker]]
- [[concepts/lwp|LWP]]

## 相关实体
- [[entities/bthread|bthread]]

## 来源提及
- "M:N"是指M个bthread会映射至N个pthread，一般M远大于N。由于linux当下的pthread实现(NPTL)是1:1的，M个bthread也相当于映射至N个LWP。 — [[sources/bthread|bthread]]
- bthread是一个M:N线程库，一个bthread被卡住不会影响其他bthread。 — [[sources/bthread|bthread]]