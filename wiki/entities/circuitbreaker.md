---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/circuit_breaker]]"]
tags: [other]
aliases:
  - "熔断器"
  - "brpc熔断器"
---


# CircuitBreaker

## 基本信息
- Type: other
- Source: [[sources/circuit_breaker|circuit_breaker]]

## 描述
CircuitBreaker 是 brpc 框架中实现可选熔断策略的核心类。它通过记录每个请求的处理结果，动态维护累计出错时长 `acc_error_cost` 和最大允许错误成本 `max_error_cost`，当累计出错时长超过阈值时触发熔断，暂时屏蔽故障节点。CircuitBreaker 使用指数移动平均（EMA）平滑延迟数据，并通过窗口大小和错误率计算 `max_error_cost`。CircuitBreaker 支持长短两个窗口，长窗口覆盖最近多笔请求以反映长期错误率，短窗口覆盖最近少量请求以区分短期抖动和持续高错误率。只有通过开启了 `enable_circuit_breaker` 的 [[entities/brpc|Channel]] 发送的请求，才会将处理结果提交到 CircuitBreaker，从而实现精细化的熔断控制。

## 相关实体
- [[entities/brpc|brpc]] — CircuitBreaker 是 brpc 框架的组成部分
- [[entities/bvar|bvar]] — 可能用于记录熔断相关的统计指标

## 相关概念
- [[concepts/熔断|熔断]] — 核心熔断保护机制概念
- [[concepts/可选熔断策略|可选熔断策略]] — CircuitBreaker 在 brpc 中作为可选策略实现
- [[concepts/EMA|EMA]] — 指数移动平均，用于平滑延迟计算
- [[concepts/acc_error_cost|acc_error_cost]] — 累计出错时长，触发熔断的关键指标
- [[concepts/max_error_cost|max_error_cost]] — 最大允许错误成本阈值
- [[concepts/长窗口|长窗口]] — 覆盖多笔请求的较长窗口，用于评估长期错误率
- [[concepts/短窗口|短窗口]] — 覆盖少量请求的较短窗口，用于检测短期抖动
- [[concepts/alpha|alpha]] — EMA 计算中的平滑系数

## 来源提及
- "可选的熔断由CircuitBreaker实现，在开启了熔断之后，CircuitBreaker会记录每一个请求的处理结果，并维护一个累计出错时长，记为acc_error_cost，当acc_error_cost > max_error_cost时，熔断该节点。" — [[sources/circuit_breaker|circuit_breaker]]
- "每次请求返回成功之后，更新max_error_cost: 1. 首先需要更新latency的EMA值，记为ema_latency: ema_latency = ema_latency * alpha + (1 - alpha) * latency。" — [[sources/circuit_breaker|circuit_breaker]]
- "只有通过开启了enable_circuit_breaker的channel发送的请求，才会将请求的处理结果提交到CircuitBreaker。" — [[sources/circuit_breaker|circuit_breaker]]