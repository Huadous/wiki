---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "PerSecond"
  - "PerSecond每秒速率"
  - "bvar::PerSecond<VAR>"
---


# bvar::PerSecond

## 定义
bvar::PerSecond 是一个模板类，用于获得某个 bvar 变量在一段时间内平均每秒的统计值。它是 [[concepts/bvar::Window|bvar::Window]] 的变种，两者逻辑基本相同，唯一的区别在于 PerSecond 的返回值会额外除以时间窗口的大小，从而将累计值转化为速率（每秒平均值）。PerSecond 同样是会自动更新的衍生变量，依赖于一个已存在的 bvar 变量。

## 关键特征
- **衍生变量**：PerSecond 本身不会直接接收数据更新，而是依赖于一个已存在的 bvar 变量，自动从中派生计算结果。
- **自动更新**：无需用户手动调用更新接口，PerSecond 会随底层 bvar 的变化而自动刷新。
- **Window 的速率化变种**：与 [[concepts/bvar::Window|bvar::Window]] 共享几乎相同的实现逻辑，仅在返回最终结果时除以时间窗口大小（秒），将窗口内的累计值转换为"每秒"速率。
- **使用场景受限（PerSecond 并不总是有意义）**：对与时间无关的量（例如一段时间内的最大值、瞬时计数等）使用 PerSecond 没有意义。此时应改用 `window_size=1` 的 [[concepts/bvar::Window|bvar::Window]]。
- **模板化设计**：以 `bvar::PerSecond<VAR>` 的形式呈现，`VAR` 为底层 bvar 变量的类型。

## 应用
- **每秒请求数（QPS）**：统计服务在指定时间窗口内平均每秒接收到的请求数量。
- **每秒错误数**：统计服务在指定时间窗口内平均每秒产生的错误数量。
- **每秒流量/带宽**：统计网络或 IO 在指定时间窗口内平均每秒传输的字节数。
- **通用速率监控**：任何需要将累计型 bvar 指标转换为"每秒速率"形式进行展示或告警的场景。

## 相关概念
- [[concepts/bvar::Window|bvar::Window]]
- [[concepts/bvar::PerSecondEx|bvar::PerSecondEx]]

## 相关实体
- 无

## 来源提及
- `bvar::PerSecond<VAR>`| 获得某个bvar在一段时间内平均每秒的累加值。PerSecond也是会自动更新的衍生变量 — [[sources/bvar_c++|bvar_c++]]
- **PerSecond并不总是有意义** — [[sources/bvar_c++|bvar_c++]]
- 它和Window基本相同，除了返回值会除以时间窗口之外。 — [[sources/bvar_c++|bvar_c++]]