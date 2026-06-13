---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bthread|bthread]]"]
tags: [term]
aliases:
  - "Native POSIX Thread Library"
  - "NPTL 线程库"
---


# NPTL

## 定义
NPTL（Native POSIX Thread Library）是 Linux 操作系统下当前主流的 POSIX 线程（pthread）实现。它采用 1:1 线程模型，即每个用户态线程（pthread）都由内核直接支持，对应一个内核可调度实体（LWP，Light-Weight Process）。

## 关键特征
- **1:1 线程模型**：每个用户态 pthread 与一个内核线程（LWP）一一对应，由内核直接调度。
- **POSIX 兼容**：实现了 POSIX 标准的线程 API（pthread）。
- **Linux 原生**：自 Linux 2.6 起成为 glibc 的默认 pthread 实现，取代了早期的 LinuxThreads。
- **调度由内核完成**：线程的创建、调度、同步等行为均由内核参与，开销相对 M:N 模型更高，但实现简单、行为可预测。

## 应用
- 作为 Linux 上 C/C++ 多线程程序的底层线程运行时，被绝大多数现代 Linux 发行版默认采用。
- 在 brpc 的 bthread 文档中被引用：bthread 的 M 个用户线程最终映射到 N 个 pthread，而由于 NPTL 是 1:1 模型，这 N 个 pthread 又等价于 N 个 LWP，因此 M 个 bthread 整体上仍映射到 N 个 LWP。

## 相关概念
- [[concepts/M:N-threading|M:N threading]]
- [[concepts/LWP|LWP]]

## 相关实体
无相关实体。

## 来源提及
- "由于linux当下的pthread实现(NPTL)是1:1的，M个bthread也相当于映射至N个LWP。" — [[sources/bthread|bthread]]