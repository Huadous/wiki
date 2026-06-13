---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "bvar::Maxer"
  - "Maxer最大值"
  - "bvar Maxer"
---


# bvar::Maxer

## 定义
bvar::Maxer 是 [[concepts/bvar::Reducer|Reducer]] 的子类，用于对一系列数值取最大值。其二元运算符为 `std::max`，单位元（identity / 默认初始值）为 `std::numeric_limits<T>::min()`。通过 `varname << N` 操作即可将变量更新为 `max(varname, N)`，等价于就地取最大值。

## 关键特征
- **继承自 Reducer**：与 [[concepts/bvar::Reducer|Reducer]] 共享同一套模板化二元运算框架，仅替换了运算类型与单位元。
- **运算符为 `std::max`**：每次 `<<` 输入都会与当前值比较并保留较大者。
- **默认值为 `std::numeric_limits<T>::min()`**：这是 `std::max` 运算下的单位元（identity），保证首次输入即可正确生效。
- **类型约束严格**：除非用户特化 `std::numeric_limits<>` 并重载 `operator<`（注意是 `operator<` 而非 `operator>`），否则不能用于通用自定义类型。
- **与 [[concepts/bvar::Miner|Miner]] 对偶**：Miner 取最小值（默认 `max()`），Maxer 取最大值（默认 `min()`），二者结构对称。

## 应用
- **响应时间最大值统计**：记录某接口在某时间窗口内的最大响应耗时。
- **并发连接数峰值**：追踪服务在运行期间达到过的最大并发连接数。
- **资源使用上限观测**：记录 CPU、内存、队列长度等指标的历史最大值。
- **延迟异常告警**：结合 [[concepts/bvar::Window|Window]] 窗口统计，在最大延迟超过阈值时触发告警。
- **性能瓶颈定位**：通过持续观察最大值指标，辅助识别偶发性的慢请求或突发流量。

## 相关概念
- [[concepts/bvar::Reducer|Reducer]]
- [[concepts/bvar::Miner]]
- [[concepts/bvar::Window]]

## 相关实体
（无相关实体）

## 来源提及
- `bvar::Maxer<T> | 求最大值，默认std::numeric_limits<T>::min()，varname << N相当于varname = max(varname, N)` — [[sources/bvar_c++|bvar_c++]]
- `用于取最大值，运算符为std::max。` — [[sources/bvar_c++|bvar_c++]]
- `Since Maxer<> use std::numeric_limits<T>::min() as the identity, it cannot be applied to generic types unless you specialized std::numeric_limits<> (and overloaded operator<, yes, not operator>).` — [[sources/bvar_c++|bvar_c++]]