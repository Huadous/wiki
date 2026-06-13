---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "bvar::Status<T>"
  - "bvar Status"
  - "Status值显示"
---


# bvar::Status

## 定义
bvar::Status 是 brpc 中用于记录和显示一个值的 bvar 类型，拥有额外的 `set_value` 函数。模板参数 Tp 需要是 `std::string` 或者 `boost::atomic<Tp>` 可接受的类型。

## 关键特征
- 用于记录和显示一个值，提供额外的 `set_value` 函数
- 模板参数 Tp 需为 `std::string` 或 `boost::atomic<Tp>` 可接受的类型
- 常用于记录和显示周期性更新或不常更新的值
- 提供多种构造方式：
  - 仅传入初始值
  - 直接在构造时曝光（expose）
  - 传入 `prefix + name` 进行曝光

## 应用
- 记录服务启动时间
- 显示当前配置值
- 记录用户名等不常变化的状态信息
- 展示周期性更新的状态数据

## 相关概念
- [[concepts/bvar::PassiveStatus]]
- [[concepts/bvar::Variable]]

## 相关实体
- 无

## 来源提及
- bvar::Status<T> | 记录和显示一个值，拥有额外的set_value函数 — [[sources/bvar_c++|bvar_c++]]
- 记录和显示一个值，拥有额外的set_value函数。 — [[sources/bvar_c++|bvar_c++]]