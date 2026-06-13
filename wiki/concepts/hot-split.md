---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management]]"]
tags: [phenomenon]
aliases:
  - "热分裂问题"
  - "hot split"
---


# hot split

## 定义
hot split 是 Go 语言 goroutine 在 1.3 版本之前使用 segmented stacks（分段栈）机制时所出现的一种性能问题。当一个 goroutine 的栈恰好在频繁执行的热点函数附近发生分裂（split）时，会反复触发栈的扩张与收缩，造成严重的运行时开销。

## 关键特征
- 出现在 Go 1.3 之前的 segmented stacks（分段栈）实现中
- 根因在于分段栈机制下，运行时需要在热点函数附近插入额外的栈边界检测代码
- 热点函数附近的栈空间使用模式容易反复越过栈边界，触发栈分裂
- 导致频繁的栈扩张与收缩循环，产生可观的运行时开销
- 属于典型的"因栈管理策略选择不当而引入的性能反优化"现象

## 应用
- Go 语言运行时历史演进的案例研究：Go 团队最终用变长连续栈（contiguous stacks，类似于 vector resizing）方案替换了 segmented stacks，从根本上解决了 hot split 问题
- 作为反面教材指导其他语言或运行时系统的栈管理设计，例如 brpc 的 bthread 栈管理在设计时也会参考该问题
- 体现"内存托管语言才适合使用连续栈扩容策略"这一工程经验

## 相关概念
- [[concepts/segmented-stacks|segmented stacks]]
- [[concepts/contiguous-stacks|变长连续栈]]
- [[concepts/bthread-stack-management|bthread 栈管理]]

## 相关实体
*暂无相关实体*

## 来源提及
- goroutine在1.3前通过segmented stacks动态地调整栈大小，发现有hot split问题后换成了变长连续栈（类似于vector resizing，只适合内存托管的语言）。 — [[sources/memory_management]]