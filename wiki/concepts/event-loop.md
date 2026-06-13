---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bthread]]"]
tags: [term]
aliases:
  - "eventloop"
  - "事件循环"
---


# event loop

## 定义
event loop（事件循环）是异步编程中的一种常见架构模式，通过事件驱动的回调机制在单线程上并发处理 I/O 与其他事件。它在计算能力上等价于一个 N:1 的合作式线程库（如 fiber、协程），但其异步代码通常以回调形式表达，而非同步顺序代码。

## 关键特征
- 事件驱动：基于事件回调而非阻塞调用来处理 I/O 与计算任务。
- 计算能力等价于 N:1 合作式线程库（如 fiber、协程）。
- 编程模型为异步回调，代码通常呈现"非顺序"风格。
- 致命缺陷：任一回调中的慢操作会阻塞整个 loop，所有等待中的事件都会被卡住。
- 可通过并行化多个 event loop 提升吞吐，但若单个 loop 中存在慢回调，仍会拖累整体表现。

## 应用
- 高并发服务器的异步 I/O 框架基础组件。
- Node.js 等运行时环境的核心调度机制。
- 历史案例：uba**a**server（百度对异步框架的尝试）由多个并行的 event loop 组成，但因单回调卡住整个 loop 的固有缺陷，真实表现糟糕，是典型反例。

## 相关概念
- [[concepts/coroutine]]
- [[concepts/fiber]]

## 相关实体
- [[entities/ubaserver]]

## 来源提及
- 一个N:1的合作式线程库，等价于event-loop库，但写的是同步代码。 — [[sources/bthread]]
- 在这点上eventloop是类似的，一个回调卡住整个loop就卡住了，比如uba**a**server是百度对异步框架的尝试，由多个并行的eventloop组成，真实表现糟糕。 — [[sources/bthread]]