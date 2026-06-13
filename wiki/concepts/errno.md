---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/en_streaming_log.md]]"]
tags: [term]
aliases:
  - "POSIX errno"
  - "errno 错误码"
---


# errno

## 定义
errno 是 POSIX 环境定义的标准错误码变量，许多系统调用（如 `open`）在失败时会将其设置为表示特定错误原因的整数值（例如 `ENOENT` 表示"没有那个文件或目录"）。在 brpc 的 streaming_log 中，`PLOG` 宏会自动读取并解码当前线程的 errno，在日志末尾追加其对应的描述字符串，行为类似 `printf` 中的 `%m` 占位符。

## 关键特征
- 由 POSIX 标准定义，位于 `<errno.h>`，本质是一个线程局部（thread-local）的整型变量
- 仅在系统调用或部分库函数失败后才有意义，成功调用不应检查或依赖其值
- 每个错误码（如 `ENOENT`、`EACCES`、`EINVAL` 等）都有对应的可读描述
- `PLOG` 宏通过 `strerror(errno)` 等机制将错误码自动转写为人类可读的字符串
- 与普通 `LOG` 宏相比，`PLOG` 消除了"日志消息 + errno 转字符串"的样板代码
- 线程安全：errno 在多线程环境下是独立的，不会产生竞争

## 应用
- C/C++ 系统编程中对系统调用失败的诊断，例如打开文件、读取网络数据时的错误排查
- brpc 中使用 `PLOG(FATAL) << "Fail to open foo.conf"` 在底层失败时自动输出形如 `Fail to open foo.conf: No such file or directory` 的完整日志
- 与 `printf` 中的 `%m`（GNU 扩展）等价，作为 errno 的格式化占位符使用
- 任何需要将底层系统错误"一键翻译"为可读字符串并写入日志的场景

## 相关概念
- [[concepts/plog|PLOG]]
- [[concepts/log|LOG]]

## 相关实体
- [[entities/streaming_log|streaming_log]]

## 来源提及
- "Under POSIX environment, the error code is `errno`." — [[sources/en_streaming_log|en_streaming_log]]
- "int fd = open(\"foo.conf\", O_RDONLY);   // foo.conf does not exist, errno was set to ENOENT" — [[sources/en_streaming_log|en_streaming_log]]
- "// \"Fail to open foo.conf: No such file or directory\"" — [[sources/en_streaming_log|en_streaming_log]]