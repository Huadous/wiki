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
tags:
  - "product"
aliases:
  - "brpc bvar"
  - "bvar多维统计库"
---

## Description
bvar 是 Apache brpc 项目中的一组 C++ 计数器类库，用于程序内部各种统计和监控指标的记录与展示。bvar 提供了多种具体的计数器类型，每种类型对应不同的统计语义，例如 LatencyRecorder 用于延迟统计的 CDF 展示，Adder/Maxer/Miner 用于基础数值聚合。bvar 是线程兼容的，在多线程环境下可安全使用。其设计强调命名规范（模块_类名_指标）以及自动化的名字归一化机制：无论用户传入 `foo::BarNum`、`foo.bar.num`、`foo bar num` 还是 `foo-bar-num`，最终都被归一化为 `foo_bar_num`。bvar 还支持衍生变量（如 Window、PerSecond）的自动更新能力，并可通过全局曝光（expose）机制将变量注册到全局表中，从而通过 HTTP 接口（/vars）或本地文件（bvar_dump）查询和导出，使外部监控系统能够方便地获取这些指标。

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/curl|curl]]
- [[entities/mbvar|mbvar]]
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
- [[concepts/bvar::Adder|bvar::Adder]]
- [[concepts/bvar::Window|bvar::Window]]
- [[concepts/bvar::PerSecond|bvar::PerSecond]]
- [[concepts/bvar::Status|bvar::Status]]

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