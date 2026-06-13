---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/auto_concurrency_limiter.md]]"
tags: [自适应限流, Little's Law, max_concurrency, best_max_concurrency, noload_latency, min_latency, peak_qps, max_qps, netflix gradient算法, EMA, concurrency, ELIMIT, alpha, 服务过载, queue_size]
aliases: ["Adaptive Concurrency Limiter", "brpc 自适应限流"]
---

# 自适应限流 - Summary

## 来源
- Original file: [[brpc/auto_concurrency_limiter.md]]
- Ingested: 2026-06-13

## 核心内容

本文档介绍 [[entities/brpc|brpc]] 框架中的自适应限流机制。当请求速度超过服务处理能力时，[[concepts/服务过载|服务过载]] 将导致请求积压，最终使服务瘫痪。自适应限流通过动态调整 [[concepts/max_concurrency|max_concurrency]]，在保证服务不过载的前提下尽可能多地处理请求。

其理论基础是 [[concepts/littles-law|Little's Law]]（concurrency = latency × qps），核心目标是将 max_concurrency 趋近于 [[concepts/best_max_concurrency|best_max_concurrency]]（即 [[concepts/noload_latency|noload_latency]] × [[concepts/peak_qps|peak_qps]]）。算法通过 [[concepts/ema|EMA]] 平滑估算 [[concepts/min_latency|min_latency]] 和 [[concepts/max_qps|max_qps]]，并使用 `max_concurrency = max_qps * ((2+alpha) * min_latency - latency)`（[[concepts/alpha|alpha]] 默认 0.3）动态计算。文档还对比了 [[entities/netflix|Netflix]] 的 [[concepts/netflix-gradient算法|gradient 算法]]，指出 brpc 方案在稳定性与准确性上的改进。

## 关键实体
- [[entities/brpc|brpc]]：Apache 开源的高性能 RPC 框架，本文档所述自适应限流的实现平台
- [[entities/netflix|netflix]]：提出 gradient 限流算法，本文将其与 brpc 算法进行了对比

## 关键概念
- [[concepts/自适应限流|自适应限流]]：动态调整服务最大并发度的限流方法
- [[concepts/littles-law|Little's Law]]：排队论基础定律，concurrency = latency × qps
- [[concepts/max_concurrency|max_concurrency]]：设置的最大并发度
- [[concepts/best_max_concurrency|best_max_concurrency]]：并发度的物理上限
- [[concepts/noload_latency|noload_latency]]：服务的固有无负载延时
- [[concepts/min_latency|min_latency]]：noload_latency 的 EMA 估算值
- [[concepts/peak_qps|peak_qps]]：服务的 QPS 上限
- [[concepts/max_qps|max_qps]]：最近测定的实际 QPS 极大值
- [[concepts/netflix-gradient算法|netflix-gradient算法]]：Netflix 提出的对比算法
- [[concepts/ema|ema]]：指数移动平均，用于平滑处理
- [[concepts/concurrency|concurrency]]：并发度，即同时处理的请求数
- [[concepts/elimit|elimit]]：超过 max_concurrency 时返回的错误码
- [[concepts/alpha|alpha]]：可接受的延时上升幅度参数
- [[concepts/服务过载|服务过载]]：请求速度超过服务处理能力的状态
- [[concepts/queue_size|queue_size]]：gradient 算法中的参数，brpc 认为其作用有限

## 要点
- **理论基础**：自适应限流基于 [[concepts/littles-law|Little's Law]]，best_max_concurrency = noload_latency × peak_qps
- **核心公式**：`max_concurrency = max_qps * ((2+alpha) * min_latency - latency)`，alpha 默认 0.3，每次调整比例有上限以保证平滑
- **使用方式**：brpc 在 method 级别支持自适应限流，将 method 的 max_concurrency 设置为 "auto" 即可启用
- **收敛机制**：通过定期降低 max_concurrency，为探测 noload_latency 变化和 min_latency 下降提供探索空间，避免算法不收敛
- **EMA 差异**：min_latency 仅在下降时更新；max_qps 的 EMA 参数仅为 min_latency 的十分之一，反映两者下降语义的差异
- **与 Netflix gradient 的区别**：brpc 使用 latency 平均值而非最小值，且不依赖 queue_size 作为缓存表示，算法更稳定准确