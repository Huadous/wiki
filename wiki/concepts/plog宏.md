---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/streaming_log|streaming_log]]"]
tags: [method]
aliases:
  - "PLOG()"
  - "PLOG 宏"
---


# PLOG宏

## 定义
PLOG 是 LOG 宏的变种，它在输出日志内容之后会自动追加错误码的可读描述信息，行为类似于 printf 中的 `%m` 占位符。在 POSIX 系统中，PLOG 会读取当前 `errno` 的值，并将其格式化为人类可读的错误信息附加在日志末尾。

## 关键特征
- 是 LOG 宏的扩展变种，保留了 LOG 的全部基础行为
- 在日志内容尾部自动追加错误码的可读描述
- 在 POSIX 系统中，等价于读取并格式化 `errno`
- 行为类似 `printf` 中的 `%m` 占位符
- 减少了开发者手动查阅 `errno` 含义并拼接字符串的工作量

## 应用
- 系统调用失败后的日志记录：例如 `open()` 失败时调用 `PLOG(FATAL)`，会输出形如 `"Fail to open foo.conf: No such file or directory"` 的日志，自动将 `errno` 翻译为可读文本
- 任何涉及 `errno` 的底层错误排查场景
- 需要快速定位系统级错误原因的调试与诊断

## 相关概念
- [[concepts/log宏|LOG宏]]

## 相关实体
（暂无相关实体）

## 来源提及
- PLOG和LOG的不同之处在于，它会在日志后加上错误码的信息，类似于printf中的%m。在posix系统中，错误码就是errno。 — [[brpc/streaming_log|streaming_log]]
- "Fail to open foo.conf: No such file or directory" — [[brpc/streaming_log|streaming_log]]