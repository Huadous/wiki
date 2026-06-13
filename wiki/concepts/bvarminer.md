---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++]]"]
tags: [term]
aliases:
  - "bvar::Miner<T>"
  - "Miner最小值"
---


# bvar::Miner

## 定义
`bvar::Miner<T>` 是 brpc `bvar` 模块中 [[concepts/bvar-reducer|bvar::Reducer]] 的子类模板，用于在并发场景下对类型 `T` 的取值持续追踪**最小值**。其底层运算符为 `std::min`，默认初值为 `std::numeric_limits<T>::max()`，因此首次写入即可正确得到一个有效最小值。语义上，`varname << N` 等价于 `varname = min(varname, N)`。

## 关键特征
- **继承自 [[concepts/bvar-reducer|bvar::Reducer]]**：复用 Reducer 的无锁/低开销并发更新机制，保证多线程下安全聚合。
- **求最小值运算**：使用 `std::min` 作为合并运算符，自动忽略更大的输入值。
- **默认初值为 `std::numeric_limits<T>::max()`**：保证在尚未写入时不会影响后续的最小值计算。
- **写入语法简洁**：`varname << N` 等价于 `varname = min(varname, N)`，调用方无需关心读取-修改-写回的并发细节。
- **类型特化要求**：要将其用于自定义类型，必须为该类型特化 `std::numeric_limits<>` 并重载 `operator<`，行为与 [[concepts/bvar-mxer|bvar::Maxer]] 对称。

## 应用
- **响应时间最小值监控**：记录接口、RPC 调用或任务处理时间的最小耗时，用于刻画系统最快路径的性能基线。
- **资源余量追踪**：例如监控进程可用内存、磁盘剩余空间、连接池空闲连接数等"取最小更值得关注"的指标。
- **延迟最优值对比**：与平均/最大值指标配合，定位系统在理想条件下的表现下界。
- **冷启动/优化效果评估**：通过观察最小值随发布迭代的变化趋势，评估性能优化是否真正生效。

## 相关概念
- [[concepts/bvar-reducer|bvar::Reducer]]
- [[concepts/bvar-mxer|bvar::Maxer]]

## 相关实体
*No related entities*

## 来源提及
- bvar::Miner<T>| 求最小值，默认std::numeric_limits<T>::max()，varname << N相当于varname = min(varname, N) — [[sources/bvar_c++]]
- 用于取最小值，运算符为std::min。 — [[sources/bvar_c++]]