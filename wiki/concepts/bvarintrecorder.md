---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "IntRecorder"
  - "bvar IntRecorder"
---


# bvar::IntRecorder

## 定义
bvar::IntRecorder 是 brpc 中 bvar 库提供的一个类，继承自 [[concepts/bvar::Variable|Variable]]，用于计算**自使用以来的所有输入值的平均值**。注意其定语并非"一段时间内"，即它记录的是从对象创建起累积的全部样本的平均值，而非滑动窗口内的平均值。若要获得时间窗口内的平均值，需要使用 [[concepts/bvar::Window|Window]] 衍生计算。

## 关键特征
- 继承自 [[concepts/bvar::Variable|Variable]]，是 bvar 框架中用于"求平均"的整数型变量类型
- 注释明确指出其语义为"求自使用以来的平均值"，定语不是"一段时间内"
- 一般需要与 [[concepts/bvar::Window|Window]] 搭配使用，由 Window 衍生出时间窗口内的平均值
- 内部通过累积和（sum）与计数（count）计算整体均值
- 适合对**累加型、平均型**指标的统计建模，而非窗口型

## 应用
- 计算平均延迟（latency）：将每次请求耗时累加进 IntRecorder 后取平均
- 计算平均响应大小：跟踪响应包体积的平均水平
- 计算平均队列长度、平均处理时长等长时间累积型指标
- 与 [[concepts/bvar::Window|Window]] 或 [[concepts/bvar::WindowEx|WindowEx]] 组合，输出每秒/每分钟等时间窗口维度的平均值
- 作为 [[concepts/bvar::LatencyRecorder|LatencyRecorder]] 的底层组件之一，用于更复杂的延迟统计

## 相关概念
- [[concepts/bvar::Window]]
- [[concepts/bvar::WindowEx]]
- [[concepts/bvar::LatencyRecorder]]

## 相关实体
无相关实体

## 来源提及
- bvar::IntRecorder| 求自使用以来的平均值。注意这里的定语不是"一段时间内"。一般要通过Window衍生出时间窗口内的平均值 — [[sources/bvar_c++|bvar_c++]]
- // For calculating average of numbers. — [[sources/bvar_c++|bvar_c++]]