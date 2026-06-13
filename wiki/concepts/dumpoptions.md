---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [other]
aliases:
  - "bvar::DumpOptions"
  - "Variable::DumpOptions"
---


# DumpOptions

## 定义
DumpOptions 是 bvar 导出机制中用于控制 `Variable::dump_exposed()` 行为的配置结构体。它定义了导出过程中的字符串格式、wildcard 匹配规则以及黑白名单过滤策略等参数。

## 关键特征
- **quote_string**：布尔类型，控制字符串类型的值在导出时是否加上引号。
- **question_mark**：用于替代 wildcard 中 `?` 的字符。
- **wildcard_separator**：指定 white/black wildcard 之间的分隔符。
- **white_wildcards**：保留的 wildcard 或精确名称列表（白名单）。
- **black_wildcards**：跳过的 wildcard 或精确名称列表（黑名单）。
- **匹配规则**：
  - 当 `white_wildcards` 和 `black_wildcards` 都为空时，匹配所有 bvar。
  - 仅 `black_wildcards` 非空时，按黑名单过滤。
  - 仅 `white_wildcards` 非空时，按白名单过滤。
- **默认构造**：提供合理默认值（如 `DumpOptions()`），可直接使用。
- 当 `options` 为 NULL 时，底层接口默认采用默认选项进行变量查找与导出。

## 应用
- 与 `Dumper` 配合，遍历并导出 bvar 中已暴露（exposed）的变量。
- 在 `dump_exposed` 接口中作为可选配置传入，灵活控制导出的变量范围与输出格式。
- 用于实现基于通配符（wildcard）的批量变量过滤与导出，例如：
  - 查找所有匹配 `white_wildcards` 且不被 `black_wildcards` 命中的已暴露变量。
  - 借助 `question_mark` 与 `wildcard_separator` 自定义通配符语法，方便与外部监控系统集成。
- 配合 [[concepts/expose|expose]] 机制，精确控制哪些 bvar 被序列化输出。

## 相关概念
- [[concepts/bvar导出]]
- [[concepts/Dumper]]
- [[concepts/expose]]

## 相关实体
- [[entities/bvar::Variable]]

## 来源提及
- "// Options for Variable::dump_exposed()." （// `Variable::dump_exposed()` 的选项。）— [[sources/bvar_c++|bvar_c++]]
- "struct DumpOptions {" — [[sources/bvar_c++|bvar_c++]]
- "    // Contructed with default options." （// 使用默认选项构造。）— [[sources/bvar_c++|bvar_c++]]
- "    DumpOptions();" — [[sources/bvar_c++|bvar_c++]]
- "    // If this is true, string-type values will be quoted." （// 若为 true，字符串类型的值会被加上引号。）— [[sources/bvar_c++|bvar_c++]]
- "    bool quote_string;" — [[sources/bvar_c++|bvar_c++]]
- "// Find all exposed variables matching `white_wildcards' but `black_wildcards' and send them to `dumper'." （// 查找所有匹配 `white_wildcards` 但被 `black_wildcards' 排除的已暴露变量，并将其发送给 `dumper`。）— [[sources/bvar_c++|bvar_c++]]
- "// Use default options when `options' is NULL." （// 当 `options` 为 NULL 时使用默认选项。）— [[sources/bvar_c++|bvar_c++]]