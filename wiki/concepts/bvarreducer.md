---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "Reducer模板类"
  - "bvar::Reducer 模板类"
---


# bvar::Reducer

## 定义
bvar::Reducer 是一个模板类 `template <typename T, typename Op> class Reducer : public Variable`，它通过一个二元运算符把多个值合并为一个值。它继承自 [[concepts/Variable|Variable]]，是 bvar 中用于多线程聚合统计的基础模板类。

## 关键特征
- **二元运算符合并**：通过 `Op` 模板参数指定的二元运算符把多个值合并为一个值。
- **结合律要求**：运算符必须满足 `a Op (b Op c) == (a Op b) Op c`，以保证运算顺序不影响结果。
- **交换律要求**：运算符必须满足 `a Op b == b Op a`，以保证操作数的顺序不影响结果。
- **无副作用要求**：运算符必须满足 `a Op b` 不会改变 `a` 和 `b`，以避免线程间的隐式数据竞争。
- **线程安全聚合**：只有同时满足结合律、交换律和无副作用三个条件，才能确保合并结果不受线程私有数据分布的影响。
- **常见子类**：常见的 Reducer 子类包括 [[concepts/bvar::Adder|Adder]]（求和）、[[concepts/bvar::Maxer|Maxer]]（求最大值）、[[concepts/bvar::Miner|Miner]]（求最小值）。

## 应用
- **多线程指标聚合**：在多线程并发场景下，将每个线程私有的局部值安全地合并为一个全局统计值。
- **自定义聚合逻辑**：用户可通过提供满足结合律、交换律、无副作用的二元运算符（如位或、位与、异或等）来自定义聚合方式。
- **监控系统构建**：作为 bvar 模块的基础组件，为监控、统计、计数等场景提供统一的并发安全聚合机制。

## 相关概念
- [[concepts/bvar::Adder]]
- [[concepts/bvar::Maxer]]
- [[concepts/bvar::Miner]]
- [[concepts/Variable]]

## 相关实体
*无相关实体*

## 来源提及
- "Reducer用二元运算符把多个值合并为一个值，运算符需满足结合律，交换律，没有副作用。" — [[sources/bvar_c++|bvar_c++]]
- "常见的Redcuer子类有bvar::Adder, bvar::Maxer, bvar::Miner。" — [[sources/bvar_c++|bvar_c++]]