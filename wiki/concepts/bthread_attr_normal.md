---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/memory_management.md]]"]
tags: [term]
aliases:
  - "BTHREAD_ATTR_NORMAL"
---


# BTHREAD_ATTR_NORMAL

## 定义
BTHREAD_ATTR_NORMAL 是 brpc 中 bthread 线程栈大小属性（Thread Attribute）的一种预设规格，对应栈尺寸为"普通"级别的使用场景，默认栈大小为 1MB。该属性属于 brpc 根据不同使用场景预设的栈规格分类体系的一部分，与 [[concepts/BTHREAD_ATTR_SMALL|BTHREAD_ATTR_SMALL]] 和 [[concepts/BTHREAD_ATTR_LARGE|BTHREAD_ATTR_LARGE]] 共同构成了 bthread 的栈规格选项。

## 关键特征
- 默认栈大小为 1MB，在栈空间需求和创建性能之间取得了平衡
- 该属性的栈由 brpc 进行 caching 管理，因此创建速度较快
- 适用于"栈尺寸普通但数量较少"的使用场景
- brpc 的 server 端默认使用 BTHREAD_ATTR_NORMAL 运行用户回调代码
- 属于 bthread 栈规格分类体系中的一个中间档位，介于 SMALL（32K）和 LARGE（与 pthread 相同）之间

## 应用
- 作为 brpc Server 端的默认栈属性，用于运行用户注册的业务回调代码
- 适用于绝大多数 RPC 请求处理场景，提供与 pthread 相比更小的栈开销，同时保留足够的栈空间应对一般业务逻辑
- 适合栈空间需求适中、但对 bthread 创建性能有要求的场景

## 相关概念
- [[concepts/BTHREAD_ATTR_SMALL]]
- [[concepts/BTHREAD_ATTR_LARGE]]
- [[concepts/bthread 栈管理]]

## 相关实体
- [[entities/brpc]]
- [[entities/bthread]]

## 来源提及
- 两种栈分别对应属性BTHREAD_ATTR_NORMAL（栈默认为1M）和BTHREAD_ATTR_SMALL（栈默认为32K）。 — [[brpc/memory_management|memory_management]]
- 用户还可以指定BTHREAD_ATTR_LARGE，这个属性的栈大小和pthread一样，由于尺寸较大，bthread不会对其做caching，创建速度较慢。 — [[brpc/memory_management|memory_management]]
- server默认使用BTHREAD_ATTR_NORMAL运行用户代码。 — [[brpc/memory_management|memory_management]]