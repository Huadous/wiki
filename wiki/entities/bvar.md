---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
  - "[[brpc/server.md]]"
  - "[[brpc/en_backup_request.md]]"
  - "[[brpc/bvar_c++.md]]"
  - "[[brpc/bvar.md]]"
tags:
  - "product"
aliases:
  - "brpc bvar"
  - "bvar多维统计库"
---

## Description
bvar 是 Apache brpc 项目内置的多线程计数器类库，位于 brpc 源代码树的 src/bvar 目录下，专门为多线程环境下的计数和监控场景设计。它通过 thread local 存储技术避免了 cache bouncing 问题，在多线程同时累加时每个线程只操作私有变量，读取时再合并所有线程数据，写入开销极低（约 20 纳秒）且几乎不随线程数增加而增长，相比百度内老计数器库 UbMonitor 几乎不会给程序增加额外性能开销，也快于竞争频繁的原子操作。bvar 包括单维度 bvar 和多维度 mbvar 两种形式，是 brpc 可观测性体系的核心组件，被 brpc 大量用于提供各类运行时统计数值，并可通过 `/vars` 与 `/vars/VARNAME` 接口进行查看。bvar 本身是线程兼容的，会做名字归一化以统一不同书写风格暴露的同名计数器。

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/curl|curl]]
- [[entities/mbvar|mbvar]]
- [[entities/bvar::LatencyRecorder|bvar::LatencyRecorder]]
- [[entities//vars|/vars]]
- [[entities/UbMonitor|UbMonitor]]
- [[entities/Prometheus|Prometheus]]
- [[entities/noah|noah]]

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
- [[concepts/bvar::Adder|bvar::Adder]]
- [[concepts/bvar::Window|bvar::Window]]
- [[concepts/bvar::PerSecond|bvar::PerSecond]]
- [[concepts/bvar::Status|bvar::Status]]
- [[concepts/bvar::LatencyRecorder|bvar::LatencyRecorder]]
- [[concepts/Cacheline|Cacheline]]
- [[concepts/cache bouncing|cache bouncing]]
- [[concepts/thread local 存储|thread local 存储]]
- [[concepts/原子操作|原子操作]]

## Mentions in Source
> **Source: [[sources/en_backup_request|en_backup_request]]**
> - `#include <bvar/bvar.h>`
> - `// All work is done here. My_func_qps, my_func_latency, my_func_latency_cdf and many other counters would be shown in /vars.`
> - `You can look the default cdf(Cumulative Distribution Function) graph of latency provided by brpc, or add it by your own.`

> **Source: [[sources/bvar_c++|bvar_c++]]**
> - `bvar分为多个具体的类，常用的有：`（bvar 分为多个具体的类，常用的有：）
> - `bvar是线程兼容的。`（bvar 是线程兼容的。）
> - `bvar会做名字归一化，不管你打入的是foo::BarNum, foo.bar.num, foo bar num , foo-bar-num，最后都是foo_bar_num。`（bvar 会做名字归一化，不管你打入的是 foo::BarNum、foo.bar.num、foo bar num、foo-bar-num，最后都是 foo_bar_num）
> - `目前bvar会做名字归一化，不管你打入的是foo::BarNum, foo.bar.num, foo bar num , foo-bar-num，最后都是foo_bar_num。`（目前 bvar 会做名字归一化，不管你打入的是 foo::BarNum、foo.bar.num、foo bar num、foo-bar-num，最后都是 foo_bar_num）

> **Source: [[sources/bvar|bvar]]**
> - `bvar是多线程环境下的计数器类库，支持单维度bvar和多维度mbvar，方便记录和查看用户程序中的各类数值`
> - `它利用了thread local存储减少了cache bouncing，相比UbMonitor(百度内的老计数器库)几乎不会给程序增加性能开销，也快于竞争频繁的原子操作`
> - `brpc集成了bvar，/vars可查看所有曝光的bvar，/vars/VARNAME可查阅某个bvar`