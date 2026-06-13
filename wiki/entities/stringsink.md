---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/streaming_log|streaming_log]]"]
tags: [other]
aliases:
  - "logging::StringSink"
  - "StringSink 类"
---


# StringSink

## 基本信息
- Type: other
- Source: [[sources/streaming_log|streaming_log]]

## 描述
StringSink 是 [[brpc/streaming_log|streaming_log]] 默认提供的一个 LogSink 实现，它同时继承自 [[entities/butil|butil]] 中的 [[entities/socketuniqueptr|socketuniqueptr]] 体系所引用的日志接收接口 LogSink 以及 C++ 标准库的 std::string，将日志内容直接存放到字符串缓冲区中。该类主要用于单元测试场景，使测试代码能够以编程方式获取并断言日志输出内容。其典型使用模式为：声明一个 `::logging::StringSink` 局部变量，通过 `::logging::SetLogSink(&log_str)` 将其设置为当前 sink 并保存原 sink 指针，然后执行待测代码并通过 `find()` 等 string 方法验证日志内容。这种设计使得对日志内容的断言测试变得简单直接，无需解析屏幕输出或文件。

## 相关实体
- [[entities/butil|butil]]（提供 LogSink 接口所在的工具库）

## 相关概念
- [[concepts/流式日志|流式日志]]

## 来源提及
- 同时继承了LogSink和string，把日志内容存放在string中，主要用于单测 — [[brpc/streaming_log|streaming_log]]
- ::logging::StringSink log_str; — [[brpc/streaming_log|streaming_log]]
- ::logging::LogSink* old_sink = ::logging::SetLogSink(&log_str); — [[brpc/streaming_log|streaming_log]]