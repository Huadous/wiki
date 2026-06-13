---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management|memory_management]]"]
tags: [product]
aliases:
  - "jemalloc 内存分配器"
  - "Facebook jemalloc"
  - "jemalloc allocator"
---


# jemalloc

## 基本信息
- Type: product
- Source: [[sources/memory_management|memory_management]]

## 描述
jemalloc 是一款由 Facebook 主导开发的高性能通用内存分配器（memory allocator），最初为 FreeBSD 操作系统设计，后被广泛应用于各类服务端与高并发场景。jemalloc 通过线程本地缓存（thread-local cache）、arena 分区等机制有效降低多线程环境下的锁竞争，提升分配与释放的吞吐量。brpc 在 [[sources/memory_management|memory_management]] 文档中将其与 [[entities/tcmalloc|tcmalloc]] 并列，作为一般应用推荐使用的成熟内存分配方案之一。但对于 brpc 这类对性能长尾（performance long tail）和等长小对象分配（fixed-size small object allocation）有极致要求的底层框架，jemalloc 这类通用分配器仍存在不足，因此 brpc 自行实现了 [[concepts/resource-pool|ResourcePool]] 与 [[concepts/object-pool|ObjectPool]] 以满足特定场景需求。

## 相关实体
- [[entities/tcmalloc|tcmalloc]]
- [[entities/brpc|brpc]]

## 相关概念
- [[concepts/memory-pool|内存池]]
- [[concepts/fixed-size-object-allocation|等长对象分配]]

## 来源提及
- "一般的应用可以使用tcmalloc、jemalloc等成熟的内存分配方案，但这对于较为底层，关注性能长尾的应用是不够的。" — [[sources/memory_management|memory_management]]