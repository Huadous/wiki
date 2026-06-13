---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management|memory_management]]"]
tags: [term]
aliases:
  - "bthread_id_t"
  - "bthread id 类型"
  - "brpc bthread_id_t"
---


# bthread_id_t

## 定义
bthread_id_t 是 brpc 中用于标识某种 bthread 相关资源的 id 类型。它与 [[concepts/bthread_t|bthread_t]] 和 [[entities/brpc|brpc]] 中的 SocketId 一样，采用 32 位版本号加 32 位偏移量的复合结构，其中偏移量通过 [[concepts/resource-pool|ResourcePool<T>]] 方案进行分配。

## 关键特征
- 采用 64 位复合结构：高 32 位为版本号，低 32 位为偏移量
- 偏移量由 [[concepts/resource-pool|ResourcePool<T>]] 方案分配，保证 O(1) 时间内的查找性能
- 版本号机制用于检测对象失效，可有效应对 [[concepts/aba问题|ABA问题]]
- 是 brpc 统一 id 生成模式的典型实例，体现了"id = 版本号 + 偏移量"的设计哲学
- 与 [[concepts/bthread_t|bthread_t]]、SocketId 共享相同的底层分配与验证机制

## 应用
- 在 brpc 中标识各类 bthread 相关资源（如 task_group、butex 等）
- 作为通用 id 模式被多个子系统复用，与 [[concepts/bthread_t|bthread_t]] 和 SocketId 统一设计
- 通过版本号机制在对象释放与重用过程中检测悬挂引用，避免 ABA 问题
- 验证了"等长对象分配 + 版本号"方案在不同资源场景下的通用性与可扩展性

## 相关概念
- [[concepts/bthread_t|bthread_t]]
- [[concepts/aba问题|ABA问题]]
- [[concepts/等长对象分配|等长对象分配]]
- [[concepts/resource-pool|ResourcePool<T>]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "这种id生成方式在brpc中应用广泛，brpc中的SocketId，bthread_id_t也是用类似的方法分配的。" — [[sources/memory_management|memory_management]]