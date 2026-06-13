---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "PerSecondEx"
  - "bvar::PerSecondEx<T>"
  - "PerSecondEx独立每秒速率"
---


# bvar::PerSecondEx

## 定义
`bvar::PerSecondEx` 是 brpc bvar 模块中的一种独立每秒速率计数器模板类，用于获取某个 bvar 在一段时间窗口内的平均每秒累加值。它不依赖其他 bvar 实例，使用时需要主动向其发送数据。`PerSecondEx` 与 `bvar::WindowEx` 的行为基本一致，唯一区别在于其返回值会额外除以时间窗口长度，从而得到"每秒"的速率。窗口大小 `window_size` 通过模板参数（而非构造函数参数）传递，便于在编译期确定窗口。

## 关键特征
- **独立计数器**：不依赖其他 bvar 即可独立工作，需要使用者主动调用接口发送数据。
- **模板参数指定窗口大小**：`window_size` 作为模板参数传入，而非构造函数参数，使用更简洁直观。
- **返回值为速率**：内部累加值会自动除以时间窗口大小，最终对外暴露的是"平均每秒"的速率。
- **与 `WindowEx` 行为相似**：数据采样与窗口维护逻辑基本相同，仅在最终输出上做了"除以时间窗口"的处理。
- **单维度统计**：属于 bvar 单维度统计体系的一员，使用方式与 `bvar::PerSecond` 类似但更灵活。

## 应用
- 统计 QPS（Queries Per Second）、RPS（Requests Per Second）等以"次/秒"为单位的速率指标。
- 监控某个操作的平均发生频率，例如消息处理速率、事件触发速率、错误发生速率等。
- 在服务监控面板中展示某段时间内的平均速率趋势。
- 与其他 bvar 配合构建更复杂的指标体系，例如配合 `bvar::PerSecond` 进行多种窗口粒度的速率对比。

## 相关概念
- [[concepts/bvar::PerSecond|bvar::PerSecond]]
- [[concepts/bvar::WindowEx|bvar::WindowEx]]

## 相关实体
无相关实体。

## 来源提及
- `bvar::PerSecondEx<T>|  获得某个bvar在一段时间内平均每秒的累加值。不依赖其他的bvar，需要给它发送数据` — [[sources/bvar_c++|bvar_c++]]
- `它和WindowEx基本相同，除了返回值会除以时间窗口之外。` — [[sources/bvar_c++|bvar_c++]]