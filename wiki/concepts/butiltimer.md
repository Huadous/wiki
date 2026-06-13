---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [method]
aliases:
  - "butil计时器"
  - "butil::Timer 类"
---


# butil::Timer

## 定义
butil::Timer 是 brpc 工具库 butil 中提供的计时器类（方法），用于测量代码段的执行时间。它通过 `STARTED` 枚举值在构造时立即开始计时，并提供 `start()` / `stop()` 控制计时起止，以及 `n_elapsed()`、`u_elapsed()`、`m_elapsed()`、`s_elapsed()` 四种时间单位（纳秒、微秒、毫秒、秒）的耗时查询接口。

## 关键特征
- 提供 `STARTED` 枚举值，通过 `explicit Timer(TimerType)` 构造函数在对象创建时立即启动计时。
- 提供 `start()` / `stop()` 方法手动控制计时的启动与停止。
- 提供四种耗时查询方法，对应不同时间粒度：
  - `n_elapsed()` — 纳秒
  - `u_elapsed()` — 微秒
  - `m_elapsed()` — 毫秒
  - `s_elapsed()` — 秒
- 属于 butil 工具库的一部分，被 [[sources/bvar_c++|bvar_c++]] 文档推荐作为延时测量的标准手段。

## 应用
- **代码段耗时测量**：在关键代码路径中通过 `butil::Timer` 测量执行时间，常用于性能基准测试与延迟分析。
- **与 [[bvar::LatencyRecorder]] 配合使用**：在 [[sources/bvar_c++|bvar_c++]] 文档中被推荐用于延时打点，典型用法为：
  ```cpp
  butil::Timer tm(butil::Timer::STARTED);
  // ... 业务逻辑 ...
  bvar::LatencyRecorder g_write_latency;
  g_write_latency << tm.u_elapsed();
  ```
  其中 `timer.u_elapsed()` 返回从构造或最近一次 `start()` 起经过的微秒数，作为延时样本写入 [[bvar::LatencyRecorder]] 进行后续统计与监控。

## 相关概念
无相关概念。

## 相关实体
- [[bvar::LatencyRecorder]]
- [[brpc]]

## 来源提及
- "计时可以使用butil::Timer，接口如下：" — [[sources/bvar_c++|bvar_c++]]
- "class Timer {\npublic:\n    enum TimerType { STARTED };" — [[sources/bvar_c++|bvar_c++]]
- "// butil::Timer tm(butil::Timer::STARTED);  // tm is already started after creation.\n    explicit Timer(TimerType);" — [[sources/bvar_c++|bvar_c++]]