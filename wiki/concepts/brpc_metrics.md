---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar|bvar]]"]
tags: [standard]
aliases:
  - "brpc Prometheus端点"
  - "brpc_metrics端点"
  - "/brpc_metrics"
---


# /brpc_metrics

## 定义
/brpc_metrics 是 brpc 框架为 [[sources/overview|Protocol Buffers]] 监控系统（具体为 [[concepts/prometheus|Prometheus]]）提供的标准 HTTP 抓取端点路径。该端点以 `/brpc_metrics` 为 URL 路径暴露进程内所有 [[concepts/bvar|bvar]] 指标数据，使 brpc 服务能够被 [[concepts/prometheus|Prometheus]] 直接拉取（scrape）并写入时序数据库，从而接入 [[concepts/prometheus|Prometheus]] + [[sources/features|Feature Settings for Editions]] 的云原生监控栈。

## 关键特征
- **标准化端点路径**：固定路径为 `/brpc_metrics`，无需在 brpc server 端进行额外开发或定制
- **基于 HTTP 暴露**：通过 brpc 内置的 HTTP 服务提供访问，端口与 brpc server 监听端口一致
- **覆盖全量 bvar 指标**：自动暴露进程内所有 [[concepts/bvar|bvar]] 指标，无需逐个注册或声明
- **与 Prometheus 文本格式兼容**：输出符合 [[concepts/prometheus|Prometheus]] exposition format 规范的指标数据
- **pull 模式采集**：由 [[concepts/prometheus|Prometheus]] server 主动定期拉取，而非进程主动推送
- **与传统方案互补**：与基于 dump 文件 + 自定义采集脚本的方案并存，覆盖云原生监控场景

## 应用
- **云原生监控接入**：将 brpc 服务快速接入基于 [[concepts/prometheus|Prometheus]] + [[sources/features|Feature Settings for Editions]] 的现代监控体系，无需编写自定义 exporter
- **时序数据存储与分析**：通过 [[concepts/prometheus|Prometheus]] 定期抓取 brpc 服务的 [[concepts/bvar|bvar]] 指标并持久化到时序数据库，支持长期趋势分析
- **典型配置示例**：当 brpc server 运行在本地 8080 端口时，将 [[concepts/prometheus|Prometheus]] 的 scrape URL 配置为 `127.0.0.1:8080/brpc_metrics` 即可开始采集
- **Kubernetes 环境部署**：在容器编排环境中，[[concepts/prometheus|Prometheus]] 可通过服务发现自动定位 brpc Pod 并抓取该端点
- **告警与可视化**：采集到的指标可在 [[sources/features|Feature Settings for Editions]] 中绘制仪表盘，并通过 [[concepts/prometheus|Prometheus]] Alertmanager 配置告警规则

## 相关概念
- [[concepts/prometheus|Prometheus]]
- [[concepts/dump功能|dump功能]]
- [[concepts/vars|/vars]]
- [[concepts/bvar|bvar]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/bvar|bvar]]
- [[entities/prometheus|Prometheus]]

## 来源提及
- 将Prometheus的抓取url地址的路径设置为/brpc_metrics即可，例如brpc server跑在本机的8080端口，则抓取url配置为127.0.0.1:8080/brpc_metrics。 — [[sources/bvar|bvar]]