---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management|memory_management]]"]
tags: [method]
aliases:
  - "ObjectPool"
  - "brpc ObjectPool"
---


# ObjectPool<T>

## 定义
ObjectPool<T> 是 brpc 中 ResourcePool<T> 的简化变种，是一种面向多线程场景的等长对象池。它在内部结构上与 ResourcePool<T> 类似，但接口不返回偏移量，而是直接返回对象指针，对使用者而言就是一个简洁的多线程对象池分配器。

## 关键特征
- 不返回偏移量，而是直接返回对象指针，使用方式更直观
- 内部结构与 [[concepts/resourcepool-t|ResourcePool<T>]] 类似，但更为简洁
- 面向等长对象（fixed-size object）进行批量分配
- 受益于批量分配机制，具备低竞争与低开销优势
- 专为多线程环境下的高频对象分配与回收设计
- 与 ResourcePool<T> 共享底层内存池优化思想

## 应用
- 在 brpc 的 `Socket::Write` 中，每个待写出的请求会被包装为 `WriteRequest`，该对象即由 `ObjectPool<WriteRequest>` 分配
- 适用于需要频繁创建和销毁固定大小对象的网络 I/O 路径
- 任何等长、高并发、短生命周期对象的分配场景均适合采用该对象池

## 相关概念
- [[concepts/resourcepool-t|ResourcePool<T>]]
- [[concepts/等长对象分配|等长对象分配]]
- [[concepts/内存池|内存池]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- 这是ResourcePool<T>的变种，不返回偏移量，而直接返回对象指针。 — [[sources/memory_management|memory_management]]
- 比如Socket::Write中把每个待写出的请求包装为WriteRequest，这个对象就是用ObjectPool<WriteRequest>分配的。 — [[sources/memory_management|memory_management]]