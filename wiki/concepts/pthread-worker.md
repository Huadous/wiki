---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bthread|bthread]]"]
tags: [term]
aliases:
  - "worker线程"
  - "pthread worker"
---


# pthread worker

## 定义
pthread worker 是 brpc 中 bthread 的执行载体，是运行在操作系统原生 pthread 之上的工作线程。任何时刻每个 pthread worker 上只会运行一个 bthread；当该 bthread 挂起（yield）时，pthread worker 会从本地 runqueue 中弹出下一个待运行的 bthread 继续执行。pthread worker 的数量通常通过 brpc 的 `ServerOptions.num_threads` 或启动参数 `-bthread_concurrency` 进行配置。

## 关键特征
- **一比一承载**：每个 pthread worker 在任意时间点最多运行一个 bthread，是 M:N 线程模型中 "N"（底层 pthread）侧的实体。
- **本地 runqueue 优先调度**：当前 bthread 挂起后，pthread worker 优先从自身关联的本地 runqueue 中取出下一个待运行 bthread。
- **阻塞时的工作窃取（work stealing）**：若正在运行的 bthread 调用了阻塞的 pthread API 或系统函数（例如 `usleep()`），当前 worker 上的其他待运行 bthread 会被空闲的 pthread worker 通过 work stealing 机制偷取并执行，避免 worker 闲置。
- **阻塞扩散风险**：当大量 bthread 同时在 pthread worker 上执行阻塞系统调用时，会占用所有 worker 资源，导致依赖该 worker 驱动的 RPC 网络收发等关键逻辑被暂停。
- **可配置并发度**：并发 worker 数量受 `ServerOptions.num_threads` 与 `-bthread_concurrency` 共同影响，应根据阻塞型调用比例和 CPU 核数合理设置。

## 应用
- **bthread 调度运行**：作为 bthread 调度的物理执行单元，是 [[concepts/bthread|bthread]]（M:N 用户态线程）真正运行起来的载体。
- **M:N 线程模型实现**：与 [[concepts/M:N threading|M:N threading]] 模型配合，使大量 bthread 可以复用在少量 pthread worker 上，从而支撑高并发服务。
- **brpc Server 并发配置**：在 brpc 服务端通过 `ServerOptions.num_threads` 或启动参数 `-bthread_concurrency` 调整 worker 数量，匹配机器资源和业务阻塞特性。
- **避免阻塞型调用耗尽 worker**：指导业务方尽量使用 bthread 提供的异步 API（如 [[sources/client|client]]、[[sources/server|server]] 中暴露的异步接口），而非直接调用阻塞的 pthread API，以防止阻塞扩散到所有 pthread worker。

## 相关概念
- [[concepts/work stealing|work stealing]]
- [[concepts/M:N threading|M:N threading]]
- [[concepts/bthread concurrency|bthread concurrency]]
- [[concepts/bthread|bthread]]

## 相关实体
- [[entities/bthread|bthread]]
- [[entities/brpc|brpc]]

## 来源提及
- pthread worker在任何时间只会运行一个bthread，当前bthread挂起时，pthread worker先尝试从本地runqueue弹出一个待运行的bthread。 — [[sources/bthread|bthread]]
- 若bthread因pthread API或系统函数而阻塞，当前pthread worker上待运行的bthread会被其他空闲的pthread worker偷过去运行。 — [[sources/bthread|bthread]]
- 比如有8个pthread worker，当有8个bthread都调用了系统usleep()后，处理网络收发的RPC代码就暂时无法运行了。 — [[sources/bthread|bthread]]