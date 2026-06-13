---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "WindowExAdapter"
  - "adapter::WindowExAdapter"
---


# bvar::WindowExAdapter

## 定义
WindowExAdapter 是 bvar 库中定义在 `adapter` 命名空间下的模板适配器类，是 `bvar::WindowEx` 与 `bvar::PerSecondEx` 的共同基类。它通过模板参数 `R` 指定数据类型，并通过第二个模板参数 `WindowExType<R>` 或 `PerSecondExType<R>` 区分两类不同行为：`WindowEx` 返回原始时间窗口内的统计值，而 `PerSecondEx` 将返回值除以时间窗口以得到平均每秒速率。其窗口大小 `window_size` 必须在编译期以模板常量传入，区别于通过构造函数参数传入的 `bvar::Window`。

## 关键特征
- 模板适配器，定义于 bvar `adapter` 命名空间
- 是 `bvar::WindowEx` 与 `bvar::PerSecondEx` 的共同基类
- 模板参数包括数据类型 `R` 与行为类型（`WindowExType<R>` / `PerSecondExType<R>`）
- 窗口大小通过模板参数 `window_size`（默认值 `0`，省略时等同于 `bvar_dump_interval`）在编译期传入
- 使用其的类（如 `WindowEx`、`PerSecondEx`）不依赖其他已存在的 bvar，需要主动向其推送数据

## 应用
- 用于实现时间窗口内的数据统计与采样（`WindowEx` 场景）
- 用于实现时间窗口内数据的每秒平均速率计算（`PerSecondEx` 场景）
- 适用于不依赖其他计数器、需要独立运行并由用户主动推送数据的指标场景

## 相关概念
- [[concepts/衍生变量|衍生变量]]

## 相关实体
- [[entities/bvar::WindowEx|bvar::WindowEx]]
- [[entities/bvar::PerSecondEx|bvar::PerSecondEx]]
- [[entities/bvar::Window|bvar::Window]]
- [[entities/bvar::PerSecond|bvar::PerSecond]]

## 来源提及
- "template <typename R, time_t window_size = 0> class WindowEx : public adapter::WindowExAdapter<R, adapter::WindowExType<R> > {" — [[sources/bvar_c++|bvar_c++]]
- "template <typename R, time_t window_size = 0> class PerSecondEx : public adapter::WindowExAdapter<R, adapter::PerSecondExType<R> > {" — [[sources/bvar_c++|bvar_c++]]
- "WindowEx不依赖其他的计数器，需要给它发送数据。使用起来比较方便；window_size是通过模板参数传递的，省略最后一个window_size(时间窗口)的话默认为bvar_dump_interval。" — [[sources/bvar_c++|bvar_c++]]