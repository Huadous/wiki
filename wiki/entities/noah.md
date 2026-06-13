---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar|bvar]]"]
tags: [product]
aliases:
  - "百度noah"
  - "noah 监控系统"
  - "Baidu noah"
---


# noah

## 基本信息
- Type: product
- Source: [[sources/bvar|bvar]]

## 描述
noah 是百度内部使用的监控系统，在 bvar 的官方文档中作为数据汇总展示平台的示例被提及。当 bvar 的 dump 功能开启后，所有 bvar 会导出到本地 monitor 目录下的 `.data` 文件中，监控系统（如 noah）会定期搜集每台单机导出的数据并把它们汇总到一起。在 noah 中，[[sources/bvar|bvar]] 定义的变量会自动出现在指标项中，用户可以勾选并查看历史曲线。noah 是百度内部基于 [[sources/bvar|bvar]] 构建监控体系的具体实践案例，展示了 bvar 数据从单机落地、采集到集中可视化展示的完整流程。

## 相关实体
- [[sources/bvar|bvar]]

## 相关概念
No related concepts

## 来源提及
- 监控系统应定期搜集每台单机导出的数据，并把它们汇总到一起。这里以百度内的noah为例，bvar定义的变量会出现在noah的指标项中，用户可勾选并查看历史曲线 — [[sources/bvar|bvar]]