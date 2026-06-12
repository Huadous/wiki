---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_io]]"]
tags: [term]
aliases:
  - "无锁"
  - "Lock-Free算法"
---


# lock-free

## 定义
无锁（lock-free）是一种非阻塞算法，至少保证一个线程能持续进展，但可能有线程饥饿。与等待自由（wait-free）相比，无锁允许某些线程可能被其他线程延迟，但整体系统仍然向前推进。在用户态线程调度和并发数据结构中，lock-free 常用于避免内核级锁的开销。

## 关键特征
- **非阻塞性**：至少一个线程在任何时刻都能继续执行
- **线程饥饿可能**：不保证每个线程都持续进展
- **逻辑正确性**：系统整体始终向前推进，不会死锁
- **CAO操作**：通常依赖CAS（Compare-And-Swap）等原子指令实现
- **低延迟**：避免上下文切换和锁竞争

## 应用
- **高性能并发容器**：如 ConcurrentHashMap、无锁队列
- **网络框架**：brpc 中 Socket::SetFailed 方法是无锁实现
- **内存管理**：如引用计数、垃圾回收中的无锁栈
- **用户态调度器**：避免内核态锁的开销

## 相关概念
- [[concepts/wait-free|wait-free]]
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/cas|CAS (Compare-And-Swap)]]

## 相关实体
- [[entities/socket|Socket]]
- [[entities/bvar|bvar]]

## 来源提及
- "This function is lock-free." — [[sources/en_io|en_io]]（此函数是无锁的）