---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/bthread]]"]
tags: [term]
aliases:
  - "协程"
  - "coroutine"
---


# coroutine

## 定义
本文中的协程特指 N:1 线程库，即所有协程运行于一个系统线程中，计算能力与各类 event loop 库等价。协程之间切换不需要系统调用，可以非常快（约 100ns–200ns），受 cache 一致性的影响也小。但代价是无法高效利用多核，代码必须非阻塞，否则所有协程都会被卡住。

## 关键特征
- **N:1 线程模型**：所有协程运行于单一系统线程之中
- **与 event loop 等价**：在计算能力上与各类 event loop 库相当
- **切换开销低**：协程间切换无需陷入内核，速度约为 100ns–200ns
- **缓存友好**：不跨线程，受 CPU cache 一致性影响较小
- **无法利用多核**：单线程模型使其不能高效地利用多核 CPU
- **必须非阻塞**：代码若包含阻塞调用，将卡住所有协程

## 应用
- 适合编写运行时间确定的 IO 服务器，典型如 [[concepts/Http Server|Http Server]]
- 适用于 I/O 密集型、不需要并行计算能力的场景
- 对开发者要求苛刻，需要编写非阻塞、可协作调度的代码

## 相关概念
- [[concepts/M:N threading|M:N threading]]
- [[concepts/event loop|event loop]]
- [[concepts/fiber|fiber]]

## 相关实体
- [[entities/ubaserver|ubaserver]]

## 来源提及
- 我们常说的协程特指N:1线程库，即所有的协程运行于一个系统线程中，计算能力和各类eventloop库等价。 — [[sources/bthread|bthread]]
- 由于不跨线程，协程之间的切换不需要系统调用，可以非常快(100ns-200ns)，受cache一致性的影响也小。但代价是协程无法高效地利用多核，代码必须非阻塞，否则所有的协程都被卡住，对开发者要求苛刻。 — [[sources/bthread|bthread]]