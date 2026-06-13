---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/lalb|streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "method"
aliases:
  - "LOG()"
  - "LOG 宏"
  - "LOG macro"
  - "LOG()"
  - "LOG 宏"
---

## Description
LOG 宏是 streaming_log 日志体系的入口与核心接口，采用 `LOG(level) << "message" << ...` 的链式调用语法，将任意可流式输出（streamable）的对象依次写入日志流，并在每条日志末尾自动追加换行，因此调用方无需手动添加 `std::endl`，否则会导致日志格式异常。支持的日志级别包括 FATAL、ERROR、WARNING、NOTICE、INFO、TRACE 等多个严重等级，宏名称和级别命名与 [[entities/glog|glog]] 完全保持一致，使熟悉 glog 的使用者可以无缝迁移。该宏在实现上基于一个临时的 [[entities/logsink|LogSink]] 对象（即 RAII 机制），在构造期累积 `<<` 传入的内容，在析构时自动将日志刷出到屏幕或日志接收器；同时借助 thread-local 缓冲降低多线程场景下的锁竞争。FATAL 级别的 LOG 默认不会触发 coredump，除非通过 `-crash_on_fatal_log` gflag 显式启用。

## Related Concepts
- [[concepts/plog|PLOG宏]]
- [[concepts/check|CHECK宏]]
- [[concepts/vlog|VLOG]]
- [[concepts/dlog|DLOG宏]]
- [[concepts/节流日志|节流日志]]
- [[concepts/流式日志|流式日志]]
- [[concepts/noflush|noflush]]

## Related Entities
- [[sources/lalb|streaming_log]]
- [[sources/en_streaming_log|en_streaming_log]]
- [[entities/glog|glog]]

## Mentions in Source
> **Source: [[sources/lalb|lalb]]**
> - `LOG(FATAL) << "Fatal error occurred! contexts=" << ...;`
> - "如果你用过glog，应该是不用学习的，因为宏名称和glog是一致的，如下打印一条FATAL。注意不需要加上std::endl。"

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "If you have ever used glog before, you should find it easy to start. The log macro is the same as glog."
> - "Note that there is no std::endl"