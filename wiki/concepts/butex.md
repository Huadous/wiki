---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bthread|bthread]]"]
tags: [term]
aliases:
  - "butex"
  - "bthread butex"
---


# butex

## 定义
butex 是 [[sources/bthread|bthread]] 提供的一种同步原语，是 bthread 的两个关键技术之一（另一个是 work stealing 调度）。butex 使得 bthread 和 pthread 能够相互等待和唤醒，从而在数百纳秒内建立并提供多种同步原语。

## 关键特征
- **跨线程模型互操作**：支持 bthread 与 pthread 之间的相互等待和唤醒，这是协程（coroutine）所不需要的功能
- **低延迟**：能够在数百纳秒内完成建立并提供多种同步原语
- **通用同步底座**：作为底层原语，可用于构建多种高层同步机制
- **M:N 线程模型基石**：与 work stealing 调度一起，构成 bthread 实现高效 M:N 线程调度的关键支撑

## 应用
- bthread 内部各种同步原语（如互斥锁、条件变量、信号量等）的基础实现
- 打通 bthread（用户态线程）与 pthread（操作系统线程）之间的同步壁垒，使得两者可以混合使用
- 支撑 bthread 在高并发服务中实现高效的等待/唤醒机制，避免上下文切换开销

## 相关概念
- [[concepts/work-stealing|work stealing]]
- [[concepts/m-n-threading|M:N threading]]

## 相关实体
- [[entities/bthread|bthread]]

## 来源提及
- "关键技术两点：work stealing调度和butex，前者让bthread更快地被调度到更多的核心上，后者让bthread和pthread可以相互等待和唤醒。" — [[sources/bthread|bthread]]