---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/builtin_service]]"
  - "[[brpc/en_backup_request.md]]"
  - "[[brpc/bvar.md]]"
tags:
  - "term"
aliases:
  - "vars服务"
  - "自定义计数器"
  - "brpc变量展示接口"
  - "/vars"
  - "vars服务"
  - "自定义计数器"
  - "brpc变量展示接口"
---

## Related Concepts
- [[concepts/status|/status]]
- [[concepts/connections|/connections]]
- [[concepts/flags|/flags]]
- [[concepts/rpcz|/rpcz]]
- [[concepts/builtin-service|内置服务]]
- [[concepts/backup-request|backup_request]]
- [[concepts/backup-request-ms|backup_request_ms]]
- [[concepts/latency-cdf|延迟 CDF]]
- [[concepts/brpc-metrics|/brpc_metrics]]
- [[concepts/dump功能|dump功能]]
- [[concepts/bvar|bvar]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/bvar|bvar]]
- [[entities/bvar-latencyrecorder|bvar::LatencyRecorder]]

## Mentions in Source
> **Source: [[sources/builtin_service|builtin_service]]**
> - "/vars: 用户可定制的，描绘各种指标的计数器。"

> **Source: [[sources/en_backup_request|en_backup_request]]**
> - "All work is done here. My_func_qps, my_func_latency, my_func_latency_cdf and many other counters would be shown in /vars."
> - "You can look the default cdf(Cumulative Distribution Function) graph of latency provided by brpc"

> **Source: [[sources/bvar|bvar]]**
> - "brpc集成了bvar，/vars可查看所有曝光的bvar，/vars/VARNAME可查阅某个bvar，在brpc中的使用方法请查看vars。"
> - "brpc大量使用了bvar提供统计数值，当你需要在多线程环境中计数并展现时，应该第一时间想到bvar。"