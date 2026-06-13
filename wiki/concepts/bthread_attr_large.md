---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management|memory_management]]"]
tags: [term]
aliases:
  - "BTHREAD_ATTR_LARGE 栈属性"
  - "bthread 大栈属性"
---


# BTHREAD_ATTR_LARGE

## 定义
BTHREAD_ATTR_LARGE 是 brpc 中 bthread 的栈大小属性之一，其栈大小与 pthread 相同。由于单次栈分配占用空间较大，brpc 不会对 BTHREAD_ATTR_LARGE 的栈做 caching 管理，因此使用该属性的 bthread 创建速度较慢。该属性是 brpc 为少数特殊用例提供的后备选项。

## 关键特征
- 栈大小与 pthread 相同，属于大栈规格
- 单次栈分配占用空间较大，brpc 不对其做 caching 管理
- 创建速度较慢，因缺少栈缓存复用机制
- 适用于栈空间需求不确定或较大的特殊场景
- 属于 brpc bthread 栈规格三级体系（Normal、Small、Large）中的最高级别

## 应用
- 栈空间需求较大或无法预估峰值的 bthread 任务
- 作为 Normal 和 Small 栈规格不满足需求时的后备选项
- 覆盖从高频小栈到低频大栈的完整需求谱系中的低频大栈场景

## 相关概念
- [[concepts/bthread-attr-normal|BTHREAD_ATTR_NORMAL]]
- [[concepts/bthread-attr-small|BTHREAD_ATTR_SMALL]]
- [[concepts/bthread-栈管理|bthread 栈管理]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/bthread|bthread]]

## 来源提及
- "用户还可以指定BTHREAD_ATTR_LARGE，这个属性的栈大小和pthread一样，由于尺寸较大，bthread不会对其做caching，创建速度较慢。" — [[sources/memory_management|memory_management]]