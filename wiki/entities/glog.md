---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[]]"
  - "[[brpc/streaming_log.md]]"
  - "[[brpc/server.md]]"
tags:
  - "product"
aliases:
  - "Google glog"
  - "glog日志库"
---

## Description
glog 是 Google 开发的 C++ 日志库，广泛用于 C++ 项目，提供了一个灵活且高效的日志框架，支持不同级别（如 INFO、WARNING、ERROR、FATAL）的日志输出。在 [[entities/brpc|brpc]] 框架中，glog 可用于替换默认的日志实现。由于 brpc 自带的日志工具与 glog 功能重叠，两者在编译时会产生冲突，因此需要显式启用 glog 支持。启用方法为在 [[entities/config_brpc.sh|config_brpc.sh]] 中添加 `--with-glog` 参数，或通过 [[entities/cmake|cmake]] 构建系统添加 `-DWITH_GLOG=ON` 选项。glog 的版本要求为 3.3 或更高。启用后，brpc 的所有日志输出将交由 glog 管理，这对于已经使用 glog 进行日志集成的项目尤为有利。

glog 的接口设计影响了 brpc 的日志体系，[[sources/streaming_log|streaming_log]] 在接口层面与 glog 保持高度兼容，宏名称和调用方式完全一致，因此熟悉 glog 的用户几乎无需额外学习即可使用 streaming_log。两者在 FATAL、ERROR、WARNING、INFO 等日志级别上存在明确的映射关系。然而 streaming_log 相比 glog 也进行了若干改进：EVERY_N 系列宏是线程安全的（而 glog 的对应宏并非线程安全），FATAL 默认不生成 coredump，并且 streaming_log 提供了 glog 所没有的 noflush 批量输出机制。

此外，glog 与 brpc 的默认日志实现 butil/logging.h 都各自实现了"最低日志级别"（-minloglevel）选项，为同名选项，行为一致。在 FATAL 日志处理上，两者存在重要差异：glog 默认在 FATAL 日志时 crash（即触发 coredump），而 brpc 通过 `-crash_on_fatal_log` gflag 提供对此行为的控制，可使程序在 FATAL 日志或 CHECK 断言违反后 abort 并产生 coredump。需要注意的是，`-crash_on_fatal_log` 只对 butil/logging.h 中的日志宏有效，对 glog 默认行为不生效。日志最终打印到自定义 LogSink 时，还需经过 LogSink 的过滤。未打印日志的开销仅为一次 if 判断，且不会评估参数，因此日志宏在运行时具有极低的性能损耗。

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/cmake|cmake]]
- [[entities/config_brpc.sh|config_brpc.sh]]

## Related Concepts
- [[concepts/日志系统|日志系统]]

## Mentions in Source
> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "To use brpc with glog, add --with-glog."
> - "brpc implements a default logging utility which conflicts with glog. To replace this with glog, add --with-glog to config_brpc.sh or add -DWITH_GLOG=ON to cmake."
> - "glog: 3.3+"

> **Source: [[sources/streaming_log|streaming_log]]**
> - "如果你用过glog，应该是不用学习的，因为宏名称和glog是一致的，如下打印一条FATAL。"
> - "streaming log的日志等级与glog映射关系如下"

> **Source: [[sources/server|server]]**
> - "此功能由butil/logging.h和glog各自实现，为同名选项。"
> - "glog默认在FATAL日志时crash。"
> - "此功能只对butil/logging.h中的日志宏有效，glog默认在FATAL日志时crash。"
> - "如果日志最终打印到自定义LogSink，那么还要经过LogSink的过滤。"