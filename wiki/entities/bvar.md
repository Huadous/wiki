---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
  - "[[brpc/server.md]]"
  - "[[brpc/en_backup_request.md]]"
tags:
  - "product"
aliases:
  - "brpc bvar"
  - "bvar多维统计库"
---

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/curl|curl]]
- [[entities/bvar::LatencyRecorder|bvar::LatencyRecorder]]
- [[entities//vars|/vars]]

## Related Concepts
- [[concepts/性能分析|性能分析]]
- [[concepts/CPU Profiler|CPU Profiler]]
- [[concepts/Heap Profiler|Heap Profiler]]
- [[concepts/Contention Profiler|Contention Profiler]]
- [[concepts/Builtin Service|Builtin Service]]
- [[concepts/fork without exec|fork without exec]]
- [[concepts/brpc::Server|brpc::Server]]
- [[concepts/CDF|CDF]]
- [[concepts/backup_request_ms|backup_request_ms]]
- [[concepts/Backup Request|Backup Request]]

## Mentions in Source
> **Source: [[sources/en_backup_request|en_backup_request]]**
> - `#include <bvar/bvar.h>`
> - `// All work is done here. My_func_qps, my_func_latency, my_func_latency_cdf and many other counters would be shown in /vars.`
> - `You can look the default cdf(Cumulative Distribution Function) graph of latency provided by brpc, or add it by your own.`