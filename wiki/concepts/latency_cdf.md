---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/backup_request]]"
  - "[[brpc/en_backup_request.md]]"
tags:
  - "method"
aliases:
  - "延迟CDF图"
  - "累积分布函数延迟图"
  - "Latency CDF Graph"
  - "CDF"
  - "延迟CDF图"
  - "累积分布函数延迟图"
  - "Latency CDF Graph"
---

## Description
latency_cdf 是 brpc 内置的延迟分布可视化工具，以累积分布函数（CDF）的形式呈现请求延迟的统计特征。该图 y 轴表示延迟（默认单位为微秒 μs），x 轴表示延迟小于 y 轴值的请求所占的累积比例（0~100%），帮助开发者通过图形化方式快速理解延迟分布形态，包括是否存在长尾延迟等关键特征。brpc 默认提供了 latency_cdf 图供开发者直接查看，同时允许用户通过 `bvar::LatencyRecorder` 自行为自定义函数添加延迟监控并生成独立的 cdf 图。latency_cdf 最核心的应用场景是辅助选择 `backup_request_ms` 参数——通过观察图中不同延迟阈值所覆盖的请求比例（如 2ms 覆盖约 95.5%、10ms 覆盖约 99.99%），开发者可根据服务的延迟容忍度确定合理的备用请求超时阈值。此外，该图还可用于 SLA 评估（如 P99、P999 延迟指标）和性能监控诊断。

## Related Concepts
- [[concepts/backup-request|backup request]]
- [[concepts/latency-recorder|LatencyRecorder]]
- [[concepts/cumulative-distribution-function|Cumulative Distribution Function (CDF)]]

## Related Entities
- [[entities/bvar|bvar]]
- [[entities/baidu|baidu]]
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/backup_request|backup_request]]**
> - "可以观察brpc默认提供的latency_cdf图，或自行添加。cdf图的y轴是延时（默认微秒），x轴是小于y轴延时的请求的比例。"
> - "在下图中，选择backup_request_ms=2ms可以大约覆盖95.5%的请求，选择backup_request_ms=10ms则可以覆盖99.99%的请求。"
> - "自行添加的方法：`my_func_latency << tm.u_elapsed();`"

> **Source: [[sources/en_backup_request|en_backup_request]]**
> - "You can look the default cdf(Cumulative Distribution Function) graph of latency provided by brpc, or add it by your own."
> - "The y-axis of the cdf graph is a latency(us by default), and the x-axis is the proportion of requests whose latencies are less than the corresponding value in y-aixs."