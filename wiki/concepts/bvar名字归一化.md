---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "名字归一化"
  - "bvar name normalization"
---


# bvar名字归一化

## 定义
bvar名字归一化是 bvar 提供的一种名称处理机制，用于将不同书写格式的变量名统一为同一种下划线分隔的标准形式。无论用户以何种形式（`::` 分隔、`.` 分隔、空格分隔、`-` 分隔等）传入变量名，bvar 都会将其归一化为统一的 `<namespace>_<module>_<name>` 形式，从而保证全局唯一标识的一致性。

## 关键特征
- 多格式兼容：接受 `foo::BarNum`、`foo.bar.num`、`foo bar num`、`foo-bar-num` 等多种写法。
- 统一输出：所有输入最终都归一化为 `foo_bar_num` 形式（下划线分隔、全小写）。
- 唯一性保证：是 bvar 全局唯一命名机制的基础，避免因格式差异导致同一逻辑指标被误识别为多个 bvar。
- 与命名规范协同：与建议的 `<namespace>_<module>_<name>` 命名规范相辅相成，进一步降低重名风险。

## 应用
- 在指标采集代码中，即使不同模块使用不同的命名习惯（如 C++ 风格 `::` 或配置文件中的 `.`），也能保证最终上报的 bvar 名称一致。
- 在多团队协作的项目中，减少因命名风格差异导致的指标重复或覆盖问题。
- 配合 [[concepts/expose|Expose]] 使用时，确保对外暴露的指标名格式统一，便于监控和告警系统识别。

## 相关概念
- [[concepts/expose|Expose]]

## 相关实体
- [[entities/bvar::Variable|bvar::Variable]]
- [[entities/bvar::Adder|bvar::Adder]]

## 来源提及
- 目前bvar会做名字归一化，不管你打入的是foo::BarNum, foo.bar.num, foo bar num , foo-bar-num，最后都是foo_bar_num。 — [[sources/bvar_c++|bvar_c++]]
- 为避免重名，bvar的名字应加上前缀，建议为`<namespace>_<module>_<name>`。 — [[sources/bvar_c++|bvar_c++]]