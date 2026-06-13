---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/streaming_log.md]]"
tags: [流式日志, LOG宏, PLOG宏, CHECK宏, VLOG, DLOG宏, 节流日志, noflush, thread-local缓冲, LOG_IF, chaining, operator<<重载, LOG_AT, DCHECK]
aliases: ["流式日志系统", "streaming_log - 流式日志输出"]
---

# streaming_log - Print log to std::ostreams - Summary

## 来源
- Original file: [[brpc/streaming_log.md]]
- Ingested: 2026-06-13

## 核心内容
本文档系统介绍了 [[entities/streaming_log|streaming_log]]（流式日志）系统，它是 [[entities/brpc|brpc]] 项目中 [[entities/butil|butil]] 基础工具库提供的日志子系统，完整实现位于 `<butil/logging.h>`。流式日志通过继承 `std::ostream` 并利用 C++ `operator<<` 的 [[concepts/chaining|chaining]] 机制，让用户可以链式地将复杂对象送入日志，避免了 printf 风格需要先转 string 的不便和大量临时内存分配。文档详细介绍了完整的日志宏家族——[[concepts/log宏|LOG宏]]、[[concepts/plog宏|PLOG宏]]、[[concepts/check宏|CHECK宏]]、[[concepts/vlog|VLOG]]、[[concepts/dlog宏|DLOG宏]] 以及 [[concepts/log_if|LOG_IF]] 条件宏；以及节流日志系列（[[concepts/节流日志|节流日志]]）用于高频热点探查。整套实现基于 [[concepts/thread-local缓冲|thread-local 缓冲]]保证线程安全，配合 [[concepts/noflush|noflush]] 机制实现同一线程内的批量输出，并通过 [[entities/logsink|LogSink]] 接口支持自定义日志输出目标。

## 关键实体
- [[entities/streaming_log|streaming_log]]：butil 库提供的流式日志系统，本文核心主题
- [[entities/brpc|brpc]]：百度开源的高性能 RPC 框架，streaming_log 所属项目
- [[entities/butil|butil]]：brpc 的基础工具库，streaming_log 的宿主环境
- [[entities/glog|glog]]：Google 开源 C++ 日志库，streaming_log 接口与其高度兼容
- [[entities/logsink|LogSink]]：日志输出目标的抽象类
- [[entities/stringsink|StringSink]]：默认提供的 LogSink 实现，主要用于单元测试
- [[entities/bthread|bthread]]：百度用户态线程库，noflush 在 bthread 上下文中支持批量刷出
- [[entities/gflags|gflags]]：Google 命令行参数库，通过 `--verbose`/`--verbose_module` 控制 VLOG 级别
- [[entities/addr2line|addr2line]]：GNU 工具，用于 CHECK 失败时将调用栈地址转换为源码行号

## 关键概念
- [[concepts/流式日志|流式日志]]：通过 `operator<<` chaining 机制将对象流式送入 `std::ostream` 的日志方式
- [[concepts/log宏|LOG宏]]：最基本日志宏 `LOG(level) << "message"`，与 glog 兼容
- [[concepts/plog宏|PLOG宏]]：在日志末尾自动追加 errno 可读信息的 LOG 变种
- [[concepts/check宏|CHECK宏]]：断言宏，失败时打印 FATAL 日志及完整调用栈，类似 gtest ASSERT
- [[concepts/vlog|VLOG]]：分层详细日志，通过 `--verbose`/`--verbose_module` gflags 控制
- [[concepts/dlog宏|DLOG宏]]：LOG 的 debug 版本，定义 NDEBUG 后不打印且不评估参数
- [[concepts/节流日志|节流日志]]：包括 `LOG_EVERY_SECOND`/`LOG_EVERY_N`/`LOG_FIRST_N`/`LOG_ONCE` 的节流家族
- [[concepts/noflush|noflush]]：哨兵对象，写入时不刷出，用于同一线程内批量输出
- [[concepts/thread-local缓冲|thread-local 缓冲]]：streaming_log 线程安全实现的关键机制
- [[concepts/log_if|LOG_IF]]：条件日志宏，等价于 `if (cond) { LOG() << ...; }`
- [[concepts/chaining|chaining]]：`operator<<` 链式调用的核心机制
- [[concepts/operator重载|operator<<重载]]：为自定义类型实现流式输出的关键技术
- [[concepts/log_at|LOG_AT]]：允许显式指定日志来源文件与行号的宏变种，常用于单测
- [[concepts/dcheck|DCHECK]]：CHECK 的 debug 版本，定义 NDEBUG 后完全移除

## 要点
- streaming_log 核心实现位于 `<butil/logging.h>`，通过继承 `std::ostream` 利用 `operator<<` chaining 机制实现复杂对象的流式打印，避免了 printf 风格需要先转 string 的临时内存开销
- 系统提供完整的日志宏家族：`LOG`（基本）、`PLOG`（自动附加 errno）、`CHECK`（断言）、`VLOG`（分层详细）、`DLOG`（debug 版本，定义 NDEBUG 后不评估参数）以及 `LOG_IF` 条件宏
- 节流日志宏 `LOG_EVERY_SECOND` / `LOG_EVERY_N` / `LOG_FIRST_N` / `LOG_ONCE` 用于高频热点监控，首次必打印，仅增加少量额外开销，且 `LOG_EVERY_N` 是线程安全的（区别于 glog 的同名宏）
- `noflush` 机制配合 thread-local 缓冲实现同一线程内的批量日志输出，支持将多个日志元素合并为一行刷新，并支持 bthread 的批量刷出场景
- 用户可通过 `LogSink` 接口自定义日志输出目标，默认提供 `StringSink` 实现用于单元测试；完整日志级别体系（FATAL/ERROR/WARNING/NOTICE/INFO/TRACE/VLOG/DEBUG）与 glog 有详细映射关系
- streaming_log 在多个方面优于 glog：EVERY_N 系列线程安全、FATAL 默认不 coredump、提供 `noflush` 批量输出机制
- 调试工作流：`CHECK` 失败时打印 call stack，第二列为代码地址，可使用 `addr2line -e ./binary <addr>` 还原源码行号