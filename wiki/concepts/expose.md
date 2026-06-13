---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [method]
aliases:
  - "曝光"
  - "bvar曝光"
  - "expose()"
---


# expose

## 定义
expose 是 bvar 中将变量注册到全局表的核心操作（"曝光"）。通过调用 `bvar::Variable::expose(name)` 或 `expose_as(prefix, name)` 将一个 bvar 变量注册到全局监控表中，使其可被外部查询与监控。曝光后的 bvar 名字为 `name` 或 `prefix + name`，可通过 `describe_exposed`、`find_exposed`、`count_exposed` 等带 `_exposed` 后缀的 static 函数进行查询。

## 关键特征
- **注册到全局表**：expose 是 bvar 从单纯的本地计数器升级为可被监控的全局变量的关键步骤，未 expose 的 bvar 只能在其作用域内被使用。
- **两种注册方式**：
  - `int expose(const butil::StringPiece& name);`
  - `int expose_as(const butil::StringPiece& prefix, const butil::StringPiece& name);`
- **命名规则**：曝光后的 bvar 名字为 `name` 或 `prefix + name`，便于在全局表中唯一标识。
- **同名冲突处理**：当相同名字的 bvar 已存在时，expose 会打印 FATAL 日志并返回 `-1`。
- **abort 行为**：当选项 `-bvar_abort_on_same_name` 设为 `true`（默认是 `false`）时，程序会直接 abort。
- **查询接口**：曝光后的 bvar 可通过 `describe_exposed`、`find_exposed`、`count_exposed` 等 static 函数进行查询。

## 应用
- **指标监控**：将业务代码中的局部计数器（如 [[entities/bvar::Adder|bvar::Adder]]、[[entities/bvar::Status|bvar::Status]] 等）注册到 bvar 全局表，供监控系统统一采集。
- **变量导出**：通过 [[concepts/Dumper|Dumper]] 配合 `DumpOptions` 将所有已曝光（exposed）的 bvar 导出为可被外部工具消费的格式（如 Prometheus）。
- **运行时查询**：在运行时通过 `find_exposed` 等接口按名称查找已曝光的 bvar，进行动态调试或在线诊断。

## 相关概念
- [[concepts/Dumper|Dumper]]
- [[concepts/DumpOptions|DumpOptions]]
- [[concepts/bvar::Variable|bvar::Variable]]

## 相关实体
- [[entities/bvar::Adder|bvar::Adder]]
- [[entities/bvar::Status|bvar::Status]]

## 来源提及
- 我们称把一个bvar注册到全局表中的行为为"曝光"，可通过`expose`函数曝光： — [[sources/bvar_c++|bvar_c++]]
- `int expose(const butil::StringPiece& name); int expose_as(const butil::StringPiece& prefix, const butil::StringPiece& name);` — [[sources/bvar_c++|bvar_c++]]
- 当相同名字的bvar已存在时，expose会打印FATAL日志并返回-1。如果选项 **-bvar_abort_on_same_name**设为true (默认是false)，程序会直接abort。 — [[sources/bvar_c++|bvar_c++]]