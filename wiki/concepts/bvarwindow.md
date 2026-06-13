---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "Window时间窗口"
  - "bvar::Window<VAR>"
---


# bvar::Window

## 定义
bvar::Window 是一个模板类，用于获得某个 bvar（多维度统计变量）在过去一段时间内的统计值，例如累加值、平均值、最大值、最小值等。它是一种"衍生变量"（derived variable），必须依赖于一个已经存在的 bvar 计数器，不能独立存在。

## 关键特征
- **依赖性**：Window 不能独立存在，必须依附于一个已有的 bvar 计数器。
- **自动更新**：无需手动向 Window 发送数据，它会自动从原计数器同步。
- **时间窗口配置**：window_size 通过构造函数参数传递，单位为秒。
- **采样机制**：出于性能考虑，Window 的数据来源于每秒一次对原计数器的采样。
- **延时特性**：在最差情况下，返回值存在 1 秒的延时。

## 应用
- 统计"上一分钟的错误数"。
- 统计"上一分钟的 CPU 占用率"。
- 任何需要观察某个指标在最近一段时间内聚合表现（如求和、求平均、极值等）的监控场景。
- 实时监控面板中展示近 N 秒内的关键指标趋势。

## 相关概念
- [[concepts/bvar::PerSecond|bvar::PerSecond]]
- [[concepts/bvar::WindowEx|bvar::WindowEx]]
- [[concepts/bvar::Adder|bvar::Adder]]

## 相关实体
（暂无相关实体）

## 来源提及
- bvar::Window<VAR>| 获得某个bvar在一段时间内的累加值。Window衍生于已存在的bvar，会自动更新 — [[sources/bvar_c++|bvar_c++]]
- Window不能独立存在，必须依赖于一个已有的计数器。Window会自动更新，不用给它发送数据。 — [[sources/bvar_c++|bvar_c++]]