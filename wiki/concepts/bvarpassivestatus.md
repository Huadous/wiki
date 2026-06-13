---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "PassiveStatus"
  - "PassiveStatus按需显示"
  - "bvar::PassiveStatus"
---


# bvar::PassiveStatus

## 定义
bvar::PassiveStatus 是 brpc bvar 模块中的一种特殊变量类型，用于按需显示值。在某些场景下，用户无法调用 `set_value` 或不确定以何种频率调用 `set_value`，此时更适合"当需要显示时才打印"的模式。PassiveStatus 通过让用户传入打印回调函数来实现按需获取值的机制。

## 关键特征
- 采用按需取值策略，无需周期性 `set_value`
- 由用户提供打印回调函数（callback），需要展示数据时回调被触发
- 无需内部存储统计量，避免冗余存储开销
- 被官方文档评价为"最有用的 bvar 之一"
- 特别适合"统计量已存在于外部，无需再次存储"的场景

## 应用
- 获取系统级统计信息（如通过 `getlogin_r` 系统调用按需获取进程用户名）
- 显示已由其他模块维护的统计数据，避免重复存储
- 任何 `set_value` 频率难以确定或不方便主动写入的统计场景
- 降低 bvar 的内存占用，仅在读取时调用回调

## 相关概念
- [[concepts/bvar::Status]]
- [[concepts/bvar::Variable]]

## 相关实体
无相关实体。

## 来源提及
- "bvar::PassiveStatus | 按需显示值。在一些场合中，我们无法set_value或不知道以何种频率set_value，更适合的方式也许是当需要显示时才打印。用户传入打印回调函数实现这个目的" — [[sources/bvar_c++|bvar_c++]]
- "虽然很简单，但PassiveStatus是最有用的bvar之一，因为很多统计量已经存在，我们不需要再次存储它们，而只要按需获取。" — [[sources/bvar_c++|bvar_c++]]