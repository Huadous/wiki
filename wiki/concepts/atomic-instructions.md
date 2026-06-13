---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_io]]"]
tags: [term]
aliases:
  - "Atomic Operations"
  - "Atomic Variables"
  - "原子操作"
---


# Atomic Instructions

## 定义
原子指令（Atomic Instructions）是硬件层面提供的一种不可分割的操作原语。在brpc中，它们被用于实现无锁（wait-free）同步机制，使得多线程环境下对共享变量的读写操作能够确保原子性，而无需依赖传统锁机制。原子变量（atomic variables）是原子指令在编程语言层面的封装，brpc利用它们在关键路径上替代互斥锁，从而显著降低延迟。

## 关键特征
- **不可分割性（Indivisibility）**：原子指令的执行要么全部完成，要么完全不执行，中间状态对其他线程不可见。
- **硬件原生支持**：由CPU直接提供（如x86的LOCK前缀指令、CMPXCHG、XADD等），属于最底层的同步基元。
- **无锁（Lock-Free）**：使用原子指令实现的同步机制不涉及线程挂起或上下文切换，避免了锁竞争带来的性能开销。
- **内存顺序约束（Memory Ordering）**：原子操作通常提供多种内存序（如relaxed、acquire、release、acq_rel、seq_cst），允许开发者在性能与可见性之间权衡。
- **组合能力**：单个原子指令可同时完成读-改-写（Read-Modify-Write）操作，例如原子地增加值（fetch_add）或比较并交换（compare_and_swap）。

## 应用
- **Socket::StartInputEvent的实现基础**：brpc的Socket模块利用原子变量和原子指令实现免锁的事件分发机制。理解原子指令是理解`StartInputEvent`函数如何确保事件投递的线程安全性的前提。
- **bthread的启动计数器**：brpc在启动bthread之前，使用原子变量以原子方式递增计数器，从而避免使用互斥锁，这是实现低延迟事件处理的关键。
- **引用计数（Reference Counting）**：`SocketUniquePtr`等智能指针内部使用原子操作管理Socket的生命周期，实现无锁的资源回收。
- **无锁队列（Lock-Free Queue）**：brpc内部的数据结构（如等待队列、任务队列）依赖原子指令实现多生产者/多消费者的高效通信。

## 相关概念
- [[concepts/wait-free|Wait-Free]]
- [[concepts/work-stealing|Work Stealing]]
- [[concepts/bthread|Bthread]]
- [[concepts/lock-free|Lock-Free]]
- [[concepts/memory-ordering|Memory Ordering]]
- [[concepts/compare-and-swap|Compare-and-Swap (CAS)]]

## 相关实体
- [[entities/socket|Socket]]
- [[entities/socketid|SocketId]]
- [[entities/socketuniqueptr|SocketUniquePtr]]
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/bthread|Bthread]]
- [[entities/bvar|bvar]]
- [[entities/braft|braft]]

## 来源提及
- To understand exactly how that atomic variable works, you can read atomic instructions first, then check Socket::StartInputEvent. — [[sources/en_io|en_io]]