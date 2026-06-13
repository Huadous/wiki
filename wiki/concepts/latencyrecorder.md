---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/backup_request]]"
  - "[[brpc/en_backup_request.md]]"
tags:
  - "term"
aliases:
  - "bvar::LatencyRecorder"
  - "延迟记录器"
  - "brpc延迟记录器"
---

## Related Concepts
- [[concepts/latency_cdf|latency_cdf]] — 延迟累积分布函数，由LatencyRecorder自动生成
- [[concepts/bvar|bvar]] — 底层统计库，LatencyRecorder依赖其聚合能力
- [[concepts/backup_request|backup_request]] — LatencyRecorder常用于优化的关键机制
- [[concepts/cdf|CDF]] — 累积分布函数，LatencyRecorder自动产出的核心统计图

## Related Entities
- [[entities/bvar|bvar]] — 提供LatencyRecorder实现的统计库
- [[entities/brpc|brpc]] — 所属框架生态

## Mentions in Source
> **Source: [[sources/backup_request|backup_request]]**
> - "自行添加的方法："
> - "bvar::LatencyRecorder my_func_latency("my_func");"
> - "my_func_latency << tm.u_elapsed();  // u代表微秒，还有s_elapsed(), m_elapsed(), n_elapsed()分别对应秒，毫秒，纳秒。"
> - "好了，在/vars中会显示my_func_qps, my_func_latency, my_func_latency_cdf等很多计数器。"

> **Source: [[sources/en_backup_request|en_backup_request]]**
> - "#include <bvar/bvar.h>"
> - "bvar::LatencyRecorder my_func_latency("my_func");"
> - "my_func_latency << tm.u_elapsed();  // u represents for microsecond, and s_elapsed(), m_elapsed(), n_elapsed() correspond to second, millisecond, nanosecond."