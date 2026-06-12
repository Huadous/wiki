---
---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[brpc/circuit_breaker.md]]"
tags: [熔断, 默认熔断策略, 可选熔断策略, EMA, 连接超时, RPC超时, 健康检查, 隔离时间, 长窗口, 短窗口, ConnectionGroup, 命名服务 (naming service), 负载均衡 (load balancing), 连接池模式 (pooled mode), gflag, acc_error_cost (累计出错时长), max_error_cost (最大出错时长)]
aliases: ["brpc熔断机制", "Circuit Breaker in brpc"]
---

# 熔断功能 - Summary

## 来源
- Original file: [[brpc/circuit_breaker.md]]
- Ingested: 2026-06-12

## 核心内容
本文档详细介绍了 [[entities/brpc|brpc]] 框架中的熔断机制。brpc 提供两种熔断策略：[[concepts/默认熔断策略|默认熔断策略]]（基于TCP连接建立失败，默认开启且无法关闭）和 [[concepts/可选熔断策略|可选熔断策略]]（基于请求出错率，通过 `enable_circuit_breaker` 开启）。可选策略由 [[entities/circuitbreaker|CircuitBreaker]] 实现，维护累计出错时长 (`[[concepts/acc_error_cost-累计出错时长|acc_error_cost]]`) 和由 [[concepts/ema|EMA]] 平滑延迟计算的最大错误成本 (`[[concepts/max_error_cost-最大出错时长|max_error_cost]]`)，当累计值超过阈值时触发熔断。同时支持[[concepts/长窗口|长窗口]]和[[concepts/短窗口|短窗口]]来区分短期抖动与长期高错误率。熔断节点先进行[[concepts/隔离时间|隔离]]（初始100ms，连续熔断翻倍，最大30秒），再通过[[concepts/健康检查|健康检查]]恢复。可通过 [[concepts/connectiongroup|ConnectionGroup]] 隔离连接池，避免一损俱损。

## 关键实体
- [[entities/brpc|brpc]] — 百度开源的高性能RPC框架，本文阐述其熔断功能实现
- [[entities/circuitbreaker|CircuitBreaker]] — 实现可选熔断策略的核心类，维护错误成本指标
- [[entities/connections-监控页面|/connections 监控页面]] — 显示熔断次数 (nBreak) 和错误数 (RecentErr)

## 关键概念
- [[concepts/熔断|熔断]] — 分布式系统的自我保护机制，自动剔除故障节点
- [[concepts/默认熔断策略|默认熔断策略]] — 基于连接失败（ECONNREFUSED等）的简单熔断
- [[concepts/可选熔断策略|可选熔断策略]] — 基于请求出错率的激进熔断方案
- [[concepts/ema|EMA (指数移动平均)]] — 用于平滑延迟计算的方法
- [[concepts/连接超时|连接超时]] — 必须小于RPC超时，否则默认熔断无法触发
- [[concepts/rpc超时|RPC超时]] — 必须大于连接超时的关键配置约束
- [[concepts/健康检查|健康检查]] — TCP连接建立作为恢复判定标准
- [[concepts/隔离时间|隔离时间]] — 熔断后节点暂时屏蔽的时间段
- [[concepts/长窗口|长窗口]] — 检测长期高错误率的熔断窗口
- [[concepts/短窗口|短窗口]] — 快速响应短期抖动的熔断窗口
- [[concepts/connectiongroup|ConnectionGroup]] — 连接隔离分组机制
- [[concepts/命名服务-naming-service|命名服务 (naming service)]] — 提供可用节点列表
- [[concepts/负载均衡-load-balancing|负载均衡 (load balancing)]] — 从节点列表中选择访问目标
- [[concepts/连接池模式-pooled-mode|连接池模式 (pooled mode)]] — 熔断影响整个连接池
- [[concepts/acc_error_cost-累计出错时长|acc_error_cost (累计出错时长)]] — 节点累积错误成本
- [[concepts/max_error_cost-最大出错时长|max_error_cost (最大出错时长)]] — 动态可调的错误容忍阈值
- [[concepts/gflag|gflag]] — 熔断策略参数的运行时配置机制

## 要点
- brpc 提供默认和可选两种熔断策略，默认策略基于 TCP 连接失败，可选策略基于请求出错率
- 默认熔断中，RPC超时必须大于连接超时，否则熔断可能永远无法触发
- 可选熔断由 CircuitBreaker 实现，使用 EMA 平滑延迟并动态调整错误容忍阈值
- 长短双窗口设计允许短期抖动同时剔除长期高错误率节点
- 熔断后节点先隔离（100ms起，连续熔断翻倍至30秒），再健康检查恢复
- 通过 connection_group 可将连接分组隔离，避免单个故障节点影响所有 Channel