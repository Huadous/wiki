---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "Adder累加器"
  - "bvar::Adder<T>"
  - "Adder"
---


# bvar::Adder

## 定义
bvar::Adder 是 bvar::Reducer 的子类模板，用于对数值进行累加操作。其底层运算符（Op）为加号 `+`，默认值为 0。`varname << N` 等价于 `varname += N`。只要类型 `T` 重载了 `T operator+(T, T)`，Adder 即可作用于该类型，因此不仅可用于基本类型，也可用于 `std::string` 等非基本类型的拼接。

## 关键特征
- 继承自 [[concepts/bvar::Reducer|bvar::Reducer]]，底层 Op 为 `+`，默认初值为 0
- 提供了 `<<` 操作符，等价于 `+=`，使用便捷
- 支持任意重载了 `T operator+(T, T)` 的类型，不仅限于基本数值类型
- 可对 `std::string` 进行拼接，体现模板泛化能力
- 内部维护数据并对外暴露统计读取接口

## 应用
- 统计请求总数（请求计数器）
- 统计错误数、失败数等异常累计量
- 统计读取/写入字节数等累计型指标
- 拼接字符串等自定义累加场景

## 相关概念
- [[concepts/bvar::Reducer|bvar::Reducer]]
- [[concepts/bvar::Window|bvar::Window]]
- [[concepts/bvar::PerSecond|bvar::PerSecond]]

## 相关实体
无相关实体。

## 来源提及
- bvar::Adder<T>| 计数器，默认0，varname << N相当于varname += N — [[sources/bvar_c++|bvar_c++]]
- 顾名思义，用于累加，Op为+。 — [[sources/bvar_c++|bvar_c++]]
- Adder<>可用于非基本类型，对应的类型至少要重载T operator+(T, T)。 — [[sources/bvar_c++|bvar_c++]]