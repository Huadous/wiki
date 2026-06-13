---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [method]
aliases:
  - "bvar变量命名规范"
  - "bvar naming convention"
---


# bvar命名规范

## 定义
bvar 命名规范是 bvar 库推荐的一套变量命名约定，采用 **模块_类名_指标** 三段式命名结构，用于避免不同模块间的变量重名冲突，确保全局变量名的唯一性。

## 关键特征
- **三段式命名结构**：模块一般是程序名（可加产品线缩写如 inf_ds、ecom_retrbs），类名是类名或函数名，指标是 count、qps、latency 等具体监控项。
- **指标后缀约定**：
  - 个数用 `_count` 后缀（如 `request_count`、`error_count`）
  - 每秒个数用 `_second` 后缀（如 `request_second`、`process_inblocks_second`），无需写成 `_count_second` 或 `_per_second`
  - 每分钟个数用 `_minute` 后缀（如 `request_minute`、`process_inblocks_minute`）
- **名字归一化处理**：bvar 内部会将 `foo::BarNum`、`foo.bar.num`、`foo-bar-num` 等不同写法统一归一化为 `foo_bar_num`。
- **全局唯一性约束**：如果全局变量名重复且 `-bvar_abort_on_same_name` 为 true，程序会直接 abort。

## 应用
- 在使用 bvar 库进行监控指标埋点时，规范化全局变量命名，避免多模块间命名冲突。
- 在大型项目中通过产品线缩写区分不同业务线的指标（如 inf_ds、ecom_retrbs）。
- 在暴露（expose）bvar 变量前，确保变量名全局唯一，防止曝光失败。

## 相关概念
- [[concepts/expose|expose]]
- [[concepts/bvar名字归一化|bvar名字归一化]]
- [[concepts/bvar导出|bvar导出]]

## 相关实体
- [[entities/bvar|bvar]]

## 来源提及
- **确认变量名是全局唯一的！** 否则会曝光失败，如果-bvar_abort_on_same_name为true，程序会直接abort。 — [[sources/bvar_c++|bvar_c++]]
- 程序中有来自各种模块不同的bvar，为避免重名，建议如此命名：**模块_类名_指标** — [[sources/bvar_c++|bvar_c++]]
- 关于指标：
- 个数以_count为后缀，比如request_count, error_count。
- 每秒的个数以_second为后缀，比如request_second, process_inblocks_second，已经足够明确，不用写成_count_second或_per_second。
- 每分钟的个数以_minute为后缀，比如request_minute, process_inblocks_minute — [[sources/bvar_c++|bvar_c++]]