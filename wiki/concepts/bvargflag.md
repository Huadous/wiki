---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "GFlag集成"
  - "GFlag Exporter"
---


# bvar::GFlag

## 定义
bvar::GFlag 是 bvar 库中的一种辅助类，用于将重要的 gflags（Google 命令行参数与配置标志）公开（expose）为 bvar 指标，从而可以通过统一的 bvar 监控系统对原本分散在 gflags 中的配置项进行集中监控与查询。

## 关键特征
- 桥接 gflags 与 bvar：将 gflag 数值同步暴露为 bvar 指标，使 gflag 也能被 `/vars` 等 bvar 查询接口检索到
- 注册便捷：仅需以 gflag 同名或自定义前缀声明一个 `bvar::GFlag` 静态变量，即可完成暴露
- 共享命名空间：与 bvar 共享同一套指标命名机制，便于按前缀聚合查看
- 轻量集成：不需要修改原 gflag 的定义或访问方式，只在 bvar 端做"镜像"声明

## 应用
- 将关键配置类 gflag（如限流阈值、超时时间、开关类参数）暴露为可监控指标
- 配合 `/vars` HTTP 接口，在不修改业务代码的前提下，把 gflag 纳入 bvar 监控面板
- 在需要按服务/模块统一暴露配置状态时，通过命名前缀对一组相关 gflag 进行归类
- 示例用法：`static bvar::GFlag s_gflag_my_flag_that_matters("my_flag_that_matters");` 即可让同名 gflag 被 bvar 查询到

## 相关概念
- [[concepts/bvar::Variable|bvar::Variable]]
- [[concepts/bvar::Status|bvar::Status]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- bvar::GFlag | 将重要的gflags公开为bvar，以便监控它们 — [[sources/bvar_c++|bvar_c++]]
- Expose important gflags as bvar so that they're monitored. — [[sources/bvar_c++|bvar_c++]]