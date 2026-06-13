---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_io]]"]
tags: [method]
aliases:
  - "原子计数器"
  - "atomic counter"
---


# atomic variable

## 定义
atomic variable（原子变量）是 brpc 中用于在边缘触发事件处理机制下，以无锁方式记录文件描述符（fd）事件到达次数的原子计数器。它利用 CPU 支持的原子操作和恰当的内存序，在 epoll 通知事件时对计数器进行原子性加一操作，实现了 fd 事件分发的 wait-free 级别并发控制。

## 关键特征
- **原子性操作**：对计数器的读取、修改和写入作为一个不可分割的单元完成，避免数据竞争
- **内存序控制**：通过恰当的内存序（如 memory_order_relaxed 或 memory_order_release）在性能与可见性之间取得平衡
- **零开销检查**：通过检查加一前的值是否为 0 来决定是否需要创建新 bthread，避免了不必要的上下文切换
- **wait-free 级别**：所有线程对同一 fd 的事件分发操作均无需等待或自旋，达到了无等待的并发级别
- **与边缘触发协同**：配合 epoll 的边缘触发模式（edge triggered），确保每个新事件都能被原子计数器准确捕获

## 应用
- **EventDispatcher 事件分发**：在 [[entities/eventdispatcher|EventDispatcher]] 中，每个活跃的 fd 关联一个 atomic variable。当 epoll 返回事件时，对相应 fd 的计数器进行原子加一，若加一前为零则启动一个 [[concepts/bthread|bthread]] 处理数据
- **Socket 事件管理**：用于 [[entities/socket|Socket]] 对象的事件状态管理中，高效记录事件到达次数而无需锁保护
- **高性能网络框架**：作为 brpc IO 机制的核心组件之一，确保高频事件分发场景下 CPU 缓存不产生无效竞争

## 相关概念
- [[concepts/edge-triggered-mode|edge triggered mode]]
- [[concepts/bthread|bthread]]
- [[concepts/work-stealing|work stealing]]
- [[concepts/wait-free-mpsc-list|Wait-free MPSC list]]

## 相关实体
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/socket|Socket]]

## 来源提及
- "After receiving an event, an atomic variable associated with the fd is added by one atomically." — [[sources/en_io]]
- "If the variable is zero before addition, a bthread is started to handle the data from the fd." — [[sources/en_io]]
- "These methods make contentions on dispatching events of one fd wait-free." — [[sources/en_io]]