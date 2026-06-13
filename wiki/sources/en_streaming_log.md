---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/en_streaming_log.md]]"
tags: [LOG macro, PLOG, VLOG, DLOG, CHECK macro, noflush, LogSink, std::ostream chaining, LOG_IF, XXX_EVERY_SECOND, XXX_EVERY_N, XXX_FIRST_N, XXX_ONCE, VLOG2, CHECK_XX, DLOG family, thread-local buffer, errno]
aliases: ["streaming_log 流式日志文档", "brpc streaming_log"]
---

# streaming_log - Print log to std::ostreams - Summary

## 来源
- Original file: [[brpc/en_streaming_log.md]]
- Ingested: 2026-06-13

## 核心内容
本文档介绍了 [[entities/butil|butil]] 库中的 [[entities/streaming_log|streaming_log]] 日志组件。该组件继承自 std::ostream,通过 [[concepts/stdostream-chaining|operator<< 链式调用]] 支持直接打印任意复杂的 C++ 对象,避免了 printf 风格格式化带来的不便与临时内存开销。文档详细说明了完整的日志宏家族:[[concepts/log-macro|LOG]]、[[concepts/plog|PLOG]]（附加 errno）、[[concepts/vlog|VLOG]]（多层级详细日志）、[[concepts/dlog|DLOG]]（仅调试期生效）以及 [[concepts/check-macro|CHECK]]（断言式检查）。同时涵盖了频率控制变体([[concepts/xxx_every_second|XXX_EVERY_SECOND]]、[[concepts/xxx_every_n|XXX_EVERY_N]]、[[concepts/xxx_first_n|XXX_FIRST_N]]、[[concepts/xxx_once|XXX_ONCE]])、条件日志 [[concepts/log_if|LOG_IF]]、通过 [[concepts/noflush|noflush]] 实现的延迟刷新机制,以及通过 [[concepts/logsink|LogSink]] 实现的自定义日志目的地。日志级别与 [[entities/glog|glog]] 对齐,并新增了 NOTICE 级别。底层使用 [[concepts/thread-local-buffer|thread-local buffer]] 保证线程安全。

## 关键实体
- [[entities/streaming_log|streaming_log]] - 流式日志组件
- [[entities/butil|butil]] - 百度基础工具库
- [[entities/brpc|brpc]] - 百度 RPC 框架
- [[entities/glog|glog]] - Google 日志库
- [[entities/bthread|bthread]] - 百度协程库
- [[entities/stringsink|stringsink]] - 内置字符串日志实现
- [[entities/log_at|log_at]] - 指定文件/行号的日志宏

## 关键概念
- [[concepts/log-macro|LOG macro]] - 核心日志宏
- [[concepts/plog|PLOG]] - 附加 errno 信息的日志宏
- [[concepts/vlog|VLOG]] - 多层级详细日志
- [[concepts/dlog|DLOG]] - 调试版本日志
- [[concepts/check-macro|CHECK macro]] - 断言式检查宏
- [[concepts/noflush|noflush]] - 延迟刷新机制
- [[concepts/logsink|LogSink]] - 自定义日志目的地接口
- [[concepts/stdostream-chaining|std::ostream chaining]] - 流式链式调用机制
- [[concepts/log_if|LOG_IF]] - 条件日志宏
- [[concepts/xxx_every_second|XXX_EVERY_SECOND]] - 每秒限频日志
- [[concepts/xxx_every_n|XXX_EVERY_N]] - 每 N 次日志
- [[concepts/xxx_first_n|XXX_FIRST_N]] - 前 N 次日志
- [[concepts/xxx_once|XXX_ONCE]] - 一次性日志
- [[concepts/vlog2|VLOG2]] - 带虚拟路径的 VLOG
- [[concepts/check_xx|CHECK_XX]] - 算术比较断言
- [[concepts/dlog-family|DLOG family]] - 调试日志宏族
- [[concepts/thread-local-buffer|thread-local buffer]] - 线程局部日志缓冲
- [[concepts/errno|errno]] - POSIX 错误码

## 要点
- streaming_log 继承自 std::ostream,通过 operator<< 链式调用支持打印任意复杂 C++ 对象,无需 printf 风格字符串转换,大幅简化代码并避免临时内存分配
- 实现采用 thread-local buffer,在完整日志记录完成后刷新到屏幕或 LogSink,具备线程安全性
- 日志级别与 glog 对齐（FATAL/ERROR/WARNING/INFO）,新增 NOTICE 用于重要业务日志,并提供 DLOG/DCHECK 系列在 NDEBUG 下完全跳过求值
- 频率控制宏族 LOG_EVERY_SECOND、LOG_EVERY_N、LOG_FIRST_N、LOG_ONCE 分别用于按秒、按次数、前 N 次、仅一次限频输出
- noflush 标记将日志暂存于线程本地缓冲,常用于循环输出合并为单行或在 bthread 中收集 RPC 日志后统一刷新（注意异步方法不得使用）
- CHECK_XX 算术断言宏失败时输出两侧具体值（如"Check failed: x > y (1 vs 2)"）,比普通 CHECK 表达式更具诊断价值
- VLOG 通过 --verbose 和 --verbose_module gflag 控制层级,后者可按文件路径覆盖全局设置
- 用户可继承 LogSink 并调用 logging::SetLogSink 实现自定义日志目的地,StringSink 是常用于单元测试的字符串实现示例