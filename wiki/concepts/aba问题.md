---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management|memory_management]]"]
tags: [phenomenon]
aliases:
  - "ABA problem"
  - "ABA 现象"
---


# ABA问题

## 定义
ABA问题是无锁编程（lock-free programming）和数据回收领域中的一种经典并发现象。它指的是：一个线程读取了某个内存位置的旧值 A 之后，期间该位置可能被其他线程修改为新值 B，再被改回 A；此时原线程虽然读到相同的 A 值，但实际上该位置已经经历了多次变更，可能导致对资源生命周期的误判（例如错误地将已回收的对象视为仍然有效）。

## 关键特征
- 属于并发编程中的典型并发缺陷，常见于基于 CAS（Compare-And-Swap）的无锁算法
- 仅靠值比较无法区分"值未变"与"值经历变化后回到原值"这两种情况
- 在对象/资源回收场景下，可能导致访问到已被回收或复用的内存
- 通常通过引入版本号（version counter）、标签指针（tagged pointer）等机制加以缓解
- 无法仅通过内存分配器本身解决，分配器只负责分配与回收，不感知 ABA 问题

## 应用
- **无锁数据结构**：无锁栈、无锁队列、Lock-Free HashMap 等并发容器的设计与正确性验证
- **内存回收机制**：基于 Hazard Pointer、RCU、Epoch-Based Reclamation 等方案的内存安全判断
- **指针复用检测**：brpc 中 bthread_t 类型通过在 id 中嵌入 32 位版本号，每次资源回收时版本递增，访问时通过版本匹配判断资源是否仍有效，从而缓解 ABA 问题
- **垃圾回收器**：追踪式 GC 与引用计数算法中对对象生命周期的判定
- **事务内存**：软件事务内存（STM）中的冲突检测

## 相关概念
- [[concepts/bthread-t|bthread_t]]
- [[concepts/lock-free-programming|无锁编程]]

## 相关实体
（暂无相关实体）

## 来源提及
- "通过对应的偏移量仍可以访问到对象，即ResourcePool只负责内存分配，并不解决ABA问题。" — [[sources/memory_management|memory_management]]
- "版本解决ABA问题，偏移量由ResourcePool<TaskMeta>分配。" — [[sources/memory_management|memory_management]]
- "注意：这只是大概的说法，在多线程环境下，即使版本相等，bthread仍可能随时失效" — [[sources/memory_management|memory_management]]