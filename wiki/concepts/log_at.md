---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/streaming_log|streaming_log]]"]
tags: [term]
aliases:
  - "LOG_AT宏"
---


# LOG_AT

## 定义
LOG_AT 是 [[concepts/streaming_log|streaming_log]] 提供的一个宏变种，允许用户显式指定日志来源的文件名和行号，而不是使用宏自动展开处的实际位置。其典型用法为 `LOG_AT(FATAL, "specified_file.cc", 12345) << "file/line is specified"`。

## 关键特征
- 显式控制日志中的文件名和行号元数据，覆盖编译器自动展开的 `__FILE__` / `__LINE__` 默认行为
- 接口形式为 `LOG_AT(severity, file, line) << message`，其中 severity 通常为日志严重级别（如 FATAL）
- 常与 [[entities/stringsink|StringSink]] 配合使用，使测试可以捕获并断言日志内容
- 适用于需要精确复现或伪造日志来源位置的场景
- 与普通 LOG 宏相比，更偏向测试与调试用途

## 应用
- 单元测试中验证日志输出是否包含预期的 `file:line` 文本，例如通过 `find("specified_file.cc:12345")` 进行断言
- 测试日志格式化逻辑时，固定文件号与行号以避免因源码改动导致测试用例脆弱
- 调试多线程或异步场景时，人为指定统一的日志来源便于在输出中定位特定代码路径
- 模拟异常代码位置的日志输出，用于文档示例或问题复现

## 相关概念
- [[concepts/streaming_log|streaming_log]]

## 相关实体
- [[entities/stringsink|StringSink]]
- [[entities/logsink|LogSink]]

## 来源提及
- `LOG_AT(FATAL, "specified_file.cc", 12345) << "file/line is specified";` — [[sources/streaming_log|streaming_log]]
- `// the file:line part should be using the argument given by us.
    ASSERT_NE(std::string::npos, log_str.find("specified_file.cc:12345"));` — [[sources/streaming_log|streaming_log]]