---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bthread|bthread]]"]
tags: [term]
aliases:
  - "Light-weight process"
  - "LWP"
---


# LWP

## 定义
LWP（Light-weight process）即轻量级进程，是操作系统层面的线程实体。在 Linux 系统中，LWP 通常与 POSIX 线程（pthread）一一对应，每个 pthread 在内核中即表现为一个 LWP。由于 Linux 当下的 pthread 实现（NPTL）采用 1:1 模型，因此 M 个用户态线程（如 bthread）映射到 N 个 pthread，等价于映射到 N 个 LWP。

## 关键特征
- 操作系统内核可调度的基本执行单元，与 POSIX 线程一一对应。
- 由 Linux 的 NPTL（Native POSIX Thread Library）以 1:1 方式实现。
- 在 1:1 线程模型中，每一个 LWP 直接由一个内核线程支持。
- 在 M:N 线程模型中，M 个用户态线程通过线程库调度到 N 个 LWP 上执行。
- 是观察进程内线程资源占用（如通过 `/proc` 中的 task 目录）时的基本单位。

## 应用
- 在 brpc 的 bthread 库中，LWP 充当底层调度目标：M 个 bthread 通过用户态调度器复用到 N 个 LWP（即 N 个 pthread）上。
- 用于性能分析与调试，例如通过 `ps -L`、`top -H` 等工具按 LWP 维度查看 CPU 占用。
- 在线程库设计与运行时实现中，作为"用户态线程 ↔ 内核线程"映射关系的参照。

## 相关概念
- [[concepts/m-n-threading|M:N threading]]
- [[concepts/nptl|NPTL]]

## 相关实体
（无相关实体）

## 来源提及
- "由于linux当下的pthread实现(NPTL)是1:1的，M个bthread也相当于映射至N个LWP。" — [[sources/bthread|bthread]]