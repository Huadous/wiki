---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [other]
aliases:
  - "bvar::Stat"
  - "Stat"
---


# bvar::Stat

## 定义
bvar::Stat 是 bvar 库中针对 IntRecorder 在时间窗口衍生类型上的统计结果结构体。它是 `bvar::WindowEx<bvar::IntRecorder>::get_value()` 和 `bvar::PerSecondEx<bvar::IntRecorder>::get_value()` 的返回值类型，用于将 IntRecorder 底层类型的统计结果以结构化形式返回给调用者。

## 关键特征
- **专用返回值类型**：专门用于 WindowEx 与 PerSecondEx 在底层类型为 IntRecorder 时的 `get_value()` 返回值。
- **整型平均值查询**：提供 `get_average_int()` 方法，可直接获取窗口内 IntRecorder 数据的整型平均值。
- **浮点平均值查询**：提供 `get_average_double()` 方法，可直接获取窗口内 IntRecorder 数据的 double 类型平均值。
- **类型区分作用**：是 WindowEx 与 PerSecondEx 在处理 IntRecorder 底层类型时，区别于普通 Adder、Maxer、Miner 等底层类型的关键类型。

## 应用
- 在 brpc 监控场景中，定义一个 `bvar::WindowEx<bvar::IntRecorder, window_size> avg_minute("avg_minute")` 后，调用 `avg_minute.get_value()` 即可获得一个 `bvar::Stat` 对象，进而通过 `get_average_int()` 或 `get_average_double()` 取出对应窗口内（如 60 秒）的平均值，无需手动计算。
- 适用于任何需要从 IntRecorder 时间窗口中直接获取整型或浮点型平均值的监控统计场景。

## 相关概念
（暂无相关概念）

## 相关实体
- [[entities/bvar::WindowEx|bvar::WindowEx]]
- [[entities/bvar::IntRecorder|bvar::IntRecorder]]
- [[entities/bvar::PerSecondEx|bvar::PerSecondEx]]

## 来源提及
- // avg_minute.get_value是60秒内的平均值(返回值是bvar::Stat)，省略最后一个window_size(时间窗口)的话默认为bvar_dump_interval。
bvar::WindowEx<bvar::IntRecorder, window_size> avg_minute("avg_minute"); — [[sources/bvar_c++|bvar_c++]]
- // 获得avg_minuter 60秒内的平均值stat
bvar::Stat avg_stat = avg_minute.get_value();
// 获得整型平均值
int64_t avg_int = avg_stat.get_average_int();
// 获得double类型平均值
double avg_double = avg_stat.get_average_double(); — [[sources/bvar_c++|bvar_c++]]