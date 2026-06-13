---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bthread]]"]
tags: [term]
aliases:
  - "合作式线程"
  - "DP fiber"
  - "Distributed Process fiber"
---


# fiber

## 定义
fiber 是百度 Distributed Process（DP）项目中的 N:1 合作式线程库，是 [[sources/bthread|bthread]] 的前身。fiber 在语义上等价于 event-loop 库，但其编程接口允许开发者编写同步风格的代码。

## 关键特征
- 采用 N:1 线程模型：多个 fiber 运行在同一个系统线程之上，由用户态调度器协作式调度
- 属于合作式线程库，fiber 自身需主动让出执行权，不会被抢占
- 编程模型等价于 event-loop 库，但 API 形式为同步代码，无需显式的回调或异步状态机
- 若不通过 hook 拦截各类阻塞的 glibc 函数，则 fiber 所在的系统线程一旦被阻塞，会导致该系统线程上所有的 fiber 全部阻塞
- 作为 bthread 的前身，奠定了后续 M:N 线程库的设计基础

## 应用
- 在 DP 项目中作为轻量级的用户态并发原语，支撑高并发服务开发
- 作为同步代码风格编写并发逻辑的早期探索，使业务代码无需处理回调地狱
- 覆盖阻塞系统调用（glibc 函数）的 hook 在 fiber 中具有实际意义：即使 hook 会让单次函数调用变慢，仍优于因系统线程阻塞而拖垮所有 fiber 的结果

## 相关概念
- [[concepts/m-n-threading|M:N threading]]
- [[concepts/coroutine|coroutine]]
- [[concepts/event-loop|event loop]]

## 相关实体
- [[entities/distributed-process|Distributed Process]]
- [[entities/bthread|bthread]]

## 来源提及
- "bthread的前身是Distributed Process(DP)中的fiber，一个N:1的合作式线程库，等价于event-loop库，但写的是同步代码。" — [[sources/bthread|bthread]]
- "但这类覆盖对N:1合作式线程库(fiber)有一定意义：虽然函数本身慢了，但若不覆盖会更慢（系统线程阻塞会导致所有fiber阻塞）。" — [[sources/bthread|bthread]]