---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [method]
aliases:
  - "bvar::expose_as"
  - "expose_as曝光"
---


# expose_as

## 定义
`expose_as` 是 `bvar::Variable` 提供的一种曝光（expose）API，其签名形式为 `int expose_as(const butil::StringPiece& prefix, const butil::StringPiece& name)`。与 `expose` 的区别在于，它额外接收一个 `prefix` 参数，在将 bvar 注册到全局表时使用 `prefix + name` 作为完整名称，从而强制实施"模块_类名_指标"形式的 bvar 命名规范，避免不同模块间的变量名冲突。

## 关键特征
- **前缀注入机制**：接收 `prefix` 与 `name` 两个参数，注册到全局表时使用 `prefix + name` 作为 bvar 的最终名称。
- **命名规范约束**：通过前缀机制强制实施 `<namespace>_<module>_<name>` 形式的命名规范，降低重名概率。
- **返回值语义与 `expose` 一致**：返回 `0` 表示成功，返回 `-1` 表示失败。
- **重名冲突处理**：当遇到同名 bvar 时，默认打印 `FATAL` 日志；若同时将 `-bvar_abort_on_same_name` 设为 `true`，则直接 `abort`。
- **典型用法**：常在类的构造函数中调用，对成员 bvar 进行曝光，例如 `ApplePie` 类构造函数中调用 `_error.expose_as("foo_bar_apple_pie", "error")`，最终生成的 bvar 名称为 `foo_bar_apple_pie_error`。

## 应用
- **模块级 bvar 注册**：在自定义类的构造函数中，对各类指标 bvar（如 `bvar::Adder`、`bvar::Gauge` 等）按"模块_类名_指标"命名进行曝光，便于按命名空间聚合。
- **大型项目中的命名隔离**：当多个模块分别维护各自的指标 bvar 时，通过为每个模块设置独立前缀，避免跨模块的 bvar 名称冲突。
- **服务监控指标暴露**：在 brpc 服务端代码中，用于把业务指标（如错误计数、调用耗时、QPS 等）按统一前缀注册到全局 bvar 表，方便通过 `/vars` 接口统一查看。

## 相关概念
- [[concepts/expose|expose]]
- [[concepts/bvar命名规范|bvar命名规范]]
- [[concepts/bvar名字归一化|bvar名字归一化]]

## 相关实体
- [[entities/bvar::Variable|bvar::Variable]]
- [[entities/bvar::Adder|bvar::Adder]]

## 来源提及
- `int expose_as(const butil::StringPiece& prefix, const butil::StringPiece& name);` — [[sources/bvar_c++|bvar_c++]]
- 为避免重名，bvar的名字应加上前缀，建议为`<namespace>_<module>_<name>`。为了方便使用，我们提供了expose_as函数，接收一个前缀。 — [[sources/bvar_c++|bvar_c++]]
- ```
  // foo_bar_apple_pie_error
             _error.expose_as("foo_bar_apple_pie", "error");
  ``` — [[sources/bvar_c++|bvar_c++]]