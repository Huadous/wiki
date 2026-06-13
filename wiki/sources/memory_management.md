---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/memory_management.md]]"
tags: [ResourcePool<T>, ObjectPool<T>, bthread, bthread_t, ABA问题, 等长对象分配, guard page, segmented stacks, 内存池, bthread 栈管理, TaskMeta, SocketId, bthread_id_t, BTHREAD_ATTR_NORMAL, BTHREAD_ATTR_SMALL, BTHREAD_ATTR_LARGE, hot split, 变长连续栈]
aliases: ["brpc Memory Management: ResourcePool and ObjectPool", "brpc内存管理机制"]
---

# brpc内存管理：ResourcePool与ObjectPool - Summary

## 来源
- Original file: [[brpc/memory_management.md]]
- Ingested: 2026-06-13

## 核心内容
本文深入讨论了 [[entities/brpc|brpc]] 框架中的内存管理机制，重点介绍 [[concepts/resourcepoolt|ResourcePool<T>]] 和 [[concepts/objectpoolt|ObjectPool<T>]] 两个核心组件。多线程内存分配需要在减少线程间竞争与降低空间浪费之间权衡，通用方案如 [[entities/tcmalloc|tcmalloc]] 和 [[entities/jemalloc|jemalloc]] 虽成熟但对底层性能敏感的应用仍不够用。brpc 利用大多数结构等长的特点，通过批量分配与归还、thread-local free block 和全局 free block 的层级化设计，实现了高效的 [[concepts/等长对象分配|等长对象分配]]。[[concepts/resourcepoolt|ResourcePool]] 返回偏移量以支持作为 64 位 id 的一部分（用于生成 [[concepts/bthread_t|bthread_t]]），[[concepts/objectpoolt|ObjectPool]] 则直接返回对象指针。[[concepts/bthread|bthread]] 的栈管理通过 mmap 分配并配合 [[concepts/guard-page|guard page]] 检测溢出，提供 [[concepts/bthread_attr_normal|NORMAL]]、[[concepts/bthread_attr_small|SMALL]]、[[concepts/bthread_attr_large|LARGE]] 三种规格。文章也对比了 goroutine 的 [[concepts/segmented-stacks|segmented stacks]] 和 [[concepts/变长连续栈|变长连续栈]] 方案，阐述了 bthread 选择等长栈的原因。

## 关键实体
- [[entities/brpc|brpc]] — Apache 开源的高性能 RPC 框架，源自百度，本文讨论的内存管理组件均属于该框架
- [[entities/tcmalloc|tcmalloc]] — Google 开发的高性能多线程内存分配器，文中作为通用方案参照
- [[entities/jemalloc|jemalloc]] — Facebook 主导开发的高性能通用内存分配器，文中作为通用方案参照

## 关键概念
- [[concepts/resourcepoolt|ResourcePool<T>]] — brpc 的核心内存分配模板类，返回偏移量而非指针，专为等长对象设计
- [[concepts/objectpoolt|ObjectPool<T>]] — ResourcePool 的变种，直接返回对象指针
- [[concepts/等长对象分配|等长对象分配]] — brpc 内存管理的核心优化假设，大幅简化分配过程
- [[concepts/内存池|内存池]] — 通过批量分配与层级缓存降低竞争与开销的技术
- [[concepts/bthread|bthread]] — brpc 的用户态线程（协程），平均创建耗时小于 200ns
- [[concepts/bthread_t|bthread_t]] — 由 32 位版本号 + 32 位偏移量组成的 bthread 标识符
- [[concepts/taskmeta|taskmeta]] — bthread 的底层数据结构，所有 TaskMeta 由 ResourcePool 分配
- [[concepts/aba问题|ABA问题]] — 无锁编程中的经典现象，通过 bthread_t 中的版本号机制缓解
- [[concepts/socketid|socketid]] — 采用与 bthread_t 相同的生成方式（版本号+偏移量）
- [[concepts/bthread_id_t|bthread_id_t]] — 采用与 bthread_t 相同的生成方式
- [[concepts/bthread-栈管理|bthread 栈管理]] — 按 NORMAL/SMALL/LARGE 三档管理 bthread 栈
- [[concepts/guard-page|guard page]] — 用于检测栈溢出的保护性内存页（4K）
- [[concepts/bthread_attr_normal|BTHREAD_ATTR_NORMAL]] — 默认 1M 栈大小，server 端默认使用
- [[concepts/bthread_attr_small|BTHREAD_ATTR_SMALL]] — 默认 32K 栈大小，适合大量小任务
- [[concepts/bthread_attr_large|BTHREAD_ATTR_LARGE]] — 与 pthread 同栈大小，不做 caching
- [[concepts/segmented-stacks|segmented stacks]] — goroutine 1.3 之前的栈管理方案，存在 hot split 问题
- [[concepts/变长连续栈|变长连续栈]] — goroutine 1.3 之后的栈管理方案，类 vector resizing
- [[concepts/hot-split|hot split]] — 分段栈中因栈边界频繁扩张/收缩导致的性能问题

## 要点
- 多线程内存分配的核心权衡在于**线程间竞争少**与**浪费空间少**之间，通用 malloc 方案对底层性能敏感的应用仍不够用
- brpc 利用"大多数结构等长"的属性，通过 [[concepts/resourcepoolt|ResourcePool]] 和 [[concepts/objectpoolt|ObjectPool]] 做极致优化，但**明确不鼓励用户在程序中滥用**
- [[concepts/resourcepoolt|ResourcePool]] 通过 thread-local free block → 全局 free block → 批量申请的三级机制实现低竞争分配，并返回偏移量（可作为 64 位 id 的一部分）
- [[concepts/bthread_t|bthread_t]] 由 32 位版本号 + 32 位偏移量组成，通过版本号解决 [[concepts/aba问题|ABA问题]]；该 id 生成方式在 brpc 中广泛应用（包括 [[concepts/socketid|SocketId]]、[[concepts/bthread_id_t|bthread_id_t]]）
- bthread 创建平均耗时小于 200ns，底层结构 [[concepts/taskmeta|taskmeta]] 由 ResourcePool 分配
- bthread 栈分为 [[concepts/bthread_attr_normal|NORMAL（1M）]]、[[concepts/bthread_attr_small|SMALL（32K）]]、[[concepts/bthread_attr_large|LARGE]] 三档，使用 mmap 分配并设置 [[concepts/guard-page|guard page]] 检测溢出
- 对比 goroutine 的 [[concepts/segmented-stacks|segmented stacks]] 和 [[concepts/变长连续栈|变长连续栈]] 方案，bthread 因主要运行在 64 位平台、虚存空间庞大，决定暂不引入变长栈