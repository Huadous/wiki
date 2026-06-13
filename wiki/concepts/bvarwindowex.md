---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "WindowEx"
  - "bvar::WindowEx<T>"
  - "WindowEx独立窗口"
---


# bvar::WindowEx

## 定义
bvar::WindowEx 是 brpc bvar 模块中的一种时间窗口计数器模板类，定义为 `bvar::WindowEx<T>`。它是 [[concepts/bvar::Window|bvar::Window]] 的独立版本，不依赖其他 bvar，需要主动向其发送数据。WindowEx 通过模板参数 `T` 传递窗口大小（window_size），而非通过构造函数，从而在某些使用场景下比 [[concepts/bvar::Window|bvar::Window]] 更为便捷。

## 关键特征
- **独立存在**：不依赖其他 bvar 计数器，需要用户主动调用接口发送数据。
- **模板参数配置窗口大小**：`window_size` 通过模板参数在编译期指定，而非运行时构造函数参数，使用更方便。
- **多类型支持**：可与 [[concepts/bvar::Adder|bvar::Adder]]、[[concepts/bvar::Maxer|bvar::Maxer]]、[[concepts/bvar::Miner|bvar::Miner]]、[[concepts/bvar::IntRecorder|bvar::IntRecorder]] 等多种底层统计类型组合使用。
- **秒级统计粒度**：出于性能考虑，WindowEx 每秒对数据做一次统计，返回值在最差情况下存在 1 秒的延时。
- **窗口累计语义**：获得某个 bvar 在一段时间内的累加值。

## 应用
- 在需要自定义窗口大小（编译期确定）的时间窗口统计场景中使用。
- 当不希望使用 [[concepts/bvar::Window|bvar::Window]] 那种依赖外部 bvar 被动收集的模式，而希望由调用方主动 push 数据时，可选用 WindowEx。
- 配合 [[concepts/bvar::Adder|bvar::Adder]] 等类型实现如每秒请求数、每秒错误数等自定义指标的时间窗口聚合。
- 与 [[concepts/bvar::PerSecondEx|bvar::PerSecondEx]] 等其他 Ex 系列组件搭配，构建完整的指标监控体系。

## 相关概念
- [[concepts/bvar::Window|bvar::Window]]
- [[concepts/bvar::PerSecondEx|bvar::PerSecondEx]]
- [[concepts/bvar::Adder|bvar::Adder]]
- [[concepts/bvar::Maxer|bvar::Maxer]]
- [[concepts/bvar::Miner|bvar::Miner]]
- [[concepts/bvar::IntRecorder|bvar::IntRecorder]]

## 相关实体
（无相关实体）

## 来源提及
- `bvar::WindowEx<T>` | 获得某个bvar在一段时间内的累加值。不依赖其他的bvar，需要给它发送数据 — [[sources/bvar_c++|bvar_c++]]
- WindowEx是独立存在的，不依赖其他的计数器，需要给它发送数据。 — [[sources/bvar_c++|bvar_c++]]