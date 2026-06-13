---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management]]"]
tags: [term]
aliases:
  - "BTHREAD_ATTR_SMALL"
  - "bthread 小栈属性"
---


# BTHREAD_ATTR_SMALL

## 定义
BTHREAD_ATTR_SMALL 是 brpc 中 bthread 的栈大小属性之一，对应尺寸小但数量众多的栈使用场景，默认栈大小为 32KB。该属性是 bthread 栈规格差异化设计的一部分，与 BTHREAD_ATTR_NORMAL（默认 1MB）和 BTHREAD_ATTR_LARGE 形成多档位栈规格体系。

## 关键特征
- 默认栈大小为 32KB，远小于 BTHREAD_ATTR_NORMAL 的 1MB
- 栈内存由 brpc 通过 mmap 分配，并由 ResourcePool 进行 caching 管理
- 与 BTHREAD_ATTR_NORMAL 相比，显著降低单个 bthread 的内存占用，允许在同等内存预算下创建更多 bthread
- 适用于"尺寸小但数量众多"的栈使用场景

## 应用
- 大量并发 bthread 且每个 bthread 栈使用较少的业务场景，例如轻量级请求处理、高并发短任务调度等
- 在内存预算有限但需要支撑高并发 bthread 数量的系统中，作为降低内存占用的优化手段
- 用户可根据具体业务场景在 BTHREAD_ATTR_SMALL、BTHREAD_ATTR_NORMAL 等不同栈规格间选择

## 相关概念
- [[concepts/bthread-栈管理|bthread 栈管理]]
- [[concepts/BTHREAD-ATTR-NORMAL|BTHREAD_ATTR_NORMAL]]
- [[concepts/BTHREAD-ATTR-LARGE|BTHREAD_ATTR_LARGE]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/bthread|bthread]]

## 来源提及
- 两种栈分别对应属性BTHREAD_ATTR_NORMAL（栈默认为1M）和BTHREAD_ATTR_SMALL（栈默认为32K）。 — [[sources/memory_management]]
- 所以我们用不同的pool管理不同大小的栈，用户可以根据场景选择。 — [[sources/memory_management]]