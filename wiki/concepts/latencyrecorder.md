---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/backup_request]]"
  - "[[brpc/en_backup_request.md]]"
  - "[[brpc/bvar_c++.md]]"
tags:
  - "term"
aliases:
  - "bvar::LatencyRecorder"
  - "延迟记录器"
  - "brpc延迟记录器"
---

## Related Concepts
- [[concepts/latency_cdf|latency_cdf]] — 延迟累积分布函数，由 LatencyRecorder 自动生成
- [[concepts/bvar|bvar]] — 底层统计库，LatencyRecorder 依赖其聚合能力
- [[concepts/backup_request|backup_request]] — LatencyRecorder 常用于优化的关键机制
- [[concepts/cdf|CDF]] — 累积分布函数，LatencyRecorder 自动产出的核心统计图
- [[concepts/bvar::adder|bvar::Adder]] — LatencyRecorder 内部用于统计平均延时（latency）的组件
- [[concepts/bvar::maxer|bvar::Maxer]] — LatencyRecorder 内部用于统计最大延时（max_latency）的组件
- [[concepts/bvar::window|bvar::Window]] — LatencyRecorder 内部使用的时间窗口组件
- [[concepts/bvar::persecond|bvar::PerSecond]] — LatencyRecorder 内部用于按窗口计算 qps 的组件

## Related Entities
- [[entities/bvar|bvar]] — 提供 LatencyRecorder 实现的统计库
- [[entities/brpc|brpc]] — 所属框架生态

## Mentions in Source
> **Source: backup_request**
> - "自行添加的方法："
> - "bvar::LatencyRecorder my_func_latency("my_func");"
> - "my_func_latency << tm.u_elapsed();  // u代表微秒，还有s_elapsed(), m_elapsed(), n_elapsed()分别对应秒，毫秒，纳秒。"
> - "好了，在/vars中会显示my_func_qps, my_func_latency, my_func_latency_cdf等很多计数器。"

> **Source: en_backup_request**
> - "#include <bvar/bvar.h>"
> - "bvar::LatencyRecorder my_func_latency("my_func");"
> - "my_func_latency << tm.u_elapsed();  // u represents for microsecond, and s_elapsed(), m_elapsed(), n_elapsed() correspond to second, millisecond, nanosecond."

> **Source: bvar_c++**
> - "bvar::LatencyRecorder| 专用于记录延时和qps的变量。输入延时，平均延时/最大延时/qps/总次数 都有了"
> - "专用于计算latency和qps的计数器。只需填入延时数据，就能获得latency / max_latency / qps / count。"
> - "注意：LatencyRecorder没有继承Variable，而是多个bvar的组合。"