---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_server]]"]
tags: [term]
aliases:
  - "BTHREAD_CONCURRENCY"
  - "bthread并发数"
  - "bthread worker thread count"
---


# bthread_concurrency

## 定义
bthread_concurrency 是一个 gflag（全局标志），用于控制 Apache brpc 进程中 bthread 工作线程的总数。它定义了所有服务器和客户端共享的底层工作线程池的大小上限，直接影响系统的并发处理能力和 CPU 利用率。默认值等于运行机器的 CPU 核心数（包括超线程）。

## 关键特征
- **全局配置**：影响整个 brpc 进程，所有基于该进程的 server 和 client 共享同一个 bthread 工作线程池。
- **默认值自适应**：默认等于 CPU 核心数（含超线程），确保充分利用硬件资源。
- **可动态调整**：可通过命令行参数 `-bthread_concurrency` 设置，运行时也可修改。
- **优先级规则**：如果多个 server 设置了不同的 `num_threads`（如 `ServerOptions.num_threads`），实际工作线程数取所有 server 中 `num_threads` 的最大值，但不得超过 `bthread_concurrency` 设定的全局上限。
- **性能边界**：该值决定了 bthread 调度器可以同时运行的 pthread 数量，从而控制并行度。

## 应用
- **并发控制**：在多服务实例部署于同一进程的场景下，通过设置一个合理的全局上限，避免工作线程过度竞争 CPU。
- **资源规划**：根据机器 CPU 和任务特性（如 I/O 密集型或计算密集型）调整该值，以优化吞吐量和延迟。
- **客户端侧优化**：客户端也可通过此标志修改并发度，从而影响出站请求的并行能力。
- **运维调试**：在线上集群中运行时修改该值，可在不重启进程的情况下调整并发策略。

## 相关概念
- [[concepts/bthread|bthread]]
- [[concepts/pthread-mode|pthread mode]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/serviceoptions|serviceoptions]]（其中包含 `num_threads` 字段）

## 来源提及
- "Channel does not have a corresponding option, but user can change number of worker pthreads at client-side by setting gflag -bthread_concurrency." — [[sources/en_server|en_server]]
- "Total number of threads is the maximum of all ServerOptions.num_threads and bthread_concurrency." — [[sources/en_server|en_server]]