---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/bthread.md]]"
tags:
  - "M:N threading"
  - "coroutine"
  - "work stealing"
  - "butex"
  - "pthread worker"
  - "fiber"
  - "ExecutionQueue"
  - "event loop"
  - "NPTL"
  - "LWP"
  - "NUMA"
  - "RPC"
  - "Channel"
  - "cache locality"
  - "上下文切换"
  - "pthread"
aliases:
  - "bthread — brpc的M:N线程库"
  - "brpc bthread 文档"
---

## 来源
- Original file: [[brpc/bthread.md]]
- Ingested: 2026-06-13

## 核心内容

本文档系统介绍了 [[entities/bthread|bthread]]，它是 [[entities/brpc|brpc]] 项目使用的 M:N 线程库，源码位于 `src/bthread` 目录下。bthread 的设计目标是在提高程序并发度的同时降低编码难度，并在多核 CPU 上提供更好的 scalability 和 [[concepts/cache-locality|cache locality]]。其核心思想是 M 个 bthread 映射到 N 个 [[concepts/pthread|pthread]]（一般 M 远大于 N），相比 [[concepts/coroutine|协程]]（N:1 模型）具有更强的多核利用能力。一个 bthread 被卡住不会影响其他 bthread，这是 bthread 相比 event-loop 库的关键优势——bthread 写的是同步代码，却能获得异步代码的并发效果。bthread 的前身为 [[entities/distributed-process|百度 Distributed Process（DP）]] 中的 [[concepts/fiber|fiber]]，一个 N:1 合作式线程库，写同步代码但底层等价于 event-loop 库。两个关键技术是 [[concepts/work-stealing|work stealing]] 调度和 [[concepts/butex|butex]] 同步原语。bthread 在数百纳秒内即可建立，并提供多种原语进行同步。文档详细列出了设计目标（数百纳秒建立 bthread、bthread API 可在 pthread 中调用、合理同步原语、充分利用多核、better cache locality）、Non-Goals（不提供 pthread 兼容接口、不覆盖阻塞的 glibc 函数、不修改内核），并通过 FAQ 回答了 bthread 与协程的区别、阻塞行为、与 pthread 互操作、Channel 设计取舍、io 线程与 worker 线程是否分离等实际问题。

## 关键实体

- [[entities/bthread|bthread]] — Apache brpc 项目的 M:N 线程库，前身为百度 DP 项目中的 fiber，数百纳秒即可建立
- [[entities/brpc|brpc]] — Apache 开源 RPC 框架，bthread 是其核心线程库
- [[entities/distributed-process|Distributed Process（DP）]] — 百度项目，包含 fiber 库，是 bthread 的前身
- [[entities/ubaserver|ubaserver]] — 百度对异步框架的尝试，基于多 eventloop，因回调卡顿表现糟糕
- [[entities/百度|百度]] — brpc、bthread 的开发维护公司，其在线服务场景催生了 bthread 设计
- [[entities/tcmalloc|tcmalloc]] — Google 的 thread-local cache 内存分配器，作为线程数过多导致 cache 稀释的反面参照
- [[entities/glibc|glibc]] — GNU C 标准库，bthread 明确拒绝覆盖其阻塞函数

## 关键概念

- [[concepts/mn-threading|M:N threading]] — M 个用户线程映射到 N 个系统线程的线程模型，bthread 的核心架构
- [[concepts/coroutine|协程]] — N:1 线程库，无法高效利用多核，bthread 的重要对比对象
- [[concepts/work-stealing|work stealing]] — bthread 的调度策略，pthread worker 从其他 worker 偷取待运行 bthread
- [[concepts/butex|butex]] — bthread 的同步原语，使 bthread 和 pthread 可相互等待和唤醒
- [[concepts/pthread-worker|pthread worker]] — bthread 的运行载体，brpc 可通过 `num_threads` 或 `-bthread_concurrency` 配置
- [[concepts/fiber|fiber]] — DP 项目中的 N:1 合作式线程库，是 bthread 的前身，写同步代码底层等价于 event-loop
- [[concepts/executionqueue|ExecutionQueue]] — bthread 提供的机制，等价于 buffered channel
- [[concepts/event-loop|event loop]] — 异步编程架构，ubaserver 即基于此但表现糟糕，fiber/bthread 用同步写法获得类似效果
- [[concepts/nptl|NPTL]] — Linux 当前的 1:1 pthread 实现
- [[concepts/lwp|LWP]] — 轻量级进程，NPTL 1:1 映射下 pthread 等价于 LWP
- [[concepts/numa|NUMA]] — bthread 设计目标中提到的可选特性
- [[concepts/rpc|RPC]] — bthread 的典型应用场景
- [[concepts/channel|Channel]] — Go 语言并发原语，bthread 明确不提供，而是以 ExecutionQueue 替代
- [[concepts/cache-locality|cache locality]] — bthread 的关键性能目标
- [[concepts/上下文切换|上下文切换]] — channel 和 io/worker 线程分离方案的主要代价
- [[concepts/pthread|pthread]] — POSIX 线程，bthread 的底层映射目标和互操作对象
- [[concepts/同步原语|同步原语]] — bthread 提供的多种原语，用于 bthread 间及 bthread 与 pthread 间的同步

## 要点

- bthread 是 brpc 的 M:N 线程库，M 个 bthread 映射到 N 个 pthread（一般 M 远大于 N），相比 N:1 协程具有更强的多核利用能力
- bthread 的两个关键技术是 work stealing 调度和 butex 同步原语
- bthread 不是协程：协程是 N:1 模型无法高效利用多核；bthread 是 M:N 模型，一个 bthread 阻塞不影响其他 bthread
- bthread 可以在 bthread 中调用阻塞的 pthread 或系统函数，只阻塞当前 pthread worker，不影响其他 worker 上的待运行 bthread
- bthread API 设计为可在 pthread 中调用并有合理行为（API 在 bthread 中影响当前 bthread，在 pthread 中影响当前 pthread）
- bthread 在数百纳秒内即可建立，并提供多种原语进行同步
- bthread 的前身 fiber 是 N:1 合作式线程库，写同步代码但等价于 event-loop 库
- bthread 相比 event-loop 库的优势：写同步代码但一个 bthread 卡住不影响其他 bthread
- bthread 的 Non-Goals 明确不提供 pthread 兼容接口、不覆盖阻塞的 glibc 函数、不修改内核支持 pthread 同核快速切换
- 大量 bthread 同时调用阻塞系统函数会影响 RPC 运行，brpc 可通过调大 worker 数或限制最大并发来缓解
- bthread 不提供 Channel（因 channel 代价大、代码难写），而是提供 ExecutionQueue 来实现 buffered channel 的功能
- bthread 相比 pthread 的性能提升很大一部分来自更集中的线程资源（M 个 bthread 最终映射到 N 个 pthread，保持了 thread-local cache 有效性）
- bthread 的前身是百度 Distributed Process（DP）项目中的 fiber，一个 N:1 合作式线程库