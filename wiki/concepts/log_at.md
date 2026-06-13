---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/streaming_log|streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "term"
aliases:
  - "LOG_AT宏"
---

## Description
LOG_AT 接收严重级别以及文件、行列号作为运行时参数，其典型签名形式为 `LOG_AT(severity, file, line) << message`，例如 `LOG_AT(FATAL, "specified_file.cc", 12345) << "file/line is specified"`。这种设计使得日志中的 `file:line` 元数据不再依赖编译器自动展开，而是由调用方主动控制，因此可以构造出位置信息可预测的日志条目。在测试实践中，LOG_AT 常与 [[entities/stringsink|StringSink]] 配合：测试代码使用 StringSink 捕获日志内容，再通过 `find("specified_file.cc:12345")` 之类的方式断言日志是否携带了指定的来源信息，例如测试中常见的 `ASSERT_NE(std::string::npos, log_str.find("specified_file.cc:12345"))`。与普通 LOG 宏相比，LOG_AT 更偏向测试与调试用途，能够避免因源码修改造成行号漂移而使测试用例变得脆弱，同时也便于人为指定统一的日志来源用于多线程、异步场景的输出定位或文档示例中的异常位置模拟。

## Related Concepts
- [[concepts/streaming_log|streaming_log]]
- [[concepts/log_if|LOG_IF]]
- [[concepts/vlog|VLOG]]

## Related Entities
- [[entities/stringsink|StringSink]]
- [[entities/logsink|LogSink]]

## Mentions in Source

> **Source: [[sources/streaming_log|streaming_log]]**
> - `LOG_AT(FATAL, "specified_file.cc", 12345) << "file/line is specified";`
> - `// the file:line part should be using the argument given by us.`
> - `ASSERT_NE(std::string::npos, log_str.find("specified_file.cc:12345"));`

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - `LOG_AT(FATAL, "specified_file.cc", 12345) << "file/line is specified";`
> - `// the file:line part should be using the argument given by us.`
> - `ASSERT_NE(std::string::npos, log_str.find("specified_file.cc:12345"));`