---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/lalb|streaming_log]]"]
tags: [method]
aliases:
  - "LOG()"
  - "LOG 宏"
---


# LOG宏

## 定义
LOG 是 streaming_log 中最基本的日志宏，采用 `LOG(level) << "message" << ...` 的链式调用形式，语法与 `std::cout` 类似，但调用结束时不需要添加 `std::endl`。支持的日志级别包括 FATAL、ERROR、WARNING、NOTICE、INFO、TRACE 等。LOG 宏的命名与设计完全沿用 glog，因此熟悉 glog 的使用者无需额外学习即可上手。

## 关键特征
- 链式调用语法：`LOG(level) << "message" << ...`，类似 `std::cout` 但无需 `std::endl`。
- 多级别支持：包含 FATAL、ERROR、WARNING、NOTICE、INFO、TRACE 等多个严重等级。
- 与 glog 完全兼容：宏名称、级别命名均与 glog 一致，便于迁移。
- 基于临时对象与 RAII：通过构造一个临时的 [[entities/logsink|LogSink]] 对象累积日志内容，在其析构时自动将日志刷出到屏幕或日志接收器。
- thread-local 缓冲：使用线程局部存储缓冲日志消息，降低多线程下的锁竞争。
- 无需显式换行：日志末尾不需要 `std::endl`，否则会导致日志格式异常。

## 应用
- 在 brpc 服务端代码中按严重等级输出运行日志、错误信息及调试信息。
- 通过 FATAL 级别在关键错误发生时立即终止程序并打印上下文。
- 与 [[concepts/plog|PLOG宏]]（系统错误增强日志）、[[concepts/check|CHECK宏]]（断言日志）、[[concepts/vlog|VLOG]]、[[concepts/dlog|DLOG宏]]（仅在 debug 模式下生效）、[[concepts/节流日志|节流日志]]等配合，构成完整的日志体系。
- 作为 [[concepts/流式日志|流式日志]]接口的基础入口，统一处理文本与结构化日志输出。

## 相关概念
- [[concepts/plog|PLOG宏]]
- [[concepts/check|CHECK宏]]
- [[concepts/vlog|VLOG]]
- [[concepts/dlog|DLOG宏]]
- [[concepts/节流日志|节流日志]]
- [[concepts/流式日志|流式日志]]

## 相关实体
- [[sources/lalb|streaming_log]]
- [[entities/glog|glog]]

## 来源提及
- `LOG(FATAL) << "Fatal error occurred! contexts=" << ...;` — [[sources/lalb|streaming_log]]
- "如果你用过glog，应该是不用学习的，因为宏名称和glog是一致的，如下打印一条FATAL。注意不需要加上std::endl。" — [[sources/lalb|streaming_log]]