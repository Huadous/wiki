---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar|bvar]]"]
tags: [product]
aliases:
  - "Prometheus"
---


# Prometheus

## 基本信息
- Type: product
- Source: [[sources/bvar|bvar]]

## 描述
Prometheus 是知名的开源时序数据库和监控系统，在本篇文档中作为 [[sources/bvar_c++|bvar]] 的外部数据消费者出现。brpc 服务器支持将 Prometheus 的抓取 URL 路径设置为 `/brpc_metrics` 进行指标抓取，例如 brpc server 跑在本机的 8080 端口，则抓取 URL 配置为 `127.0.0.1:8080/brpc_metrics` 即可。通过这种方式，Prometheus 可以定期从 brpc 服务中采集 [[sources/bvar_c++|bvar]] 指标，实现分布式监控数据的统一汇聚和展示。

## 相关实体
- [[entities/bvar|bvar]]
- [[entities/brpc|brpc]]

## 相关概念
（暂无相关概念）

## 来源提及
- 将Prometheus的抓取url地址的路径设置为/brpc_metrics即可 — [[sources/bvar|bvar]]
- 例如brpc server跑在本机的8080端口，则抓取url配置为127.0.0.1:8080/brpc_metrics — [[sources/bvar|bvar]]